---
title: "Task NN: [short imperative title]"
task: NN
chapter: 03
status: todo
agent: builder
tags: [task, icom]
context_load:
  - context/architecture/data/your-data-layer.md
---

# Task NN — [short imperative title]

> [!TEACH] Teach
> One sentence: what this task makes real, and why it is the smallest revertible
> change that does so. Keep this file under the 100-line budget in
> [constraints](../03-plan/constraints/global.md) — if it won't fit, decompose the task.

## Inputs (ICOM+)

Layer-3 context list — **artifact · form · where · from executor.** An agent loads exactly these and nothing else. Mirror paths in frontmatter `context_load:`.

| Artifact | Form | Where | From |
|:---|:---|:---|:---|
| [[02-design/layers/...\|layer design section]] | file | `02-design/layers/data.md` | prior session |
| [context-file-name] | [file\|DB entry\|shell\|git object] | [path\|DB name\|ref] | [executor name] |

## Controls (ICOM+)

**Inherited:** [constraints](../03-plan/constraints/global.md) (repo, scope, AI-execution, budgets) + [constraints/project](../03-plan/constraints/project.md).

**Scope — modify** (agent touches only these):

- [file-or-directory-path]
- [...]

**Scope — read-only** (agent may read, must not edit):

- [file-or-directory-path]
- [...]

**Preconditions** *(required when this task is an irreversible gate — merge, deploy, schema migration, or Supervisor is `human` for an irreversible action; optional otherwise)*:

| Precondition | Check | If unmet |
| :----------- | :---- | :------- |
| [e.g. acceptance criteria drafted] | [how to verify] | [block / escalate / human gate] |

## Mechanisms (ICOM+)

**Executor:** [agent type: `builder` (default) \| other specialist \| `human`]

**Supervisor:** [who accepts output — `human` for irreversible gates; default: project owner]

**Tool:** [external execution tool only — e.g. OpenHands, IDE; repo scripts are inputs/canon per [icom-plus-convention](../_playground/icom-plus-convention.md)]

**Postconditions** *(required for irreversible-gate tasks — same triggers as Preconditions above; optional otherwise)*:

| Postcondition | Evidence | Owner |
| :------------ | :------- | :---- |
| [e.g. each Gherkin Then quoted in commit] | [path, trace, log] | Supervisor |

*If non-default Executor, Supervisor, or Tool, state why.*

> [!WARNING] Unstructured orchestration
> Do not describe ad-hoc multi-agent chains in prose. If work spans agents,
> split into tasks with explicit Outputs → Inputs handoff. One Executor per
> task sitting ([icom-plus-convention](../_playground/icom-plus-convention.md) v0.4).

## Outputs (ICOM+)

Artifacts this task must produce — **artifact · form · where · to executor.**

| Artifact | Form | Where | To |
|:---|:---|:---|:---|
| [output-name] | [file\|DB entry\|commit\|signal] | [path\|table\|branch\|channel] | [next executor] |
| [another] | | | |

## Acceptance criteria (Gherkin)

Written before work starts. Task specification *is* test suite: agent quotes each `Then` clause as evidence in commit or post-mortem ([ADR-002](../02-design/decisions/ADR-002-modeling-conventions.md)). Missing quote blocks closure.

```gherkin
Scenario: [what completion looks like]
  Given [the inputs above are present]
  When [the transformation this task describes runs]
  Then [observable, checkable outcome]
  And [another — each Then is one test]
```
