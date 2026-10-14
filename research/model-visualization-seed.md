---
title: "Seed: model selection and session visualization (Perplexity research)"
status: reference
date: 2026-06-12
tags: [research, seed, provenance, modeling, visualization]
---

# Seed — Visual Notation Strategy

Distilled from `_inbox/Visual Notation Strategy for an AI-Assisted Software Methodology Book.md`
(Perplexity deep research, 2026-06-12). Three-way analysis against
project-harness: confirms, adds, challenges. Provenance: `perplexity → section`.

**Citation status:** Strong on OMG specs, Simon Brown C4, NN/g cognitive load,
Anthropic agents paper. Practitioner criticism (LinkedIn, Reddit) is secondary —
treat as leads. Track B session viz and ICOM+Gherkin combo lack published
validation — book-original with conceptual precedent.

**Feeds:** `_playground/diagram-taxonomy.md` v0.3 (next), session dashboard
evolution, ADR-002 addendum candidate.

---

## Confirms (keep current direction)

- **L1→L4 progressive disclosure** — validated by C4 hierarchy, arc42, Nielsen
  progressive disclosure; one level per view, do not compound levels on one page.
- **L4 = task (one sitting); L3 = multi-step workflow** — confirmed; L3 duality
  is *static* C4 Component vs *dynamic* BPMN2 Process — same zoom, different
  question, **never same diagram**.
- **C4 core four are static** — Context, Container, Component, Code; no
  flowcharts in C4 proper.
- **ICOM concept for L4 tasks** — IDEF0-derived frame; keep Inputs/Controls/
  Mechanisms/Outputs as structured spec (table or box), not strict IDEF0 graphics
  as default.
- **Session ops ≠ product BPMN** — separate track; dashboard/STATE are not
  C4 L3 process diagrams.
- **DMN + BPMN at gateway** — canonical OMG combination; best-documented
  multi-notation pair.
- **Gherkin stays** — as textual task spec paired with ICOM (dual coding), not
  as a "diagram type."

---

## Adds (new material)

### C4 supplementaries (correction to v0.2)

Simon Brown defines **three supplementary** C4 diagrams beyond the four levels:

| Supplementary | Use |
| :------------ | :-- |
| System Landscape | Wider than one system |
| **Dynamic** | Runtime collaboration on C4 elements (numbered arrows) — C4-native behaviour without UML |
| Deployment | Infrastructure mapping (separate from Container — do not merge) |

Teach Dynamic as alternative to UML sequence at L2/L3 when staying in C4 notation.

### Minimal default set (7 product diagram types)

1. C4 Context (L1)
2. C4 Container (L2)
3. C4 Component **or** C4 Dynamic (L3)
4. BPMN2 Process — **core subset** only (L3)
5. ICOM task frame as md table/box (L4)
6. UML Sequence or State (L3/L4 boundary)
7. DMN decision table (L3/L4 at gateways)

### BPMN2 core subset (default — not full spec)

Pool, Lane, Task, Gateway (XOR/AND/OR), Data Object, Message Flow.
**Appendix:** choreography, conversation.

### Track B — session visualization model

**Primary:** Kanban board — `Backlog | In Progress (WIP≤2) | Waiting Review | Merged | Closed`

**Secondary:** Session status table (emoji + short labels for ESL) in STATE or
dashboard L3 — task ID, executor, context files, gate.

**Tertiary (appendix):** Cumulative flow diagram for multi-day sessions.

**Avoid for sessions:** BPMN, C4 misapplied to sessions, Gantt roadmaps, story points.

**Orientation:** always mark "current task" / you-are-here.

### ESL / cognitive load rules (book-enforceable)

- Labels ≤ **5 words**; verb + object pattern
- Embedded legend on every diagram (not separate page)
- Color = role only; non-color fallback for accessibility
- Node budgets: L1 ≤7, L2 ≤12, L3 ≤15 (split if exceeded)
- Diagram **title = the question answered**, not diagram type name
- L3/L4: interactive HTML OK; print needs static fallback

