---
title: "L1: Session governance (book repo)"
status: experiment
level: L1
capability_id: app_book_harness
tags: [playground, l1, session, capability]
---

# L1 — Session governance (book repo)

**Question:** How does the harness book repo stay coherent across agent sessions?

**Track B** — meta-repo operations, not the reader's product.

**Capability ID:** `app_book_harness` · **C4 link:** **app** at System Context
(actors: `human:Alex`, `agent:cursor`; system: book-as-folder-structure).

---

## Capability box

| Field | Value |
| :---- | :---- |
| **Capability ID** | `app_book_harness` |
| **Capability name** | Govern book-repo sessions |
| **Owner** | `human:Alex` |
| **Level** | L1 (process stack) |

### Input

| Artifact | Form | Where | From |
| :------- | :--- | :---- | :--- |
| Reader / author product intent | signal | chat · plan docs | `human:Alex` |
| Chapter spine + ADR discipline | file | `00`–`08` paths | `app_book_harness` (canon) |
| Agent team + constraints | file | `04-your-agents/`, `constraints/` | `app_book_harness` (canon) |

### Output

| Artifact | Form | Where | To |
| :------- | :--- | :---- | :--- |
| Durable repo state on `main` | git ref | remote | `human:Alex` |
| STATE + dashboard handoff | file | `STATE.md`, `_index/dashboard/` | `human:Alex` · `exe_agent_cursor` |
| Closed session record | file | `context/system/sessions/` | `human:Alex` |

### Tools

| Tool | Used for |
| :--- | :------- |
| `git` | Branching, merge, history |
| Obsidian | Vault navigation |
| Cursor | Agent execution surface |

---

## Child processes

| Process ID | Name | File |
| :--------- | :--- | :--- |
| `proc_session_build` | Run one session build | [L2-proc-session-build](L2-proc-session-build.md) |
| `proc_session_close` | Close session · merge `main` | [L2 close](../session-close/L2-proc-session-close.md) |
