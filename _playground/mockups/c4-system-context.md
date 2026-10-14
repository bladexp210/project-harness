---
title: "Mockup: C4 System Context"
status: experiment
tags: [mockup, c4, static, L1]
---

# C4 — System Context diagram (L1)

> **FICTITIOUS** — OrderLine shop. **Family:** static. **Not** a flowchart.

```mermaid
flowchart LR
    Customer([Customer])
    Admin([Shop Admin])
    OL[OrderLine System]
    Pay[Payment Provider]
    Ship[Shipping API]
    Customer -->|places orders| OL
    Admin -->|manages catalog| OL
    OL -->|charges| Pay
    OL -->|labels| Ship
```

**Shows well:** one system boundary; people and external systems.  
**Poor at:** containers inside OrderLine; message order.
