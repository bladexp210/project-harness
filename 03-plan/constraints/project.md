---
title: Project Constraints
chapter: 03
status: living
audience: [novice, seasoned, both]
tags: [constraint, harness]
---

# Project constraints — this harness repo

Project-specific rules for **this book-as-harness repository**. You inherit
[[global|constraints/global]] and [[host|constraints/host]]; this file holds
identity, track choice, and tool adapters — not OS/shell facts (those live in
`host.md`).

> [!LEARN] Learn It
> **Global vs host vs project:** `global.md` — inherited guardrails.
> `host.md` — your machine and shell (copy-paste dialect, D-001).
> `project.md` — tool choices, git layout, adapters.

> [!TIP] Fast Track
> Fill [[host|constraints/host]] first → identity → execution track → git layout
> → tool adapters → models.

## Identity

| Field | Value |
| :---- | :---- |
| Project | Methodology book / harness (`project-harness`) |
| Product type | Docs-only repo — teaches and operates as a real harness |
| Primary author | Human (Alex) + Track B IDE agents |
| Remote | None (local-only; D-001 per [[host\|constraints/host]]) |

## Execution track

| Field | Value |
| :---- | :---- |
| **Authoring today** | Track B — Cursor IDE agent |
| **Target for build tasks** | Track A — [[openhands]] when Docker + LiteLLM ready (S21) |
| **Decision record** | [[ADR-007-dual-execution-tracks]] |
| **Session ritual** | [[session-workflow]] — branch `session-NN/<topic>` per session |

## Git layout

| Field | Value |
| :---- | :---- |
| **Current (ramp)** | Normal clone; session branches on same working tree |
| **Target** | Bare hub + worktrees per [[bare-worktree-setup]] |
| **Protected branch** | `main` — merge only after session close + human review |
| **Commit author** | Human on host shell — see `constraints/host.md` (D-001) |

## Tool adapters (Track B — VS Code hub / Cursor)

Living instance of `_templates/tooling-manifest.md`. Map [[track-b-checklist]]
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
| Observability export | Path C planned S44; process trace via STATE + git ([[ADR-009-observability-paths-abc]]) |

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

Rules beyond [[global|constraints/global]] for **this repo**:

- **Meta-work** (STATE, dashboard, session docs) may touch `context/system/` and
  `_index/dashboard/` on session branches — not during arbitrary build tasks.
- **Build tasks** use `04-your-agents/tasks/*.md` scope lists only.
- **`_playground/`** is experiment space — never load into agent context unless
  the human names a path ([[Agents.md|Agents]]).
- **`_inbox/`** is intake — not canon until promoted into chapter paths.
- **No reader product code** in this repo — spine completion is harness/canon
  work per [[session-roadmap-s19-s23]].

## Out of scope (this project)

| Item | Why |
| :---- | :---- |
| Reader's own app codebase | Separate repo when the reader starts their product |
| Langfuse / `viz/` / arc42 | Langfuse **done (S27)**; skeleton **done (S28)**; `viz/` stubs **done (S31)**; arc42 **done (S32)** |
| Full Ch. 07/08 reader product artifacts | Type A Harness Gap — reader repos |

## Reference

- Global guardrails: [[global|constraints/global]]
- Host machine: [[host|constraints/host]]
- Living task order: [[03-plan/PROJECT-PLAN|PROJECT-PLAN]]
- Execution: [[vscode-hub]] · [[track-b-checklist]] · [[openhands]] · [[bare-worktree-setup]]
- Tooling seam: `_templates/tooling-manifest.md` · [[ADR-010-vscode-hub-barbell]]
- Host seam: `_templates/host-profile.md` · [[ADR-011-host-profile-seam]]
