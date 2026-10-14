---
title: Path C hook contract — Langfuse trace bridge
chapter: 05
status: in-progress
audience: [novice, seasoned, both]
tags: [execution, track-b, observability, hooks, langfuse]
---

# Path C hook contract — Langfuse trace bridge

Book-owned **core** for Track B observability ([ADR-009](../../02-design/decisions/ADR-009-observability-paths-abc.md)).
Cursor/VS Code hooks call `scripts/langfuse_trace_bridge.py`; the bridge emits
spans to self-hosted Langfuse (track-a compose on `:3001`). Complements
**process trace** (STATE, git, session gates) — never replaces it.

> [!LEARN] Learn It
> Path C captures IDE agent behavior (tools, shell, edits, MCP). It does **not**
> capture subscription token/cost — use Path A when Docker is up.

> [!TIP] Fast Track
> Copy `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` from track-a `.env` →
> restart Cursor → run one agent turn → open **http://127.0.0.1:3001** → Traces.

## Artifacts

| Artifact | Owner | Purpose |
| :------- | :---- | :------ |
| `.cursor/hooks.json` | Book | Full hook event wiring (project hooks) |
| `scripts/langfuse_trace_bridge.py` | Book | Stdlib-only ingestion; fail-open |
| `.cursor/langfuse-session.json` | Runtime | Trace/session correlation (gitignored) |
| `.cursor/langfuse-queue/` | Runtime | Local queue when Langfuse down (gitignored) |
| `track-a/.env` keys | Reader | `LANGFUSE_*` — same project as Path A |

## Hook events (full set)

| Event | Langfuse emit | Gates agent? |
| :---- | :------------ | :----------- |
| `sessionStart` | `trace-create`; flush queue | No |
| `sessionEnd` | `event-create`; clear session state | No |
| `beforeSubmitPrompt` | `span-create` | Allow (audit) |
| `preToolUse` | `span-create` | Allow |
| `postToolUse` | `span-create` (+ endTime) | No |
| `postToolUseFailure` | `span-create` | No |
| `beforeShellExecution` | `span-create` | Allow |
| `afterShellExecution` | `span-create` (+ endTime) | No |
| `beforeMCPExecution` | `span-create` | Allow |
| `afterMCPExecution` | `span-create` (+ endTime) | No |
| `beforeReadFile` | `span-create` | Allow |
| `afterFileEdit` | `span-create` (+ endTime) | No |
| `stop` | `event-create` | No |
| `afterAgentResponse` | `span-create` (+ endTime) | No |

## Temporal layer (S45)

ISO timestamps on **agent-session hook** events feed **dual write**: Langfuse spans (above) +
`logs/sessions/<id>.md` (runtime, gitignored).

### Temporal events

| Event | Session log | Langfuse |
| :---- | :---------- | :------- |
| `sessionStart` | Init log + canon freshness | `trace-create` + freshness metadata |
| `beforeSubmitPrompt` | Timeline row | `span-create` |
| `afterAgentResponse` / `stop` | Timeline row | `span-create` / `event-create` |
| `sessionEnd` | Finalize metrics | `event-create` |
| Human gate (Proceed / merge) | Gates table + timeline | `cursor.human_gate.<gate>` span |

### Human gates (dual source)

| Source | Detection |
| :----- | :-------- |
| **Hook-detected** | `beforeSubmitPrompt` containing `proceed`; merge via prompt or `git merge` in shell |
| **Manual** | `python scripts/annotate_session_gate.py proceed\|merge [--note "..."]` |

### Canon freshness banner

At `sessionStart`, bridge compares `updated` frontmatter on STATE + dashboard L1–L3
to host time. Stale (>24h) files produce a **stderr banner** and a session-log
section; metadata also ships on the Langfuse trace.

### Session log schema (`logs/sessions/<id>.md`)

Runtime artifact — **gitignored**. YAML frontmatter + Markdown tables:

| Section | Content |
| :------ | :------ |
| Frontmatter | `status: runtime`, `session_id`, `started_at`, `ended_at`, `canon_freshness`, `metrics` |
| Timeline | Hook events with UTC timestamps |
| Human gates | Proceed / merge rows (hook-detected or manual) |
| Metrics | Session duration, mean human latency, decision count, prompt count |

### Metrics (computed at `sessionEnd`)

| Metric | Definition |
| :----- | :--------- |
| Session duration | `sessionEnd` − `sessionStart` |
| Mean human latency | Mean(`beforeSubmitPrompt` − prior `stop` / `afterAgentResponse`) |
| Decision count | Human gate events |
| Prompt count | `beforeSubmitPrompt` rows |

## Configuration

| Variable | Source | Default |
| :------- | :----- | :------ |
| `LANGFUSE_PUBLIC_KEY` | `track-a/.env` or env | — (required for traces) |
| `LANGFUSE_SECRET_KEY` | `track-a/.env` or env | — (required for traces) |
| `LANGFUSE_HOST` / `LANGFUSE_BASE_URL` | env | `http://127.0.0.1:3001` |

Bridge loads `05-build/execution-tools/track-a/.env` when keys are not already
in the process environment. Hooks inherit the IDE process env — restart the IDE
after editing `.env`.

## Fail-open rules

| Condition | Behavior |
| :-------- | :------- |
| Langfuse unreachable | Append batch to `.cursor/langfuse-queue/pending.jsonl` |
| Keys missing | No-op; agent continues |
| Bridge exception | Swallowed; gate hooks still return `allow` |
| Langfuse timeout (>2s) | Queue locally; never block |

## Redaction (v1)

| Rule | Detail |
| :---- | :----- |
| Max field length | 500 chars then truncate + sha256 suffix |
| Patterns | `api_key`, `secret`, `password`, `token`, `Bearer`, `sk-`, `pk-` |
| Prompts | Metadata only — do not log full prompts in shared Langfuse |

Reader owns scrub policy for compliance; ADR-009 documents the duty.

## Smoke test

1. Start track-a compose — [track-a-setup](track-a-setup.md) step 4 (`langfuse-web` on `:3001`).
2. Confirm `.env` has `LANGFUSE_PUBLIC_KEY` and `LANGFUSE_SECRET_KEY`.
3. Restart Cursor (reload hooks).
4. Start a new agent chat (fires `sessionStart`).
5. Run one tool action (e.g. read a file).
6. Langfuse UI → **Traces** → filter tag `path-c` → see `cursor-agent-session`.

Manual invoke (no IDE):

```powershell
'{"workspace":"/tmp/test"}' | python scripts/langfuse_trace_bridge.py sessionStart
'{"tool":"Read"}' | python scripts/langfuse_trace_bridge.py preToolUse
```

## VS Code–compatible IDEs

Same contract: project hooks at repo root. Forks (Cursor, Windsurf) use the
same `.cursor/hooks.json` path. Update **your** tooling manifest — not this file.

## Reference

- Decision: [ADR-009-observability-paths-abc](../../02-design/decisions/ADR-009-observability-paths-abc.md)
- Hub: [vscode-hub](vscode-hub.md)
- Track B checklist: [track-b-checklist](track-b-checklist.md)
- Path A compose: [track-a-setup](track-a-setup.md)
- Temporal layer: [session-roadmap-s40-plus](../../context/system/sessions/session-roadmap-s40-plus.md) (S45)
