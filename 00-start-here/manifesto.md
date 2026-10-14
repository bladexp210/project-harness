---
title: Manifesto
chapter: 00
status: in-progress
audience: [novice, seasoned, both]
tags: [orientation, philosophy]
---

# Manifesto

This system is designed for durability, not just speed.

AI is a multiplier — not a substitute for understanding. Every tool in this
book accelerates a decision you make; none of them makes the decision for you.
When a step is automated, the book tells you what is happening underneath, so
that automation never becomes dependence.

This book is not AI-first. It is human-agency-first. The order matters:
intent, constraints, and decision authority are yours; AI operates inside
the structure those create — never the other way around. A system where the
governance came first can adopt any model, swap any vendor, and survive any
outage. A system where the AI came first cannot explain itself.

No practice earns authority by reputation. Before you adopt one — from this
book or anywhere else — run it through four questions: what problem was it
built to solve, is that problem actually present in your project, under what
conditions does it fail, and what outcome (not what proxy) will tell you it is
working. A practice that can't answer these is cargo cult, however canonical it
sounds. The methods in this book are held to the same test.

Every decision is documented. Not as bureaucracy — as memory. The decision
records keep the options we rejected and why, because the rejected option is
exactly what you'll reach for in six months when the context has faded.

The system is built as a barbell. The core — identity, money, production
data — stays boring, proven, and tightly held; nothing experimental touches
it. The edge — new models, speculative features — is where novelty runs,
isolated and blast-radius-capped, so failure there is cheap and survivable.
Spend your risk budget where a mistake teaches you something; refuse to spend
it where a mistake costs you what you can't get back.

Every failure feeds back. A mistake that updates a constraint, a trigger, or a
checklist was tuition. The same mistake twice is a system defect, and the
system — not your discipline — is what gets fixed.

When AI is unavailable, expensive, or wrong, the documented system still runs.
You can read every file, trace every decision, and continue by hand.

When you bring someone new onto the project — human or AI — they can read,
understand, and trust what was built, and why.

That is the whole philosophy. The remaining chapters are just this page,
applied.

---

## Addendum — Plain language and visuals

*(Session 14 — aligns with [ADR-008](../02-design/decisions/ADR-008-reader-facing-language-and-visuals.md))*

Trust requires **readability**, not performance. If someone needs insider
vocabulary to use the harness, the harness failed — whether their English is
native or not, whether they are new or senior.

**We write so the problem stays in focus:**

- **Say what to do first.** One sentence: what this section is for.
- **Show structure.** Use a table or diagram when comparing paths, listing
  steps, or showing who hands off to whom. A picture of the workflow beats
  three paragraphs of " furthermore."
- **Use plain words.** Prefer "confirm the table is correct" over ritual
  language that only regulars understand. Define a project term once; link
  it; reuse it.
- **Keep sentences short.** One idea at a time. Tell the reader what to run,
  open, or check — not what they "might consider exploring."
- **Same bar for everyone.** Writing that works for English as a third
  language works for a tired expert on a deadline. Simplicity is respect, not
  condescension.

The dual path (`[!LEARN]` / `[!TIP]`) still applies: the scaffold teaches with
visuals and steps; the fast track gives commands and tables for people who
skip the tour. Both paths must be **clear**, not clever.

When you finish a section, you should know **what you can do now** that you
could not do before — without needing a glossary of book-culture.
