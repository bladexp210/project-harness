---
title: Use Cases
chapter: 01
status: template
audience: [novice, seasoned, both]
tags: [understand, use-cases]
---

# Use Cases — what each role needs to do

## What this is

> [!TEACH] Teach
> A use case is one thing a role needs to accomplish, written as an outcome:
> "Shopper completes a purchase," not "implement checkout API." Each use case
> gets two ratings — **frequency** (how often it happens) and **importance**
> (how bad it is when it fails) — and those two numbers, not anyone's
> enthusiasm, decide build order in [Plan](../03-plan/).

## Why it matters

> [!TEACH] Teach
> The frequency × importance matrix is the book's first real guardrail against
> vibe-driven scope. A daily-critical use case outranks a rarely-nice one no
> matter which is more fun to build. Dead branches in the decomposition tree
> point back here: *this* is the evidence a pruning decision cites.

## How to fill it in

> [!TEACH] Teach
> For each role in [user-roles](user-roles.md), list what they need to do. Rate frequency
> as Daily / Weekly / Rarely and importance as Critical / High / Medium / Low.
> Priority is derived, not assigned — see the scoring below.

> [!LEARN] Learn It
> **What this is:** a deterministic way to turn two ratings into one build
> order. **Why it matters:** if priority is derived, nobody can quietly
> promote a pet feature — they would have to argue the ratings, in writing.
>
> Step 1: score frequency — Daily = 3, Weekly = 2, Rarely = 1
> Step 2: score importance — Critical = 4, High = 3, Medium = 2, Low = 1
> Step 3: priority = frequency × importance (max 12)
> Step 4: sort descending; ties broken by importance, then by your judgment
> — recorded in one line.
>
> **What's happening underneath:** this is a crude utility function, and
> crude is fine. Its job isn't precision — it's forcing every use case
> through the same two questions and making the answers comparable.

> [!TIP] Fast Track
> `priority = freq(3/2/1) × importance(4/3/2/1)`, sort descending.
> You own the outcome.

> [!WARNING] The must-have lane (override)
> Two kinds of use case bypass scoring entirely and go straight to the top:
> **regulatory obligations** (data deletion, export, accessibility — a
> Rarely × Critical score of 4 must never lose to a Daily × Medium feature
> at 6) and **assumed basics** users never mention because they take them
> for granted (login works, data isn't lost — the Kano insight). Mark these
> rows `MUST` in the Priority column; the formula ranks everything else.

> [!TEACH] Teach
> One more rating trap: frequency measures *how often the case occurs*, not
> how loudly a few users ask for it. Five enthusiasts requesting daily ≠
> high frequency if your other thousand users never would. Estimate reach,
> not noise.
>
> Two categories are easy to forget because they haven't happened yet:
>
> - **Operational use cases** — checking system health, restoring a backup,
>   investigating "why was I charged twice?". These belong to the Operator
>   role; [Ship & Operate](../07-ship-operate/README.md) depends on them being here.
> - **Offboarding use cases** (the user lifecycle's ending — see
>   [ADR-004-lifecycle-vocabulary](../02-design/decisions/ADR-004-lifecycle-vocabulary.md)) — "export all my data," "delete my
>   account and everything about me." Rare by definition, often Critical by
>   law, and owed to users from day one — not only at the end: product
>   [sunset](../08-sunset/README.md) is mass offboarding, so pricing these in now is
>   what makes it cheap later.
>
> One category is deliberately deferred, not forgotten: every use case has
> an **abuse case** — how a hostile actor would use the same capability.
> You don't score those here (damage, not frequency × importance, rates
> them); you write them in the [Ch. 02 threat model](../02-design/threat-model.md), working
> from this table. Finish the table knowing it has that second reader.

> [!NOTE] Ask your AI agent
> "Here are my user roles: [paste from user-roles.md]. Help me list use
> cases for each, including operational and end-of-life cases. Then
> challenge my frequency and importance ratings — argue the other side
> before I lock them in."

---

## Template

| Role | Use Case | Frequency | Importance | Priority |
| :---- | :---- | :---- | :---- | :---- |
| [Shopper] | [Complete a purchase] | Daily | Critical | 12 |
| [Shopper] | [Track an order] | Weekly | High | 6 |
| [Store owner] | [Add a product] | Weekly | Critical | 8 |
| [Operator] | [Restore from backup] | Rarely | Critical | 4 |
| [Shopper] | [Export personal data] | Rarely | Critical | 4 |
| [ ] | [ ] | | | |

### Notes & tie-breaks

[One line per judgment call — e.g., "Ranked order tracking above product
add despite equal scores: shoppers outnumber owners 1000:1."]

---

> [!TEACH] Teach
> When the table is sorted and the top five rows would survive you reading
> them to a skeptical co-founder, carry the order into
> [PROJECT-PLAN](../03-plan/).

---

## Worked example — documentation drift

Fictional internal case. Three systems describe the same policy and they disagree: an HR handbook PDF, a pinned chat message, and a tooltip in the HR system. Nobody owns which sentence is current.

| Role | Use Case | Frequency | Importance | Priority |
| :--- | :--- | :--- | :--- | :--- |
| Employee | Get the current PTO rule with the clause it came from | Daily | High | 9 |
| HR editor | Replace the approved policy text without asking engineering | Weekly | Critical | 8 |
| Operator | See questions the bot refused to answer | Weekly | High | 6 |
| Employee | Export or delete what the bot stored about them | Rarely | Critical | MUST |

Tie-break: the export/delete row is `MUST` (assumed basic plus a privacy duty), so it outranks the daily FAQ even though the formula score is lower.

The full skim path for this case is [examples/acme-pto-faq](../examples/acme-pto-faq/README.md).
