---
title: "arc42 §4 — Solution Strategy"
chapter: 02
status: reference
audience: [novice, seasoned, both]
tags: [arc42, design, harness]
---

# arc42 §4 — Solution Strategy

**Question answered:** What fundamental approaches shape the architecture?

> [!NOTE] REAL — harness-meta
> Strategy for **this repo** — prose summary, not a diagram dump. Decisions
> with full rationale live in `decisions/` and index in §9.

## 1. Book-as-folder-structure

The harness **is** the documentation: chapters `00`–`08` teach the method and
hold operational artifacts (agents, tasks, constraints, validator). One repo
serves two readers simultaneously — the human following the book and the AI
agent loading files as context ([ADR-001-chapter-folder-naming](../decisions/ADR-001-chapter-folder-naming.md)).

| Principle | How it shows up |
| :-------- | :-------------- |
| Folder = chapter | Navigation matches mental model; Obsidian wiki-links |
| Dual-purpose files | Teaching callouts + artifact zones (ADR-006) |
| Meta alongside spine | `STATE`, dashboard, `context/` without polluting Ch. 00–08 prose |
| Fork path | [reader-skeleton](../../06-learn/boilerplate/reader-skeleton/README.md) strips harness meta for reader products |

Building-block detail: [05-building-block-view](05-building-block-view.md) · [container](../../viz/c4/container.md).

## 2. Dual execution tracks

Two execution paths — same method, different tooling ([ADR-007-dual-execution-tracks](../decisions/ADR-007-dual-execution-tracks.md)):

| Track | Role today | Stack |
| :---- | :--------- | :---- |
| **Track B** | Authoring canon, session meta-work | Cursor IDE agent, `AGENTS.md`, task `context_load` |
| **Track A** | Build tasks when Docker is ready | OpenHands + LiteLLM + optional Langfuse ([track-a-setup](../../05-build/execution-tools/track-a-setup.md)) |

**Strategy:** Teach and operate Track B first; prove Track A on golden path
(Task 02). Reader chooses track per task mechanism in ICOM+ Controls — see
[decision-table](../../viz/dmn/decision-table.md) Variant B.

Constraints: `project.md` · Runtime: [06-runtime-view](06-runtime-view.md).

## 3. Four design layers

Below the folder strategy, product design uses four layers ([data](../layers/data.md),
[application](../layers/application.md), [ux](../layers/ux.md), [communication](../layers/communication.md)).
Work order: data → application → communication; UX cuts across all three.

In this harness, layer files are **teaching scaffolds** with harness-meta
examples; the reader's fork replaces content with their product decisions.
Crosscutting patterns (observability, context loading, prose rules): [08-crosscutting-concepts](08-crosscutting-concepts.md).

## 4. Quality and decision tactics

| Tactic | Supports quality goal (§1) | Anchor |
| :----- | :------------------------- | :----- |
| Frequency × importance planning | Build order from use cases, not enthusiasm | [use-cases](../../01-understand/use-cases.md) · [PROJECT-PLAN](../../03-plan/PROJECT-PLAN.md) |
| Session workflow state machine | Handoff continuity | [session-workflow](../../context/system/session-workflow.md) |
| Human gates on irreversible steps | Proceed, validate, merge (D-001) | [Agents](../../Agents.md), [decision-table](../../viz/dmn/decision-table.md) |
| Validator + golden tasks | Verifiable canon before merge | `scripts/validate_md.py`, `test_golden_tasks.py` |
| ADR at decision time | One decision per file; §9 index | [09-architectural-decisions](09-architectural-decisions.md) |
| Notation in `viz/` | Single source for diagrams; arc42 links | [viz/](../../viz/README.md) |

## 5. Organization and review

| Boundary | Rule |
| :------- | :--- |
| Session | One branch `session-NN/<topic>`; close draft updates STATE + dashboard |
| Task | Scope — modify list in `tasks/*.md` only |
| Agent team | Roles in `agents/*.yaml`; Brooks-style specialization ([agent-team](../../context/system/agent-team.md)) |
| Human | Co-author approves scope and runs git; agent never force-pushes `main` |

## ESL checklist (this section)

| Rule | Pass |
| :---- | :---- |
| Prose strategy | No pasted C4/BPMN canvases |
| Leads with book-as-folder + dual tracks | Sections 1–2 before layers |
| Links to §5 and §9 | Building blocks and ADRs referenced |
| Product fork reminder | Reader replaces strategy examples |

## Where to go next

- **Introduction (§1):** [01-introduction-and-goals](01-introduction-and-goals.md)
- **Constraints (§2):** [02-constraints](02-constraints.md)
- **Building blocks (§5):** [05-building-block-view](05-building-block-view.md)
- **Decisions (§9):** [09-architectural-decisions](09-architectural-decisions.md)
- **Section index:** [README](README.md)
