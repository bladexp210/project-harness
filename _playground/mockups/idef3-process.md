---
title: "Mockup: IDEF3 Process"
status: experiment
tags: [mockup, idef, dynamic, L3]
---

# IDEF3 — Process description (L3)

> **FICTITIOUS** — rework loop on review. **Family:** dynamic.

```mermaid
flowchart LR
    U1[U1 Review threats]
    J1{J1 Find gap?}
    U2[U2 Update model]
    U3[U3 Re-review]
    U1 --> J1
    J1 -->|yes| U2
    U2 --> U3
    U3 --> J1
    J1 -->|no| Done([Gate B pass])
```

**Shows well:** junctions, fan-out/in, precedence, feedback.  
**Poor at:** data definitions (IDEF1X); deployment.

*IDEF3 uses units (U) and junctions (J) — Mermaid approximates for learning.*
