---
title: Acme PTO FAQ — spec and constraints
status: living
tags: [example]
---

# Spec and constraints

## Spec

Build an internal FAQ assistant for Acme PTO policy.

- One approved source: `policies/pto.md`, edited by HR
- Every answer cites the heading it used
- If the source does not cover the question, the assistant says so and logs the question
- It does not give legal advice, approve a request, or write to payroll
- HR can change the policy file without an engineer
- An engineer can run a small test set that includes refusal cases

## Constraints

| Constraint | Rule |
| :--- | :--- |
| Source of truth | Only `policies/pto.md` in this example repo |
| Secrets | No API keys in git. Use `YOUR_DOCS_TOKEN` locally if you add a connector |
| Identity | Example users only (`employee@example.com`) |
| Scope | Read-only answers. No ticket creation in v1 |
| Failure | Wrong clause cited, or a guess when the file is silent, is a failed task |

## Out of scope

- Replacing the HR system
- Answering benefits questions other than PTO
- Training a custom model
