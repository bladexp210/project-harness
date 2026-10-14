---
title: "Seed: red-team critique of canonical practices (independent research)"
status: reference
date: 2026-06-11
tags: [research, seed, provenance, red-team]
---

# Seed — Against the Canon (red-team research)

Distilled from `_inbox/Against the Canon  A Rigorous Critique of Mainstream
System-Design and AI-Assisted Development Practices.md` (Alex's
independent red-team research, 2026-06-11). Like the playbook seed, this is
a **three-way analysis against project-harness**: confirms / adds /
challenges. Provenance: `canon → section`.

**Citation status — better than the playbook.** This source carries a full
68-entry bibliography. The primary papers are directly citable: Kleppmann
CAP critique (arXiv 1509.05393), METR productivity RCT (arXiv 2507.09089),
Pearce et al. Copilot security (NYU Tandon), GitClear longitudinal report,
Panickssery et al. self-preference (NeurIPS 2024), EMNLP/NeurIPS 2025
LLM-judge studies, CSET Georgetown automation-bias analysis. The rest are
secondary (blogs, LinkedIn, one Reddit) — treat as leads, cite the primary
underneath. **It also closes the playbook seed's open verification debt:
skill-erosion now has primary literature (CSET + GitClear, `canon → 3.3`).**

---

## Confirms (external validation, now citable)

- **Modular monolith as default** — Prime Video 90% cost reduction after
  collapsing to a monolith; Shopify's explicit modular-monolith choice;
  Fowler's prerequisites (rapid provisioning, monitoring, DevOps culture)
  and "successful microservice stories started with a monolith." Upgrades
  the playbook's architecture rule from assertion to cited evidence.
  `canon → 1.1`
- **Decompose by domain boundary, never by technical layer** — the
  distributed-monolith anti-pattern is the named failure of ignoring this.
  Direct input for the application/communication layer split discussion.
  `canon → 1.2`
- **Start small, scale on evidence** — Startup Genome: 74% of high-growth
  startup failures trace to premature scaling. Backs the discovery seed's
  "freq×importance works below ~500 users" stance and the manifesto's
  conservative core. `canon → 1.3`
- **AI-generated code as untrusted input** — Pearce et al.: ~40% of
  Copilot outputs in security-sensitive scenarios exploitable; ACM 2024:
  29.5% Python / 24.2% JS weaknesses in real repos; 2025 multi-LLM study:
  *no* model implemented CSRF, security headers, CORS, or MFA unprompted.
  Quadruple-sources the AI execution discipline in
  [constraints/global](../03-plan/constraints/global.md). `canon → 3.2`
- **Skill-erosion counter-practices justified** — CSET automation-bias
  analysis (Tesla/aviation/medical: verification effort decays with
  reliability), GitClear refactoring decline (25% → <10%) + 8× duplicate
  blocks. The playbook seed's Ch. 04/06 candidate is now evidence-backed.
  `canon → 3.3`
- **A11y compliance theatre** — automated scanners verify structure, not
  meaning; corroborates ux-heuristics-seed's "checkers catch 13-40%"
  from the enforcement side. `canon → 4.4`
- **Kano/RICE limits** — Kano temporal decay (delight → basic),
  stated-vs-revealed preference gap, RICE's ordinal-as-cardinal category
  error and confidence-launders-bias. Corroborates the discovery seed's
  critique and validates our *derived* (never assigned) priority rule —
  freq×importance uses observable inputs, not self-scored impact.
  `canon → 4.1, 4.2, 4.3`
- **Gates must be enforced, not aspirational** — Knight Capital: one
  unverified deploy step, $440M in 45 minutes. Backs the pre-commit
  validator, the pre-mortem-as-gate rule, and Gate-style chapter exits.
  `canon → 5.4`
- **Measurement displacement** — proxy metrics (ADRs written, checklist
  items ticked) replacing outcome metrics is the report's second
  meta-pattern; aligns with the harness-metrics thread (cost/task, rework
  rate, escaped defects — outcomes, not volume). `canon → Synthesis`

## Adds (new material per chapter)

