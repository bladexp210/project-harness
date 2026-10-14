---
title: "arc42 §12 — Glossary"
chapter: 02
status: reference
audience: [novice, seasoned, both]
tags: [arc42, design, vocabulary, harness]
---

# arc42 §12 — Glossary

**Question answered:** What do domain terms mean in this project?

> [!NOTE] REAL — harness-meta
> Terms for **this repo**. Define once; link from prose with
> `[[12-glossary#term|term]]`. Canonical ADR and index definitions live in
> `02-design/decisions/` and [[../../_index/glossary|_index/glossary.md]] —
> **link, do not duplicate** long rationale here.

## How to use this section

| Rule | Why |
| :---- | :---- |
| One definition per term | arc42 §12 is the architecture doc index; `_index/glossary.md` is the repo-wide quick reference |
| ADR terms → link to ADR | prune/retire/sunset, ADR-004 five kinds, failure conditions — full text in decisions/ |
| Product terms below the harness table | Your fork adds rows; keep harness rows as examples |

Full qualified-vocabulary table and budget limits: [[../../_index/glossary|_index/glossary.md]].

## Harness and methodology terms

| Term | Definition |
| :---- | :--------- |
| **Harness Gap (Type A)** | A book-repo slot that should hold reader-specific content but is still empty or stub-only in this repo. See dashboard [[../../_index/dashboard/02-containers\|L2 Containers]]. |
| **Canon Gap (Type B)** | Methodology or teaching debt that affects every reader — not a missing product artifact. |
| **Book-as-folder-structure** | This repo: chapters `00`–`08` teach the method and operate as the project harness. |
| **Session workflow** | Plan → Proceed → Execute → Close draft → Validate → Merge. Canonical: [[session-workflow]]. |
| **Human gate** | Explicit human approval before irreversible or scope-binding action — Proceed, validate, merge. |
| **Close draft** | Agent updates STATE + dashboard L1–L3 + next bootstrap **before** merge is offered. |
| **Bootstrap** | STATE **Next session bootstrap** block — branch, primary, load first, defer. |
| **Meta-work** | Harness maintenance (STATE, dashboard, `context/system/`, arc42) vs reader product code in a fork. |
| **Golden task** | Evaluator fixture in `04-your-agents/golden-tasks/` — proves agent pack + loader behavior. |
| **Grounding package** | Deterministic `context/` tree loaded per task — no vector search. |

## Execution tracks (ADR-007)

| Term | Definition |
| :---- | :--------- |
| **Track A** | Ideal build path — OpenHands + LiteLLM compose on Docker; Langfuse observability. [[track-a-setup]] |
| **Track B** | Fallback authoring — IDE agent (Cursor) + `AGENTS.md` load table; human git (D-001). |

## Removal verbs (ADR-003) and ADR-004 vocabulary

Link for full rationale — do not redefine in prose.

| Term | Canonical definition |
| :---- | :------------------- |
| **prune** | Remove from plan before build — [[../decisions/ADR-003-removal-vocabulary\|ADR-003]] |
| **retire** | Turn off a shipped feature — [[../decisions/ADR-003-removal-vocabulary\|ADR-003]] |
| **sunset** | End the product — [[../decisions/ADR-003-removal-vocabulary\|ADR-003]] |
| **Product / user / feature / data / task lifecycle** | Five named kinds — always qualify the noun — [[../decisions/ADR-004-lifecycle-vocabulary\|ADR-004]] |

## Design and documentation terms

| Term | Definition |
| :---- | :--------- |
| **arc42** | 12-section architecture documentation template — this folder. Not a diagram notation. |
| **ICOM+** | Task notation — Inputs, Outputs, Controls, Mechanisms. [[icom-plus-convention]] |
| **ADR** | Architecture Decision Record — `02-design/decisions/`; indexed in §9. |
| **Failure condition** | Named circumstances when a recommended pattern is wrong — [[../decisions/ADR-005-failure-condition-convention\|ADR-005]]. |
| **Teaching block** | Instruction delimited from artifact zones — [[../decisions/ADR-006-teaching-block-convention\|ADR-006]]. |
| **viz/** | Rendered diagram stubs and harness examples — C4, BPMN, UML, DMN, ICOM. |

## Debt IDs (active)

| ID | One-line summary |
| :---- | :---------------- |
| D-001 | Git writes on host shell only — see `constraints/host.md` ([[ADR-011-host-profile-seam]]) |
| D-002 | Session-1 `###` promotion pending |
| D-004 | STATE manual close — automate if two skips |
| D-005 | NC-ND cache specifics — re-verify before external Ch. 02 publish |

Resolved IDs and budget table: [[../../_index/glossary#Debt IDs|_index/glossary.md]].

## Your product terms

Add rows below when you fork — keep harness rows above as reference examples.

| Term | Definition |
| :---- | :--------- |
| *(your domain term)* | *(one sentence)* |

## ESL checklist (this section)

| Rule | Pass |
| :---- | :---- |
| ADR terms linked, not copied | Removal + ADR-004 rows link to ADR-003/004 |
| Harness vs product split clear | "Your product terms" table empty scaffold |
| Cross-link to _index/glossary | Budget + resolved debts delegated |
| Product fork reminder | Reader adds domain rows |

## Where to go next

- **Repo glossary index:** [[../../_index/glossary]]
- **ADR vocabulary decisions:** [[09-architectural-decisions]]
- **Section index:** [[README]]
