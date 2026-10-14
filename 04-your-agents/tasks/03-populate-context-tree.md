---
title: "Task 03: Populate context example tree"
task: 03
chapter: 04
status: done
agent: dev
tags: [task, agents, context]
context_load:
  - context/system/overview.md
  - context/system/book-architecture.md
  - context/architecture/data/harness-artifacts.md
  - context/architecture/application/validation-and-loader.md
  - context/architecture/communication/handoff-and-git.md
  - context/architecture/ux/book-structure.md
---

# Task 03 — Populate `context/` example tree

Document the three-layer context model for this harness repo: **harness-meta**
distillations in `context/architecture/` (four Ch. 02 domains) plus
`context/implementation/` for task-narrow scope. Document-only in S22 — no
Track A/B execution run.

## Inputs

- [[overview]] — three-layer context principle
- [[book-architecture]] — Ch. 04 reader job (populate `context/`)
- [[context-loader]] — strip rules and `task_context.py` wiring
- Layer 2 arch files under `context/architecture/` (created by this task)
- [[implementation/context-tree/task-03-scope]] — deliverables checklist

## Controls

*Inherited — do not rewrite.* Governed by [[global|constraints]] and the
acceptance criteria below.

**Scope — modify:**

- `context/README.md`
- `context/architecture/**/*.md`
- `context/implementation/**/*.md`
- `04-your-agents/README.md` (context section + harness task table)
- `03-plan/PROJECT-PLAN.md` (row 03 file column and status only)

**Scope — read-only:** `04-your-agents/tasks/03-populate-context-tree.md`,
`04-your-agents/agents/dev-agent.yaml`, `context/system/overview.md`,
`scripts/context_loader.py`, `scripts/test_context_loader.py`

## Mechanisms

Run by the **dev agent** ([[dev-agent]]). Context via
`python scripts/task_context.py` per [[context-loader]].

| Track | Guide | S22 choice |
| :---- | :---- | :---- |
| **A** (ideal) | [[openhands]] | **Not run** — document-only session |
| **B** (fallback) | [[track-b-checklist]] | **Not run** — canon authored directly |

## Outputs

- Rich harness-meta context tree (4 architecture domains + 1 implementation feature)
- `context/README.md` orientation with layer map and wiring steps
- Task 03 row in PROJECT-PLAN marked `done` with file path
- Ch. 04 README updated with task 03 in harness example table

## Acceptance criteria

```gherkin
Scenario: Context example tree is documented
  Given task 02 is done and Ch. 04 Harness Gap lists context/ unfilled
  When task 03 scope is applied on branch session-22/ch04-context-tree
  Then context/README.md describes all three layers
  And context/architecture/ contains data, application, communication, and ux domains
  And context/implementation/context-tree/task-03-scope.md exists
  And 04-your-agents/README.md links the context tree
  And PROJECT-PLAN row 03 points to this task file with status done
  And validate_md.py --all reports 0 failures
  And test_context_loader.py and test_task_context.py pass
```
