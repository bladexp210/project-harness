---
title: Diagram Taxonomy — L3–L4 and reference
layer: 1-system
status: reference
version: "0.3"
updated_at: 2026-06-15T20:00:00
tags: [modeling, taxonomy, reference]
---

# Diagram taxonomy — levels L3–L4 and reference

> [!NOTE] Part 2 of 2
> Foundations and L1–L2: [[diagram-taxonomy]].

---

## L3 — Component / workflow

*Inside one container **or** a named workflow (`wf_*`).*

| Model | Diagram | Family | Focus | Blind spots | Use for | Do not use for |
| :---- | :------ | :----- | :---- | :---------- | :------ | :------------- |
| **C4** | Component | Static | Interfaces inside container | Timing | Module boundaries | Multi-container deploy |
| **C4** | Dynamic | Dynamic | Numbered interactions | Branch policy | L3 behaviour in C4 notation | Task-level ICOM+ |
| **UML** | Component | Static | Provided/required IF | Behaviour | Interface contracts | User journey |
| **UML** | Class | Static | Types; associations | Message order | Domain model | End-user process |
| **UML** | Sequence | Dynamic | Message order | Policy tables | One use-case interaction | Product map |
| **UML** | Activity | Dynamic | Forks; joins | Deployment | Approval branches | Static nesting |
| **UML** | State machine | Dynamic | Task lifecycle transitions | Data schema | Entity / task status | Container map |
| **BPMN2** | Process (subset) | Dynamic | Tasks; gateways; lanes | Class structure | Executable workflow | Static architecture |
| **Book** | ICOM+ workflow | Dynamic | `wf_*` decomposition to `t_*` | Automated proof alone | Track B + product workflows | Replacing C4 Component |
| **ER** | Physical ER | Static | Tables; keys | Process | Migrations | API sequence |
| **DMN** | Decision table | Decision | Gateway logic | Who acts | BPMN branch rules | Component diagram |

*REAL L3 examples:* [[_playground/l4-models/commit-process/L3-commit-process|wf_commit_process]] ·
[[_playground/l4-models/session-close/L3-wf-session-close|wf_session_close]].

*Dropped from core:* IDEF3 (use BPMN or UML Activity) · BPMN choreography/
conversation (appendix).

---

## L4 — Task

*One sitting; `t_*`; Executor + Supervisor per [[icom-plus-convention|ICOM+]].*

| Model | Diagram / artifact | Family | Focus | Blind spots | Use for | Do not use for |
| :---- | :----------------- | :----- | :---- | :---------- | :------ | :------------- |
| **C4** | Code | Static | Classes in code | Runtime order | Refactor boundary | Acceptance criteria |
| **UML** | Class (detailed) | Static | Methods; patterns | Execution evidence | Implementation sketch | Roadmap |
| **UML** | Object | Static | Instance snapshot | History | Examples; debug state | Workflow |
| **UML** | Sequence | Dynamic | One scenario order | Policy | Mechanism trace inset | Chapter map |
| **UML** | State (object) | Dynamic | Object during task | Multi-actor flow | Task status | Container map |
| **BPMN2** | Process fragment | Dynamic | Subprocess + review gate | Full pools | Human review gate | Whole chapter |
| **Book** | **ICOM+** box | Dynamic | I/C/Ctl/O/Tools/Meas/Exec/Sup | Verification alone | **Default L4 task spec** | Architecture |
| **Book** | Gherkin | Specification | Observable done-when | Structure | Paired with ICOM+ | Diagram canvas |
| **DMN** | Decision table | Decision | Task-local branch | UI layout | Escalation rules | Sequence |

*Canon at L4:* `tasks/*.md` and playground `l4-models/**/0N-*.md`. HTML ICOM
cards are **views**, not a second grammar.

*Dropped from core:* strict IDEF0 graphics (appendix); Gherkin listed as diagram.

---

## Track B — Session operations

*Book repo — parallel to product L1–L4. Process stack applies.*

| Model | Visual | Family | Use for | Do not use for |
| :---- | :----- | :----- | :------ | :------------- |
| **Book** | Kanban board | Dynamic | `Backlog \| In Progress \| Waiting Review \| Merged \| Closed` | Product architecture |
| **Book** | Dashboard tables | Static | STATE + `_index/dashboard/` L1–L3 | Reader product workflows |
| **Book** | ICOM+ `proc_*` / `wf_*` | Dynamic | Session build/close (REAL) | Teaching spine only |
| **Book** | Spine flowchart | Static | Chapter order pedagogy | Executable spec |

