---
title: "ADR-003: Removal vocabulary — prune / retire / sunset"
chapter: 2
status: accepted
date: 2026-06-11
tags: [decision, vocabulary]
---

# ADR-003 — Removal vocabulary: prune / retire / sunset

**Status:** accepted — 2026-06-11, by human review.

## Context

The `lifecycle-playbook-seed` added *operational pruning* (removing shipped
features, providers, data flows) to Ch. 07 — but the book already uses
"pruning" for killing un-built decomposition-tree branches
(`[PRUNED: reason]` in PROJECT-PLAN.md, [[global|constraints]], ADR-001).
One word for two different acts confuses exactly the two readers this book
serves: a human skimming, and an agent loading context. Three removal acts
exist at three product-lifecycle moments; each needs its own verb before Ch. 02
layer files and Ch. 07 are written.

## Decision

| Verb | What is removed | When | Lives in | Notation / mechanics |
| :---- | :---- | :---- | :---- | :---- |
| **Prune** | A branch never built | Plan (design-time) | Ch. 03 | `[PRUNED: reason]` + ADR cite |
| **Retire** | A shipped feature, provider, or data flow | Operate | Ch. 07 | deprecate → migrate → remove (notice, RFC 8594 headers) |
| **Sunset** | The whole product | End of life | Ch. 08 | sunset checklist, Gate F |

Cost gradient as the memory hook: pruning costs nothing (it never existed),
retiring costs a migration, sunsetting costs the product. The three verbs
are reserved — book text never uses one for another's act.

**Reversibility & blast radius:** medium reversibility — a superseding ADR
can rename, but the verbs will spread through chapters, templates, and
agent context as they're written, so renaming cost grows with every
session. Blast radius if wrong: vocabulary confusion only, no structural
damage. Fallback: vault-wide find-and-replace plus superseding ADR.

## Why

"Prune" keeps its existing, entrenched meaning — zero migration. "Retire"
is the industry-standard term for removing live capabilities, is distinct
from "deprecate" (which names only the announce phase *within*
retirement), and chains naturally: you retire features all product life;
sunset is retiring the last one. Agents benefit most: an unambiguous verb
in TASK.md or a constraint file needs no disambiguating context.

## Alternatives considered (red-teamed)

- **Qualified same word** ("design-time pruning" vs "operational pruning")
  — honest about the kinship between the acts; rejected because qualifiers
  get dropped in casual use and the bare word goes ambiguous again — the
  exact failure this ADR exists to prevent.
- **"Deprecate" as the Ch. 07 verb** — the most common industry word;
  rejected because deprecation is properly the *first phase* of retirement
  (announce), not the whole arc; using it for the arc would leave the
  announce phase nameless.
- **"Sunset a feature"** — evocative; rejected: collides head-on with
  Ch. 08's reserved meaning.

### AI-suggested approach considered and rejected

None — this decision originated from human confusion flagged by Alex;
the AI proposal above is the first candidate and was not preceded by a
rejected AI alternative.

## Pre-mortem

*If this decision fails a year from now, why?*

1. **The verbs drift in casual writing** (a chapter says "prune the old
   API") → mitigation: the three verbs + definitions go into the Ch. 00
   glossary block and Layer-1 context, so every writing agent loads them;
   reviewers treat misuse as a defect.
2. **A fourth removal act appears** (e.g. archiving data without removing
   capability) → the table extends with a new verb; the scheme is additive.
   Accepted risk: none significant.
3. **Readers find "retire" too gentle for deleting things users love** →
   tone is a chapter-writing concern, not a vocabulary one; Ch. 07 text
   carries the honesty (notice, migration, refunds), the verb stays.

## Left on the table

A full book glossary file (`00-start-here/glossary.md`) — these three
verbs plus k, ICOM, ADR, and the dual-path terms are accumulating; worth
creating when Ch. 00 setup files are written.
