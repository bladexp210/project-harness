---
title: Design tools — index
chapter: 00
status: in-progress
audience: [novice, seasoned, both]
tags: [setup, design]
---

# Design tools — index

Pick **one design tool** for design-phase work (Ch. 00–04): understanding
roles and use cases, filling layer designs, writing ADRs, and shaping tasks
before build execution. Execution-phase tools live in
[execution-tools](../execution-tools/README.md) (separate folder).

**All listed tools are alternatives** — choose based on how you prefer to work
with local files, Obsidian, and agent-assisted authoring. There is no single
mandated vendor. Track B readers often use the same VS Code–compatible IDE for
design and build; see [vscode-hub](../../../05-build/execution-tools/vscode-hub.md).

## Tools

| Tool | Role | Book documentation |
| :---- | :---- | :----------------- |
| **Claude Cowork** | Desktop, local files, project memory | [cowork](cowork.md) |
| **Cursor** | IDE-integrated agent; overlaps Track B hub | [cursor](cursor.md) |
| **Antigravity** | Agent-first IDE, parallel agents | [antigravity](antigravity.md) |

Stubs note how each differs from the others. Full install scaffolds ship in a
later canon pass.

## What design tools do in this book

| Phase | Design tool owns | Execution tool owns (Ch. 05) |
| :---- | :--------------- | :----------------------------- |
| Ch. 01–02 | Roles, use cases, layer designs, ADRs | — |
| Ch. 03–04 | Task shaping, agent yaml review, context tree | — |
| Ch. 05+ | Review, course corrections | Bounded task runs from `tasks/*.md` via [vscode-hub](../../../05-build/execution-tools/vscode-hub.md) or [openhands](../../../05-build/execution-tools/openhands.md) |

Diagram and notation conventions apply across both phases — see
[diagram-taxonomy](../../../_playground/diagram-taxonomy.md) and [icom-plus-convention](../../../_playground/icom-plus-convention.md).

## Where to go next

- **Stubs:** [cowork](cowork.md) · [cursor](cursor.md) · [antigravity](antigravity.md)
- **Execution tools (build phase):** [execution-tools index](../execution-tools/README.md)
- **VS Code hub (Track B):** [vscode-hub](../../../05-build/execution-tools/vscode-hub.md)
- **Philosophy:** [manifesto](../../manifesto.md)
- **Decision records:** [ADR-007-dual-execution-tracks](../../../02-design/decisions/ADR-007-dual-execution-tracks.md) · [ADR-010-vscode-hub-barbell](../../../02-design/decisions/ADR-010-vscode-hub-barbell.md)
