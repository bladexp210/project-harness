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
[[../execution-tools/README|execution-tools]] (separate folder).

**All listed tools are alternatives** — choose based on how you prefer to work
with local files, Obsidian, and agent-assisted authoring. There is no single
mandated vendor. Track B readers often use the same VS Code–compatible IDE for
design and build; see [[vscode-hub]].

## Tools

| Tool | Role | Book documentation |
| :---- | :---- | :----------------- |
| **Claude Cowork** | Desktop, local files, project memory | [[cowork]] |
| **Cursor** | IDE-integrated agent; overlaps Track B hub | [[cursor]] |
| **Antigravity** | Agent-first IDE, parallel agents | [[antigravity]] |

Stubs note how each differs from the others. Full install scaffolds ship in a
later canon pass.

## What design tools do in this book

| Phase | Design tool owns | Execution tool owns (Ch. 05) |
| :---- | :--------------- | :----------------------------- |
| Ch. 01–02 | Roles, use cases, layer designs, ADRs | — |
| Ch. 03–04 | Task shaping, agent yaml review, context tree | — |
| Ch. 05+ | Review, course corrections | Bounded task runs from `tasks/*.md` via [[vscode-hub]] or [[openhands]] |

Diagram and notation conventions apply across both phases — see
[[diagram-taxonomy]] and [[icom-plus-convention]].

## Where to go next

- **Stubs:** [[cowork]] · [[cursor]] · [[antigravity]]
- **Execution tools (build phase):** [[../execution-tools/README|execution-tools index]]
- **VS Code hub (Track B):** [[vscode-hub]]
- **Philosophy:** [[manifesto]]
- **Decision records:** [[ADR-007-dual-execution-tracks]] · [[ADR-010-vscode-hub-barbell]]
