---
title: "Golden 02: Dev bounded patch"
task: golden-02
chapter: 04
status: reference
agent: dev
tags: [golden-task, dev, scope]
context_load:
  - 03-plan/constraints/project.md
---

# Golden 02 — Dev bounded patch (dev fixture)

**Fixture only.** Simulates a one-file doc patch within Scope — modify. Proves
dev agent defaults (`global`, `new-task`, `agent-team`) merge with task
`context_load` and ADR-006 strip.

## Scenario

Harness task asks the dev agent to append one row to the **Models and endpoints**
table in [constraints/project](../../03-plan/constraints/project.md) — no code, no Layer 1/2 context edits.

## Inputs

- [constraints/project](../../03-plan/constraints/project.md) (Models table — artifact section)
- Dev agent defaults via `agents/dev-agent.yaml`

## Controls

Inherited constraints: [constraints](../../03-plan/constraints/global.md).

**Scope — modify:** `03-plan/constraints/project.md` (Models table row only)

**Scope — read-only:** `04-your-agents/golden-tasks/02-dev-bounded-patch.md`

## ICOM

| I | Project constraint row for verified model alias |
| :-- | :---- |
| C | Dev agent + human reviewer |
| O | One new table row with endpoint evidence |
| M | `task_context.py` + Track A or B execution |

## Gherkin

```gherkin
Given a TASK.md with Scope — modify listing only project.md Models table
When the dev agent loads context via task_context.py
Then stripped output includes atomic commit and scope discipline from global constraints
And output excludes TEACH callouts from dual-purpose inputs
And the agent does not touch files outside the modify list
```

## Acceptance criteria

- [ ] Context load includes `03-plan/constraints/global.md` and `_templates/new-task.md`
- [ ] Patched row cites LiteLLM alias, not raw provider model id
- [ ] Human reviews diff before commit (D-001)
