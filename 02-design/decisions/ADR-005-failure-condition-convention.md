---
title: "ADR-005: Failure-condition convention for recommended patterns"
chapter: 02
status: accepted
date: 2026-06-11
tags: [decision, conventions, ch02]
---

# ADR-005 — Failure-condition convention for recommended patterns

**Status:** accepted — 2026-06-11, by human review (session 6 decide-first
gate) after pre-mortem.

## Context

The four [Ch. 02](../README.md) layer files are about to be written, and each
will recommend patterns: modular monolith, Postgres-first, cache strategies,
latency budgets. The red-team seed (`research/red-team-seed.md`) shows what
happens to recommendations that travel without their limits: cargo-cult
adoption — microservices applied without Fowler's prerequisites, NoSQL
chosen where JSONB sufficed, service meshes burning up to 90% of resources
as sidecar overhead. Every one of those patterns was *correct somewhere*;
the failure was missing context about where it stops being correct. The
decision must land before the first layer file, because the convention
shapes their structure.

## Decision

Every recommended pattern in this book carries its **failure condition**,
using the Claim → Evidence → Failure Condition structure:

- **Claim** — the recommendation, stated plainly.
- **Evidence** — why it's believed (citation, seed reference, or named
  experience; per the provenance discipline, `source → section`).
- **Failure condition** — the observable circumstances under which the
  recommendation is wrong, stated concretely enough that a reader can check
  their own project against it.

In [ADR-002](ADR-002-modeling-conventions.md) decision tables, the failure
condition surfaces as a **"when NOT to apply"** row/column. In prose, it is
a closing sentence or callout per pattern — no new heading ceremony
required. Binding on all four layer files, the threat-model artifact, and
any future chapter content that recommends a pattern.

**Foundational filters (Brooks, Parnas).** Failure conditions are the
book's operational form of axiomatic and strategic checks:

- **Brooks test:** if the failure would persist after changing frameworks or
  vendors, the pattern addresses **essential** complexity — state that
  honestly in the failure condition rather than blaming the tool.
- **Parnas over-application:** failure conditions on decomposition patterns
  must name **observable coupling** ("adjacent services share database
  tables") — not vague "depends on context."
- **Hoare link:** a failure condition is the class of **violated
  postconditions** under which the recommendation fails; pair with
  pre/post tables on irreversible-gate tasks ([ADR-002](ADR-002-modeling-conventions.md)
  Part 3).

Use the five-question checklist in [Ch. 02 README](../README.md) before
locking layer decisions.

**Reversibility & blast radius:** reversible by superseding ADR; existing
files keep the structure (it degrades to harmless extra context). Blast
radius is authoring cost only — no tooling or pipeline depends on it.

## Why

The convention is the book's own context-check protocol applied to itself:
"under what conditions does the practice fail" becomes a required field
instead of an exercise left to the reader. It directly serves the audience
constraint in [overview](../../context/system/overview.md) — novices cannot supply missing context
themselves, so the guardrail must carry it. And it is cheap: one sentence
or one table row per pattern, written while the evidence is already open.

## Alternatives considered (red-teamed)

- **Soft convention, no ADR** — same content, less ceremony; the writing
  session can just do it. Rejected because Ch. 02 is not the last consumer:
  Ch. 03 task templates and Ch. 04 agent docs will also recommend patterns,
  and an unwritten convention does not bind future sessions (the exact
  spec-entropy failure the red-team seed documents).
- **Full evidence-grading scheme** (GRADE-style confidence levels per
  claim) — more honest about evidence quality, anticipates challenge 4
  (our own seeds carry survivorship bias). Rejected as ceremony beyond
  what a book chapter bears; the `source → section` provenance markers
  plus a failure condition capture the actionable 90%. Revisit if a
  claim's evidence quality itself becomes a dispute.
- **Defer until the data layer shows the need** — cheapest now; rejected
  because the data layer was *chosen first precisely to stress-test the
  convention* (CAP, cache invalidation, sharding all have crisp failure
  conditions) — deferring inverts the session design.

### AI-suggested approach considered and rejected

None — the AI co-author recommended adoption via ADR, and the human
accepted.

## Pre-mortem

*If this decision fails a year from now, why?*

Run by the red-team agent before acceptance.

1. **Failure conditions rot into boilerplate** — authors write vague
   filler ("may not suit all projects") to satisfy the convention →
   mitigation: a failure condition must be *observable and checkable*
   ("you have one team and < 10k daily users" — yes; "depends on context"
   — no). The validator can't check this, but review can: a failure
   condition a reader cannot test against their project is a
   [DEBT-LEDGER](../../06-learn/DEBT-LEDGER.md) entry.
2. **Convention applied asymmetrically** — patterns the author likes get
   weak failure conditions → mitigation: the red-team agent's review seat
   covers layer files; its brief includes challenging the failure
   conditions of *recommended* options hardest.
3. **Authoring drag** — every pattern needs evidence the writer doesn't
   have → accepted risk: if evidence is missing, the honest move is to say
   so inline ("asserted, not proven" — the ADR-honesty rule from the
   red-team seed) rather than skip the pattern or fabricate a citation.

## Left on the table

Machine-checkable enforcement — a lint rule that flags a decision table
missing a "when NOT to apply" row. Worth revisiting when the validator
grows its next rule batch (pairs with the bare-[lifecycle](ADR-004-lifecycle-vocabulary.md) vocabulary lint in T7).
GRADE-style evidence grading, if a future chapter's claims get disputed on
evidence quality.
