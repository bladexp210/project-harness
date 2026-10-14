---
title: Diagram Taxonomy v3
layer: 1-system
status: reference
version: "0.3"
created_at: 2026-06-12T18:00:00
updated_at: 2026-06-15T19:00:00
tags: [modeling, taxonomy, reference]
---

# Diagram taxonomy v3 — which diagram at which level

> [!NOTE] Reference v0.3
> **Rendering stubs** live in [[viz/README|viz/]] (Mermaid first; HTML explorers later).
> **Architecture documentation template:** [[02-design/arc42/README|arc42/]] (12 sections under Ch. 02).
> This file answers: *which diagram type, at which level, for which question?*
> Dynamic task boxes: [[icom-plus-convention|ICOM+ v0.3]]. Mockups:
> `_playground/mockups/` · **FICTITIOUS** unless marked REAL.

---

## Foundations (read once)

### Two stacks (do not merge)

| Stack | IDs | Question | Taxonomy role |
| :---- | :-- | :------- | :------------ |
| **Process** | `app_*` · `proc_*` · `wf_*` · `t_*` | What happens? | ICOM+ boxes, BPMN, sequence |
| **C4 static** | Context · Container · Component · Code | What exists? | Structure diagrams only |

Capability ≈ app · Process ≈ module (Container in C4 labels) · Workflow ≈
component grain · Task ≈ one sitting. **Link** stacks in prose; do not rename C4
levels into process levels. REAL Track B: [[_playground/l4-models/README|l4-models/]].

### C4 — four core + three supplementaries

**Core four** (static only — no flowcharts, sequence, or swimlanes):

| C4 level | Diagram | What it shows |
| :------: | :------ | :------------ |
| 1 | **System Context** | System boundary; users; external systems |
| 2 | **Container** | Apps, data stores, runtimes *(say **module** in prose)* |
| 3 | **Component** | Parts inside one container |
| 4 | **Code** | Types and relationships inside one component |

**Supplementaries** (Simon Brown — not replacements for core four):

| Supplementary | Use | Typical level |
| :------------ | :-- | :------------ |
| **System Landscape** | Wider than one system | L1 |
| **Dynamic** | Numbered runtime collaboration on C4 elements | L2–L3 |
| **Deployment** | Infrastructure mapping | L2 |

Do **not** merge Container + Deployment on one canvas.

### Diagram families

| Family | What it captures | Default in this book |
| :----- | :--------------- | :------------------- |
| **Static** | What exists; topology | C4 core + ER + UML class/component/deployment |
| **Dynamic** | Order; handoffs; behaviour | **ICOM+** (L4), BPMN2 subset (L3), UML sequence/state |
| **Decision** | Rules; outcomes from inputs | DMN tables at gateways |
| **Specification** *(fourth — text)* | Acceptance criteria | **Gherkin** paired with ICOM+ — not a diagram |

### Book levels vs C4 (do not conflate)

| Book level | Grain | C4 static (structure question) | Dynamic / decision (behaviour question) |
| :--------: | :---- | :----------------------------- | :--------------------------------------- |
| **L1** | Product in its world | Context (+ Landscape supplementary) | Use case; blackbox BPMN summary |
| **L2** | Containers / modules | Container; Deployment supplementary | C4 Dynamic; collaboration BPMN; ER overview |
| **L3** | Component **or** multi-step workflow | Component | BPMN Process (subset); ICOM+ workflow; sequence; state |
| **L4** | One task — one sitting | Code (when code structure is the question) | **ICOM+** box; sequence inset; DMN at gateway |

**Session operations** (STATE, dashboard, Kanban) are **Track B** — not product L1–L4.

### Minimal default set (7 product types)

1. C4 Context (L1)
2. C4 Container (L2)
3. C4 Component **or** C4 Dynamic (L3)
4. BPMN2 Process — **core subset** (L3)
5. **ICOM+** task box (L4) — replaces generic ICOM / strict IDEF0 graphics
6. UML Sequence or State (L3/L4 boundary)
7. DMN decision table (L3/L4 at gateways)

### BPMN2 core subset (default)

Pool · Lane · Task · Gateway (XOR/AND/OR) · Data Object · Message Flow.

