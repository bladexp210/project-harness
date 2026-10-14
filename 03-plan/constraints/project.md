---
title: Project Constraints
chapter: 03
status: living
audience: [novice, seasoned, both]
tags: [constraint, harness]
---

# Project constraints — this harness repo

Project-specific rules for **this book-as-harness repository**. You inherit
[constraints/global](global.md) and [constraints/host](host.md); this file holds
identity, track choice, and tool adapters — not OS/shell facts (those live in
`host.md`).

> [!LEARN] Learn It
> **Global vs host vs project:** `global.md` — inherited guardrails.
> `host.md` — your machine and shell (copy-paste dialect, D-001).
> `project.md` — tool choices, git layout, adapters.

> [!TIP] Fast Track
> Fill [constraints/host](host.md) first → identity → execution track → git layout
> → tool adapters → models.

## Identity

| Field | Value |
| :---- | :---- |
| Project | Methodology book / harness (`project-harness`) |
| Product type | Docs-only repo — teaches and operates as a real harness |
| Primary author | Human (Alex) + Track B IDE agents |
| Remote | None (local-only; D-001 per [constraints/host](host.md)) |

## Execution track

| Field | Value |
| :---- | :---- |
| **Authoring today** | Track B — Cursor IDE agent |
| **Target for build tasks** | Track A — [openhands](../../05-build/execution-tools/openhands.md) when Docker + LiteLLM ready (S21) |
| **Decision record** | [ADR-007-dual-execution-tracks](../../02-design/decisions/ADR-007-dual-execution-tracks.md) |
| **Session ritual** | [session-workflow](../../context/system/session-workflow.md) — branch `session-NN/<topic>` per session |

## Git layout

| Field | Value |
| :---- | :---- |
| **Current (ramp)** | Normal clone; session branches on same working tree |
| **Target** | Bare hub + worktrees per [bare-worktree-setup](../../05-build/execution-tools/bare-worktree-setup.md) |
| **Protected branch** | `main` — merge only after session close + human review |
| **Commit author** | Human on host shell — see `constraints/host.md` (D-001) |

## Tool adapters (Track B — VS Code hub / Cursor)

Living instance of `_templates/tooling-manifest.md`. Map [track-b-checklist](../../05-build/execution-tools/track-b-checklist.md)
concerns to this workspace — update here and in the manifest when tools change.

| Checklist concern | This project |
| :---------------- | :----------- |
| IDE shell | Cursor (VS Code–compatible) — workspace = harness clone |
| Persistent rules | `AGENTS.md`, `.cursor/rules/` |
| Scoped files | Chat @-mentions; explicit Scope — modify in task files |
| Stripped context | `python scripts/task_context.py <task.md>` output pasted into chat |
| Diff review | Cursor source control panel |
| Model choice | Composer / subscription tier (yaml aliases advisory until LiteLLM wired) |
| Automation hooks | Cursor skills, MCP (Obsidian, browser, Atlassian as enabled) |
| Observability export | Path C planned S44; process trace via STATE + git ([ADR-009-observability-paths-abc](../../02-design/decisions/ADR-009-observability-paths-abc.md)) |

## Models and endpoints

Fill when Track A is live. Record after first successful stack bring-up (task 02).

| Alias (agent yaml) | Routing | Status |
| :----------------- | :------ | :----- |
| `frontier-llm` | LiteLLM → OpenRouter (`anthropic/claude-sonnet-4`) | wired — not smoke-tested |
| `capable-llm` | LiteLLM → OpenRouter (`anthropic/claude-sonnet-4`) | **verified** smoke test 2026-06-20 |
| `fast-llm` | LiteLLM → OpenRouter (`anthropic/claude-haiku-4-5`) | wired — not smoke-tested |
| LiteLLM (human / curl) | `http://127.0.0.1:4000` | live |
| LiteLLM (OpenHands profiles) | `http://host.docker.internal:4000` | live — required for agent-server sandbox |
| OpenHands | `1.8` + agent-server `1.26.0-python` | **verified** smoke test 2026-06-20 |

## Harness-specific scope

Rules beyond [constraints/global](global.md) for **this repo**:

- **Meta-work** (STATE, dashboard, session docs) may touch `context/system/` and
  `_index/dashboard/` on session branches — not during arbitrary build tasks.
- **Build tasks** use `04-your-agents/tasks/*.md` scope lists only.
- **`_playground/`** is experiment space — never load into agent context unless
  the human names a path ([Agents](../../Agents.md)).
- **`_inbox/`** is intake — not canon until promoted into chapter paths.
- **No reader product code** in this repo — spine completion is harness/canon
  work per [session-roadmap-s19-s23](../../context/system/sessions/session-roadmap-s19-s23.md).

## Out of scope (this project)

| Item | Why |
| :---- | :---- |
| Reader's own app codebase | Separate repo when the reader starts their product |
| Langfuse / `viz/` / arc42 | Langfuse **done (S27)**; skeleton **done (S28)**; `viz/` stubs **done (S31)**; arc42 **done (S32)** |
| Full Ch. 07/08 reader product artifacts | Type A Harness Gap — reader repos |

## Reference

- Global guardrails: [constraints/global](global.md)
- Host machine: [constraints/host](host.md)
- Living task order: [PROJECT-PLAN](../PROJECT-PLAN.md)
- Execution: [vscode-hub](../../05-build/execution-tools/vscode-hub.md) · [track-b-checklist](../../05-build/execution-tools/track-b-checklist.md) · [openhands](../../05-build/execution-tools/openhands.md) · [bare-worktree-setup](../../05-build/execution-tools/bare-worktree-setup.md)
- Tooling seam: `_templates/tooling-manifest.md` · [ADR-010-vscode-hub-barbell](../../02-design/decisions/ADR-010-vscode-hub-barbell.md)
- Host seam: `_templates/host-profile.md` · [ADR-011-host-profile-seam](../../02-design/decisions/ADR-011-host-profile-seam.md)
