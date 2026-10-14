---
title: Session close models
status: experiment
updated_at: 2026-06-15T17:00:00
tags: [playground, session, close]
---

# Session close — `proc_session_close`

> [!NOTE] Playground — not canon
> Precondition: [[../commit-process/L3-commit-process|wf_commit_process]] complete.

## Stack slice

```mermaid
flowchart TB
    classDef roleManager fill:#5b2d8e,stroke:#3b0764,color:#fff
    L1["app_book_harness"]
    L2b["proc_session_build"]
    L2c["proc_session_close"]:::roleManager
    L3["wf_session_close"]
    L1 --> L2b
    L1 --> L2c
    L2c --> L3
    style L3 fill:#ecfdf5,stroke:#0d6e6e
```

| Level | ID | File |
| :---- | :--- | :--- |
| L1 | `app_book_harness` | [[../commit-process/L1-cap-session-governance|L1]] |
| L2 | `proc_session_close` | [[L2-proc-session-close]] |
| L3 | `wf_session_close` | [[L3-wf-session-close]] |
| L4 | `t_01` … `t_06` | `01`–`06` below |

**Canon procedure:** [[session-workflow]] close checklist A–E.

## L4 tasks

| # | File | Checklist |
| :-: | :--- | :-------- |
| 01 | [[01-final-validate]] | A Verify |
| 02 | [[02-draft-state]] | B STATE |
| 03 | [[03-draft-dashboard]] | C Dashboard |
| 04 | [[04-draft-bootstrap]] | D Bootstrap + merge PS |
| 05 | [[05-human-review-close]] | Human gate |
| 06 | [[06-human-merge-main]] | E Git (irreversible) |

## Session lifecycle

```mermaid
flowchart LR
    classDef roleExecAgent fill:#b45309,stroke:#92400e,color:#fff
    classDef roleSupGate fill:#9f1239,stroke:#881337,color:#fff,stroke-width:2px
    boot[Bootstrap] --> build[proc_session_build]
    build -->|wf_commit_process x N| close[proc_session_close]
    close -->|wf_session_close| main[main merged]
```

**Diagram:** full colored L4 chain in [[context/system/icom-plus-examples-trackb#Example G — L3/L4 REAL Track B (`wf_session_close`)|ICOM+ Example G]].

## Pending

- [ ] Auditing as `t_*` task (optional)
