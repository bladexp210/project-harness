---
title: "L4 Task 04: Human git commit"
status: experiment
level: L4
task: 04
task_id: t_04_human_git_commit
parent: wf_commit_process
tags: [playground, l4, commit]
---

# L4 — Human git commit

| Field | Value |
| :---- | :---- |
| **Task ID** | `t_04_human_git_commit` |
| **Task name** | Git commit |
| **Parent** | `wf_commit_process` (L3 · [[L3-commit-process]]) |
| **Executor** | `exe_human_alex` · `human:Alex` |
| **Supervisor** | `human:Alex` (**irreversible gate** — human only) |

**Process stack:** Task (L4 behaviour) inside workflow `wf_commit_process`.  
**C4 link:** writes to **module** `m_book_repo` git store (C4 Container).

---

## Input

Handoffs **from executors only**.

| Artifact | Form | Where | From |
| :------- | :--- | :---- | :--- |
| Explicit approval | signal | chat | `exe_human_alex` ← [[03-human-review-diff]] |
| PS `git add` / `git commit` blocks | shell | chat transcript | `exe_agent_cursor` ← [[02-draft-commit-blocks]] |
| Staging intent (only listed paths) | signal | local judgment | `exe_human_alex` |

---

## Output

Handoffs **to executors only**.

| Artifact | Form | Where | To |
| :------- | :--- | :---- | :--- |
| New commit SHA | git object | `session-NN/topic` ref | `exe_human_alex` (local repo) |
| Clean status for staged batch | shell | `git status` stdout | `exe_human_alex` |
| Pre-commit hook pass log | shell | terminal | `exe_human_alex` |
| Hook failure + auto-fixed files | shell + file | terminal · worktree | `exe_agent_cursor` → [[01-validate-batch]] |
| Confirmation in chat | signal | chat transcript | `exe_agent_cursor` (session continuity) |

---

## Tools

External only — not developed in this repo.

| Tool | Used for |
| :--- | :------- |
| `git` | `add`, `commit`, `log`, `status` |
| `powershell` | Host shell on Windows (D-001) |
| pre-commit | gitleaks, validate-md hooks |

---

## Control

| Type | Reference |
| :--- | :-------- |
| Policy | D-001 (git on Windows host); [[global]] — no `--no-verify` unless explicit |
| Policy | User commit rules — **new** commit on hook fix, no amend unless allowed |
| Gherkin | see below |

```gherkin
Scenario: Human commits one logical batch
  Given task 03 approval exists in chat
  And PS git blocks list only intended paths
  When Alex runs git add and git commit on the Windows host
  Then pre-commit hooks pass
  And git log -1 shows a Conventional Commit message
  And Alex confirms in chat
```

---

## Measures

| KPI | Target | Source |
| :-- | :----- | :----- |
| Pre-commit hook result | pass | terminal exit code |
| Commit message format | Conventional Commits | `git log -1` |
| Unexpected staged paths | `0` | `git diff --cached --name-only` |
| Commits in batch | matches task 02 plan | `git log` count |

---

## Done when

Supervisor confirms: `git log -1` matches intent, hooks green, chat confirmation
posted. **Merge to `main`** is [[../session-close/L3-wf-session-close|wf_session_close]] —
separate workflow at session close.
