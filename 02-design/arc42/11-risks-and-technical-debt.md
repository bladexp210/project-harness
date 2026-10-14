---
title: "arc42 §11 — Risks and Technical Debt"
chapter: 02
status: reference
audience: [novice, seasoned, both]
tags: [arc42, design, harness]
---

# arc42 §11 — Risks and Technical Debt

**Question answered:** What can go wrong, what debt exists, and what is the
mitigation plan?

> [!NOTE] REAL — harness-meta
> Living register for **this repo**. The Ch. 02 [[../threat-model|threat
> model]] remains a **teaching template** and Gate B scaffold for the
> reader's product — pre-mortem gaps G1–G5 are **accepted harness-meta
> risks** here, not blockers for book work. Your fork replaces rows; keep
> §11 current when layers or ADRs change.

## Risk register — harness meta (accepted)

Sourced from threat-model pre-mortem (2026-06-17, task 01) — status
**accepted** for the book-as-harness; mitigations name enforcement hooks.

| ID | Risk | Prob. | Impact | Mitigation | Status |
| :---- | :---- | :---- | :----- | :--------- | :----- |
| R1 | **Stale handoff** — STATE or dashboard L1–L3 wrong after merge; next session re-discovers from chat | Med | High | Close checklist A–D mandatory before merge offer; human validate gate; D-004 trigger | accepted |
| R2 | **Automation bias** — human skips diff review as agent seems reliable | Med | High | Proceed/validate gates cannot bind silently; periodic human-only git; Knight Capital cited in threat-model | accepted |
| R3 | **Crown jewels unnamed in threat-model template** (G1) | Low | Med | Harness assets listed below; §11 + session-workflow own handoff integrity; reader fills template for product | accepted |
| R4 | **No abuse cases in threat-model table** (G2) | Low | Med | Harness use cases are meta-work; abuse analog = silent STATE overwrite — covered by R1 | accepted |
| R5 | **Empty threat-table row** (G3) | Low | Med | §11 is the harness living register; threat-model template stays for reader Gate B | accepted |
| R6 | **Gate B SLOs undefined for meta-work** (G4) | Low | Low | Harness SLO = validator green + handoff accurate; reader defines product SLOs in PROJECT-PLAN | accepted |
| R7 | **AI controls not fully traced to validator** (G5) | Med | Med | gitleaks pre-commit; no-secrets-in-prompts rule; dependency provenance in [[global]]; partial — full trace deferred | accepted |
| R8 | **Track A secrets in compose** — `.env` leaked or committed | Low | High | `.env` gitignored; gitleaks; Track A docs warn; human rotates keys | accepted |
| R9 | **Sandbox git corruption** (D-001) | Low | High | All git on Windows; NUL-byte validator check | accepted |

### Harness crown jewels (§11 supplement for G1)

Assets whose loss or silent corruption ends harness work — not duplicated in
the threat-model template.

| # | Asset | Why it matters | Where it lives |
| :-: | :---- | :------------- | :------------- |
| 1 | Session handoff | Wrong STATE = disoriented next agent | `STATE.md`, `_index/dashboard/` |
| 2 | Canon markdown | Book + operational context | `00`–`08`, `context/`, `Agents.md` |
| 3 | Agent roster + tasks | Wrong yaml = wrong agent behavior | `04-your-agents/` |
| 4 | Validator + loader | Green gate without enforcement = false confidence | `scripts/validate_md.py`, `task_context.py` |

## Technical debt register

Active entries from [[06-learn/DEBT-LEDGER|DEBT-LEDGER]] — full trigger
contracts stay in Ch. 06; §11 indexes open items only.

| ID | Debt (one line) | Paydown trigger | Status |
| :---- | :---- | :-------------- | :----- |
| D-001 | Git Windows-side only (sandbox NUL corruption) | Sandbox git proven safe on this host | active |
| D-002 | Session-1 sub-headings not promoted to `###` | First deep edit of each legacy doc | active |
| D-004 | STATE.md manual session close | Two closes without update → automate reminder | active |
| D-005 | NC-ND cache specifics need vendor re-verify | External publication of Ch. 02 data layer | active |

**Resolved (reference only):** D-003 link resolution (S9), D-006 budget enforcement (S8), D-007 Layer-1 budget 200 (S8). See [[../../_index/glossary#Debt IDs|glossary debt table]].

## Open threads

| Source | Count | Note |
| :----- | :---- | :---- |
| STATE open threads | 0 | Post-spine T9 closed S32 |
| Threat-model Gate B | Open for reader product | Template `status`; harness meta-work proceeds |

When a thread opens, add a row here and link from STATE **Open threads**.

## Review cadence

| Trigger | Action | Owner |
| :------ | :----- | :---- |
| Layer file or ADR changes security posture | Re-read threat-model failure condition; update §11 if harness risk shifts | red-team agent + human |
| Session close with new debt | Append DEBT-LEDGER + one row here | Agent close draft |
| Track A stack change | Review R8; update [[track-a-setup]] | Operator |
| S40 roadmap approved | Reconcile defer list vs new threads | **Done** — [[session-roadmap-s40-plus]] |

Last §11 review: **2026-06-30** (S39 harness fill — G1–G5 accepted).

## ESL checklist (this section)

| Rule | Pass |
| :---- | :---- |
| Risks have mitigation + status | R1–R9 table complete |
| Debt links to DEBT-LEDGER | D-001, D-002, D-004, D-005 indexed |
| Threat-model relationship clear | Template for reader; §11 for harness |
| Product fork reminder | Reader replaces register rows |

## Where to go next

- **Threat model (Ch. 02 Gate B template):** [[../threat-model]]
- **Debt ledger (full contracts):** [[06-learn/DEBT-LEDGER]]
- **Quality scenarios (§10):** [[10-quality-requirements]]
- **Section index:** [[README]]
