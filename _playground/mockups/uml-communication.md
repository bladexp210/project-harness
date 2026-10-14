---
title: "Mockup: UML Communication"
status: experiment
tags: [mockup, uml, dynamic, L3]
---

# UML — Communication diagram (L3)

> **FICTITIOUS** — object links during order flow. **Family:** dynamic.

```mermaid
flowchart LR
    Customer -->|1: submit| Controller
    Controller -->|2: charge| PaymentAdapter
    Controller -->|3: save| Repository
```

**Shows well:** which objects collaborate; numbered steps optional.  
**Poor at:** strict time axis (use sequence or timing).
