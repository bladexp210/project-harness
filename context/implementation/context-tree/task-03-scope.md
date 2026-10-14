---
title: Task 03 — context tree scope
layer: 3-implementation
feature: context-tree
status: reference
tags: [context, task-03, harness]
---

# Implementation — populating the context tree (task 03)

Narrow context for [Task 03](../../../04-your-agents/tasks/03-populate-context-tree.md).
Layer 2 arch files describe domains; this file lists exactly what task 03
creates and how to verify it.

## Deliverables checklist

| # | Path | Purpose |
| :-- | :---- | :---- |
| 1 | `context/README.md` | Layer map + wiring instructions |
| 2 | `context/architecture/data/harness-artifacts.md` | Data-layer harness-meta |
| 3 | `context/architecture/application/validation-and-loader.md` | Application-layer tooling |
| 4 | `context/architecture/communication/handoff-and-git.md` | Communication / workflow |
| 5 | `context/architecture/ux/book-structure.md` | UX / chapter journey |
| 6 | `context/implementation/context-tree/task-03-scope.md` | This file |
| 7 | `04-your-agents/tasks/03-populate-context-tree.md` | ICOM task spec |
| 8 | `04-your-agents/README.md` | Harness example row + context link |

## PROJECT-PLAN linkage

Row 03 in [PROJECT-PLAN](../../../03-plan/PROJECT-PLAN.md) points to the task file.
Depends on task 02 (Track A proof). Unblocks task 04 (Ch. 06 learn loop, S23).

## Verification commands

```powershell
python scripts/validate_md.py --all
python scripts/test_context_loader.py
python scripts/test_task_context.py
python scripts/task_context.py 04-your-agents/tasks/03-populate-context-tree.md
```

## context_load for this task

Task 03 loads system orientation plus all four architecture domains:

- `context/system/overview.md`
- `context/system/book-architecture.md`
- `context/architecture/data/harness-artifacts.md`
- `context/architecture/application/validation-and-loader.md`
- `context/architecture/communication/handoff-and-git.md`
- `context/architecture/ux/book-structure.md`

Layer 3 (`this file`) is referenced in Inputs for humans; optional in
`context_load` when the task is documenting itself.

## Out of scope (S22 defer)

- Golden-task expansion
- Evaluator changes
- Live Track A/B execution of task 03
- Langfuse wiring (T8)
