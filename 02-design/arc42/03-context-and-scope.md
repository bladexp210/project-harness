---
title: "arc42 §3 — Context and Scope"
chapter: 02
status: reference
audience: [novice, seasoned, both]
tags: [arc42, design, harness, L1]
---

# arc42 §3 — Context and Scope

**Question answered:** Where does the system end, who uses it, and which
external systems does it talk to?

> [!NOTE] REAL — harness-meta
> This section describes **this repo** (the book-as-harness). Your product
> fork replaces the central system, actors, and externals — keep the same
> arc42 shape.

## Scope statement

The **Project Harness Book** is the system under documentation: a
book-as-folder-structure (`00`–`08`) that teaches AI-assisted software
development and operates as a functional project harness (validator, agents,
session workflow, Track A/B execution guides).

**In scope:** reader-facing chapters, harness meta (`STATE`, dashboard,
`context/`), notation stubs (`viz/`), and execution scaffolds (Track A
compose, reader-skeleton template).

**Out of scope:** the reader's own product codebase (separate repo when they
build), full Ch. 07/08 reader-product runbooks, and `_playground/` experiments
until promoted.

## Context diagram

arc42 §3 maps to **C4 System Context** (L1 static). The worked harness
diagram lives in [context](../../viz/c4/context.md) — single source; this section links it
rather than duplicating the canvas.

| Element | In this harness |
| :------ | :-------------- |
| Central system | Project Harness Book repo |
| Human actors | Reader; co-author (human gate) |
| External systems | Reader product repo; LLM API; Obsidian vault |
| Not at this zoom | LiteLLM, OpenHands, Langfuse — L2 Container ([container](../../viz/c4/container.md)) |

Open the diagram: [C4 System Context — harness example](../../viz/c4/context.md)

## External interfaces (summary)

| External | Direction | Purpose |
| :------- | :-------- | :------ |
| Reader | In | Follows chapters; runs session workflow |
| Obsidian | In/out | Vault editing; wiki-links; Quartz publish chain |
| LLM API | Out | Track A agent calls via LiteLLM / OpenRouter |
| Reader product repo | Out | Scaffolded by book; not stored in harness |

## ESL checklist (this section)

| Rule | Pass |
| :---- | :---- |
| Boundary explicit | In/out scope table above |
| Diagram linked not pasted | [context](../../viz/c4/context.md) |
| L1 node budget | See diagram file (≤ 7) |
| Static context only | Runtime order → §6 or [dynamic](../../viz/c4/dynamic.md) |

## Where to go next

- **C4 Context diagram:** [context](../../viz/c4/context.md)
- **Building blocks (§5):** [05-building-block-view](05-building-block-view.md)
- **Dashboard L1 (session zoom, not C4):** `_index/dashboard/01-context.md`
