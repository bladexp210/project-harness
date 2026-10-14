---
title: Glossary
status: reference
tags: [glossary, vocabulary, index]
---

# Glossary

Quick reference for qualified vocabulary, decisions, budgets, and debt IDs.
See [[ADR-004-lifecycle-vocabulary]] for the full lifecycle rationale.

## Qualified lifecycles (ADR-004)

Book text never uses `lifecycle` bare — always qualify with the subject:

| Term | Subject | Ending verb |
| :---- | :---- | :---- |
| **Product lifecycle** | the product | sunset |
| **User lifecycle** | one user/account | offboard |
| **Feature lifecycle** | one capability | retire (or prune if never built) |
| **Data lifecycle** | one record/class | delete / archive |
| **Task lifecycle** | one unit of work | close |

Removal verbs (ADR-003): **prune** (never built) · **retire** (shipped feature) · **sunset** (product).

## ADR index

| ID | Title | Status |
| :---- | :---- | :---- |
| [[ADR-001-chapter-folder-naming]] | Chapter folder naming | accepted |
| [[ADR-002-modeling-conventions]] | Modeling — Mermaid + ICOM/Gherkin | accepted |
| [[ADR-003-removal-vocabulary]] | Removal vocabulary — prune/retire/sunset | accepted |
| [[ADR-004-lifecycle-vocabulary]] | Five lifecycles, never bare | accepted |
| [[ADR-005-failure-condition-convention]] | Failure-condition convention | accepted |
| [[ADR-006-teaching-block-convention]] | Teaching-block convention | accepted |

## Budget table

From [[global|constraints/global]] — machine-enforced by `validate_md.py` (≤5% over = WARN, >5% = FAIL):

| Artifact | Limit |
| :---- | :---- |
| Agent definition (yaml) | ≤ 60 lines |
| TASK.md | ≤ 100 lines |
| Layer-1 context file | ≤ 200 lines |
| Source module (.py) | ≤ 300 lines |
| Mermaid diagram | ≤ 20 nodes (ADR-002) |

## Debt IDs

| ID | One-line summary | Status |
| :---- | :---- | :---- |
| D-001 | Git Windows-side only (sandbox NUL corruption) | active |
| D-002 | Session-1 sub-headings not promoted to `###` | active |
| D-003 | Wiki-link resolution in validator | **resolved S9** |
| D-004 | STATE.md manual session close | active |
| D-005 | NC-ND cache specifics need vendor re-verify | active |
| D-006 | Budget enforcement in validator | **resolved S8** |
| D-007 | Layer-1 budget 150 → 200 renegotiation | **resolved S8** |
