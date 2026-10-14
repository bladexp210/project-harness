---
title: Your Agents
chapter: 04
status: in-progress
audience: [novice, seasoned, both]
tags: [agents, team, orientation]
---

# 04 — Your Agents

This chapter turns the plan from [Ch. 03](../03-plan/PROJECT-PLAN.md) into an
agent team that can execute it. Each agent is a bounded role in a `.yaml`
file (≤ 60 lines); each task from [new-task](../_templates/new-task.md) names which agent runs it
and exactly which context files to load.

> [!LEARN] Learn It
> Agents are not chat personas — they are **contracts**: a mandate, a model
> axis, a context-load list, and scope rules. The human orchestrates; agents
> execute bounded tasks. The red-team agent holds the security/compliance
> seat and runs pre-mortems before decisions land.

> [!TIP] Fast Track
> Start with the five-role core team below. Fork specialists only when
> post-mortems show a systematic gap.

## Core team

Permanent on every project. Full reference: [agent-team](../context/system/agent-team.md).

| Role | File | Mandate |
| :---- | :---- | :---- |
| Dev Agent | [dev-agent](agents/dev-agent.yaml) | Execute bounded build tasks |
| General Tester | [tester-agent](agents/tester-agent.yaml) | Break the implementation |
| Security Tester | [security-tester](agents/security-tester.yaml) | Injection, auth bypass, CVE patterns |
| Evaluator | [evaluator](evaluator.md) | Score options; run as k-voting tiebreaker |
| Red-team | [red-team-agent](agents/red-team-agent.yaml) | Pre-mortems, threat model, must-have lane challenges |

Each role is a `.yaml` contract (mandate, model alias, context load, outputs).
The red-team agent holds the security/compliance seat (ADR pre-mortems,
[threat-model](../02-design/threat-model.md) Gate B, use-case must-have challenges) — see
`research/red-team-seed.md` and `research/lifecycle-playbook-seed.md`.

## Orchestration rule

Every agent run is bound to **one task file** with named Executor, Supervisor,
and scope. Agents do not spawn follow-on tasks or invoke sibling agents unless
the active task's Outputs explicitly hand off to the next task file. Multi-agent
work splits across tasks with explicit Outputs → Inputs handoff — one Executor
per task sitting. See [agent-team](../context/system/agent-team.md) and [icom-plus-convention](../_playground/icom-plus-convention.md).

## Context loading

Agents load only what their task lists. The [context-loader](context-loader.md) strips
`[!LEARN]` / `[!TIP]` / `[!TEACH]` teaching blocks per [ADR-006](../02-design/decisions/ADR-006-teaching-block-convention.md)
before passing dual-purpose files to the model.

**Worked example:** this repo's harness-meta tree lives in `context/` — see
[context/README.md](../context/README.md) for the three-layer map (system →
architecture → implementation). Your product repo starts from
[reader-skeleton](../06-learn/boilerplate/reader-skeleton/README.md); replace Layer
2/3 with distillations from Ch. 02 layer designs.

## Evaluator and golden tasks

Scoring, k-voting tiebreak, and bias mitigations: [evaluator](evaluator.md). Fixture
tasks that regression-test the evaluator path: `golden-tasks/` (see
`scripts/test_golden_tasks.py`).

## Harness example task

This book's own threat model is the first task run through the template:

| # | Task | Agent | File |
| :-- | :-- | :-- | :-- |
| 01 | Threat-model pre-mortem review | red-team | [01-threat-model-premortem](tasks/01-threat-model-premortem.md) |
| 02 | Track A golden-path task run | dev | [02-track-a-golden-path](tasks/02-track-a-golden-path.md) |
| 03 | Populate `context/` example tree | dev | [03-populate-context-tree](tasks/03-populate-context-tree.md) |
| 04 | Ch. 06 learn-loop templates | dev | [04-ch06-learn-loop-templates](tasks/04-ch06-learn-loop-templates.md) |

*Your project replaces these rows with real tasks from PROJECT-PLAN.md.*
