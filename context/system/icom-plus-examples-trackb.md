---
title: ICOM+ Examples F–G (Track B)
layer: 1-system
status: reference
version: "0.3"
updated_at: 2026-06-15T20:00:00
tags: [icom, examples, track-b, reference]
---

# ICOM+ examples F–G — Track B REAL

> [!NOTE] Verified in Obsidian 2026-06-15
> Convention: [[icom-plus-convention]] · Taxonomy: [[diagram-taxonomy]].

---

## Example F — L3/L4 REAL Track B (`wf_commit_process`)

**Question:** How does one logical commit batch leave the agent and land on the
session branch?

**Stack:** `app_book_harness` → `proc_session_build` → `wf_commit_process` →
`t_01`…`t_04`. Full prose boxes:
[[_playground/l4-models/commit-process/L1-cap-session-governance|L1]] ·
[[_playground/l4-models/commit-process/L2-proc-session-build|L2]] ·
[[_playground/l4-models/commit-process/L3-commit-process|L3]] ·
[[_playground/l4-models/commit-process/01-validate-batch|L4 reference]].

```mermaid
flowchart LR
    classDef roleExecAgent fill:#b45309,stroke:#92400e,color:#fff
    classDef roleExecHuman fill:#2d6a4f,stroke:#1b4332,color:#fff
    classDef roleSupGate fill:#9f1239,stroke:#881337,color:#fff,stroke-width:2px
    subgraph L3_wf["wf_commit_process · Orchestrator: human + agent"]
        fb_t01["<b>t_01 validate</b><br/><b>Exec:</b> exe_agent_cursor<br/><b>Sup:</b> human:Alex"]:::roleExecAgent
        fb_t02["<b>t_02 draft blocks</b><br/><b>Exec:</b> exe_agent_cursor"]:::roleExecAgent
        fb_t03["<b>t_03 review</b><br/><b>Exec:</b> exe_human_alex<br/><b>Sup:</b> human (gate)"]:::roleSupGate
        fb_t04["<b>t_04 git commit</b><br/><b>Exec:</b> exe_human_alex<br/><b>Sup:</b> human (irreversible)"]:::roleSupGate
    end
    style L3_wf fill:#ecfdf5,stroke:#0d6e6e
    fb_t01 -->|go signal| fb_t02
    fb_t02 -->|PS blocks| fb_t03
    fb_t03 -->|approve| fb_t04
    fb_t03 -.->|reject| fb_t01
```

Legend: amber = agent executor · rose = human gate · green stroke band = workflow.

**C4 link:** `m_book_repo` (Container), `m_scripts` (validator module).  
**Auditing:** model as a normal `t_*` task when needed — no special box type.

---

## Example G — L3/L4 REAL Track B (`wf_session_close`)

**Question:** How does a session branch close and merge to `main`?

**Stack:** `app_book_harness` → `proc_session_close` → `wf_session_close` →
`t_01`…`t_06`. Full prose boxes: [[_playground/l4-models/session-close/README|session-close/]].

```mermaid
flowchart LR
    classDef roleExecAgent fill:#b45309,stroke:#92400e,color:#fff
    classDef roleSupGate fill:#9f1239,stroke:#881337,color:#fff,stroke-width:2px
    subgraph L3_close["wf_session_close · Orchestrator: human + agent"]
        g01["<b>t_01 final validate</b><br/><b>Exec:</b> exe_agent_cursor"]:::roleExecAgent
        g02["<b>t_02 draft STATE</b><br/><b>Exec:</b> exe_agent_cursor"]:::roleExecAgent
        g03["<b>t_03 dashboard</b><br/><b>Exec:</b> exe_agent_cursor"]:::roleExecAgent
        g04["<b>t_04 bootstrap</b><br/><b>Exec:</b> exe_agent_cursor"]:::roleExecAgent
        g05["<b>t_05 review close</b><br/><b>Sup:</b> human gate"]:::roleSupGate
        g06["<b>t_06 merge main</b><br/><b>Sup:</b> irreversible"]:::roleSupGate
    end
    style L3_close fill:#ecfdf5,stroke:#0d6e6e
    g01 --> g02 --> g03 --> g04 --> g05 --> g06
    g05 -.->|reject STATE| g02
    g05 -.->|reject dashboard| g03
    g05 -.->|reject bootstrap| g04
```

Legend: amber = agent executor · rose = human gate · maps to [[session-workflow]]
close checklist A→E.

**Parent process:** `proc_session_close` (`roleManager` if drawn as L2 node).
**Precondition:** `wf_commit_process` complete on session branch.

