---
title: "arc42 §5 — Building Block View"
chapter: 02
status: reference
audience: [novice, seasoned, both]
tags: [arc42, design, static, harness, L2, L3]
---

# arc42 §5 — Building Block View

**Question answered:** Of what static parts does the system consist, and how
are they nested?

> [!NOTE] REAL — harness-meta
> White-box hierarchy for **this repo** (the book-as-harness). Your product
> fork replaces containers and components — keep the same arc42 shape and
> link diagrams in `viz/` rather than pasting canvases here.

## Decomposition summary

The harness decomposes into eight **logical containers** (C4 L2) inside the
repo boundary. One container — **Agent pack** — has a worked **component**
view (C4 L3). Other containers stay at L2 unless you need their internals.

| Level           | Question                          | Harness diagram       |
| :-------------- | :-------------------------------- | :-------------------- |
| L2 — Containers | What modules make up the repo?    | [[viz/c4/container]]  |
| L3 — Components | What parts sit inside Agent pack? | [[viz/c4/component]]  |
| L4 — Task grain | One ICOM+ work unit               | [[viz/icom/task-box]] |
| Code grain      | Optional C4 Code                  | defer until needed    |

Open the diagrams:

- [[viz/c4/container|C4 Container — harness example]]
- [[viz/c4/component|C4 Component — harness example]]

## Container inventory (this harness)

| Container | Path / anchor | Role |
| :-------- | :------------ | :--- |
| Chapter spine | `00`–`08` | Teaching chapters the reader follows |
| Harness meta | `STATE.md`, `_index/dashboard/` | Session truth and visual status |
| Agent pack | `04-your-agents/` | Agent yaml, tasks, golden-tasks, evaluator |
| Context tree | `context/` | Layered architecture + implementation context |
| Design canon | `02-design/`, `viz/`, `arc42/` | ADRs, notation, arc42 sections |
| Plan layer | `03-plan/` | PROJECT-PLAN, constraints |
| Validator scripts | `scripts/`, pre-commit | `validate_md.py`, golden-task tests |
| Execution tools | `05-build/execution-tools/` | Track A/B guides, compose scaffolds |

Cross-container dependencies (static only) are on the [[viz/c4/container]]
canvas — not repeated here.

## Component zoom — Agent pack

When the question is *inside* `04-your-agents/`, use L3:

| Component | Role |
| :-------- | :--- |
| Agent definitions | `agents/*.yaml` — roles and policies |
| Task specs | `tasks/*.md` — ICOM+ work units with `context_load` |
| Golden tasks | Regression fixtures for evaluator |
| Context loader | `task_context.py` + [[context-loader]] rules |
| Evaluator path | Golden tests + fog-word lint |

Full diagram: [[viz/c4/component|C4 Component — harness example]]

## ESL checklist (this section)

| Rule | Pass |
| :---- | :---- |
| Static decomposition only | Runtime order → §6 or [[viz/c4/dynamic]] |
| Diagram linked not pasted | [[viz/c4/container]], [[viz/c4/component]] |
| L2 before L3 | Container drawn before Component zoom |
| Container ≠ Deployment | Physical nodes → §7 or [[viz/c4/deployment]] |
| One container per L3 canvas | Agent pack only at L3 in harness |

## Where to go next

- **Context boundary (§3):** [[03-context-and-scope]]
- **Runtime collaboration (§6):** [[06-runtime-view]]
- **C4 section index:** [[viz/c4/README]]
- **Section index:** [[README]]
