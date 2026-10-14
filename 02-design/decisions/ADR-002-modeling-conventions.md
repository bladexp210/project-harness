---
title: "ADR-002: Modeling conventions — diagrams and task model"
chapter: 2
status: accepted
date: 2026-06-10
tags:
  - decision
  - modeling
---

# ADR-002 — Modeling conventions: diagrams and the task model

**Status:** accepted — 2026-06-10, by human review after pre-mortem.

## Context

Models compress meaning for both readers: humans parse a diagram faster than
prose, and AI agents parse structured text cheaper than prose (fewer tokens,
less ambiguity). But "use models" is not a convention — without one, every
chapter would invent its own notation. Two questions are being forced now,
before [[02-design|Ch. 02]] layer files and Ch. 03 task templates are
written: (1) which diagram notations the book uses, and (2) how a *task* is
modeled — its inputs, transformation, outputs, and success criteria.
Candidate notations analyzed: C4, UML, BPMN 2.0, DMN, IDEF0, Gherkin, Petri
nets (analysis preserved in `_inbox/`). Hard constraint: the publishing
chain (Obsidian → git → Quartz) natively renders **Mermaid and markdown
only**.

## Decision

**Part 1 — Diagrams.** All diagrams are Mermaid, chosen by the *question*
the diagram answers, not by notation loyalty:

| Question | Mermaid dialect | Borrowed thinking |
| :---- | :---- | :---- |
| What are the parts and how do they connect? | `flowchart` + subgraphs | C4 (zoom levels) |
| Who does what, in what order? | `sequenceDiagram` | UML |
| What states can this thing be in? | `stateDiagram-v2` | UML |
| What data exists and how does it relate? | `erDiagram` | ER |
| How does a process flow, with branches? | `flowchart` + swim-lane subgraphs | BPMN-lite |
| Which rule fires on which input? | Markdown decision table | DMN-lite |

Size budget: **≤ 20 nodes per diagram**. Bigger means the model is at the
wrong zoom level — split it C4-style (context → container → component).

**Part 2 — Task model.** Every task file (Ch. 03/05 `tasks/`) is an
**ICOM frame** (IDEF0 thinking) in plain markdown sections:

- **Inputs** — context files and artifacts the task consumes (the Layer-3
  context list)
- **Controls** — what governs the transformation: [[global|constraints]],
  budgets, and the acceptance criteria below
- **Mechanisms** — which agent ([[agent-team]]) and execution tool run it
- **Outputs** — the artifacts the task must produce

Acceptance criteria are written in **Gherkin** (`Given / When / Then`), so
the task specification *is* its test suite — the agent quotes the `Then`
clauses as evidence when closing the task:

```gherkin
Scenario: Task is complete
  Given the inputs listed above
  When the transformation described in this task runs
  Then [observable, checkable outcome]
  And [another — each Then is one test]
```

**Part 3 — Foundational filters (Parnas, Liskov, Hoare).** The ICOM frame
implements three classic design filters without new ceremony:

| Filter | Paper | Where in the task model |
| :----- | :---- | :-------------------- |
| Information hiding | Parnas | Controls scope (modify/read-only) hides what may change; Inputs/Outputs name the stable boundary |
| Data abstraction | Liskov | Inputs/Outputs tables — artifact · form · where · from/to — are contracts clients may rely on |
| Axiomatic checks | Hoare | Gherkin `Given` = preconditions, `When` = transformation, `Then` = postconditions |

For **irreversible-gate tasks** (human Supervisor for merge, deploy, or
schema migration), Controls must include an explicit **Preconditions** table
and Mechanisms an explicit **Postconditions** table — see
[[icom-plus-irreversible-gates]]. Ch. 05 requires postcondition evidence:
each `Then` quoted with proof in the closing commit or post-mortem.

## Why

One rendering chain, zero plugins, every model diffable in git and readable
raw — the same durability argument as [[manifesto]]. The question→dialect
table keeps notation choice mechanical for agents writing chapters. The ICOM
frame is not new structure: Inputs/Controls/Mechanisms/Outputs map one-to-one
onto what the system already does (Layer-3 context, constraints + budgets,
agent team, atomic commits) — the convention just names it. Gherkin binds
success criteria to the task definition itself, closing the gap where tests
are an afterthought; it is also the most token-efficient of the candidates
and needs no tooling to be useful as a checklist.

## Alternatives considered (red-teamed)

- **Native BPMN 2.0 / DMN / IDEF0 tooling** — richest semantics for
  process and decision modeling, purpose-built for exactly this; rejected
  because nothing in the chain renders them, XML artifacts are hostile to
  git diff and to novice readers, and the useful 90% survives translation
  into flowcharts and decision tables.
- **Mermaid's native `C4Context`/`C4Container`** — semantically labeled,
  closest to the real notation; rejected as primary because the syntax is
  experimental and renders poorly; flowchart-with-subgraphs is stable and
  visually equivalent. Revisit if it stabilizes.
- **PlantUML** — full UML + solid C4 support, more expressive than Mermaid;
  rejected because it needs a rendering server or plugin, breaking the
  zero-plugin durability rule.
- **Petri nets** — mathematically verifiable concurrency, elegant for
  deployment gates; rejected: no rendering path, and the audience includes
  complete novices. Overkill until a design problem demands proof.
- **Diagrams as images** (draw.io exports etc.) — fastest to author;
  rejected: not diffable, not machine-readable, rot silently.

## Pre-mortem

*If this decision fails a year from now, why?*

1. **Gherkin criteria rot** — written once, never checked, tasks close on
   vibes → mitigation: Ch. 05 execution convention requires the agent to
   quote each `Then` clause with evidence in the closing commit or
   post-mortem; a missing quote blocks task closure.
2. **Diagrams drift from reality** as the system evolves → mitigation: a
   stale diagram is a [[DEBT-LEDGER]] entry like any other debt; the 20-node
   budget keeps redraw cost trivial.
3. **Mermaid C4 stabilizes or the chain gains PlantUML** → the convention
   names *questions*, not dialects; a superseding ADR can remap one row of
   the table without touching the frame. Accepted risk: some files would
   carry the old dialect until touched.
4. **ICOM frame becomes ceremony** — novices fill four headings with noise
   → mitigation: the Ch. 03 task template pre-fills Controls (constraints
   are inherited, not written) and Mechanisms (agent defaults), leaving the
   reader only Inputs, Outputs, and the Gherkin block.

## Left on the table

Executable Gherkin (Cucumber/Behave) — the criteria are already in the
right syntax; wiring them to a runner becomes attractive the moment a
project in Ch. 05 has real test automation. Petri nets for
concurrency-critical designs (blue/green switchovers) — revisit if a
design problem needs formal verification. Native DMN with FEEL expressions
— if decision logic ever grows beyond what a markdown table holds.
