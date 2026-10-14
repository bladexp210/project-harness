---
title: "L4 Task 03: Human review diff"
status: experiment
level: L4
task: 03
task_id: t_03_human_review_diff
parent: wf_commit_process
tags: [playground, l4, commit]
---

# L4 — Human review diff

| Field | Value |
| :---- | :---- |
| **Task ID** | `t_03_human_review_diff` |
| **Task name** | Review diff |
| **Parent** | `wf_commit_process` (L3 · [L3-commit-process](L3-commit-process.md)) |
| **Executor** | `exe_human_alex` · `human:Alex` |
| **Supervisor** | `human:Alex` (accept/reject gate before irreversible commit) |

**Process stack:** Task (L4 behaviour) inside workflow `wf_commit_process`.  
**C4 link:** reviews diff in **module** `m_book_repo` worktree (C4 Container).

---

## Input

Handoffs **from executors only**.

| Artifact | Form | Where | From |
| :------- | :--- | :---- | :--- |
| PS commit blocks + batch summary | shell | chat transcript | `exe_agent_cursor` ← [02-draft-commit-blocks](02-draft-commit-blocks.md) |
| Working tree diff | file | IDE / `git diff` | `exe_human_alex` |
| Validator pass evidence | shell | chat transcript | `exe_agent_cursor` ← [01-validate-batch](01-validate-batch.md) |
| Scope + atomic-commit rules | file | [global](../../../03-plan/constraints/global.md) | `exe_human_alex` (inherited) |

---

## Output

Handoffs **to executors only**.

| Artifact | Form | Where | To |
| :------- | :--- | :---- | :--- |
| **Approve** — OK to commit | signal | chat | `exe_human_alex` → [04-human-git-commit](04-human-git-commit.md) |
| **Reject** — line-level feedback | signal | chat | `exe_agent_cursor` → [01-validate-batch](01-validate-batch.md) |
| **Split** — smaller commits requested | signal | chat | `exe_agent_cursor` → [02-draft-commit-blocks](02-draft-commit-blocks.md) |

---

## Tools

External only — not developed in this repo.

| Tool | Used for |
| :--- | :------- |
| `git` | Read-only diff, status |
| Cursor / Obsidian | Diff UI on Windows |

---

## Control

| Type | Reference |
| :--- | :-------- |
| Policy | [global](../../../03-plan/constraints/global.md) — no secrets, scope, atomic commits; no agent `git commit` |
| Policy | D-001 — human owns protected git path |
| Gherkin | see below |

```gherkin
Scenario: Human approves batch for commit
  Given PS commit blocks and validator evidence are in chat
  When Alex reviews the diff against the claimed scope
  Then Alex explicitly approves or rejects in chat
  And no git commit runs without approval
```

---

## Measures

| KPI | Target | Source |
| :-- | :----- | :----- |
| Explicit decision | approve or reject stated | chat |
| Secrets in diff | none found | human review |
| Unrelated paths in batch | none | diff vs summary |
| Teaching bloat in agent paths | within scope | human judgment |

---

## Done when

Supervisor posts explicit approve, reject, or split request. Task 04 stays
closed until **Approve**.
