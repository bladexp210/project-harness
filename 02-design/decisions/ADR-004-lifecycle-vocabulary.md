---
title: "ADR-004: Lifecycle vocabulary — five lifecycles, never bare"
chapter: 2
status: accepted
date: 2026-06-11
tags: [decision, vocabulary]
---

# ADR-004 — Lifecycle vocabulary: five lifecycles, never bare

**Status:** accepted — 2026-06-11, by human review.

## Context

The book's spine is "the lifecycle" (ideation → sunset), but at least four
other things in its pages also live and die: users, features, data, and
tasks. The word "lifecycle" unqualified is already ambiguous in our own
files — [use-cases](../../01-understand/use-cases.md) says "end-of-life use cases" for *export my data /
delete my account*, which is a **user** leaving a healthy product, not the
**product** ending. The 02-design session is about to write the data layer
(data lifecycle) and ux layer (user lifecycle states); the vocabulary must
be fixed first, while renaming is still cheap. Companion to
[ADR-003-removal-vocabulary](ADR-003-removal-vocabulary.md).

## Decision

Five recognized lifecycles. Book text **never uses "lifecycle" bare** —
always qualified with its subject:

| Lifecycle | Subject | Arc | Owner chapters |
| :---- | :---- | :---- | :---- |
| **Product lifecycle** | the product | idea → understand → design → build → operate → sunset | the spine (00–08) |
| **User lifecycle** | one user/account | onboard → active → dormant → **offboard** | 01 (use cases), 02-ux (states), 07 (operations) |
| **Feature lifecycle** | one capability | pruned ∣ built → shipped → **retired** | 03 → 05 → 07 (verbs per ADR-003) |
| **Data lifecycle** | one record/class | created → used → retained → **deleted/archived** | 02-data, 07, 08 |
| **Task lifecycle** | one unit of work | defined → executed → verified → **closed** | 03, 05 (ICOM + Gherkin) |

Reserved endings (each lifecycle ends with its own verb, per the table):
**offboard** is the user-side ending — "end-of-life" is reserved for the
product. [use-cases](../../01-understand/use-cases.md) wording changes from "end-of-life use cases" to
"offboarding use cases".

The connecting insight (book text should state it once, in Ch. 08):
**product sunset is mass user offboarding** — the export and deletion
mechanics built for routine offboarding (GDPR obligations that exist from
day one) are exactly what makes sunset cheap. Likewise sunset is mass
feature retirement and the final stage of every record's data lifecycle.
The lifecycles nest; the vocabulary keeps the levels apart.

**Reversibility & blast radius:** same profile as ADR-003 — renaming cost
grows with every chapter written; blast radius is confusion, not
structure. Fallback: vault-wide audit + superseding ADR.

## Why

Humans skim and agents load fragments — both lose the disambiguating
context around a bare "lifecycle" or "end-of-life". Qualified-always is a
mechanical rule that needs no judgment to follow, and the five subjects
were all already present in our seeds (user lifecycle in the UX/discovery
seeds, data lifecycle in the EOL seed's retention classes, feature
lifecycle in ADR-003, task lifecycle in ADR-002) — this ADR names what
exists rather than inventing structure.

## Alternatives considered (red-teamed)

- **Define only product + user now, others later** — smallest decision;
  rejected: the other three are already in committed text (ADR-002,
  ADR-003, retention classes in seeds), so deferring them just schedules a
  second vocabulary session for no savings.
- **"Churn" for user ending** — the standard SaaS metric term; rejected as
  the *verb*: churn names the business phenomenon (involuntary, measured in
  aggregate); offboarding names the designed pathway one user walks. Churn
  stays available as a metric word in Ch. 07.
- **"Account lifecycle" instead of "user lifecycle"** — more precise where
  one human holds several accounts; rejected as primary because Ch. 01
  models *people* (user roles), and account-vs-user splits are a
  product-specific design call — noted for the data layer template as a
  prompt, not a vocabulary rule.

### AI-suggested approach considered and rejected

None — flagged by Alex; this is the first worked proposal.

## Pre-mortem

*If this decision fails a year from now, why?*

1. **Bare "lifecycle" creeps back in** as chapters multiply → mitigation:
   the five-row table joins the three ADR-003 verbs in the planned glossary
   block and Layer-1 context; candidate future lint: flag bare "lifecycle"
   in validate_md.py (logged in Left on the table).
2. **A product genuinely needs a sixth lifecycle** (e.g. model lifecycle
   for ML products: trained → deployed → drifted → retrained) → additive;
   the table extends. The rule "never bare, always qualified" already
   covers unknown additions.
3. **Offboard/retire confusion at the boundary** (removing a feature forces
   users to offboard from it) → Ch. 07 retirement mechanics explicitly
   include the user-communication step; the verbs name *what is removed*
   (capability vs account), not who is affected.

## Left on the table

A `validate_md.py` rule flagging unqualified "lifecycle" outside code
fences and this ADR — cheap, mechanical, catches drift at commit time.
The glossary file (`00-start-here/glossary.md`) — now carrying ADR-003's
three verbs plus this table; create when Ch. 00 setup files are written.
Model lifecycle as a sixth row — add when an ML-product example enters the
book.
