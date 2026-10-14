---
title: "arc42 §9 — Architectural Decisions"
chapter: 02
status: reference
audience: [novice, seasoned, both]
tags: [arc42, design, decisions, harness]
---

# arc42 §9 — Architectural Decisions

**Question answered:** Which significant design choices were made, when, and
why?

> [!NOTE] REAL — harness-meta
> This index lists **all accepted ADRs** for the book harness. Full text,
> alternatives, and pre-mortems stay in `02-design/decisions/` — §9 is the
> arc42 decision log, not a duplicate archive.

## Decision log

| ID | Title | Status | Date | Decision (one line) |
| :---- | :---- | :----- | :--- | :------------------ |
| [ADR-001](../decisions/ADR-001-chapter-folder-naming.md) | Chapter folder naming | accepted | 2026-06-10 | Kebab-case, zero-padded `NN-short-title/` for all chapters |
| [ADR-002](../decisions/ADR-002-modeling-conventions.md) | Modeling conventions | accepted | 2026-06-10 | Mermaid by question; ICOM+ task model; ≤ 20 nodes |
| [ADR-003](../decisions/ADR-003-removal-vocabulary.md) | Removal vocabulary | accepted | 2026-06-11 | **prune** (plan) · **retire** (shipped feature) · **sunset** (product) |
| [ADR-004](../decisions/ADR-004-lifecycle-vocabulary.md) | Product/user/feature/data/task vocabulary | accepted | 2026-06-11 | Five named kinds — always qualify the noun |
| [ADR-005](../decisions/ADR-005-failure-condition-convention.md) | Failure-condition convention | accepted | 2026-06-11 | Every recommended pattern names when *not* to apply it |
| [ADR-006](../decisions/ADR-006-teaching-block-convention.md) | Teaching-block convention | accepted | 2026-06-19 | Instruction delimited from artifact zones (evaluator + lint) |
| [ADR-007](../decisions/ADR-007-dual-execution-tracks.md) | Dual execution tracks | accepted | 2026-06-17 | Track A ideal (OpenHands stack); Track B fallback (IDE agents) |
| [ADR-008](../decisions/ADR-008-reader-facing-language-and-visuals.md) | Reader-facing language and visuals | accepted | 2026-06-19 | Plain language gates; tables over fog; wiki-link conventions |
| [ADR-009](../decisions/ADR-009-observability-paths-abc.md) | Observability Paths A/B/C | accepted | 2026-07-01 | Path A live; Path B documented; Path C S44; process trace mandatory |

## Process

New decisions use [the ADR template](../../_templates/new-decision.md) — write at
decision time, not after. When you add an ADR, append one row to the table
above.

| Step | Action |
| :---- | :----- |
| 1 | Copy `new-decision` template → `decisions/ADR-NNN-short-title.md` |
| 2 | Record context, decision, reversibility, rejected alternatives |
| 3 | Add row to this §9 table |
| 4 | Link from affected layer files or chapter prose |

## Where to go next

- **ADR files:** `02-design/decisions/`
- **Template:** [new-decision](../../_templates/new-decision.md)
- **Ch. 02 decisions section:** [../](../README.md#decisions-live-in-decisions)
- **Section index:** [README](README.md)
