---
title: "Harness example: document-only task spec"
chapter: 06
status: reference
tags: [boilerplate, task, harness-meta]
---

# Harness task spec — document-only pattern

Worked **harness-meta** example: a task that closes with canon edits and
validator evidence — no Track A/B run. Derived from
`04-your-agents/tasks/03-populate-context-tree.md`.

## When to use

- Spine or canon sessions that ship docs, not product code
- Smallest revertible change that clears a Harness or Canon Gap
- Acceptance criteria verifiable with `validate_md.py --all` and targeted tests

## Skeleton (copy and fill)

```markdown
---
title: "Task NN: [imperative title]"
task: NN
chapter: 04
status: todo
agent: dev
tags: [task]
context_load:
  - context/system/overview.md
  - [layer-2 or layer-3 files — explicit list only]
---

# Task NN — [title]

One sentence: smallest change that closes the gap.

## Inputs

- [[wiki-link-to-artifact]]

## Controls

*Inherited — do not rewrite.* Governed by [[global|constraints]].

**Scope — modify:** [exact paths]

**Scope — read-only:** [exact paths]

## Mechanisms

| Track | Guide | This task |
| :---- | :---- | :---- |
| **A** | [[openhands]] | Run / **Not run** — reason |
| **B** | [[track-b-checklist]] | Run / **Not run** — reason |

## Outputs

- [artifact list]

## Acceptance criteria

\`\`\`gherkin
Scenario: [completion shape]
  Given [preconditions from PROJECT-PLAN or prior task]
  When [this task's scope is applied on branch session-NN/topic]
  Then [observable outcome]
  And validate_md.py --all reports 0 failures
\`\`\`
```

## Evidence table (closure)

| Then clause | Evidence location |
| :---- | :---- |
| Canon file exists | Path in repo |
| Validator clean | `validate_md.py --all` output |
| PROJECT-PLAN row | Status `done` + file link |

Quote each `Then` in the closing commit message or post-mortem per [ADR-002](../../../02-design/decisions/ADR-002-modeling-conventions.md).
