---
title: "arc42 §6 — Runtime View"
chapter: 02
status: reference
audience: [novice, seasoned, both]
tags: [arc42, design, dynamic, harness]
---

# arc42 §6 — Runtime View

**Question answered:** How do building blocks collaborate at runtime?

> [!NOTE] REAL — harness-meta
> Runtime views for **this repo** — session operations (Track B) and Track A
> task execution. Use the **process stack** (BPMN, UML sequence, C4 Dynamic,
> DMN) — not static C4 Context/Container canvases. See
> [diagram-taxonomy](../../_playground/diagram-taxonomy.md#two-stacks-do-not-merge).

## Scenario map

| Priority | Scenario | Primary notation | Diagram |
| :------- | :------- | :--------------- | :------ |
| **Primary** | Session close → merge to `main` | C4 Dynamic | [dynamic](../../viz/c4/dynamic.md) |
| **Secondary** | Task 02 golden path on Track A | BPMN Variant B | [process-subset](../../viz/bpmn/process-subset.md) |
| **Secondary** | Task 02 message trace (OpenHands stack) | UML sequence Variant B | [sequence](../../viz/uml/sequence.md) |
| **Secondary** | Track A vs Track B mechanism choice | DMN Variant B | [decision-table](../../viz/dmn/decision-table.md) |
| Alternative | Session open → Proceed gate | BPMN / UML / DMN Variant A | [process-subset](../../viz/bpmn/process-subset.md), [sequence](../../viz/uml/sequence.md), [decision-table](../../viz/dmn/decision-table.md) |

Draw **one scenario per canvas**. Pair with static [§5](05-building-block-view.md)
containers before adding numbered flows.

## Primary — session close (C4 Dynamic)

**Question:** How do harness containers collaborate when a reader closes a
session and merges to `main`?

The worked diagram reuses elements from [container](../../viz/c4/container.md) with **numbered
collaboration arrows** — validate diff, close draft, run validator, human git
(D-001), archive session.

Open: [C4 Dynamic — harness example](../../viz/c4/dynamic.md)

| Step | Building block | Harness action |
| :---- | :------------- | :------------- |
| 1 | Reader + Harness meta | Human validates work diff + handoff docs |
| 2–3 | Agent pack + Harness meta | Agent updates STATE + dashboard L1–L3 |
| 4–5 | Validator scripts | `validate_md.py --all` — zero failures |
| 6–7 | Reader + Harness meta + Chapter spine | Human commit/merge; session archived |

Procedure detail: [session-workflow](../../context/system/session-workflow.md) · [Agents](../../Agents.md) § Session close

## Secondary — Track A Task 02

**Question:** How does the golden-path task run on the OpenHands stack?

These three diagrams answer **different facets** of the same Track A scenario
— pick by question, not by preference for one notation.

| Notation | Question it answers | Link |
| :------- | :---------------- | :--- |
| BPMN Variant B | Step-by-step process with lanes | [process-subset](../../viz/bpmn/process-subset.md) |
| UML sequence Variant B | Message order (OpenHands, LiteLLM, repo) | [sequence](../../viz/uml/sequence.md) |
| DMN Variant B | When Track A vs Track B applies | [decision-table](../../viz/dmn/decision-table.md) |

Task spec: `04-your-agents/tasks/02-track-a-golden-path.md` · Stack:
[track-a-setup](../../05-build/execution-tools/track-a-setup.md)

## Alternative — session open (Variant A family)

When the question is **Plan → Proceed → Execute** rather than close/merge,
use Variant A in the same viz files — or [dynamic](../../viz/c4/dynamic.md)'s pairing table
for notation choice.

| Notation | Variant A focus |
| :------- | :-------------- |
| BPMN | Gateways: Proceed, Validate, Merge |
| UML sequence | `start session N` through merge offer |
| DMN | Proceed gate truth table |

## ESL checklist (this section)

| Rule | Pass |
| :---- | :---- |
| Dynamic stack only | No static C4 Context on runtime canvas |
| Uses §5 elements | Containers from [container](../../viz/c4/container.md) |
| One scenario per diagram | Primary + secondaries listed separately |
| Supplementary diagrams | Dynamic does not replace Container |
| Irreversible gates named | DMN Variant A/B; ICOM+ Controls on tasks |

## Where to go next

- **Building blocks (§5):** [05-building-block-view](05-building-block-view.md)
- **Deployment mapping (§7):** [07-deployment-view](07-deployment-view.md)
- **Taxonomy:** [diagram-taxonomy](../../_playground/diagram-taxonomy.md)
- **ICOM+ tasks (L4):** [task-box](../../viz/icom/task-box.md)
- **Section index:** [README](README.md)
