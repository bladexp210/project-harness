---
title: "Mockup: UML Sequence"
status: experiment
tags: [mockup, uml, dynamic, L3]
---

# UML — Sequence diagram (L3/L4)

> **FICTITIOUS** — place order happy path. **Family:** dynamic.  
> **In harness:** `02-design/layers/communication.md`, `05-build/.../openhands.md`.

```mermaid
sequenceDiagram
    participant C as Customer
    participant API as API
    participant Pay as Payment
    C->>API: POST /orders
    API->>Pay: authorize(amount)
    Pay-->>API: approved
    API-->>C: 201 Created
```

**Shows well:** who talks to whom, in order.  
**Poor at:** deployment layout; policy tables.
