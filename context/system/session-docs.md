---
title: Session Documents
layer: 1-system
status: reference
tags: [session, decisions, history]
---

# Session Documents

Load this file when you need full architectural detail or want to verify a decision's rationale. These documents contain the complete design decisions made in Session 1 (June 9, 2026).

Local copies live in `context/system/sessions/` — the vault is self-sufficient. Google Docs links are retained as provenance only.

---

## Document Registry

### v1 — Dimensions 1–7 (full detail)

**Local:** [session-1-v1](sessions/session-1-v1.md) · **Provenance:** [Google Doc](https://docs.google.com/document/d/1MdxaChwpc-Ej3JOEDjpcDjLDPf5pVZ_IUQNNa57HCuI)

Covers: LLM Routing, Tracing, Isolation, Blast Radius, Hooks, Post-mortems, Composability. Machine context, guiding principles, the antifragility loop, key repos, decisions not taken and why.

### v2 — Design-first Workflow (full detail)

**Local:** [session-1-v2](sessions/session-1-v2.md) · **Provenance:** [Google Doc](https://docs.google.com/document/d/13_uRIJTv_fGH_Ny53vA-j54ZJzSoKe3wRzD6FKHhFeY)

Covers: Exploration-Execution loops, two-axis model selection, three-layer context (C4 × DOK), WhiteBoxMAKER / ahead-by-k voting, boilerplate `lifecycle`, ADRs, full file structure, workflow phases. Also contains: the five workflow phases and three human approval gates.

### A/B Testing Addendum

**Local:** [session-1-ab-testing](sessions/session-1-ab-testing.md) · **Provenance:** [Google Doc](https://docs.google.com/document/d/1KpFg7_bPr5aAyYmt_U2OKQ3Dbyq1qMoEDW_CzaVty2s)

Covers: A/B testing as selective tool (not systematic gate), dual triggers (judgment + process), evaluator agent, Langfuse experiment runner, evaluation criteria templates per layer type, k-voting tiebreaker flow, design phase comparison flow, integration with existing stack.

### Agent Composition Addendum

**Local:** [session-1-agent-composition](sessions/session-1-agent-composition.md) · **Provenance:** [Google Doc](https://docs.google.com/document/d/1efd5Sw5baf-cbKHs5fztJi-nIdM2CW8Lr37QOHat8Jg)

Covers: k as margin (not agent count), three criticality dimensions (runs, k, specialists), core team (5 roles), specialist team (3 forks), orchestrator (human + tools), all seed repositories with purpose, coherence principles.

### Book Architecture & Session Close

**Local:** [session-1-book-architecture](sessions/session-1-book-architecture.md) · **Provenance:** [Google Doc](https://docs.google.com/document/d/1vTN4-kaLRHax4hMzdLCeWThNVjNw70j6UHRuEduoDDY)

Covers: The meta-reframe (this IS the system, not a project using the system), the slogan, manifesto, audience, Agents.md naming, dual path rationale, Obsidian optimization, publication workflow (Drive → GitHub → Quartz), Cowork as author, full book structure, tool alternatives for design and execution, next session agenda.

---

## Research Foundation

### Perplexity Deep Research Report

**Local:** *Best-in-Class Multi-Agent AI Coding Systems on GitHub (Full Edition)* — PDF in vault `research/` (no markdown note yet) · **Provenance:** [original PDF on Drive](https://drive.google.com/file/d/1U7IyAt2RIcoevzuUXmhEg_Nmve-yjQMg/view)

Best-in-class open-source implementations across all five tracks (git isolation, TDD, voting/ensemble, observability/resilience, composability/A/B testing). Key finding: no single repository closes all seven antifragility dimensions. Informed seed repo selection and gap identification.

### Reflexion Paper (post-mortem foundation)

[https://arxiv.org/abs/2303.11366](https://arxiv.org/abs/2303.11366) Foundation for the post-mortem learning loop (rohansx/reflect implements this with persistence).

---

## Key Decisions That Are Easy to Get Wrong

**k definition:** k = required winning margin, NOT number of agents. With 5 agents and k=4, the winner must beat second place by 4 votes — near-unanimity.

**Model selection axes are independent:**

- Complexity → model capability (cheap/capable/frontier)  
- Criticality → k threshold (1/2/4/5) During voting, cheap models can be used regardless of model used for primary implementation.

**Blast radius protection:** holds only while the decision stays within task scope. Signal it has drifted: if a task-level decision would modify a Layer 2 or Layer 1 context file → escalate.

**Context loading is deterministic:** TASK.md explicitly lists which files to load. No semantic search, no fuzzy retrieval. The human decides at planning time. Agents load exactly that.

**Agents.md vs CLAUDE.md:** always Agents.md — solution-agnostic, works with any AI tool.

---

## Next Session Agenda (Session 2)

1. System design refinements — deeper research into specific stack components  
2. Cross-project knowledge seeding — how learnings bootstrap subsequent projects  
3. Book writing begins via Cowork — starting with 00/README.md and 00/manifesto.md

