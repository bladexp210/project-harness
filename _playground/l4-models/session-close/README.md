---
title: Session close models
status: experiment
updated_at: 2026-06-15T17:00:00
tags: [playground, session, close]
---

# Session close — `proc_session_close`

> [!NOTE] Playground — not canon
> Precondition: [wf_commit_process](../commit-process/L3-commit-process.md) complete.

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
| L1 | `app_book_harness` | [L1](../commit-process/L1-cap-session-governance.md) |
| L2 | `proc_session_close` | [L2-proc-session-close](L2-proc-session-close.md) |
| L3 | `wf_session_close` | [L3-wf-session-close](L3-wf-session-close.md) |
| L4 | `t_01` … `t_06` | `01`–`06` below |

**Canon procedure:** [session-workflow](../../../context/system/session-workflow.md) close checklist A–E.

## L4 tasks

| # | File | Checklist |
| :-: | :--- | :-------- |
| 01 | [01-final-validate](01-final-validate.md) | A Verify |
| 02 | [02-draft-state](02-draft-state.md) | B STATE |
| 03 | [03-draft-dashboard](03-draft-dashboard.md) | C Dashboard |
| 04 | [04-draft-bootstrap](04-draft-bootstrap.md) | D Bootstrap + merge PS |
| 05 | [05-human-review-close](05-human-review-close.md) | Human gate |
| 06 | [06-human-merge-main](06-human-merge-main.md) | E Git (irreversible) |

## Session lifecycle

```mermaid
flowchart LR
    classDef roleExecAgent fill:#b45309,stroke:#92400e,color:#fff
    classDef roleSupGate fill:#9f1239,stroke:#881337,color:#fff,stroke-width:2px
    boot[Bootstrap] --> build[proc_session_build]
    build -->|wf_commit_process x N| close[proc_session_close]
    close -->|wf_session_close| main[main merged]
```

**Diagram:** full colored L4 chain in [ICOM+ Example G](../../../context/system/icom-plus-examples-trackb.md#example-g-l3l4-real-track-b-wf_session_close).

## Pending

- [ ] Auditing as `t_*` task (optional)
