---
title: Execution tools — index
chapter: 00
status: in-progress
audience: [novice, seasoned, both]
tags: [setup, execution]
---

# Execution tools — index

Pick **one execution runtime** for build-phase work (Ch. 05). Design-phase tools
live in [design-tools](../design-tools/README.md) (separate folder — not listed
here).

**Track A (OpenHands) is ideal; Track B (VS Code hub) is fallback** when setup
confidence or budget favors IDE subscriptions over Docker + LiteLLM/OpenRouter.
See [ADR-007-dual-execution-tracks](../../../02-design/decisions/ADR-007-dual-execution-tracks.md) for drivers and [vscode-hub](../../../05-build/execution-tools/vscode-hub.md) for the
Track B shell pattern.

## Tracks

| Track | Runtime | Book documentation |
| :---- | :------ | :----------------- |
| **A** — sandbox agent loop | OpenHands (Docker + LiteLLM/OpenRouter) | [track-a-setup](../../../05-build/execution-tools/track-a-setup.md) · [openhands](../../../05-build/execution-tools/openhands.md) |
| **B** — VS Code hub | VS Code shell + extensions + CLI agents in terminal | [vscode-hub](../../../05-build/execution-tools/vscode-hub.md) · [track-b-checklist](../../../05-build/execution-tools/track-b-checklist.md) |

Track B **adapter products** (Cursor, Claude Code, Codex, OpenCode, …) map to
stable concerns in `_templates/tooling-manifest.md` — not per-vendor guides.

## Barbell pattern (Track B)

| Zone | You touch | Book owns |
| :---- | :-------- | :-------- |
| **Core** | Follow ritual | [session-workflow](../../../context/system/session-workflow.md), tasks, validators, `task_context.py` |
| **Host** | Fill [constraints/host](../../../03-plan/constraints/host.md) | Concern rows in `_templates/host-profile.md` |
| **Tooling** | Fill [tooling-manifest](../../../_templates/tooling-manifest.md) + [constraints/project](../../../03-plan/constraints/project.md) adapters | Concern rows only |
| **Shell** | VS Code workspace, extensions, terminal CLI | [vscode-hub](../../../05-build/execution-tools/vscode-hub.md) pattern |

Decision records: [ADR-007-dual-execution-tracks](../../../02-design/decisions/ADR-007-dual-execution-tracks.md) · [ADR-010-vscode-hub-barbell](../../../02-design/decisions/ADR-010-vscode-hub-barbell.md) · [ADR-011-host-profile-seam](../../../02-design/decisions/ADR-011-host-profile-seam.md)

## Shared harness (both tracks)

`tasks/*.md` · `scripts/task_context.py` · [icom-plus-convention](../../../_playground/icom-plus-convention.md) ·
[session-workflow](../../../context/system/session-workflow.md) · D-001 (git on host shell — [constraints/host](../../../03-plan/constraints/host.md)) · [bare-worktree-setup](../../../05-build/execution-tools/bare-worktree-setup.md)

## Where to go next

- **Design tools (Ch. 00):** [design-tools index](../design-tools/README.md)
- **Track B hub:** [vscode-hub](../../../05-build/execution-tools/vscode-hub.md)
- **Track B checklist:** [track-b-checklist](../../../05-build/execution-tools/track-b-checklist.md)
- **Host profile:** [constraints/host](../../../03-plan/constraints/host.md) · `_templates/host-profile.md`
- **Tooling manifest template:** [_templates/tooling-manifest.md](../../../_templates/tooling-manifest.md)
- **Path C hooks (Track B observability):** [path-c-hook-contract](../../../05-build/execution-tools/path-c-hook-contract.md)
- **Decision records:** [ADR-007-dual-execution-tracks](../../../02-design/decisions/ADR-007-dual-execution-tracks.md) · [ADR-009-observability-paths-abc](../../../02-design/decisions/ADR-009-observability-paths-abc.md) · [ADR-010-vscode-hub-barbell](../../../02-design/decisions/ADR-010-vscode-hub-barbell.md) · [ADR-011-host-profile-seam](../../../02-design/decisions/ADR-011-host-profile-seam.md)
- **Track A setup:** [track-a-setup](../../../05-build/execution-tools/track-a-setup.md)
- **Track A execution:** [openhands](../../../05-build/execution-tools/openhands.md)
- **Git layout:** [bare-worktree-setup](../../../05-build/execution-tools/bare-worktree-setup.md)
- **Agent roster:** [agent-team](../../../context/system/agent-team.md)
