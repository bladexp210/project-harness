---
title: "Golden 05: Red-team pre-mortem gate"
task: golden-05
chapter: 04
status: reference
agent: red-team
tags: [golden-task, red-team, premortem]
context_load:
  - 02-design/decisions/ADR-005-failure-condition-convention.md
---

# Golden 05 — Red-team pre-mortem gate (red-team fixture)

**Fixture only.** Simulates Gate B pre-mortem on a hypothetical caching ADR
before implementation binds. Proves red-team defaults load threat model, seeds,
and pre-mortem mandate in stripped context.

## Scenario

Team proposes ADR: "Redis cache-aside for catalog reads." Red-team runs
pre-mortem checklist — reversibility, blast radius, abuse cases, Gate B items —
without implementing the cache.

## Inputs

- [[ADR-005-failure-condition-convention]] (failure-condition convention)
- Red-team defaults (`threat-model.md`, `red-team-seed.md`, `lifecycle-playbook-seed.md`)

## Controls

Inherited constraints: [[global|constraints]].

**Scope — modify:** none (fixture — pre-mortem notes only)

**Scope — read-only:** `02-design/threat-model.md`, draft ADR under review

## ICOM

| I | Draft ADR + threat-model crown jewels |
| :-- | :---- |
| C | Red-team agent + human gate |
| O | Pre-mortem log: pass/fail per Gate B item |
| M | Sequential challenge before decision binds |

## Gherkin

```gherkin
Given a draft ADR for external cache on read path
When the red-team agent loads context via task_context.py
Then output includes pre-mortem or Gate B language from lifecycle seed
And failure-condition detection/recovery required per ADR-005
And must-have lane omissions are flagged if absent from use cases
```

## Acceptance criteria

- [ ] Each Gate B item explicitly pass or fail with evidence
- [ ] Open abuse cases name detection or recovery control
- [ ] Human records outcome before ADR accepted
