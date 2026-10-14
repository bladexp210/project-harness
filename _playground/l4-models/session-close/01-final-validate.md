---
title: "L4 Task 01: Final validate"
status: experiment
level: L4
task: 01
task_id: t_01_final_validate
parent: wf_session_close
tags: [playground, l4, session, close]
---

# L4 — Final validate

| Field | Value |
| :---- | :---- |
| **Task ID** | `t_01_final_validate` |
| **Task name** | Final validate |
| **Parent** | `wf_session_close` (L3 · [L3-wf-session-close](L3-wf-session-close.md)) |
| **Executor** | `exe_agent_cursor` · `agent:cursor` |
| **Supervisor** | `human:Alex` |

**Maps to:** [session-workflow](../../../context/system/session-workflow.md) close checklist **A. Verify**.

---

## Input

| Artifact | Form | Where | From |
| :------- | :--- | :---- | :--- |
| Full repo tree on session branch | file list | worktree | `exe_agent_cursor` |
| Validator entrypoint | file | `scripts/validate_md.py` | `exe_agent_cursor` (canon) |

## Output

| Artifact | Form | Where | To |
| :------- | :--- | :---- | :--- |
| `validate_md: N checked, 0 failed` | shell | chat | `human:Alex` |
| Unit test pass logs | shell | chat | `human:Alex` |
| Go / no-go for close draft | signal | task handoff | `exe_agent_cursor` → [02-draft-state](02-draft-state.md) |

## Tools

| Tool | Used for |
| :--- | :------- |
| `python` | `validate_md.py --all`, `test_*.py` |
| `shell` | Exit codes |

## Control

| Type | Reference |
| :--- | :-------- |
| Policy | [session-workflow](../../../context/system/session-workflow.md) A — 0 failures before close draft |

## Measures

| KPI | Target | Source |
| :-- | :----- | :----- |
| Validator failures | `0` | stdout |
| Relevant test failures | `0` | test stdout |

## Done when

Supervisor sees 0 failures. Close draft tasks stay closed on failure.
