---
title: Automation portfolio scorecard
status: living
tags: [enablement, prioritization]
---

# Automation portfolio scorecard

Use this when deciding what to automate next, what to keep, and what to retire. Score candidates before building. Revisit live automations on a fixed cadence.

## Intake score (before build)

| Factor | How to score (1–5) |
| :--- | :--- |
| **Weekly hours saved** | Time removed for one person × how often the work happens |
| **Team reach** | How many people benefit when it works |
| **Urgency / pain** | How loud the pain is today (errors, blocked work, morale) |
| **Build effort** | Spec + agent work + review cost (invert: 5 = cheap) |
| **Maintenance burden** | How often it will break or need policy updates (invert: 5 = cheap) |
| **Blast radius if wrong** | Safety, legal, or trust damage if it fails (invert: 5 = low risk) |

**Rough rank:** `(hours_saved × reach × pain) × (build + maintenance + safety_inverted) / 3` is enough. Prefer small wins that compound. Refuse automations that replace human judgment on moral or irreversible calls.

## Portfolio health (sample — fictional)

| Automation | Status | Owner | Last review | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Acme PTO FAQ (policy reader) | Active | HR + enablement | 2026-10-14 | Cite-or-refuse; golden tests green |
| Weekly research digest draft | Degraded | Comms | 2026-09-01 | Source feed changed; fix or retire next sprint |
| Legacy FAQ scraper (pre-policy file) | Retired | — | 2026-08-01 | Superseded by single `policies/pto.md` source |

## Retirement triggers

- Maintenance cost exceeds hours saved for two review cycles
- A better system of record now owns the same answers
- Failure modes keep expanding the blast radius
- Nobody will own the runbook

Record retirements under chapter `08-sunset/` for real products.
