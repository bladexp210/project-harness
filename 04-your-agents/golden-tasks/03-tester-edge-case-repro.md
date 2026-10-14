---
title: "Golden 03: Tester edge-case repro"
task: golden-03
chapter: 04
status: reference
agent: tester
tags: [golden-task, tester, adversarial]
context_load:
  - 04-your-agents/tasks/02-track-a-golden-path.md
---

# Golden 03 — Tester edge-case repro (tester fixture)

**Fixture only.** Simulates adversarial testing when Track A run log accepts a
pass without LiteLLM health evidence. Proves tester defaults include
`lifecycle-playbook-seed.md` Gate B language and break-the-build mandate in
stripped context.

## Scenario

Dev agent marked task 02 **pass** in the OpenHands run log. Tester agent must
produce a failing repro: health check not cited in the log row.

## Inputs

- [02-track-a-golden-path](../tasks/02-track-a-golden-path.md) (acceptance criteria — artifact)
- Tester agent defaults (`lifecycle-playbook-seed.md`, `agent-team.md`)

## Controls

Inherited constraints: [constraints](../../03-plan/constraints/global.md).

**Scope — modify:** none (fixture — report only)

**Scope — read-only:** `05-build/execution-tools/openhands.md` run log section

## ICOM

| I | Run log row + task 02 Gherkin |
| :-- | :---- |
| C | Tester agent |
| O | Minimal repro steps; no production fix |
| M | Adversarial review against acceptance criteria |

## Gherkin

```gherkin
Given a run log row marked pass without LiteLLM health evidence
When the tester agent loads context via task_context.py
Then output includes Gate B testable-requirements language from lifecycle seed
And the tester reports repro steps, not implementation patches
And edge-case or invalid-state framing appears in the fixture criteria
```

## Acceptance criteria

- [ ] Repro cites missing health-check evidence from task 02 Then clause
- [ ] No code changes in tester output — report only
- [ ] Human triages finding before dev re-run
