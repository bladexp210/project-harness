---
title: "Seed: lifecycle playbook distillation (independent research)"
status: reference
date: 2026-06-10
tags: [research, seed, provenance]
---

# Seed — AI-Assisted Lifecycle Playbook

Distilled from `_inbox/ai-assisted-software-product-lifecycle-playbook.md`
(Alex's independent research, 2026-06-10). Unlike the repo seeds, this
source is already a synthesized methodology — so this seed is a **three-way
analysis against project-harness**: what it confirms, what it adds, what it
challenges. Provenance: `playbook → section`.

**Citation caveat:** the source cites numbered references with no
bibliography. Treat its claims as synthesis to verify, not citable
research. Where the book needs the underlying source (e.g. skill-erosion
studies), find the primary literature first.

---

## Confirms (external validation, no action)

- **Artifact spine ≈ the book itself.** Its recommended repo structure
  (thesis → discovery → architecture/ADRs → AI governance → delivery →
  operations → sunset) is our chapter structure independently rederived —
  including the closing note that folder names matter less than decisions
  being versioned and findable. `playbook → Recommended repository structure`
- **AI grounding package ≈ `context/` files** (domain invariants, forbidden
  patterns, approved deps, perf budgets, required tests). Confirms the
  company framework's include/exclude discipline from a third direction.
  `playbook → Grounding package`
- **Task brief ≈ our ICOM frame** — purpose, scope, contracts/invariants,
  constraints, required tests, acceptance criteria. `playbook → Task brief template`
- **Provider independence ≈ dimension 1** (gateway abstraction, per-task
  budget/latency policy). `playbook → Provider independence`
- **Human authority over decisions, AI as constrained accelerator;
  generated code as untrusted input; layered verification; expand-contract
  migrations; canary + auto-rollback; incident → durable artifact** — all
  already in our seeds; now triple-sourced. `playbook → throughout`
- **Anti-pattern list** overlaps the evaluation report's critiques
  (output-volume metrics, decisions hidden in prompts, no sunset plan).
  `playbook → Anti-patterns`

## Adds (new material per chapter)

### Ch. 00 / manifesto
- **Barbell antifragility** — conservative core (identity, money,
  production data: boring, proven, tight) + experimental edge (new models,
  speculative features: isolated, blast-radius-capped). Cheap failure where
  novelty is high; every incident converts to an invariant, test, monitor,
  or runbook line. *Best vocabulary upgrade on offer for the manifesto's
  antifragility claim.* `playbook → Barbell antifragility`
- **Legibility over hidden cleverness** — knowledge in versioned artifacts,
  not prompt craft or operator habit; names the *knowledge-monopoly* risk
  (capability trapped in vendor behavior or one person's prompts).
  `playbook → Legibility`

### Ch. 01
- **Problem memo before any prototype:** pain, current workaround, why
  existing options fail, what must be true, what evidence would *disprove*
  the thesis. Plus an **assumption register** (assumption → disconfirming
  signal → decision deadline) and **kill criteria written before funding**.
  `playbook → Strategy and ideation`
- **Negative requirements:** behaviors that must be rejected even if they
  look useful — vague requirements are an open invitation for AI to invent
  plausible filler (explicitness as anti-hallucination control).
  `playbook → Discovery and requirements`
- **Data classification matrix + compliance obligation map** as discovery
  artifacts, not afterthoughts. `playbook → Discovery artifacts`

### Ch. 02
- **Threat modeling as a design-phase gate** — our biggest genuine gap.
  Assets/crown jewels, trust boundaries, abuse cases, AI-specific threats
  (prompt injection, data leakage, hallucinated dependencies, untrusted
  tool output), detection + recovery per major threat. Candidate: a
  threat-model section or file in 02-design, red-team agent as natural
  owner. `playbook → Threat model contents`
- **Modular monolith as the stated default** — split only with demonstrated
  need; explicit boundaries *inside* the monolith. Sharper than anything in
  the repo seeds; decision-table-friendly. `playbook → Architecture rules`
- **Reversibility and blast radius as ADR fields** — our template has
  pre-mortem but not an explicit reversibility/blast-radius/fallback line.
  Candidate template addition (second one — batch with the AI-rejection
  field already shipped). `playbook → Required artifact spine`

### Ch. 03
- **Gate B (before implementation):** requirements testable, non-goals +
  abuse cases documented, threat model reviewed, grounding package updated,
  SLOs + perf budgets defined. The six stage-gates (A–F) map cleanly onto
  chapter exits; worth adopting as each chapter's closing checklist.
  `playbook → Stage-gate checklists`
- **Hard implementation rules** as constraints/global.md candidates: no
  AI changes to protected branches, no secrets in prompts, no new
  dependency without provenance + license review, no schema change without
  rollback notes. `playbook → Hard implementation rules`

### Ch. 04
- **Golden-task eval suite for provider substitution** — the missing test
  for our LiteLLM swap claim: vendor-agnosticism is only real if you can
  *prove* a substitute passes the same task suite. `playbook → Provider independence`
- **Human skill preservation** — skill-erosion counter-practices: human-
  written notes for important changes, periodic low-AI tasks, train on
  internals not just tools, track "can the team still explain and repair
  the system without the assistant?" New theme, absent from all other
  seeds; candidate for Ch. 04 or 06. *Verify primary literature before
  citing.* `playbook → Human skill preservation`

### Ch. 07 / 08
- **Evolution & deprecation as a distinct phase between operate and
  sunset** — AI accelerates addition, so governance must deliberately
  accelerate *pruning*: quarterly low-usage feature review, provider
  concentration review, dependency abandonment risk. Evolvability test:
  can you remove a feature / replace a provider / retire a data flow
  without existential risk? Candidate: a section in Ch. 07 rather than a
  tenth chapter. `playbook → Evolution and deprecation`
- **Sunset checklist + Gate F** — first concrete sunset material in any
  seed: export paths, deletion by retention class, credential revocation,
  vendor termination, searchable archive, final retrospective on reusable
  capabilities. Exit: "no orphaned access, unmanaged data, unsupported
  dependency, or unowned obligation." Cross-check against the Perplexity
  sunset report when it lands. `playbook → Sunset and archival`

## Challenges (where it pushes against our decisions)

1. **9 stages vs 9 chapters — split points differ.** It separates
   *verification* from *implementation* and *evolution/deprecation* from
   *operations*. We fold verification into Ch. 05 (Gherkin closes tasks)
   and have no explicit evolution phase. Verdict: keep our folds, but Ch.
   05 should name verification as its second half, and Ch. 07 gets an
   evolution/pruning section. No new chapters.
2. **Roles topology vs agent team.** It names six human role-owners
   (product, technical, security, delivery, ops, AI governance) and says
   one person may hold several, but responsibilities stay explicit. Our
   agent team covers some; *security/compliance owner* has no counterpart
   — red-team agent is the closest seat. Worth one paragraph in Ch. 04.
3. **Ceremony cadences** (weekly portfolio/risk review, monthly resilience,
   quarterly sunset review) — we are artifact-driven, not calendar-driven.
   Tension is real: artifacts without cadence rot (the evaluation report's
   "living document needs a heartbeat"). Candidate compromise: cadences as
   *reader-facing suggestions* in Ch. 06/07, not book mechanics.
4. **"Governance-first, not AI-first."** Its closing synthesis directly
   counters the company framework's first tenet. The book's actual position
   is closer to the playbook — worth stating explicitly in the manifesto
   rather than inheriting "AI-First" branding uninspected.

## Immediate action candidates (this session or next)

1. ADR template: add reversibility / blast radius / fallback line.
2. `03-plan/constraints/global.md`: merge the hard implementation rules.
3. STATE open thread: threat-model artifact for 02-design.
