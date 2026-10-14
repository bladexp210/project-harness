---
title: "Task 02: Track A golden-path task run"
task: 02
chapter: 04
status: done
agent: dev
tags: [task, build, track-a, openhands]
context_load:
  - 05-build/execution-tools/track-a-setup.md
  - 05-build/execution-tools/openhands.md
  - 05-build/execution-tools/track-a/docker-compose.yml
  - 05-build/execution-tools/track-a/litellm_config.yaml
  - 03-plan/constraints/project.md
---

# Task 02 — Track A golden-path task run

Prove the **Track A** execution path end-to-end: bring up the Docker stack,
run this task via OpenHands with stripped context, and record evidence in
canon. Smallest harness task that exercises OpenHands + LiteLLM + human review
gate without product code.

## Inputs

- [track-a-setup](../../05-build/execution-tools/track-a-setup.md) — stack setup, `.env`, virtual keys
- [openhands](../../05-build/execution-tools/openhands.md) — stack setup, prompt template, run log table
- `05-build/execution-tools/track-a/docker-compose.yml` — pinned compose
- `05-build/execution-tools/track-a/litellm_config.yaml` — agent yaml aliases
- [constraints/project](../../03-plan/constraints/project.md) — model and version rows to fill

## Controls

*Inherited — do not rewrite.* Governed by [constraints](../../03-plan/constraints/global.md) and the
acceptance criteria below.

**Scope — modify:**

- `05-build/execution-tools/openhands.md` — append one row to **Track A run log** only
- `03-plan/constraints/project.md` — **Models and endpoints** table only

**Scope — read-only:** `04-your-agents/tasks/02-track-a-golden-path.md`,
`04-your-agents/agents/dev-agent.yaml`, `03-plan/PROJECT-PLAN.md`,
`05-build/execution-tools/track-a-setup.md`

## Mechanisms

Run by the **dev agent** ([dev-agent](../agents/dev-agent.yaml)). Context via
`python scripts/task_context.py` per [context-loader](../context-loader.md).

| Track | Guide | When |
| :---- | :---- | :--- |
| **A** (ideal) | [openhands](../../05-build/execution-tools/openhands.md) + `track-a/` stack | This task — golden path proof |
| **B** (fallback) | [track-b-checklist](../../05-build/execution-tools/track-b-checklist.md) | Only if Docker blocked — document blocker instead |

Stack rules (non-negotiable):

- OpenHands → LiteLLM → OpenRouter — never bypass LiteLLM
- Virtual key for OpenHands — not `LITELLM_MASTER_KEY`
- `WORKSPACE_PATH` = session worktree or single-clone ramp — not home directory
- Git commit on Windows host only (D-001)

## Outputs

- One dated row in `openhands.md` **Track A run log** (task id, branch, model
  alias, pass/fail, short notes)
- `project.md` **Models and endpoints** filled: OpenHands version, LiteLLM
  endpoint, alias routing status
- Evidence that LiteLLM health check passed before OpenHands started

## Acceptance criteria

```gherkin
Scenario: Track A golden path completes
  Given track-a compose and litellm_config exist with pinned image tags
  And LiteLLM health check returns 200 before OpenHands starts
  When the dev agent runs this task via OpenHands with stripped context
  Then openhands.md Track A run log has a dated entry for task 02
  And project.md Models table records OpenHands version and LiteLLM endpoint
  And only Scope — modify files were changed
  And the human reviewed the diff on Windows before any commit
```

```gherkin
Scenario: Track A blocked by environment
  Given Docker or API keys are unavailable after documented setup attempt
  When the human records the blocker with evidence
  Then openhands.md run log notes the blocker and unblock condition
  And project.md status rows show blocked with reason
  And no secrets appear in committed files
```
