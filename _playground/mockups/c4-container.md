---
title: "Mockup: C4 Container"
status: experiment
tags: [mockup, c4, static, L2]
---

# C4 — Container diagram (L2)

> **FICTITIOUS** — inside OrderLine. **Family:** static.

```mermaid
flowchart TB
    subgraph OrderLine
        SPA[Web App SPA]
        API[API Application]
        DB[(PostgreSQL)]
        Queue[Event Queue]
    end
    Customer([Customer]) --> SPA
    SPA --> API
    API --> DB
    API --> Queue
```

**Shows well:** deployable parts and data stores.  
**Poor at:** classes; step-by-step checkout flow (use BPMN2 or sequence).
