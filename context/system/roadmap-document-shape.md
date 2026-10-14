---
title: Roadmap Document Shape
layer: 1-system
status: reference
updated: 2026-06-30 22:25
tags: [roadmap, planning, handoff, workflow]
---

# Roadmap document shape

Mandatory structure for approved multi-session plans. Complements
[session-workflow](session-workflow.md) and examples [session-roadmap-s19-s23](sessions/session-roadmap-s19-s23.md),
[session-roadmap-s40-plus](sessions/session-roadmap-s40-plus.md), [spine-sitrep-s26](sessions/spine-sitrep-s26.md).

## When this applies

| Applies | Does not apply |
| :------ | :------------- |
| Multi-session arcs (`session-roadmap-*.md`) | Single-session build (use STATE Milestones) |
| Sitreps with embedded roadmaps (S26-style) | Brainstorm-only sessions with no arc table |

## Required sections (in order)

| # | Section | Purpose |
| :-: | :------ | :------ |
| 1 | Mission / design intent | Why this arc exists |
| 2 | Session table + mermaid | Ordered work with branch, defer, success-when |
| 3 | Explicit deferrals | Out of scope with rationale |
| 4 | **Target snapshot (`SNN` end state)** | Project status if the arc ships in full |
| 5 | Next-session bootstrap | Copy block for STATE at approving session close |
| 6 | History | Approval + final close rows |

## Target snapshot rules

Write **Target snapshot (SNN end state)** **before** human approval. Include at
minimum:

1. **One line** — outcome in plain English
2. **Project signals** — spine %, threads, git, ADRs, inbox, mission
3. **Milestones** — arc rows with target session numbers
4. **Chapter / container status** — expected L2 state (honest about Type A gaps)
5. **Success criteria** — pass-when table aligned to mission
6. **Out of scope** — permanent deferrals (not failures if unchanged)
7. **Honest grade (forecast)** — optional; recommended for stakeholder review

At **final session close** of the arc: add **Achieved** / **Partial** / **Deferred**
per milestone — **do not delete** the target snapshot. Retroactive roadmaps may
add **Status at review** when the arc is already complete (see S19–S23, S26 sitrep).

## Examples

| Document | Final session | Target snapshot |
| :------- | :------------ | :-------------- |
| [session-roadmap-s19-s23](sessions/session-roadmap-s19-s23.md) | S23 | Achieved 2026-06-23 |
| [spine-sitrep-s26](sessions/spine-sitrep-s26.md) | S30 | Achieved 2026-06-28 |
| [session-roadmap-s40-plus](sessions/session-roadmap-s40-plus.md) | S47 | Pending — compare at S47 close |

## History

| When | Change | Snapshot |
| :---- | :----- | :------- |
| 2026-06-30 22:25 | Created | Extracted from session-workflow; S47 target added |
