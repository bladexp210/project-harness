---
title: "ADR-NNN: [short decision title]"
chapter: 02
status: proposed
date: YYYY-MM-DD
tags: [decision]
---

# ADR-NNN — [Short decision title]

**Status:** proposed | accepted | superseded by [[ADR-MMM]] — date, by what
(commit, session, review).

## Context

[Why this decision is being forced *now*. What exists, what broke, or what is
about to be built that can't proceed without it. Two to five sentences.]

## Decision

[What was decided, stated so a future agent can act on it without reading
anything else. Include the concrete artifact where applicable — naming
scheme, config block, chosen tool.]

**Reversibility & blast radius:** [how undoable is this — one-line revert,
superseding ADR, or one-way door? What is exposed if it's wrong, and what
is the fallback? This feeds the criticality axis / k threshold.]

## Why

[The positive case. Tie it to the project's constraints in
[global](../03-plan/constraints/global.md) and the priorities in [use-cases](../01-understand/use-cases.md) where relevant.]

## Alternatives considered (red-teamed)

[Each rejected option with the *strongest* version of its case, then why it
still lost. An alternative dismissed in one clause wasn't red-teamed.]

- **[Alternative A]** — [its best argument]; rejected because [reason].
- **[Alternative B]** — [its best argument]; rejected because [reason].

### AI-suggested approach considered and rejected

[When an AI agent proposed a different approach during this decision: what
it recommended, the specific reason it was wrong for *this* system, and
what that reveals the AI was missing. Feed that missing knowledge back into
the relevant context/ file — that is the point of this field. Write "none"
if the AI's suggestion was adopted or no AI was consulted.]

## Pre-mortem

*If this decision fails a year from now, why?*

Run by the **red-team agent** before status moves to accepted — see
[agent-team](../context/system/agent-team.md). The red-team agent assumes the decision has already failed
and works backward to the cause; the human accepts the decision only after
each failure path has a mitigation or an explicit "accepted risk" note.

1. [Failure path] → mitigation: [what blunts it, or "accepted risk: why".]
2. [Failure path] → mitigation: [...]
3. [Failure path] → mitigation: [...]

## Left on the table

[Options not pursued but not wrong — what would make them worth revisiting.
This is where the *next* project shops first.]
