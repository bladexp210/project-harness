---
title: "Golden 01: Design-option tiebreak"
task: golden-01
chapter: 04
status: reference
agent: evaluator
tags: [golden-task, evaluator, k-voting]
context_load:
  - 04-your-agents/evaluator.md
---

# Golden 01 — Design-option tiebreak (evaluator fixture)

**Fixture only.** Simulates k-voting split on a cache strategy choice. Run
through `task_context.py` to verify evaluator context load and ADR-006 strip.

## Scenario

Parallel voters split on two options for a read-heavy catalog API:

| Option | Summary |
| :---- | :---- |
| A | Redis cache-aside on product reads |
| B | In-process LRU; no external cache |

k margin **not** cleared. Evaluator runs as tiebreaker per [evaluator](../evaluator.md).

## Inputs

- [evaluator](../evaluator.md) (bias mitigations + tiebreak flow)
- Criteria below (artifact — not teaching prose)

## Controls

Apply all four bias mitigations from [evaluator](../evaluator.md) before scoring.

Inherited constraints: [constraints](../../03-plan/constraints/global.md).

## ICOM

| I | Cache read path for product catalog |
| :-- | :---- |
| C | Evaluator agent + human reviewer |
| O | Score matrix per criterion |
| M | k-voting split; mitigations recorded |

## Gherkin

```gherkin
Given two design options A and B and a split k-voting result
When the evaluator scores each option on latency, ops cost, and failure modes
And position swap and family separation are applied
Then the output is a per-criterion score matrix with no sole-judge verdict
And a human records the winner with evidence
```

## Acceptance criteria

- [ ] Score matrix covers latency, ops cost, failure modes separately
- [ ] Position-swap rerun documented when ranks flip
- [ ] Human sign-off before winner is recorded
