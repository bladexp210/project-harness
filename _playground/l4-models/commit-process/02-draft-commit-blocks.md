---
title: "L4 Task 02: Draft commit blocks"
status: experiment
level: L4
task: 02
task_id: t_02_draft_commit_blocks
parent: wf_commit_process
tags: [playground, l4, commit]
---

# L4 — Draft commit blocks

| Field | Value |
| :---- | :---- |
| **Task ID** | `t_02_draft_commit_blocks` |
| **Task name** | Draft commit blocks |
| **Parent** | `wf_commit_process` (L3 · [L3-commit-process](L3-commit-process.md)) |
| **Executor** | `exe_agent_cursor` · `agent:cursor` |
| **Supervisor** | `human:Alex` (accepts blocks before review) |

**Process stack:** Task (L4 behaviour) inside workflow `wf_commit_process`.  
**C4 link:** reads **module** `m_book_repo` worktree (C4 Container).

---

## Input

Handoffs **from executors only**.

| Artifact | Form | Where | From |
| :------- | :--- | :---- | :--- |
| Go signal from validation | signal | task handoff | `exe_agent_cursor` ← [01-validate-batch](01-validate-batch.md) |
| `git status -sb` output | shell | terminal stdout | `exe_agent_cursor` (read-only) |
| `git diff` output | shell | terminal stdout | `exe_agent_cursor` (read-only) |
| Recent commit subjects | shell | `git log` stdout | `exe_agent_cursor` (read-only) |
| Files grouped by logical change | file list | agent working memory | `exe_agent_cursor` |

---

## Output

Handoffs **to executors only**.

| Artifact | Form | Where | To |
| :------- | :--- | :---- | :--- |
| PS `git add <paths>` lines | shell | chat transcript | `human:Alex` |
| PS `git commit -m "type(scope): subject" -m "Body."` | shell | chat transcript | `human:Alex` |
| One block per atomic commit | shell | chat transcript | `human:Alex` |
| Batch summary (what + why per commit) | signal | chat transcript | `human:Alex` → [03-human-review-diff](03-human-review-diff.md) |

---

## Tools

External only — not developed in this repo.

| Tool | Used for |
| :--- | :------- |
| `git` | Read-only `status`, `diff`, `log` |
| `powershell` | Block syntax for human copy-paste (D-001) |

Conventional Commits types (`feat`, `fix`, `docs`, `chore`, …) are **control**,
not tools.

---

## Control

| Type | Reference |
| :--- | :-------- |
| Policy | [session-workflow](../../../context/system/session-workflow.md) — one logical batch; atomic commits |
| Policy | D-001 — agent does **not** run `git commit` unless Alex asks |
| Gherkin | see below |

```gherkin
Scenario: Agent drafts commit blocks
  Given task 01 go signal exists
  When the agent runs read-only git commands
  Then chat contains PS add/commit blocks for each atomic commit
  And each block has a Conventional Commit message
  And the agent has not run git commit
```

---

## Measures

| KPI | Target | Source |
| :-- | :----- | :----- |
| Commits drafted | ≥1 per logical change | chat block count |
| `git write` commands run by agent | `0` | chat / terminal |
| Files per commit | single logical scope | human review in task 03 |

---

## Done when

Supervisor has PS blocks for every commit in this batch. Executor must not run
`git commit` unless Alex explicitly requests it in chat.
