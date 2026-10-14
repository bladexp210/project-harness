---
title: Code Boilerplate
chapter: 06
status: outline
tags: [boilerplate, code]
---

# Code boilerplate

Runnable implementation patterns live here — auth middleware, API route
handlers, test fixtures, migration stubs. **This book harness** is
markdown-first; your reader product fills this folder after the first
successful build tasks.

## When to promote

- Same pattern appears in two or more tasks unchanged
- Human reviewed and tests pass on the promoting commit
- One-line header states *when to use* and *last verified* date

## Structure (reader product)

```
code/
  auth/           ← e.g. jwt-service.ts
  api/            ← e.g. route-handler.ts
  tests/          ← shared fixtures
```

Reference promoted paths in task files under **Boilerplate to use**.