### AI agent workflow mapping (Anthropic patterns → diagrams)

| Pattern | Visual |
| :------ | :----- |
| Prompt chaining | Sequence or BPMN linear |
| Routing | BPMN XOR + DMN table |
| Parallelization | BPMN parallel gateway |
| Orchestrator-worker | C4 Container + sequence inset |
| Evaluator-optimizer | State machine loop |

Human review gate = BPMN user task (product) / **Waiting Review** column (session).

### Combination matrix (allowed composites)

| Composite | Verdict |
| :-------- | :------ |
| BPMN + DMN inset at gateway | ✅ canonical |
| C4 Container + ER inset per data store | ✅ |
| C4 Context + System Landscape | ✅ |
| C4 Dynamic on C4 elements | ✅ |
| ICOM frame + Gherkin block | ✅ book hybrid |
| BPMN + UML sequence as **labelled inset** | ✅ conditional |
| C4 Component + UML class as inset | ✅ conditional |
| C4 Container + BPMN swimlane | ⚠️ only if pools = containers, explicit |
| C4 Container + Deployment merged | ❌ |
| BPMN + IDEF0 graphics | ❌ |
| C4 + ArchiMate layer | ❌ |
| Wardley + operational diagram | ❌ |

### arc42 as documentation template

Not a notation — 12-chapter doc structure compatible with C4 levels; candidate
for Ch. 02 architecture doc scaffold (optional reference).

### Event Storming

Discovery **workshop protocol**, not deliverable diagram — output → C4 / BPMN.

---

## Challenges (change the catalog)

| Current harness claim | Research says |
| :-------------------- | :------------ |
| "Full BPMN2" default | Teach **core subset**; full spec in appendix |
| IDEF3 in taxonomy | **Drop** — use BPMN Process or UML Activity |
| IDEF0 strict graphics | **ICOM as table/box** default; strict IDEF0 appendix-only |
| Gherkin as diagram type | **Category error** — text spec only |
| ArchiMate, SysML in catalog | **Drop from core** (appendix or remove) |
| Petri nets in core | **Appendix** only |
| Choreography/conversation BPMN in core | **Appendix** |
| Mermaid = sufficient for all | BPMN2, IDEF0, DMN tables need HTML/SVG/draw.io |

---

## Drop list (default catalog)

IDEF3 · SysML · ArchiMate (core) · Petri nets (core) · full BPMN choreography/
conversation · Event Storming as diagram · User Story Map as architecture visual ·
Gherkin as diagram type.

---

## Open gaps (no evidence yet)

- ICOM + Gherkin + session Kanban as integrated system — book-original; validate
  with Alex's use.
- AI agent session viz — no published standard; AGENTS.md + spec-kit are textual.
- C4 academic evidence thin — practitioner-strong only.

---

## Recommended actions (priority)

1. **Taxonomy v0.3** — apply drop list, C4 supplementaries, BPMN subset, combination matrix.
2. **Session dashboard L3** — evolve toward Kanban columns + status table + you-are-here (not BPMN).
3. **ADR-002 addendum** — C4 supplementaries, BPMN subset default, session track separation.
4. **Mockups** — trim dropped types; add C4 Dynamic, Kanban session board.
5. **Next turn** — combination testing per use case (user-driven).

---

## Provenance index

| Seed section | Source section |
| :----------- | :------------- |
| Confirms L1-L4 | Executive 11, 29; Track A zoom table |
| C4 supplementaries | Executive 1; Track A static |
| BPMN subset | Executive 2; Track A dynamic; Challenges |
| Session Kanban | Executive 9; Track B |
| Combination matrix | Combination Matrix section |
| ESL rules | ESL section |
| Drop list | Recommendations DROP + Executive 6,8,19 |
| AI patterns | AI-Assisted Development section |

Raw: `_inbox/Visual Notation Strategy for an AI-Assisted Software Methodology Book.md`
