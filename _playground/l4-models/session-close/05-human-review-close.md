---
title: "L4 Task 05: Human review close"
status: experiment
level: L4
task: 05
task_id: t_05_human_review_close
parent: wf_session_close
tags: [playground, l4, session, close]
---

# L4 — Human review close

| Field | Value |
| :---- | :---- |
| **Task ID** | `t_05_human_review_close` |
| **Task name** | Review close pack |
| **Parent** | `wf_session_close` (L3 · [L3-wf-session-close](L3-wf-session-close.md)) |
| **Executor** | `exe_human_alex` · `human:Alex` |
| **Supervisor** | `human:Alex` (gate before irreversible merge) |

**Maps to:** Human gate before [session-workflow](../../../context/system/session-workflow.md) checklist **E. Git**.

**C4 link:** reviews **module** `m_book_repo` close artifacts (C4 Container).

---

## Input

| Artifact | Form | Where | From |
| :------- | :--- | :---- | :--- |
| Draft `STATE.md` | file | IDE diff | `exe_agent_cursor` ← [02-draft-state](02-draft-state.md) |
| Draft dashboard L1–L3 | file | IDE diff | `exe_agent_cursor` ← [03-draft-dashboard](03-draft-dashboard.md) |
| Bootstrap + merge PS blocks | shell | chat | `exe_agent_cursor` ← [04-draft-bootstrap](04-draft-bootstrap.md) |
| Final validate evidence | shell | chat | `exe_agent_cursor` ← [01-final-validate](01-final-validate.md) |
| Optional: human re-run `validate_md --all` | shell | terminal | `exe_human_alex` |

## Output

| Artifact | Form | Where | To |
| :------- | :--- | :---- | :--- |
| **Approve** — OK to merge | signal | chat | `exe_human_alex` → [06-human-merge-main](06-human-merge-main.md) |
| **Reject STATE** — fix threads/position | signal | chat | `exe_agent_cursor` → [02-draft-state](02-draft-state.md) |
| **Reject dashboard** — fix zoom files | signal | chat | `exe_agent_cursor` → [03-draft-dashboard](03-draft-dashboard.md) |
| **Reject bootstrap** — fix next-session block | signal | chat | `exe_agent_cursor` → [04-draft-bootstrap](04-draft-bootstrap.md) |

## Tools

| Tool | Used for |
| :--- | :------- |
| Cursor / Obsidian | Diff review |
| `git` | Read-only diff on session branch |
| `python` | Optional final validate re-run |

## Control

| Type | Reference |
| :--- | :-------- |
| Policy | [session-workflow](../../../context/system/session-workflow.md) — dashboard + STATE mandatory; canvas optional |
| Policy | D-004 — inaccurate STATE = disoriented next session |
| Gherkin | see below |

```gherkin
Scenario: Human approves close pack
  Given STATE dashboard and merge blocks are drafted
  When Alex reviews diffs against session outcome
  Then Alex explicitly approves or rejects with a target task
  And task 06 stays closed until Approve
```

## Measures

| KPI | Target | Source |
| :-- | :----- | :----- |
| Explicit decision | approve or reject stated | chat |
| STATE ↔ dashboard consistency | session # and threads match | human review |
| Merge branch name | matches session branch | chat vs git |

## Done when

Supervisor posts **Approve** or targeted **Reject**. Task 06 stays closed until
**Approve**.
