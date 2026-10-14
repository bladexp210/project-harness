---
title: "L4 Task 04: Draft next bootstrap"
status: experiment
level: L4
task: 04
task_id: t_04_draft_bootstrap
parent: wf_session_close
tags: [playground, l4, session, close]
---

# L4 — Draft next bootstrap

| Field | Value |
| :---- | :---- |
| **Task ID** | `t_04_draft_bootstrap` |
| **Task name** | Draft next bootstrap |
| **Parent** | `wf_session_close` (L3 · [[L3-wf-session-close]]) |
| **Executor** | `exe_agent_cursor` · `agent:cursor` |
| **Supervisor** | `human:Alex` |

**Maps to:** [[session-workflow]] close checklist **D. Next-session bootstrap**
+ merge PS blocks for task 06.

---

## Input

| Artifact | Form | Where | From |
| :------- | :--- | :---- | :--- |
| Go signal from dashboard draft | signal | task handoff | `exe_agent_cursor` ← [[03-draft-dashboard]] |
| Draft `STATE.md` (threads, defer list) | file | repo root | `exe_agent_cursor` |
| Session branch name | git ref | chat · `STATE.md` | `human:Alex` |
| Final validate evidence | shell | chat | `exe_agent_cursor` ← [[01-final-validate]] |

## Output

| Artifact | Form | Where | To |
| :------- | :--- | :---- | :--- |
| `## Next session bootstrap` block | file | `STATE.md` | `human:Alex` |
| PS `git checkout main` line | shell | chat | `human:Alex` |
| PS `git merge session-NN/topic` line | shell | chat | `human:Alex` |
| PS `git branch -d session-NN/topic` line | shell | chat | `human:Alex` |
| Optional `git push` line | shell | chat | `human:Alex` |
| Close pack summary | signal | chat | `human:Alex` → [[05-human-review-close]] |

## Tools

| Tool | Used for |
| :--- | :------- |
| `git` | Read-only `branch` / `status` for block accuracy |

## Control

| Type | Reference |
| :--- | :-------- |
| Policy | [[session-workflow]] D — bootstrap overwrites each close |
| Policy | D-001 — PS blocks for human; agent does not merge |
| Policy | No force-push to `main` unless explicit |
| Gherkin | see below |

```gherkin
Scenario: Agent drafts bootstrap and merge blocks
  Given tasks 02 and 03 drafts exist
  When the agent writes Next session bootstrap in STATE
  And posts PowerShell merge blocks in chat
  Then bootstrap names session-(N+1) branch and primary thread
  And merge blocks reference the correct session branch
```

## Measures

| KPI | Target | Source |
| :-- | :----- | :----- |
| Bootstrap fields present | Branch, Primary, Load, Defer, Gate | `STATE.md` |
| Merge block count | ≥3 lines (checkout, merge, branch -d) | chat |

## Done when

`STATE.md` contains a complete bootstrap block and chat has merge PS blocks.
Task 05 stays closed until done.
