---
title: User Roles
chapter: 01
status: template
audience: [novice, seasoned, both]
tags: [understand, roles]
---

# User Roles — who is this software for?

## What this is

A user role is a *reason* someone uses your software, not a job title. One
person can hold several roles (a shop owner who also answers support email),
and one role can be held by thousands of people. Everything downstream hangs
on this file: [[use-cases]] are written per role, the
[[02-design|UX layer]] is designed per role, and the
[[03-plan|decomposition tree]] is ordered by what the most important roles
need most often.

## Why it matters

Skipping this step is how products grow features nobody asked for. When a
role is written down, every later decision can be tested against it: "which
role needs this, and how badly?" If the answer is "none, but it would be
cool" — that branch gets pruned in [[03-plan|Plan]], with the reasoning
recorded.

## How to fill it in

Name each role, describe it in one or two sentences, and list its primary
goals — what success looks like *for them*, in their words. Three to six
roles is typical. If you have more than eight, some are probably the same
role wearing different clothes; merge them.

Don't forget the roles the product creates for *you*: someone will operate
this thing ([[07-ship-operate|Ship & Operate]]) and someone will answer for
it when it winds down ([[08-sunset|Sunset]]). Usually that's the reader —
write yourself in.

> [!NOTE] Ask your AI agent
> "Help me discover the user roles for [describe your software in one
> sentence]. Interview me one question at a time, and challenge any role
> that looks like a job title instead of a reason to use the software."

## Discovery boundaries

Before naming roles, run lightweight discovery — not a substitute for later UX
work, but enough to avoid encoding founder bias as fake evidence. Distilled from
`research/discovery-research-seed.md` (inbox report archived S47).

| Method | Answers | Use when | Do not use when |
| :---- | :---- | :---- | :---- |
| **JTBD** | What progress is the user trying to make? | Switch/churn analysis, prioritizing outcomes | Replacing workflow design; B2B buyer ≠ user without split |
| **Personas** | Empathy narrative for a segment | After real interviews; ≤4–5 primaries | Before interviews; demographic-heavy cards |
| **User roles** (this file) | Functional relationship to the system | Authorization, requirements, B2B | Consumer apps driven by emotion/social signaling alone |
| **Story mapping** | Journey backbone + vertical detail | MVP scoping, sequential flows | Dashboards, API-first products where journey distorts |

**Practitioner default:** roles as the functional skeleton; personas on top for
empathy where interviews exist.

---

## Template

### Role: [name, e.g., "Shopper"]

- **Who they are:** [one or two sentences — e.g., "A first-time visitor who
  arrived from a search result and has never heard of the brand."]
- **Primary goals:** [what success looks like for them — e.g., "Find the
  product, trust the site enough to pay, get a receipt."]
- **Context & constraints:** [device, time pressure, expertise — e.g.,
  "On a phone, mid-commute, will abandon after one confusing screen."]

### Role: [name, e.g., "Store owner"]

- **Who they are:**
- **Primary goals:**
- **Context & constraints:**

### Role: Operator *(usually you — keep unless truly serverless)*

- **Who they are:** [whoever deploys, monitors, and fixes the system —
  see [[07-ship-operate|Ship & Operate]]]
- **Primary goals:** [e.g., "Know the system is healthy without checking
  manually; recover from failure in minutes, not days."]
- **Context & constraints:**

---

When every role has goals you could read aloud to a real person in that role
without embarrassment, move on to [[use-cases]].