### Ch. 00 / manifesto
- **The context-check protocol** (the report's synthesis, four steps):
  (1) what problem was this practice designed to solve, (2) is that
  problem present *here*, (3) under what conditions does the practice
  fail, (4) measure outcomes, not proxies. Candidate: manifesto section or
  Ch. 02 preamble — it is the antidote the whole report argues for.
  `canon → Synthesis`
- **Productivity expectation-setting** — METR RCT: devs predicted 24%
  faster, felt 20% faster, measured 19% *slower*; DX: 10% plateau at 92.6%
  adoption. The honest frame for the slogan: raw tool use yields ~0-10%;
  the harness/discipline *is* the differentiator. `canon → 3.1`

### Ch. 02 (the layers session — richest vein)
- **Failure-condition convention**: every recommended pattern in a layer
  file ships with its *failure condition* (the report's Claim → Evidence →
  Failure Condition structure). Maps cleanly onto ADR-002's decision-table
  row: "when does this NOT apply." Candidate convention to adopt at the
  top of the layers session. `canon → throughout`
- **Data layer ammunition**: Kleppmann's delay-sensitivity framing over
  AP/CP shorthand; NoSQL → Postgres reversals (JSONB killed most document
  use cases); unmanaged schema evolution = invisible rigidity; cache
  invalidation as first-class design concern (stampede, TTL staleness,
  origin-overwhelm); premature sharding masks real bottlenecks (query
  patterns, not node count). `canon → 1.3, 1.4, 1.5`
- **Communication layer ammunition**: distributed monolith (sync REST
  chains, shared DBs, coordinated deploys); service-mesh overhead (sidecars
  up to 90% of resources) — mesh only with platform capacity; simpler
  alternatives first (API gateway, app-level instrumentation).
  `canon → 1.2, 1.6`
- **Application layer ammunition**: explicit boundaries *inside* the
  monolith; GoF patterns are language-contextual workarounds, not
  universal insights — first-class functions collapse Visitor/Strategy/
  Command to a line. Anti-cargo-cult framing for any pattern table.
  `canon → 1.1, 5.3`
- **UX layer ammunition**: research validity limits (convenience samples,
  stated preferences, findings with no expiry); human a11y testing as a
  non-negotiable beside automated checks. `canon → 4.3, 4.4`

### Ch. 04
- **Evaluator-agent bias mitigations** — required, not optional, for
  ahead-by-k: self-preference bias (judge from a *different* model family
  than the generator), positional bias (swap order, average), multilingual
  unreliability (Kappa ~0.3), rating indeterminacy (forced-choice
  validation picks judges up to 31% worse — prefer multi-label). LLM judge
  never as sole ground truth on the criticality axis. `canon → 3.4`

### Ch. 06
- **Churn/duplication as harness metrics** — GitClear's measures (refactor
  rate, duplicate blocks, % lines surviving >1 month) are exactly the
  outcome metrics that catch AI-assisted erosion early. Candidates for the
  Langfuse/metrics thread. `canon → 3.2, 3.3`

## Challenges (where it pushes against our decisions)

1. **The book is an ADR-heavy, documentation-first methodology — the
   report attacks both.** ADR-as-ritual (GDS: only works inside normal
   rhythm; abandonment after 3-5; *no RCT evidence ADRs improve
   decisions*) and spec entropy (docs accurate at authoring, noise later).
   Our mitigations already exist — pre-mortem gate, heartbeats-box
   direction, DEBT-LEDGER staleness, `updated` frontmatter — but the book
   should *say honestly* that ADR value is asserted, not proven, and bind
   ADR writing to decision time (a decision without a contemporaneous ADR
   doesn't exist). Verdict: keep the spine, add the heartbeat + honesty.
   `canon → 2.1, 2.3`
2. **BDUF critique vs design-first workflow.** Requirements drift,
   designers can't foresee without implementation feedback, committee
   capitulation. Our design-first is *bounded* (exploration-execution
   loops, ≤20-node diagrams, decision tables), and the reversibility ADR
   field is the precise mitigation: irreversible decisions earn design
   effort, reversible ones get defaults and move on. This needs to be
   *stated* in the Ch. 02 intro, or the book reads as BDUF to a hostile
   reviewer. `canon → 2.2`
3. **LLM-as-judge biases vs WhiteBoxMAKER ahead-by-k.** The mechanism's
   validity depends on mitigations the system docs don't yet specify
   (family separation, position swapping, multi-label). Without them,
   k-margins can be artifacts of judge bias, not solution quality.
   Verdict: amend dimension 8 / evaluator spec in Ch. 04. `canon → 3.4`
4. **Cargo-cult and survivorship bias apply to *our own seeds*.** The
   system-design seed derives from successful repos; the company framework
   from one company's context; engineering blogs are survivor-filtered
   (Prime Video published only because Amazon could afford to). The book
   must teach pattern adoption *with* context verification — and its own
   provenance discipline (`source → section` markers) should carry a
   confidence/context note. `canon → 5.1, 5.2`
5. **"Top 1% AI-assisted" slogan vs the productivity paradox.** Even
   experts mispredict AI gains by ~40 points. The slogan survives only
   with the harness-as-differentiator framing made explicit (Ch. 00) —
   otherwise it's the inflated belief the METR data debunks.
   `canon → 3.1`

## Immediate action candidates

1. **02-design session:** adopt the failure-condition convention for layer
   files; use the per-layer ammunition above as primary content input.
2. **Ch. 02 intro:** one paragraph positioning bounded design-first against
   BDUF (reversibility field as the mechanism).
3. **Ch. 04 backlog:** evaluator-agent bias mitigations (family
   separation, position swap, multi-label, never-sole-judge).
4. **Manifesto/Ch. 00 backlog:** context-check protocol + productivity
   expectation-setting paragraph.
5. **ADR practice rule:** ADRs written at decision time, heartbeat
   cadence; state the evidence honesty note.
