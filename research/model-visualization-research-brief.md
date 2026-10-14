---
title: "Research brief: model selection and visual combinations"
status: reference
date: 2026-06-12
tags: [research, modeling, visualization, sessions]
---

# Research brief — which models, when, and how to combine

Companion to [perplexity-prompts](perplexity-prompts.md) **Prompt 4** and playground
`_playground/diagram-taxonomy.md` v0.2. This brief scopes the Perplexity
deep-research run; the report distills into `research/model-visualization-seed.md`.

## Why this research now

The book already commits to:

- **Static / dynamic / decision** diagram families (taxonomy v0.2)
- **C4** for structure (four diagrams — not flowcharts)
- **ICOM + Gherkin** for L4 tasks
- **BPMN2, IDEF0, UML** as candidates at L2–L3
- **Session ops** separate from product execution (`STATE`, dashboard L1–L3)

Open questions the taxonomy **defers** to evidence:

1. Which models earn a **primary** slot vs optional/alternative?
2. **Combination rules** — when may two diagrams share one view without noise?
3. **Novice + ESL** readers — which notations reduce cognitive load?
4. **AI-assisted sessions** — how should humans/agents visualize handoff,
   progress, and task-to-task navigation?
5. What to **borrow without importing** whole notations (hybrid views)?

We are **not** obliged to keep every diagram in the taxonomy catalog — research
should recommend a **minimal sufficient set** for the book's use cases.

## Two visualization tracks (must stay separate in research)

| Track | Audience question | Examples in harness |
| :---- | :---------------- | :------------------ |
| **Product / reader software** | How do I design, plan, build my product? | Ch. 02 layers, tasks, workflows |
| **Session / meta** | Where are we in *this book repo session*? | STATE, dashboard, bootstrap → build → close |

Research must address **both**, with explicit rules so session Kanban-like
views are not confused with BPMN2 product workflows.

## Use cases the book must support (drive visual selection)

Research should map notation → use case, not notation → notation:

| Phase | Reader use case | Visual need |
| :---- | :-------------- | :------------ |
| Ch. 01 | Discover roles and use cases | Scope boundaries; priority |
| Ch. 02 | Design four layers + threat model | Structure + trust zones + abuse |
| Ch. 03 | Decompose plan; gate before build | Dependencies; readiness |
| Ch. 04 | Configure agents; load context | Team roles; context boundaries |
| Ch. 05 | Execute one task per sitting | Task I/C/O/M; acceptance evidence |
| Ch. 05+ | Move task → task without getting lost | Workflow progression; parent/child |
| Meta | Human + agent session handoff | Session state; next action; human gates |

## Deliverables expected from Perplexity

1. **Model inventory** — C4, UML, BPMN2, IDEF, ER, DMN, plus credible
   alternatives (event storming, story maps, ArchiMate, etc.) with *when*
   each wins and fails.
2. **Combination matrix** — allowed pairs on same view (e.g. C4 Container +
   ER logical; BPMN2 + DMN at gateway) with anti-patterns.
3. **Minimal set recommendation** for a methodology book (novice → seasoned).
4. **Session visualization** — published patterns for dev session status,
   agent handoff, cognitive load; applicability to AI pair-programming.
5. **ESL / accessibility** — short-label, link-rich, non-prose-first layouts.
6. **AI-specific** — what teams document when agents execute bounded tasks;
   human review gates as visual elements.
7. **Source list** with primary references; failure conditions per recommendation.

## After the report lands

1. Save raw export → `_inbox/` (dated filename).
2. Distill → `research/model-visualization-seed.md` (provenance table like
   other seeds).
3. Update `_playground/diagram-taxonomy.md` v0.3 — combination section from
   research, not guesswork.
4. Red-team pass → optional challenges in seed before promotion to
   `context/system/`.
5. Session dashboard evolution informed by research track (separate from
   product L3/L4 HTML).

## Red-team line (append to Prompt 4)

See [perplexity-prompts](perplexity-prompts.md#red-team-note) — append the critic paragraph to
Prompt 4 before running.
