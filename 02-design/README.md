---
title: Design
chapter: 02
status: in-progress
audience: [novice, seasoned, both]
tags: [orientation, design]
---

# 02 — Design

You know who your users are and what they need ([Ch. 01](../01-understand/)).
Before any task list or line of code, this chapter makes the decisions that
are expensive to change later — and *only* those.

## Design-first is not Big Design Up Front

The classic critique of BDUF is correct: requirements drift, designers
cannot foresee what only implementation reveals, and committees produce
documents nobody reads. This chapter is built to dodge exactly that. Design
here is **bounded** — exploration-execution loops instead of a one-shot
blueprint, diagrams capped at 20 nodes ([ADR-002](decisions/ADR-002-modeling-conventions.md)),
decision tables instead of essays. And the **reversibility field** in every
ADR is the mechanism that decides where effort goes: an irreversible
decision (your data model, your one identity provider) earns real design
work; a reversible one gets a sensible default and a note, and you move on.
You are not designing everything up front. You are spending design effort
in proportion to how expensive each decision is to undo.

## The four layers

Every software product, regardless of stack, has the same four design
surfaces. Each gets one file; each file teaches the layer and then
scaffolds *your* decisions for it:

| Layer | File | Decides |
| :---- | :---- | :---- |
| Data | [data](layers/data.md) | What is stored, how it relates, how it evolves, how it leaves |
| Application | [application](layers/application.md) | How logic is organized, where the boundaries are |
| UX | [ux](layers/ux.md) | How humans experience it — latency, accessibility, AI-product patterns |
| Communication | [communication](layers/communication.md) | How parts talk to each other and to the outside |

Work them in that order: data constrains application, application
constrains communication, and ux cuts across all three.

## Honest recommendations

Every pattern this chapter recommends carries its **failure condition** —
the observable circumstances under which the recommendation is wrong
([ADR-005](decisions/ADR-005-failure-condition-convention.md)). In decision tables that
is the "when NOT to apply" row. Patterns are correct *somewhere*; the
failure condition tells you whether your project is that somewhere.

## Decisions live in `decisions/`

Each significant design choice becomes an ADR from
[the template](../_templates/new-decision.md) — context, decision, reversibility,
red-teamed alternatives, pre-mortem. Write the ADR when you decide, not
after: a decision without a contemporaneous record doesn't exist.

## Architecture documentation (arc42)

The [arc42 template](arc42/README.md) under this chapter scaffolds **12
documentation sections** — introduction through glossary. It is a *structure*
for your architecture docs, not a diagram notation. Diagrams render in
[viz/](../viz/README.md); significant choices stay in `decisions/` and index in
arc42 §9.

| You have | Fill arc42 section |
| :------- | :----------------- |
| Roles and use cases (Ch. 01) | §1 Introduction and Goals |
| Constraints | §2 Constraints |
| System boundary | §3 Context — start with [context](../viz/c4/context.md) |
| ADRs | §9 Architectural Decisions |
| Threat model | §11 Risks (living register) |

## Five-paper design review

Run this checklist before locking layer decisions or promoting a task to
[Build](../05-build/README.md). Each question maps to a foundational paper — lineage in
[ADR-002](decisions/ADR-002-modeling-conventions.md) and
[ADR-005](decisions/ADR-005-failure-condition-convention.md). Full brainstorm:
[session-33-five-papers-brainstorm](../context/system/sessions/session-33-five-papers-brainstorm.md).

| # | Question | Paper | Pass when |
| :-: | :------- | :---- | :-------- |
| 1 | What **design decision** does this module, service, agent, or team boundary hide? | Parnas | You can name the volatile decision; adjacent parts depend on an interface, not internals |
| 2 | What are the **exact abstractions** at the boundary — IDs, operations, invariants? | Liskov | A new contributor can use the contract without tribal knowledge |
| 3 | What are the **states and transitions** of this workflow? | Dijkstra | You can answer: current state, valid next states, evidence of last transition |
| 4 | Which **preconditions and postconditions** are worth enforcing because mistakes are expensive? | Hoare | High-risk paths have explicit checks; routine paths stay lightweight |
| 5 | Which difficulties are **essential** to the problem vs **accidental** from tooling or process? | Brooks | Essential items get ADR/design time; accidental items get simplification or tool change |

**Over-application guards** (ADR-005 "when NOT"):

- Do not split into modules or services that still require intimate mutual knowledge (Parnas).
- Do not treat private fields or ORM entities as abstractions without behavioral contracts (Liskov).
- Do not equate absence of `goto` with clarity — nested branches can still be unreadable (Dijkstra).
- Do not demand formal proof where a checklist or Gherkin scenario suffices (Hoare).
- Do not use "no silver bullet" to block measured incremental improvements (Brooks).

## The exit gate

This chapter closes with a [threat model](threat-model.md) — what can go
wrong, on purpose — written against the four layer files and reviewed by
the red-team agent *before any implementation begins*. Design changes are
cheap this week; the same discoveries in [Build](../05-build/README.md) are rework.