**Avoid for sessions:** BPMN · C4 misapplied to sessions · Gantt · story points.

**Orientation:** always mark you-are-here / current `t_*`.

---

## Combination matrix

| Composite | Verdict | Notes |
| :-------- | :------ | :---- |
| BPMN + DMN inset at gateway | ✅ canonical | OMG default pair |
| C4 Container + ER inset per store | ✅ | One inset per data store |
| C4 Context + System Landscape | ✅ | Wider ecosystem |
| C4 Dynamic on C4 elements | ✅ | Alternative to UML sequence |
| ICOM+ box + Gherkin block | ✅ | Book hybrid; dual coding |
| BPMN + UML sequence as labelled inset | ✅ conditional | Different questions |
| C4 Component + UML class as inset | ✅ conditional | Structure + detail |
| C4 Container + BPMN swimlane | ⚠️ conditional | Only if pools = containers |
| Process stack + C4 static link in prose | ✅ | Two stacks pattern |
| C4 Container + Deployment merged | ❌ | Separate diagrams |
| BPMN + IDEF0 strict graphics | ❌ | Pick one dynamic grammar |
| C4 + ArchiMate | ❌ | Not in core catalog |
| Wardley + operational diagram | ❌ | Different purpose |

---

## Core catalog vs appendix

### In core (default teaching)

| Model | Static | Dynamic | Decision / spec |
| :---- | :----- | :------ | :-------------- |
| **C4** | Context, Container, Component, Code + Landscape, Dynamic, Deployment | Dynamic supplementary | — |
| **UML 2** | Class, Object, Component, Package, Deployment | Use case, Sequence, Activity, State | — |
| **BPMN2** | — | Process, Collaboration (subset default) | refs DMN |
| **ER** | Conceptual, logical, physical | — | — |
| **DMN** | Requirements diagram | — | Decision table |
| **Book** | Dashboard | **ICOM+**, Kanban | Gherkin (text) |

### Appendix only (not default)

IDEF3 · IDEF0 strict graphics · SysML · ArchiMate · Petri nets · BPMN
choreography/conversation · Event Storming as deliverable · User Story Map as
architecture visual.

**Explicitly not C4:** generic teaching flowchart / Mermaid `flowchart` spine —
pedagogical journey, not a C4 type.

---

## AI agent patterns → diagrams

| Agent workflow | Visual |
| :------ | :----- |
| Prompt chaining | Sequence or linear BPMN |
| Routing | BPMN XOR + DMN |
| Parallelization | BPMN parallel gateway |
| Orchestrator–worker | C4 Container + sequence inset |
| Evaluator–optimizer | State machine loop |
| Human review gate | BPMN user task (product) · Kanban Waiting Review (session) |

---

## v0.3 scope

| Done in v0.3 | Deferred |
| :----------- | :------- |
| Drop list applied; appendix split | ADR-002 addendum |
| C4 supplementaries | Rendering channel rules per notation |
| BPMN core subset | Mockup trim (dropped types) |
| Combination matrix | Combination testing per use case |
| ICOM+ v0.3 as default L4 dynamic | C4 Dynamic mockup |
| Track B Kanban + process stack refs | Session dashboard Kanban UI |
| ESL + color link to ICOM+ | viz/ stubs (S31); arc42 scaffold (S32) **done** |

**Provenance:** [[research/model-visualization-seed|model-visualization-seed]]
(Perplexity 2026-06-12) + ICOM+ v0.3 decisions (2026-06-15).

**Mockups:** `_playground/mockups/README.md` — learning examples; some types now
appendix-only.

---

## History

| updated_at | Change |
| :--------- | :----- |
| 2026-06-15T19:00:00 | v0.3 — drop list, C4 supplementaries, BPMN subset, combination matrix, ICOM+ default, two stacks, Track B Kanban |
| 2026-06-12T16:54:00 | v0.2 — C4 corrected; per-level tables; three families |
| 2026-06-15T20:00:00 | Promoted from _playground/ to context/system/ |
| 2026-06-12T16:23:00 | v0.1 — superseded |
