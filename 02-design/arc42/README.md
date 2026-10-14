---
title: arc42 — architecture documentation template
chapter: 02
status: in-progress
audience: [novice, seasoned, both]
tags: [arc42, design, documentation]
---

# arc42 — section index

[arc42](https://arc42.org/overview/) is a **12-section template** for
architecture documentation — not a diagram notation. It answers *what to
document* and *in what order*. Diagram types (C4, BPMN, ICOM+, etc.) live in
[[diagram-taxonomy]] and render in [[viz/README|viz/]].

> [!NOTE] Harness fills
> **§1–§12** ship harness-meta examples linked to `viz/`, canon, and
> `_index/glossary.md`. Your product fork replaces content — keep the arc42
> shape and link outward instead of duplicating ADRs.

## Sections

| § | File | Topic | Status |
| :-: | :---- | :---- | :----- |
| 1 | [[01-introduction-and-goals]] | Requirements, quality goals, stakeholders | **harness example** |
| 2 | [[02-constraints]] | Design and process constraints | **harness example** |
| 3 | [[03-context-and-scope]] | System boundary; external interfaces | **harness example** |
| 4 | [[04-solution-strategy]] | Fundamental decisions and strategies | **harness example** |
| 5 | [[05-building-block-view]] | Static decomposition (white boxes) | **harness example** |
| 6 | [[06-runtime-view]] | Runtime behavior and collaboration | **harness example** |
| 7 | [[07-deployment-view]] | Infrastructure and deployment mapping | **harness example** |
| 8 | [[08-crosscutting-concepts]] | Shared concepts (security, logging, …) | **harness example** |
| 9 | [[09-architectural-decisions]] | ADR index and decision log | **harness example** |
| 10 | [[10-quality-requirements]] | Quality tree and scenarios | **harness example** |
| 11 | [[11-risks-and-technical-debt]] | Risks, debt, mitigation | **harness example** |
| 12 | [[12-glossary]] | Terms and definitions | **harness example** |

## How arc42 maps to this book

| arc42 section | Book anchor |
| :------------ | :---------- |
| §1 Introduction | [[01-understand\|Ch. 01]] roles and use cases |
| §2 Constraints | [[03-plan/constraints/project\|constraints/project]] + [[global]] |
| §3 Context | [[viz/c4/context\|C4 System Context]] (L1 static) |
| §5 Building blocks | C4 Container / Component — [[viz/c4/README\|viz/c4/]] |
| §6 Runtime | BPMN, sequence, C4 Dynamic — [[diagram-taxonomy]] |
| §9 Decisions | [[../decisions/ADR-001-chapter-folder-naming\|decisions/]] ADR template |
| §11 Risks | [[11-risks-and-technical-debt]] (living register) + [[../threat-model\|threat model]] (Gate B template) |
| §12 Glossary | [[12-glossary]] + [[../../_index/glossary\|_index/glossary.md]] |

## Rules for your fork

| Rule | Why |
| :---- | :---- |
| Document only what prevents expensive misunderstandings | arc42 "minimal but honest" — not a blank encyclopedia |
| Link diagrams; do not paste screenshots into prose | Single source in `viz/` or your product repo |
| One ADR per significant decision | §9 stays an index — full text stays in `decisions/` |
| Match section depth to reversibility | Irreversible choices earn pages; reversible ones get a row |

## Where to go next

- **Ch. 02 orientation:** [[../README]]
- **Which diagram when:** [[diagram-taxonomy]]
- **Rendering stubs:** [[viz/README|viz/]]
- **Intake reference:** `_inbox/An_introduction_to_arc42…_Medium.md`
