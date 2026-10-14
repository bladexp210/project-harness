---
title: Golden-Task Suite
chapter: 04
status: reference
audience: [novice, seasoned, both]
tags: [agents, testing, fixtures]
---

# Golden-task suite — agent path fixtures

These tasks are **harness fixtures**, not reader product work. Each one proves
one agent role loads the right context through `task_context.py` and ADR-006
stripping.

| # | Agent | Proves |
| :-- | :---- | :---- |
| 01 | evaluator | Tiebreak scoring path + bias mitigations in context |
| 02 | dev | Bounded patch within Scope — modify; global + new-task defaults |
| 03 | tester | Adversarial repro + playbook Gate B seed in context |
| 04 | security-tester | Threat-model §4 injection + red-team seed in context |
| 05 | red-team | Pre-mortem Gate B + ADR-005 failure conditions in context |

Teaching walkthrough (Ch. 03): [[golden-task-examples|03-plan/golden-task-examples]].

Add a row when a new core role needs a regression fixture. Keep each file
≤ 100 lines ([[global|constraints]]).

Tests: `python scripts/test_golden_tasks.py`.
