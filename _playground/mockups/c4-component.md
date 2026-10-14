---
title: "Mockup: C4 Component"
status: experiment
tags: [mockup, c4, static, L3]
---

# C4 — Component diagram (L3)

> **FICTITIOUS** — inside API Application container. **Family:** static.

```mermaid
flowchart LR
    subgraph API Application
        OC[Order Controller]
        OS[Order Service]
        PR[Payment Router]
        RE[Order Repository]
    end
    OC --> OS
    OS --> PR
    OS --> RE
```

**Shows well:** modules inside one container.  
**Poor at:** cross-container deployment; runtime timing.
