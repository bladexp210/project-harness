---
title: "Task 04: Ch. 06 learn-loop templates"
task: 04
chapter: 04
status: done
agent: dev
tags: [task, learn, boilerplate, post-mortem]
context_load:
  - 06-learn/DEBT-LEDGER.md
  - context/system/session-workflow.md
  - context/system/sessions/session-1-v2.md
  - 05-build/README.md
---

# Task 04 — Ch. 06 learn-loop templates

Ship Ch. 06 **Canon Gap (Type B)**: boilerplate library stubs with two
harness-meta worked examples, a single post-mortem template, and chapter README
wiring the learn loop. Document-only in S23 — no Track A/B run.

## Inputs

- [[DEBT-LEDGER]] — debt register pattern to reference from post-mortems
- [[session-workflow]] — session close checklist source
- [[session-1-v2]] — boilerplate promotion loop (design intent)
- [[05-build/README]] — build → learn handoff

## Controls

*Inherited — do not rewrite.* Governed by [[global|constraints]] and the
acceptance criteria below.

**Scope — modify:**

- `06-learn/README.md`
- `06-learn/boilerplate/**`
- `06-learn/post-mortems/**`
- `_templates/post-mortem.md`
- `04-your-agents/README.md` (harness task table — row 04 only)
- `03-plan/PROJECT-PLAN.md` (row 04 file column and status only)
- `05-build/README.md` (learn-loop cross-link only)

**Scope — read-only:** `04-your-agents/tasks/04-ch06-learn-loop-templates.md`,
`_templates/new-task.md`, `context/system/sessions/session-roadmap-s19-s23.md`

## Mechanisms

Run by the **dev agent** ([[dev-agent]]).

| Track | Guide | S23 choice |
| :---- | :---- | :---- |
| **A** (ideal) | [[openhands]] | **Not run** — document-only session |
| **B** (fallback) | [[track-b-checklist]] | **Not run** — canon authored directly |

## Outputs

- Ch. 06 README with learning-loop diagram
- `boilerplate/` tree with two harness-meta spec examples
- `_templates/post-mortem.md` + `post-mortems/` README and one worked example
- Task 04 row in PROJECT-PLAN marked `done`
- Ch. 04 README task table includes row 04

## Acceptance criteria

```gherkin
Scenario: Ch. 06 learn loop is usable after a build cycle
  Given task 03 is done and Ch. 06 Canon Gap lists boilerplate and post-mortems
  When task 04 scope is applied on branch session-23/ch06-learn-loop
  Then 06-learn/README.md describes the learning loop and three sinks
  And 06-learn/boilerplate/specs/ contains two harness-meta worked examples
  And _templates/post-mortem.md exists as the single post-mortem template
  And 06-learn/post-mortems/README.md explains how to copy and file post-mortems
  And 04-your-agents/README.md links task 04
  And PROJECT-PLAN row 04 points to this task file with status done
  And validate_md.py --all reports 0 failures
```
