---
title: "Mockup: UML Object"
status: experiment
tags: [mockup, uml, static, L4]
---

# UML — Object diagram (L4)

> **FICTITIOUS** — snapshot at checkout moment. **Family:** static (one instant).

```mermaid
flowchart LR
    c1[cart:Cart]
    i1[item1:LineItem sku=ABC]
    i2[item2:LineItem sku=XYZ]
    c1 --- i1
    c1 --- i2
```

**Shows well:** particular instances and links at one moment.  
**Poor at:** history over time (use sequence or state).
