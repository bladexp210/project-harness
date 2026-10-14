---
title: Runbooks
chapter: 07
status: living
tags: [runbook, operations]
---

# Runbooks

One runbook per **service**, **environment**, or **operational surface** you
must keep running. A runbook is not a wiki dump — it is the minimum an on-call
responder needs without reading the whole repo.

## How to create

1. Copy `_templates/runbook.md` → `runbook/<service-name>.md`
2. Fill every section before the first production deploy
3. Update after every incident post-mortem that touched this service
4. Review quarterly — stale runbooks are a Canon Gap

## Harness-meta example

This book maintains one worked example for its own operational surface:

| Runbook | Covers |
| :---- | :---- |
| [[example-harness-track-a-runbook]] | `validate_md.py`, pre-commit, Track A Docker stack health |

Your reader product replaces this with your API, database, and deployment
targets.

## Linking

Reference runbook paths in:

- [[03-plan/PROJECT-PLAN|PROJECT-PLAN]] operational tasks
- Post-mortem **Artifacts updated** sections
- Layer 2 context if the service is architecturally significant
