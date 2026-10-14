---
title: "L4 Task 06: Human merge main"
status: experiment
level: L4
task: 06
task_id: t_06_human_merge_main
parent: wf_session_close
tags: [playground, l4, session, close]
---

# L4 — Human merge main

| Field | Value |
| :---- | :---- |
| **Task ID** | `t_06_human_merge_main` |
| **Task name** | Merge to main |
| **Parent** | `wf_session_close` (L3 · [L3-wf-session-close](L3-wf-session-close.md)) |
| **Executor** | `exe_human_alex` · `human:Alex` |
| **Supervisor** | `human:Alex` (**irreversible gate**) |

**Maps to:** [session-workflow](../../../context/system/session-workflow.md) close checklist **E. Git**.

---

## Input

| Artifact | Form | Where | From |
| :------- | :--- | :---- | :--- |
| Approval from task 05 | signal | chat | `exe_human_alex` ← [05-human-review-close](05-human-review-close.md) |
| PS merge + branch-delete blocks | shell | chat | `exe_agent_cursor` ← [04-draft-bootstrap](04-draft-bootstrap.md) |
| Final validate evidence | shell | chat | `exe_agent_cursor` ← [01-final-validate](01-final-validate.md) |

## Output

| Artifact | Form | Where | To |
| :------- | :--- | :---- | :--- |
| `main` fast-forward or merge commit | git ref | local repo | `exe_human_alex` |
| Optional: remote `main` pushed | git ref | origin | `exe_human_alex` |
| Deleted `session-NN/topic` branch | git ref | — | `exe_human_alex` |
| Confirmation in chat | signal | chat | `exe_agent_cursor` |

## Tools

| Tool | Used for |
| :--- | :------- |
| `git` | `checkout main`, `merge`, `branch -d`, `push` |
| `powershell` | Windows host (D-001) |

## Control

| Type | Reference |
| :--- | :-------- |
| Policy | D-001 — human on Windows host; no force-push to `main` without explicit ask |
| Policy | Conventional Commits already on session branch |

```gherkin
Scenario: Session merges to main
  Given task 05 approval and final validate evidence exist
  When Alex merges session-NN/topic into main on Windows
  Then main contains the session commits
  And Alex confirms in chat
```

## Measures

| KPI | Target | Source |
| :-- | :----- | :----- |
| Merge result | success | `git merge` exit code |
| `main` validator | 0 failures | post-merge optional sweep |

## Done when

Supervisor confirms `main` has session work and chat confirmation posted.
Bootstrap for session N+1 is in `STATE.md` from [04-draft-bootstrap](04-draft-bootstrap.md).
