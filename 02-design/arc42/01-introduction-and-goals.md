---
title: "arc42 §1 — Introduction and Goals"
chapter: 02
status: reference
audience: [novice, seasoned, both]
tags: [arc42, design, harness]
---

# arc42 §1 — Introduction and Goals

**Question answered:** What should the system do, for whom, and which quality
goals matter most?

> [!NOTE] REAL — harness-meta
> Requirements for **this repo** (the book-as-harness). Your product fork
> replaces stakeholders, use cases, and quality goals — keep the same arc42
> shape and link to Ch. 01 rather than duplicating whole chapters.

## Requirements overview

The **Project Harness Book** teaches AI-assisted software development through
a book-as-folder-structure (`00`–`08`) that also **operates** as a functional
harness: session workflow, validator, agent pack, context tree, and Track A/B
execution guides.

**Slogan:** Go beyond vibe coding to reach top 1% AI-assisted software project
development ([manifesto](../../00-start-here/manifesto.md)).

**Primary outcomes:**

| Outcome | Evidence in harness |
| :------ | :------------------ |
| Reader learns the method by doing | Chapter spine + golden tasks |
| Reader runs real sessions with agents | [session-workflow](../../context/system/session-workflow.md), [Agents](../../Agents.md) |
| Reader forks to their own product repo | [reader-skeleton](../../06-learn/boilerplate/reader-skeleton/README.md) |
| Canon stays verifiable | `validate_md.py`, golden-task evaluator |

Full role and use-case methodology: [Ch. 01user roles](../../01-understand/user-roles.md) · [Ch. 01 use cases](../../01-understand/use-cases.md).

## Stakeholders (this harness)

| Stakeholder | Role | Primary expectation |
| :---------- | :--- | :------------------ |
| Reader | Follows chapters; runs sessions; builds their product in a separate repo | Clear next step every session; no stale handoff |
| Co-author | Human gate — scope, review, git on Windows (D-001) | Know what each approval binds and does not bind |
| AI agent | Track B authoring today; Track A for build tasks when stack is live | Load only task-listed context; never commit unless asked |
| Operator | Same person as co-author for this repo | Validator green; session branch merged cleanly |

Context diagram actors: [03-context-and-scope](03-context-and-scope.md) · [context](../../viz/c4/context.md).

## Use cases and priorities

Harness-meta use cases rated with the **same frequency × importance matrix**
as Ch. 01 (`priority = freq × importance`, max 12). Full teaching template:
[use-cases](../../01-understand/use-cases.md).

| Role | Use case | Frequency | Importance | Priority |
| :---- | :------- | :-------- | :--------- | :------- |
| Reader | Complete a session (open → build → close → merge) | Daily | Critical | 12 |
| Co-author | Approve scope at Proceed gate | Daily | Critical | 12 |
| Co-author | Run git commit and merge (D-001) | Daily | Critical | 12 |
| Agent | Load only paths listed in `context_load` | Daily | Critical | 12 |
| Reader | Follow chapter spine and apply to own product | Weekly | Critical | 8 |
| Agent | Produce close draft (STATE + dashboard L1–L3) | Weekly | Critical | 8 |
| Reader | Run Track A golden path (Task 02) | Weekly | High | 6 |
| Co-author | Validate work diff and handoff before merge | Daily | Critical | 12 |

**Tie-break note:** Daily × Critical rows share priority 12 — session
workflow order (Plan → Proceed → Execute → Close) sequences them; see
[session-workflow](../../context/system/session-workflow.md).

## Quality goals (derived from priorities)

Top three goals mirror the **highest-scoring use cases** above — not a
separate wish list.

| # | Quality goal | Measurable signal | Use cases served |
| :-: | :----------- | :---------------- | :--------------- |
| 1 | **Handoff continuity** | STATE + dashboard L1–L3 accurate at every session close; next agent needs no re-discovery | Session complete; close draft |
| 2 | **Human gate integrity** | Irreversible actions (merge, scope bind) require explicit human signal; D-001 git on Windows | Proceed; commit/merge; validate |
| 3 | **Verifiable canon** | `validate_md.py --all` zero failures and golden-task suite green before merge offered | Context load; chapter follow |

Deferred quality work (lower priority): full Ch. 07/08 reader-product
runbooks, diagram-explorer HTML, bulk `_inbox/` promotion.

## ESL checklist (this section)

| Rule | Pass |
| :---- | :---- |
| One-page summary | Overview + tables; Ch. 01 holds full methodology |
| Stakeholders named | Reader, co-author, agent, operator |
| Quality goals trace to use cases | Top 3 derived from priority 12 rows |
| Product fork reminder | Reader replaces harness-meta rows |

## Where to go next

- **Ch. 01 templates:** [user-roles](../../01-understand/user-roles.md), [use-cases](../../01-understand/use-cases.md)
- **Constraints (§2):** [02-constraints](02-constraints.md)
- **Context boundary (§3):** [03-context-and-scope](03-context-and-scope.md)
- **Section index:** [README](README.md)
