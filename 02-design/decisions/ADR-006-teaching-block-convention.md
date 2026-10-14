---
title: "ADR-006: Teaching-block convention — instruction delimited from artifact"
chapter: 2
status: accepted
date: 2026-06-11
tags:
  - decision
  - conventions
  - legibility
---

# ADR-006 — Teaching-block convention: instruction delimited from artifact

**Status:** accepted — 2026-06-11, by human decision after the Session 7
critical-analysis review.

## Context

The book's central conceit — every file teaches the reader *and* operates as a
functional project artifact — bundles instructional prose and reader-fillable
artifact in the same file. An independent critical analysis
(`_inbox/2026-06-11 1617 project-harness_critical_analysis.md`) named the cost:
a builder agent loading `02-design/layers/ux.md` for a task must wade through
WCAG and Fitts's-Law prose to reach a five-row table, inflating context and
directly contradicting [[Agents.md|Agents]]' "load only what your task needs."
The tension was real and undecided; this ADR resolves it without splitting the
vault.

## Decision

In **dual-purpose files** — chapter files that mix instruction with
reader-fillable artifact (layer designs, use-cases, PROJECT-PLAN, task files,
constraint files) — instructional content lives inside **delimited teaching
blocks**; everything outside them is project artifact.

The delimiter is the existing Obsidian callout family, extended by one:

- `> [!LEARN]` — the scaffold-path explanation (existing)
- `> [!TIP]` — the fast-track (existing)
- `> [!TEACH]` — explanatory instructional prose that is neither dual-path
  branch (new; replaces bare instructional paragraphs)

Rule: **teaching = callout; artifact = plain markdown.** A context loader
(Ch. 04) strips `[!LEARN]` / `[!TIP]` / `[!TEACH]` blocks when loading a file
as task context; a human reading or editing the vault sees both, rendered
natively.

Out of scope: pure-orientation files (`00-start-here/README.md`,
`manifesto.md`) and pure-decision files (ADRs) — they are not dual-purpose and
stay as prose.

**Reversibility & blast radius:** high reversibility — a convention, not a
structure. Reverting means the loader stops stripping; nothing else changes.
Blast radius low: a misclassified block is either loaded when it could have
been skipped (mild bloat) or skipped when it should have loaded (caught in
review). No artifact data is moved or duplicated. Not a one-way door.

## Why

It resolves the bloat contradiction at its source — agents drop instruction,
keep artifact — while preserving "the folder you are standing in *is* the
method": one tree, no duplication, no sync burden. Callouts keep instruction
*visible and versioned* rather than hidden in HTML comments, honoring the
[[manifesto]]'s legibility-over-hidden-cleverness stance. It reuses the
dominant existing pattern (`[!LEARN]` / `[!TIP]`), so most dual-purpose files
are already half-compliant. The strip rule is mechanical, so the Ch. 04 loader
and a future lint can both act on it without parsing meaning.

## Alternatives considered (red-teamed)

- **Dual-directory split (`guide/` + `project/`)** — the critical analysis's
  lead recommendation; cleanest separation of concerns, agents read only
  `project/`. Rejected: it breaks the core thesis ("the folder is the
  method"), and it reintroduces exactly the duplication-and-drift problem the
  project fights everywhere else — two files per chapter to keep in sync, the
  artifact silently diverging from the guide. Trades in-file bloat for
  cross-file rot.
- **HTML-comment fences (`<!-- teach -->`)** — invisible in the rendered view,
  trivially machine-detectable. Rejected: hides instruction in the raw file,
  against legibility; content inside comments rots unseen.
- **Accept until Ch. 05** — do nothing until an agent actually consumes a
  layer file as build context. Rejected as the primary path: the convention is
  far cheaper to set now, before task and layer files multiply, than to
  retrofit a larger corpus later. Its one merit — low urgency — is acknowledged
  in pre-mortem #1.

### AI-suggested approach considered and rejected

The critical-analysis document is itself AI-generated; its Recommendation A
(the dual-directory split above) is the AI-suggested approach, and it was
rejected for the reasons listed. What the suggestion was missing: the
non-negotiable weight of the "folder is the method" thesis and the project's
aversion to duplicated sources of truth. That context now lives in this ADR so
the next agent does not re-propose the split.

## Pre-mortem

*If this decision fails a year from now, why?*

1. **Nothing strips the blocks** — the Ch. 04 loader is never built, so the
   convention is documentation theatre and the bloat persists → mitigation:
   the payoff is realized at the loader; until Ch. 04 exists this is an
   *accepted, low-cost* convention that already improves human readability.
   The loader is the named consumer for thread T9.
2. **Authors misfile content** — artifact text ends up inside a teaching
   callout, or instruction leaks into plain prose → mitigation: a lint rule
   (T7 batch) flags reader-fillable placeholders inside teaching blocks; review
   is the interim gate.
3. **Callout soup** — `[!TEACH]` spreads until dual-purpose files are mostly
   callout → mitigation: scope is dual-purpose files only. A file that is
   *all* teaching belongs in Ch. 00 or is a pure guide — a signal to re-place
   it, not to wrap it.

## Left on the table

A build-time "artifact-only" rendered view (Quartz query or script) for
readers who want the clean project without instruction. Executable stripping
wired into the Ch. 04 context loader — the natural home, deferred until that
chapter exists.
