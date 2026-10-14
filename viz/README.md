---
title: Visual notation — index
status: in-progress
audience: [novice, seasoned, both]
tags: [viz, notation, diagrams]
---

# Visual notation — index

`viz/` holds **rendering stubs** for each diagram type in the book's core
catalog. [[diagram-taxonomy]] answers *which diagram at which level*; this
folder answers *how to render it* (Mermaid first; HTML explorers later).

> [!NOTE] Stubs in S31 · fills in S36
> Each notation family has a section folder: index + per-type files.
> **C4 Context** was the first worked harness example (S31). **S36** filled
> all remaining stubs — C4 L2–Deployment, ICOM task box, BPMN, UML, DMN.
> BPMN / UML / DMN include **two harness examples each** — session operations
> (Track B) and Track A task execution — because they answer different questions.

## Notation families

| Family | Book level | Section | Default types |
| :----- | :--------- | :------ | :------------ |
| **C4** | L1–L3 static (+ Dynamic supplementary) | [[c4/README]] | Context, Container, Component, Dynamic, Deployment |
| **BPMN 2.0** | L3 dynamic (subset) | [[bpmn/README]] | Process (core subset) |
| **ICOM+** | L4 dynamic | [[icom/README]] | Task box |
| **UML 2** | L3/L4 boundary | [[uml/README]] | Sequence, State |
| **DMN** | L3/L4 at gateways | [[dmn/README]] | Decision table |

## Rules (all families)

From [[diagram-taxonomy]] ESL row and [[icom-plus-convention]] color map:

| Rule | Enforce |
| :---- | :------ |
| Title | Question answered — not notation name |
| Labels | ≤ 5 words; verb + object |
| Legend | Embedded on every diagram |
| Color | Role only — link to ICOM+ color map |
| Node budget | L1 ≤ 7 · L2 ≤ 12 · L3 ≤ 15 |

**Two stacks:** do not merge C4 static structure with BPMN process flow on
one canvas. Link in prose instead ([[diagram-taxonomy#Two stacks (do not merge)]]).

## Promotion from playground

Working HTML or mockup experiments promote **into** `viz/<family>/` — not
directly into chapters. `_playground/README.md` records `promote_to:` paths
such as `viz/icom/task-01.html`.

## Where to go next

- **Taxonomy (which diagram):** [[diagram-taxonomy]]
- **Worked C4 Context (harness):** [[c4/context]]
- **ICOM+ grammar:** [[icom-plus-convention]]
- **Design phase tools:** `00-start-here/setup/design-tools/README`
- **Ch. 02 design:** `02-design/README`
- **arc42 documentation template:** `02-design/arc42/README`
