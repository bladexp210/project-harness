---
title: "Mockup: UML Composite Structure"
status: experiment
tags: [mockup, uml, static, L3]
---

# UML — Composite structure diagram (L3)

> **FICTITIOUS** — internals of Checkout widget. **Family:** static.

```mermaid
flowchart TB
    subgraph CheckoutWidget
        CartView[Cart View]
        PayForm[Payment Form]
        subgraph Controller
            CC[Checkout Controller]
        end
    end
    CartView --> CC
    PayForm --> CC
```

**Shows well:** internal parts of one component.  
**Poor at:** cross-system pools (use BPMN2 collaboration).
