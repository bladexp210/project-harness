---
title: "Mockup: UML State Machine"
status: experiment
tags: [mockup, uml, dynamic, L3]
---

# UML — State machine diagram (L3/L4)

> **FICTITIOUS** — order lifecycle. **Family:** dynamic.

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Paid: payment_ok
    Paid --> Shipped: label_created
    Shipped --> Delivered: carrier_confirms
    Delivered --> [*]
    Paid --> Cancelled: timeout
    Cancelled --> [*]
```

**Shows well:** states and transitions for one entity.  
**Poor at:** multi-actor swimlanes (use BPMN2).
