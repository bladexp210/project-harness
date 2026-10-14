---
title: "L4 Task 02: Draft STATE close"
status: experiment
level: L4
task: 02
task_id: t_02_draft_state
parent: wf_session_close
tags: [playground, l4, session, close]
---

# L4 — Draft STATE close

| Field | Value |
| :---- | :---- |
| **Task ID** | `t_02_draft_state` |
| **Task name** | Draft STATE close |
| **Parent** | `wf_session_close` (L3 · [L3-wf-session-close](L3-wf-session-close.md)) |
| **Executor** | `exe_agent_cursor` · `agent:cursor` |
| **Supervisor** | `human:Alex` |

**Maps to:** [session-workflow](../../../context/system/session-workflow.md) close checklist **B. STATE.md**.

**C4 link:** writes **module** `m_book_repo` file `STATE.md` (uncommitted until merge).

---

## Input

| Artifact | Form | Where | From |
| :------- | :--- | :---- | :--- |
| Go signal from final validate | signal | task handoff | `exe_agent_cursor` ← [01-final-validate](01-final-validate.md) |
| Current `STATE.md` on session branch | file | repo root | `exe_agent_cursor` |
| Session outcome (shipped, branch, threads) | signal | chat | `human:Alex` |

## Output

| Artifact | Form | Where | To |
| :------- | :--- | :---- | :--- |
| **Closed** paragraph in Current position | file | `STATE.md` | `human:Alex` |
| Updated **Open threads** table | file | `STATE.md` | `human:Alex` |
| Updated **Last 3 decisions** | file | `STATE.md` | `human:Alex` |
| **Current branch** → `main` (post-merge intent) | file | `STATE.md` | `human:Alex` |
| Trimmed Current position (≤~15 lines) | file | `STATE.md` | `human:Alex` |
| Archive pointer if prose moved | signal | chat | `human:Alex` → [session-docs](../../../context/system/session-docs.md) |
| Go for dashboard draft | signal | task handoff | `exe_agent_cursor` → [03-draft-dashboard](03-draft-dashboard.md) |

## Tools

| Tool | Used for |
| :--- | :------- |
| Cursor | Edit markdown in worktree |

Harness `STATE.md` is **canon / input**, not a Tool.

## Control

| Type | Reference |
| :--- | :-------- |
| Policy | [session-workflow](../../../context/system/session-workflow.md) B — boot line → closed paragraph |
| Policy | D-004 — STATE must be accurate for next session |
| Gherkin | see below |

```gherkin
Scenario: Agent drafts STATE close
  Given task 01 go signal and session outcome in chat
  When the agent updates STATE.md on the session branch
  Then the boot line is replaced with a closed session paragraph
  And open threads and last 3 decisions reflect reality
  And current branch names main after merge intent
```

## Measures

| KPI | Target | Source |
| :-- | :----- | :----- |
| Boot line remaining | `0` | `STATE.md` |
| Open thread rows | accurate vs chat | human spot-check in task 05 |
| Current position lines | ≤15 | `STATE.md` |

## Done when

Supervisor can diff `STATE.md` in task 05. Task 03 stays closed until this
task completes.
