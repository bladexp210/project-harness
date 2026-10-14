---
title: Claude Cowork
chapter: 00
status: in-progress
audience: [novice, seasoned, both]
tags: [setup, design, cowork]
---

# Claude Cowork — primary design tool

Claude Cowork is the book's **primary design-phase tool**: a desktop agent
environment for working with local files, project memory, and Obsidian-compatible
vaults. Use it for Ch. 01–04 authoring — roles, layer designs, ADRs, task
shaping — before handing bounded build work to an execution tool (Ch. 05).

> [!LEARN] Learn It
> **What this is:** Anthropic's Cowork runs Claude on your machine with access
> to folders you choose — similar spirit to this book's "folder is the method"
> layout.
> **Why it is primary here:** local files stay in git, Obsidian wiki-links and
> callouts remain intact, and design work stays separate from Docker-based
> execution (Track A) or IDE build loops (Track B).
>
> Full install and workflow scaffold — step-by-step setup, memory configuration,
> and Obsidian vault wiring — ships in a later canon pass. This stub orients
> you; you still own tool versions and accounts.

> [!TIP] Fast Track
> Install Cowork → grant access to your product repo (or this harness for
> learning) → open Ch. 01 → use the agent for discovery questions in each
> template section. Pair with git session branches per [[session-workflow]].
> You own the outcome.

## Role in the harness

| Concern | Cowork | Not Cowork |
| :------ | :----- | :--------- |
| Fill `user-roles.md`, layer files, ADRs | Yes | — |
| Run OpenHands / Track B on `tasks/*.md` | — | Ch. 05 execution tools |
| Commit or merge on Windows (D-001) | Human | Agent proposes; human runs git |

## vs. alternatives

| vs. | Cowork advantage |
| :-- | :--------------- |
| [[cursor]] | Desktop-first project memory; less tied to a single IDE workspace |
| [[antigravity]] | Mature desktop workflow; Cowork is the book's default design path |

## Where to go next

- **Design tools index:** [[README]]
- **Execution tools:** [[../execution-tools/README|execution-tools]]
- **Notation:** [[diagram-taxonomy]] · [[icom-plus-convention]]

## Connector stub (fictional)

This public book does not wire agents to a private wiki, ticket system, or employer source of truth. When you connect a tool, use a stub like this and replace the values yourself:

| Field | Example value |
| :--- | :--- |
| Source name | `acme-policy-docs` |
| Base URL | `https://docs.example.internal` |
| Auth | Local secret named `YOUR_DOCS_TOKEN` — never commit the value |
| Allowed reads | `/policies/pto.md` only |
| Procedure | Cite the clause. If the source and the question disagree, stop and ask a human. |
