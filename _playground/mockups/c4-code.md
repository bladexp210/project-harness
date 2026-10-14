---
title: "Mockup: C4 Code"
status: experiment
tags: [mockup, c4, static, L4]
---

# C4 — Code diagram (L4)

> **FICTITIOUS** — Order Service component. **Family:** static. (UML class view.)

```mermaid
classDiagram
    class OrderService {
        +createOrder(cart) Order
        -validate(cart) bool
    }
    class Order {
        +id UUID
        +status Status
    }
    class PaymentPort {
        <<interface>>
        +charge(amount)
    }
    OrderService --> Order
    OrderService ..> PaymentPort
```

**Shows well:** types and relationships in code.  
**Poor at:** acceptance criteria (use Gherkin).
