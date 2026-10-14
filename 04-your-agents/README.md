---
title: Your Agents
chapter: 04
status: in-progress
audience: [novice, seasoned, both]
tags: [agents, team, orientation]
---

# 04 — Your Agents

This chapter turns the plan from [[03-plan/PROJECT-PLAN|Ch. 03]] into an
agent team that can execute it. Each agent is a bounded role in a `.yaml`
file (≤ 60 lines); each task from [[new-task]] names which agent runs it
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

Permanent on every project. Full reference: [[agent-team]].

| Role | File | Mandate |
| :---- | :---- | :---- |
| Dev Agent | [[dev-agent]] | Execute bounded build tasks |
| General Tester | [[tester-agent]] | Break the implementation |
| Security Tester | [[security-tester]] | Injection, auth bypass, CVE patterns |
| Evaluator | [[evaluator]] | Score options; run as k-voting tiebreaker |
| Red-team | [[red-team-agent]] | Pre-mortems, threat model, must-have lane challenges |

Each role is a `.yaml` contract (mandate, model alias, context load, outputs).
The red-team agent holds the security/compliance seat (ADR pre-mortems,
[[threat-model]] Gate B, use-case must-have challenges) — see
`research/red-team-seed.md` and `research/lifecycle-playbook-seed.md`.

## Orchestration rule

Every agent run is bound to **one task file** with named Executor, Supervisor,
and scope. Agents do not spawn follow-on tasks or invoke sibling agents unless
the active task's Outputs explicitly hand off to the next task file. Multi-agent
work splits across tasks with explicit Outputs → Inputs handoff — one Executor
per task sitting. See [[agent-team]] and [[icom-plus-convention]].

## Context loading

Agents load only what their task lists. The [[context-loader]] strips
`[!LEARN]` / `[!TIP]` / `[!TEACH]` teaching blocks per [[ADR-006-teaching-block-convention|ADR-006]]
before passing dual-purpose files to the model.

**Worked example:** this repo's harness-meta tree lives in `context/` — see
[[context/README|context/README.md]] for the three-layer map (system →
architecture → implementation). Your product repo starts from
[[06-learn/boilerplate/reader-skeleton/README|reader-skeleton]]; replace Layer
2/3 with distillations from Ch. 02 layer designs.

## Evaluator and golden tasks

Scoring, k-voting tiebreak, and bias mitigations: [[evaluator]]. Fixture
tasks that regression-test the evaluator path: `golden-tasks/` (see
`scripts/test_golden_tasks.py`).

## Harness example task

This book's own threat model is the first task run through the template:

| # | Task | Agent | File |
| :-- | :-- | :-- | :-- |
| 01 | Threat-model pre-mortem review | red-team | [[tasks/01-threat-model-premortem]] |
| 02 | Track A golden-path task run | dev | [[tasks/02-track-a-golden-path]] |
| 03 | Populate `context/` example tree | dev | [[tasks/03-populate-context-tree]] |
| 04 | Ch. 06 learn-loop templates | dev | [[tasks/04-ch06-learn-loop-templates]] |

*Your project replaces these rows with real tasks from PROJECT-PLAN.md.*
