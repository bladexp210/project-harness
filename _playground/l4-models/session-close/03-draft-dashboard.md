---
title: "L4 Task 03: Draft dashboard"
status: experiment
level: L4
task: 03
task_id: t_03_draft_dashboard
parent: wf_session_close
tags: [playground, l4, session, close]
---

# L4 — Draft dashboard

| Field | Value |
| :---- | :---- |
| **Task ID** | `t_03_draft_dashboard` |
| **Task name** | Draft dashboard |
| **Parent** | `wf_session_close` (L3 · [[L3-wf-session-close]]) |
| **Executor** | `exe_agent_cursor` · `agent:cursor` |
| **Supervisor** | `human:Alex` |

**Maps to:** [[session-workflow]] close checklist **C. Dashboard**.

**C4 link:** writes **module** `m_book_repo` paths under `_index/dashboard/`.

---

## Input

| Artifact | Form | Where | From |
| :------- | :--- | :---- | :--- |
| Go signal from STATE draft | signal | task handoff | `exe_agent_cursor` ← [[02-draft-state]] |
| Draft `STATE.md` (threads, session #) | file | repo root | `exe_agent_cursor` |
| Current dashboard L1–L3 | file | `_index/dashboard/` | `exe_agent_cursor` (canon) |
| Validator count from task 01 | shell | chat | `exe_agent_cursor` ← [[01-final-validate]] |

## Output

| Artifact | Form | Where | To |
| :------- | :--- | :---- | :--- |
| Updated `01-context.md` | file | `_index/dashboard/` | `human:Alex` |
| Updated `02-containers.md` | file | `_index/dashboard/` | `human:Alex` |
| Updated `03-components.md` | file | `_index/dashboard/` | `human:Alex` |
| History row per file (same timestamp) | file | each dashboard History table | `human:Alex` |
| Go for bootstrap draft | signal | task handoff | `exe_agent_cursor` → [[04-draft-bootstrap]] |

## Tools

| Tool | Used for |
| :--- | :------- |
| Cursor | Edit markdown |

## Control

| Type | Reference |
| :--- | :-------- |
| Policy | [[session-workflow]] C — all three zoom files in one pass |
| Policy | History max 10 rows; archive older to `dashboard-history-archive.md` |
| Gherkin | see below |

```gherkin
Scenario: Agent drafts dashboard close
  Given task 02 completed and STATE draft exists
  When the agent updates dashboard L1 L2 and L3
  Then all three files share the same updated timestamp
  And each History table has a new row
```

## Measures

| KPI | Target | Source |
| :-- | :----- | :----- |
| Dashboard files touched | `3` | git diff |
| Shared `updated` date | one value across L1–L3 | frontmatter |
| History rows added | `3` | file diff |

## Done when

All three dashboard zoom files updated in one pass. Task 04 stays closed until
done.
