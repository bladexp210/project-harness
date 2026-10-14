---
title: "Task 01: Threat-model pre-mortem review"
task: 01
chapter: 04
status: done
agent: red-team
tags: [task, security, premortem]
context_load:
  - 02-design/threat-model.md
  - 02-design/decisions/ADR-005-failure-condition-convention.md
---

# Task 01 — Threat-model pre-mortem review

Run the red-team agent's pre-mortem pass on the harness project's
[threat-model](../../02-design/threat-model.md) before Ch. 05 build work begins — smallest task that
exercises agent assignment + context load + ICOM/Gherkin closure.

## Inputs

- [threat-model](../../02-design/threat-model.md) (artifact sections — loader strips teaching blocks)
- [ADR-005-failure-condition-convention](../../02-design/decisions/ADR-005-failure-condition-convention.md) (failure-condition convention)
- `research/red-team-seed.md` (AI-specific threat evidence)
- `research/lifecycle-playbook-seed.md` (Gate B — design-phase gate)

## Controls

*Inherited — do not rewrite.* Governed by [constraints](../../03-plan/constraints/global.md) and the
acceptance criteria below.

**Scope — modify:** `02-design/threat-model.md` (add review-log section only)

**Scope — read-only:** `01-understand/use-cases.md`, `03-plan/PROJECT-PLAN.md`,
`04-your-agents/agents/red-team-agent.yaml`

## Mechanisms

Run by the **red-team agent** ([red-team-agent](../agents/red-team-agent.yaml)). Context via
`python scripts/task_context.py` per [context-loader](../context-loader.md) — teaching callouts
stripped from dual-purpose inputs.

| Track | Guide | When |
| :---- | :---- | :--- |
| **A** (ideal) | [openhands](../../05-build/execution-tools/openhands.md) | Docker + LiteLLM/OpenRouter ready |
| **B** (fallback) | [track-b-checklist](../../05-build/execution-tools/track-b-checklist.md) | IDE/CLI agent; use checklist §1–§7 |

Pick one track per run; same task file and acceptance criteria either way
([ADR-007-dual-execution-tracks](../../02-design/decisions/ADR-007-dual-execution-tracks.md)).

> [!NOTE] Visual map (experimental)
> Open `_playground/icom/task-01/task-01.html` in a browser for an ICOM
> layout with short labels and file links — not agent-loaded.

## Outputs

- `## Review log` section appended to `02-design/threat-model.md` with
  dated pre-mortem entry (threats challenged, gaps found, Gate B status)
- One escalation note if a must-have use-case control is missing

## Acceptance criteria

```gherkin
Scenario: Threat-model pre-mortem completes
  Given the threat-model crown-jewels and AI-specific threat table exist
  When the red-team agent runs the pre-mortem checklist
  Then a dated review-log entry exists in threat-model.md
  And every open abuse case names a detection or recovery control
  And Gate B checklist items are explicitly pass or fail with evidence
```
