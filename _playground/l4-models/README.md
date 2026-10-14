---
title: L4 models playground
status: experiment
updated_at: 2026-06-15T15:00:00
tags: [playground, modeling, process-stack]
---

# Process-stack models (playground)

Ground-up dynamic models. **Not canon** until promoted.

## Stack (decisions 2026-06-15)

```mermaid
flowchart TB
    L1["L1 Capability · app_* · Owner"]
    L2["L2 Process · proc_* · Manager"]
    L3["L3 Workflow · wf_* · Orchestrator"]
    L4["L4 Task · t_* · Executor + Supervisor"]
    L1 --> L2 --> L3 --> L4
```

**C4 static** (Container/module `m_*`, Component `comp_*`) links in prose —
not merged into process level names.

## Folders

| Folder | Capability | Process | Workflow |
| :----- | :--------- | :------ | :------- |
| [[commit-process/README\|commit-process/]] | `app_book_harness` | `proc_session_build` | `wf_commit_process` |
| [[session-close/README\|session-close/]] | `app_book_harness` | `proc_session_close` | `wf_session_close` |

Convention detail: [[context/system/icom-plus-convention|ICOM+ v0.3]] ·
[[context/system/diagram-taxonomy|Diagram taxonomy v0.3]] ·
[[context/system/icom-plus-convention#Color map (roles)|role colors]] ·
box schema in [[commit-process/README|commit-process/README]].
