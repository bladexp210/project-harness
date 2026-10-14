---
title: "Mockup: UML Component"
status: experiment
tags: [mockup, uml, static, L3]
---

# UML — Component diagram (L3)

> **FICTITIOUS** — interfaces between modules. **Family:** static.

```mermaid
flowchart LR
    subgraph OrderModule
        OS[Order Service]
    end
    subgraph PaymentModule
        PA[Payment Adapter]
    end
    OS -->|IPaymentPort| PA
```

**Shows well:** provided/required interfaces.  
**Poor at:** message sequence (use sequence diagram).
