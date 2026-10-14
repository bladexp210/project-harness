---
title: ICOM+ Irreversible-Gate Tasks (Hoare)
layer: 1-system
status: reference
version: "0.4"
updated: 2026-06-28 23:45
tags: [icom, hoare, gates]
---

# ICOM+ — irreversible-gate tasks (Hoare)

Load with [icom-plus-convention](icom-plus-convention.md) v0.4 when writing or reviewing tasks that
touch merge, deploy, schema migration, or other hard-to-undo outcomes.

## When Preconditions and Postconditions are required

A task is an **irreversible gate** when any of the following hold:

- **Supervisor** is `human` and the output action is hard to undo.
- **Controls** scope includes paths or operations marked irreversible in ADRs
  or [constraints/project](../../03-plan/constraints/project.md).
- Gherkin outcomes cannot be reverted with a single git command.

On irreversible-gate tasks, Controls **Preconditions** and Mechanisms
**Postconditions** tables in `tasks/*.md` are **required**. Routine
revertible tasks omit both; Gherkin alone suffices.

## Hoare ↔ Gherkin ↔ ICOM+

| Hoare | Gherkin | ICOM+ home |
| :---- | :------ | :--------- |
| Precondition | `Given` | Controls → Preconditions |
| Command | `When` | Mechanisms Executor |
| Postcondition | `Then` / `And` | Mechanisms → Postconditions |

Table shape: [new-task](../../_templates/new-task.md). Lineage: [ADR-002](../../02-design/decisions/ADR-002-modeling-conventions.md) Part 3.

## Orchestration (Dijkstra)

One **Executor** per L4 sitting. Split multi-agent work across tasks with
explicit Outputs → Inputs handoff — do not model opportunistic chains in one
task file ([new-task](../../_templates/new-task.md) anti-pattern callout).
