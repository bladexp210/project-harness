---
title: "L4 Task 01: Validate batch"
status: experiment
level: L4
task: 01
task_id: t_01_validate_batch
parent: wf_commit_process
tags: [playground, l4, commit, reference-box]
---

# L4 — Validate batch

> [!NOTE] Reference box
> First L4 task shaped by decisions 1–5 (2026-06-15): two stacks, Executor at L4,
> `m_*`/`comp_*` prefixes, Supervisor, Container alias in prose.

| Field | Value |
| :---- | :---- |
| **Task ID** | `t_01_validate_batch` |
| **Task name** | Validate batch |
| **Parent** | `wf_commit_process` (L3 · [L3-commit-process](L3-commit-process.md)) |
| **Executor** | `exe_agent_cursor` · `agent:cursor` |
| **Supervisor** | `human:Alex` (accepts evidence; can halt batch) |

**Process stack:** Task (L4 behaviour) inside workflow `wf_commit_process`.  
**C4 link:** runs against harness **module** `m_scripts` (C4 Container) — diagram
label stays **Container**.

---

## Input

Handoffs **from executors only** (another workflow may supply the executor).

| Artifact | Form | Where | From |
| :------- | :--- | :---- | :--- |
| Batch file path list (staged + unstaged) | file list | session branch worktree | `exe_agent_cursor` |
| Validator entrypoint | file | `scripts/validate_md.py` | `exe_agent_cursor` (canon) |
| Unit test entrypoints (if area touched) | file | `scripts/test_*.py` | `exe_agent_cursor` (canon) |

---

## Output

Handoffs **to executors only**; next task or supervisor.

| Artifact | Form | Where | To |
| :------- | :--- | :---- | :--- |
| Validator summary (`N checked, 0 failed`) | shell | chat transcript | `human:Alex` |
| Unit test summary (`all passed` or failures) | shell | chat transcript | `human:Alex` |
| FAIL / WARN lines with paths | shell | chat transcript | `exe_agent_cursor` (fix loop) |
| Go / no-go for commit batch | signal | task handoff | `exe_agent_cursor` → [02-draft-commit-blocks](02-draft-commit-blocks.md) |

---

## Tools

External only — not developed in this repo.

| Tool | Used for |
| :--- | :------- |
| `python` (runtime) | Run validator and tests |
| `shell` (terminal) | Capture exit code and stdout |

Harness scripts (`validate_md.py`, `test_*.py`) are **inputs / canon**, not tools.

---

## Control

| Type | Reference |
| :--- | :-------- |
| Policy | [global](../../../03-plan/constraints/global.md) — WARN grace band; 0 failures before task 02 |
| Gherkin | see below |

```gherkin
Scenario: Batch validation passes
  Given the agent has a list of paths changed this batch
  When validate_md.py --all runs with exit code 0
  And relevant test_*.py suites pass when their area was touched
  Then the chat shows 0 validator failures
  And the agent may open task 02 draft commit blocks
```

---

## Measures

| KPI | Target | Source |
| :-- | :----- | :----- |
| Validator failures | `0` | `validate_md.py` stdout |
| Validator exit code | `0` | shell |
| Unit test failures | `0` (when run) | `pytest` / test script stdout |
| Wall time | record optional | session chat timestamp |

---

## Done when

Supervisor sees **0 failures** in validator output (WARN acceptable per
[global](../../../03-plan/constraints/global.md)). On failure, executor loops here — task 02 stays closed.
