---
title: Execution tools — index
chapter: 00
status: in-progress
audience: [novice, seasoned, both]
tags: [setup, execution]
---

# Execution tools — index

Pick **one execution runtime** for build-phase work (Ch. 05). Design-phase tools
live in [[../design-tools/README|design-tools]] (separate folder — not listed
here).

**Track A (OpenHands) is ideal; Track B (VS Code hub) is fallback** when setup
confidence or budget favors IDE subscriptions over Docker + LiteLLM/OpenRouter.
See [[ADR-007-dual-execution-tracks]] for drivers and [[vscode-hub]] for the
Track B shell pattern.

## Tracks

| Track | Runtime | Book documentation |
| :---- | :------ | :----------------- |
| **A** — sandbox agent loop | OpenHands (Docker + LiteLLM/OpenRouter) | [[track-a-setup]] · [[openhands]] |
| **B** — VS Code hub | VS Code shell + extensions + CLI agents in terminal | [[vscode-hub]] · [[track-b-checklist]] |

Track B **adapter products** (Cursor, Claude Code, Codex, OpenCode, …) map to
stable concerns in `_templates/tooling-manifest.md` — not per-vendor guides.

## Barbell pattern (Track B)

| Zone | You touch | Book owns |
| :---- | :-------- | :-------- |
| **Core** | Follow ritual | [[session-workflow]], tasks, validators, `task_context.py` |
| **Host** | Fill [[host\|constraints/host]] | Concern rows in `_templates/host-profile.md` |
| **Tooling** | Fill [[tooling-manifest\|tooling-manifest]] + [[project\|constraints/project]] adapters | Concern rows only |
| **Shell** | VS Code workspace, extensions, terminal CLI | [[vscode-hub]] pattern |

Decision records: [[ADR-007-dual-execution-tracks]] · [[ADR-010-vscode-hub-barbell]] · [[ADR-011-host-profile-seam]]

## Shared harness (both tracks)

`tasks/*.md` · `scripts/task_context.py` · [[icom-plus-convention]] ·
[[session-workflow]] · D-001 (git on host shell — [[host|constraints/host]]) · [[bare-worktree-setup]]

## Where to go next

- **Design tools (Ch. 00):** [[../design-tools/README|design-tools index]]
- **Track B hub:** [[vscode-hub]]
- **Track B checklist:** [[track-b-checklist]]
- **Host profile:** [[host|constraints/host]] · `_templates/host-profile.md`
- **Tooling manifest template:** [[tooling-manifest|_templates/tooling-manifest.md]]
- **Path C hooks (Track B observability):** [[path-c-hook-contract]]
- **Decision records:** [[ADR-007-dual-execution-tracks]] · [[ADR-009-observability-paths-abc]] · [[ADR-010-vscode-hub-barbell]] · [[ADR-011-host-profile-seam]]
- **Track A setup:** [[track-a-setup]]
- **Track A execution:** [[openhands]]
- **Git layout:** [[bare-worktree-setup]]
- **Agent roster:** [[agent-team]]
