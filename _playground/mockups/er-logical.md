---
title: "Mockup: ER Logical"
status: experiment
tags: [mockup, er, static, L2]
---

# ER — Logical entity-relationship (L2/L3)

> **FICTITIOUS** — OrderLine data. **Family:** static.  
> **In harness:** `02-design/layers/data.md`.

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE_ITEM : contains
    PRODUCT ||--o{ LINE_ITEM : references
    ORDER {
        uuid id
        string status
    }
```

**Shows well:** entities and cardinalities.  
**Poor at:** API call order; deployment.