**Appendix only:** choreography · conversation · full BPMN2 spec.

### ESL rules (enforce on every diagram)

- Title = **question answered**, not notation name
- Labels ≤ **5 words**; verb + object
- Embedded legend on every diagram
- **Color = role only** — see [[icom-plus-convention#Color map (roles)|ICOM+ color map]]
- Node budgets: L1 ≤7 · L2 ≤12 · L3 ≤15 (split if exceeded)
- Non-color fallback prefixes required (`[Exec:agent]`, etc.)

---

## L1 — System context

*Whole product, users, external systems.*

| Model | Diagram | Family | Focus | Blind spots | Use for | Do not use for |
| :---- | :------ | :----- | :---- | :---------- | :------ | :------------- |
| **C4** | System Context | Static | Boundary; actors; external deps | Internals; message order | First structural picture | Code; step-by-step flow |
| **C4** | System Landscape | Static | Multi-system map | Single-system detail | Portfolio / ecosystem view | Component internals |
| **UML** | Use case | Dynamic/spec | Actors; goals; scope | Order; deployment | Named capabilities at edge | Task acceptance |
| **BPMN2** | Process (blackbox) | Dynamic | One pool; happy path | Cross-pool detail | Executive product lifecycle summary | L4 task steps |
| **ER** | Conceptual ER | Static | Core entities | Attribute detail | Shared vocabulary | Service boundaries |
| **DMN** | Decision table | Decision | Policy outcomes | Process order | Product-level policy | Layout |

---

## L2 — Container / module

*Deployable parts: web app, API, database, agent runner.*

| Model | Diagram | Family | Focus | Blind spots | Use for | Do not use for |
| :---- | :------ | :----- | :---- | :---------- | :------ | :------------- |
| **C4** | Container | Static | Apps; stores; comms between | Classes; timing | Architecture handoff; threat zones | API call sequence |
| **C4** | Deployment | Static | Infra; nodes; network | Business rules | Where agents run | Logical domain model |
| **C4** | Dynamic | Dynamic | Runtime collaboration on C4 elems | Policy tables | Behaviour without leaving C4 | Static nesting |
| **UML** | Deployment | Static | Artifacts on nodes | UX rules | Ops structure | Domain model |
| **UML** | Package | Static | Namespaces; packages | Runtime messaging | Monorepo areas | Production network |
| **BPMN2** | Collaboration | Dynamic | Pools; message flows | Inside-pool steps | Multi-container overview | L4 ICOM+ |
| **BPMN2** | Process (per pool) | Dynamic | Steps in one container | Other pools | Container-local workflow | Class design |
| **ER** | Logical ER | Static | Entities; cardinalities | API contracts | Schema design input | Request order |
| **DMN** | Decision requirements | Decision | Decision dependencies | Execution order | Container-level rules map | Infra diagram |

*Harness L2 example:* chapters `00`–`08` as containers; validator, loader,
OpenHands as runtime containers.

---

---

## Notation selection rationale

Distilled from the Visual Notation Strategy inbox report (archived
`research/archive/`). The book's L1–L4 zoom model matches C4 hierarchy,
arc42 building blocks, and progressive disclosure — one standalone diagram per
level, never compound zoom on one page.

| Principle | Rule |
| :---- | :---- |
| **Static vs dynamic** | C4 answers structure; BPMN answers step sequence — never on the same diagram |
| **BPMN default subset** | Pool + lane + task + gateway + data object + message flow — not full OMG spec |
| **L4 task frame** | ICOM+ concept as Markdown table ([[icom-plus-convention]]) — strict IDEF0 syntax optional |
| **Track B sessions** | Kanban status board — not BPMN (different question: session orientation) |
| **ESL readability** | ≤5 words per node label; integrated legend; diagram + prose dual coding |
| **AI agent workflows** | No published notation standard yet — use sequence/state at L3/L4 boundary |

Full report (67K) stays in archive for bibliography; canon holds this section
only. Primary references: Simon Brown *The C4 Model*; OMG BPMN 2.0 subset;
[[ADR-002-modeling-conventions|ADR-002]] Mermaid budgets.

---

## Continued

L3–L4 tables, Track B, combination matrix, appendix: [[diagram-taxonomy-levels]].

