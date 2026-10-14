---
title: "arc42 §2 — Constraints"
chapter: 02
status: reference
audience: [novice, seasoned, both]
tags: [arc42, design, harness]
---

# arc42 §2 — Constraints

**Question answered:** What limits design and implementation choices for the
whole system?

> [!NOTE] REAL — harness-meta
> Constraints for **this repo**. Single source of truth lives in
> `03-plan/constraints/` — this section indexes and summarizes; it does not
> duplicate every row.

## Constraint sources

| Layer | File | Scope |
| :---- | :--- | :---- |
| Global (inherited) | [global](../../03-plan/constraints/global.md) | Every reader inherits — repo discipline, budgets, AI execution |
| Host (reader machine) | [constraints/host](../../03-plan/constraints/host.md) | OS, shell, copy-paste dialect, D-001 instance |
| Project (this harness) | [project](../../03-plan/constraints/project.md) | Tool choices, git layout, Track A/B, harness-specific scope |

Open the full files before changing behavior — §2 is the arc42 index.

## Organizational and process

| Constraint | In this harness | Source |
| :--------- | :-------------- | :----- |
| Session ritual | Branch `session-NN/<topic>`; Plan → Proceed → Execute; close draft before merge | [session-workflow](../../context/system/session-workflow.md), `project.md` |
| Git writes on host shell | Human runs commit, merge, push (D-001) per [constraints/host](../../03-plan/constraints/host.md) | `host.md`, [Agents](../../Agents.md) |
| Protected `main` | Merge only after human validates work diff + handoff docs | `project.md` |
| Atomic commits | One logical change per commit; Conventional Commits | [global](../../03-plan/constraints/global.md) |
| Significant decisions → ADR | Red-team challenge before final; index in §9 | [global](../../03-plan/constraints/global.md), [09-architectural-decisions](09-architectural-decisions.md) |
| Meta-work scope | STATE, dashboard, `context/system/` on session branches — not arbitrary build tasks | `project.md` |

## Technical

| Constraint | In this harness | Source |
| :--------- | :-------------- | :----- |
| Docs-only product | Book-as-folder-structure; no reader app code in this repo | `project.md` |
| Track B authoring | Cursor IDE agent + `AGENTS.md` load table today | `project.md`, [ADR-007-dual-execution-tracks](../decisions/ADR-007-dual-execution-tracks.md) |
| Track A build target | OpenHands + LiteLLM compose when Docker ready | `project.md`, [track-a-setup](../../05-build/execution-tools/track-a-setup.md) |
| Deterministic context | Tasks name `context_load` paths — no vector search | [context-loader](../../04-your-agents/context-loader.md), `project.md` |
| Validator on every commit | `validate_md.py` + pre-commit; frontmatter required | [global](../../03-plan/constraints/global.md) |
| Diagram budgets | ≤ 20 Mermaid nodes ([ADR-002-modeling-conventions](../decisions/ADR-002-modeling-conventions.md)); separate Container vs Deployment canvases | [diagram-taxonomy](../../_playground/diagram-taxonomy.md), `viz/` |
| No secrets in repo | gitleaks on commit; `.env` never committed | [global](../../03-plan/constraints/global.md) |

## Conventions

| Constraint | In this harness | Source |
| :--------- | :-------------- | :----- |
| Chapter folders | `NN-short-title/` kebab-case ([ADR-001-chapter-folder-naming](../decisions/ADR-001-chapter-folder-naming.md)) | ADR-001 |
| Teaching vs artifact zones | ADR-006 delimiters; fog-word lint on artifact zones | [ADR-006-teaching-block-convention](../decisions/ADR-006-teaching-block-convention.md) |
| Reader-facing gates | Plain language; numbered scope lists ([ADR-008-reader-facing-language-and-visuals](../decisions/ADR-008-reader-facing-language-and-visuals.md)) | ADR-008 |
| Removal vocabulary | prune · retire · sunset ([ADR-003-removal-vocabulary](../decisions/ADR-003-removal-vocabulary.md)) | ADR-003 |
| Failure conditions | Every pattern names when not to apply ([ADR-005-failure-condition-convention](../decisions/ADR-005-failure-condition-convention.md)) | ADR-005 |

## Budgets (split triggers)

Inherited from [global](../../03-plan/constraints/global.md) — machine-checked by `validate_md.py`:

| Artifact | Budget | Over-budget action |
| :------- | :----- | :----------------- |
| Source module | ≤ 300 lines | Decompose or renegotiate + DEBT-LEDGER |
| Layer 1 context file | ≤ 200 lines | Move detail to Layer 2 |
| TASK.md | ≤ 100 lines | Decompose the task |
| Agent yaml | ≤ 60 lines | Fork a specialist role |

Grace band: ≤ 5% over = warning; > 5% = commit blocked.

## Out of scope (project-level)

From `project.md` — not constraints on the *method*, but boundaries on *this
repo*:

| Item | Why |
| :---- | :---- |
| Reader's product codebase | Separate repo when reader builds |
| `_playground/` in agent context | Experiments — not canon until promoted |
| `_inbox/` as canon | Intake only until promoted to chapter paths |

## ESL checklist (this section)

| Rule | Pass |
| :---- | :---- |
| Link don't duplicate | Full rows in `constraints/` |
| Global + host + project split | All three sources indexed |
| Applies everywhere | Process, technical, and convention rows |
| Product fork reminder | Reader replaces `project.md` |

## Where to go next

- **Global guardrails:** [global](../../03-plan/constraints/global.md)
- **Host profile:** [constraints/host](../../03-plan/constraints/host.md)
- **Harness project file:** [project](../../03-plan/constraints/project.md)
- **Solution strategy (§4):** [04-solution-strategy](04-solution-strategy.md)
- **Section index:** [README](README.md)
