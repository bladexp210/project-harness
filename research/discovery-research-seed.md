---
title: "Seed: requirements discovery and early user research"
status: reference
date: 2026-06-10
tags: [research, seed, provenance]
---

# Requirements discovery and early user research — distilled seed

Source: `_inbox/Evidence-Based Requirements Discovery & Early User
Research.md` (Perplexity research report, imported 2026-06-10). Everything
below is reworded; provenance is given as "report → section". Primary-source
links are kept where the report supplied them. The report's framing: the
costliest failure is building the wrong thing precisely, because teams swap
discovery for assumption and then listen to the wrong signals (report →
Executive Summary).

## Ch. 01 — Understand: discovery frameworks

**Jobs-to-Be-Done (JTBD).** Ask what progress a person is trying to make
when they "hire" a product, rather than what features they want. Two schools:
Christensen/Moesta's narrative version (functional, social, emotional job
dimensions; good for switch/churn analysis) and Ulwick's quantitative
Outcome-Driven Innovation (jobs decomposed into measurable desired outcomes;
good for finding under-served segments). Do NOT use it as a substitute for
interaction design or workflow analysis — it explains why, not how — and it
degrades in B2B multi-stakeholder purchases where buyer's job and user's job
diverge; over-applied it yields requirements too abstract to build against.
Origin: Christensen/Moesta, *Competing Against Luck*
(https://www.christenseninstitute.org/theory/jobs-to-be-done/); Ulwick,
*What Customers Want* (https://strategyn.com/jobs-to-be-done/). Provenance:
report → Part 1.1.

**Personas.** Narrative stand-ins for user segments (name, goals, pains)
that build team empathy and block the "designing for yourself" trap. Do NOT
use them before interviews exist (assumption personas encode founder bias as
fake evidence), with demographic-heavy content, or in quantity — more than
4–5 primaries signals over-segmentation. They also systematically exclude
edge-case users (disabilities, linguistic minorities). Origin: Cooper, *The
Inmates Are Running the Asylum* (1999). The report cites a Forrester finding
of ~4x ROI for persona-using teams, and Tomer Sharon's finding that 86% of
PMs sourced ideas from personal pain vs 2% from user research. Provenance:
report → Part 1.2.

**User role modeling.** A user role is a relationship between a person and a
system — goals, permissions, interaction patterns — not a fictional
biography. Stronger than personas for requirements engineering,
authorization design, and B2B/enterprise; it naturally surfaces forgotten
operational roles. Do NOT lean on it for consumer apps where emotion and
social signaling drive adoption. Practitioner consensus: use roles as the
functional skeleton, personas on top for empathy. Origin: Constantine &
Lockwood, *Software for Use* (1999). The report's personas-vs-roles
comparison table is a decision-table candidate. Provenance: report →
Part 1.3.

**User story mapping.** Arrange stories spatially: the user's journey as a
horizontal backbone, increasing detail vertically. Makes a true "minimum"
visible for MVP scoping and exposes workflow gaps. Do NOT use it for
non-sequential products (dashboards, analytics, API-first) where the
journey metaphor distorts, and remember it never explains *why* users take
each step — that needs interviews. Origin: Patton, *User Story Mapping*
(O'Reilly 2014; https://jpattonassociates.com/story-mapping/). Provenance:
report → Part 1.4.

**Impact mapping.** A four-level map — Why (measurable business goal) → Who
(actors) → How (behavior change) → What (deliverables) — that forces
outcome-first thinking and makes behavioral assumptions explicit. Do NOT run
it without a crisp measurable goal: it collapses into a feature brainstorm
shaped like a tree. It also gives no workflow or implementation detail.
Origin: Adzic, *Impact Mapping* (2012;
https://gojko.net/books/impact-mapping/). Provenance: report → Part 1.5.

**Event storming.** Wall-of-stickies workshop mapping past-tense domain
events ("Order Placed", "Payment Failed"), then actors, commands, policies.
The strongest tool for domain discovery and for catching linguistic splits
(sales' "deal" = engineering's "order" = support's "case"). Do NOT use it
for simple CRUD products (overkill), without a skilled facilitator, or as a
motivation tool — it maps structure, not why users care. Big Picture
sessions cost 1–2 days. Origin: Brandolini
(https://www.eventstorming.com). Provenance: report → Part 1.6.

## Ch. 01 — Understand: validation before building

**The Mom Test.** Interview rules that prevent false positives: talk about
their life, not your idea; ask about specific past events, never
hypotheticals; talk less. Do NOT apply it past problem discovery — it
deliberately excludes solution-testing, so teams using it throughout the
lifecycle under-test solution fit. Origin: Fitzpatrick, *The Mom Test*
(2013; https://www.momtestbook.com). Provenance: report → Part 3.1.

**Commitment signal hierarchy (decision-table candidate, has weights).**
Fitzpatrick ranks evidence: "that's interesting" ≈ zero; "I'd definitely
use that" = weak; a stated price = moderate; a pre-order or deposit =
strong; an existing manual workaround = very strong; begging for early
access = strongest. Provenance: report → Part 3.1.

**Problem vs. solution interviews.** Blank's two-phase split: first validate
the problem is real, frequent, and costly (anchor on "when did this last
happen, what did it cost, how do you solve it today"), and only then show a
prototype. Do NOT mix the phases — pitching during problem interviews
teaches you only that people are polite. Origin: Blank, *The Four Steps to
the Epiphany* (2005; https://steveblank.com). Provenance: report → Part 3.2.

**Smoke tests.** Validate demand before engineering: landing page + email
capture (Dropbox's 2007 video drove 75,000 signups pre-product), fake-door
buttons, pre-orders, Concierge MVP (deliver the service manually), Wizard of
Oz. Do NOT over-read a landing page: it measures interest in your headline,
confounded by copy and traffic source; it says nothing about usability or
feasibility. The report's cost-vs-signal-strength table (interview = medium
signal, survey = low, landing page = medium-high, pre-order = high,
concierge = very high) is a decision-table candidate. Provenance: report →
Part 3.3.

## Ch. 01 — Understand: forgotten user roles

Three roles interviews never volunteer (report → Part 6): the **operator**
who deploys and configures the product and wants auditability, permissions,
and an API — interview the deployer, not just the user; the **support
agent** who sees the system under failure and needs case lookup,
act-on-behalf, and audit trails; and the **data-deletion requester** —
GDPR Art. 17 gives every user an erasure right with a one-month SLA and
fines up to EUR 20M or 4% of global turnover
(https://gdpr-info.eu/art-17-gdpr/). Users never raise this in interviews
because they don't know the right exists until they need it. Apple's 2022
account-deletion mandate shows regulators turning NFRs into product
features. Mature teams write compliance, accessibility, and operability as
user stories with actors and verifiable outcomes (Oxford UX NFR spec:
https://staff.admin.ox.ac.uk/ux/procurement/non-functional-requirements).
Provenance: report → Parts 6.1–6.4.

## Ch. 03 — Plan: prioritization methods

The report's meta-finding: prioritization frameworks are worth more as
communication tools than as calculators — the numbers are rarely reliable,
the conversation they force is (report → Part 2 intro).

**RICE** = (Reach × Impact × Confidence) / Effort, from Intercom
(https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/).
Impact on a 0.25–3 scale, Confidence at 50/80/100%. Do NOT use it under
~1,000 users (Reach can't differentiate — "intuition with paperwork"),
without an analytics source of truth for Reach (gaming), or to compare
unlike units (retention vs acquisition reach). Provenance: report → 2.1.

**MoSCoW** (Clegg 1994, DSDM): Must/Should/Could/Won't, built for time-boxed
fixed-deadline delivery. Do NOT use it for continuous product development;
expect Must-have inflation (teams ending up 80% Must) and Won't items
re-entering under new names. Provenance: report → 2.2.

**Kano** (Kano 1984): features split into Basic (absence enrages, presence
unnoticed), Performance (linear more-is-better), and Attractive (delighters)
— plus a often-omitted Reverse category. Do NOT use it pre-product-market
fit (needs roughly N > 30 per segment) or treat results as durable:
Attractive features decay into Basic over time. Link:
https://www.ifm.eng.cam.ac.uk/research/dmg/tools-and-techniques/kano-model/.
Provenance: report → 2.3.

**WSJF** = Cost of Delay / Job Duration (Reinertsen 2009 via SAFe;
https://framework.scaledagile.com/wsjf). Do NOT use it on small teams or in
early discovery — it's built for sequencing across multiple dependent
teams; expect denominator gaming and hand-wavy Cost of Delay. Provenance:
report → 2.4.

**Framework decision reference (decision-table candidate).** The report's
appendix maps situations to methods, e.g. "don't know the problem → JTBD +
Mom Test, avoid personas"; "pre-seed, first 20 interviews → Mom Test +
frequency × importance, avoid all numerical frameworks"; "fixed deadline →
MoSCoW, avoid WSJF". Worth converting wholesale into a Ch. 03 table.
Provenance: report → Appendix.

## Bearing on our frequency × importance choice

Our Ch. 01 template scores priority = frequency (Daily/Weekly/Rarely =
3/2/1) × importance (Critical/High/Medium/Low = 4/3/2/1). The report bears
on this directly (report → 2.5, 2.3, 2.1):

**Supports.** NN/g rates frequency-importance matrices among the most
effective lightweight tools for small teams precisely because they work
from interview data without numeric scores
(https://www.nngroup.com/articles/prioritization-methods/). Practitioner
consensus (Patton, Torres, Fitzpatrick): below ~500 users, frequency ×
importance on qualitative data beats RICE/WSJF false precision. Our context
(early, interview-driven) is exactly where the report says this tool wins.

**Challenges.**
- *Kano non-linearity:* satisfaction is not linear in any score. Basic
  features are invisible in interviews (users assume them), so they arrive
  with low observed frequency and get underrated by our formula; and the
  matrix has no slot for Attractive/delighter features at all.
- *Rare-but-critical events:* a "Rarely × Critical" item scores 1 × 4 = 4,
  below "Daily × Medium" at 3 × 2 = 6 — yet GDPR deletion or safety
  requirements must work regardless of score. We need a non-negotiable
  override lane (MoSCoW-style "Must") outside the multiplication.
- *Frequency capture:* loud minority segments inflate frequency. A
  high-frequency bug hitting 2% of power users can outscore a moderate
  problem hitting 80%. Our frequency axis measures per-user encounter rate,
  not reach — RICE's separate Reach and Confidence dimensions exist exactly
  to fix this. Worth adding at least an informal reach check.
- *Note our scale ordering:* the report's NN/g version is a 2×2 from
  interview data; our derived 3×4 numeric product re-introduces a little of
  the false precision the report warns about. Keep the numbers as a tie
  breaker, not an oracle.

## Ch. 04/05 — AI in discovery

**LLM interview synthesis (Torres,
https://www.producttalk.org/customer-interview-analysis-ai/).** Helps:
transcription, second-opinion synthesis after you've done your own, metadata
tagging for cross-interview search. Hurts: dumping all transcripts into one
prompt skips per-interview synthesis and kills empathy; Torres measured
~30% fabricated or wrong direct quotes from ChatGPT summaries; training-data
bias overrides your actual population; outsourcing synthesis atrophies the
very expertise needed to audit AI output. Recommended flow: synthesize each
interview yourself first, then run AI as one voice among several, never
ground truth. Provenance: report → 5.1.

**Synthetic users.** NN/g's 2024 evaluation
(https://www.nngroup.com/articles/synthetic-users/) found sycophancy
(idealized self-reports vs real users' messy dropouts), shallow
everything-is-important answers, modeling of hypothetical rather than
actual behavior, and unreliability for niche populations outside the
English/Western/affluent training skew. Valid use is desk research only:
domain familiarization, hypothesis generation, piloting interview guides —
never a replacement for real users. A 2026 ACM CHI paper grounds agents in
real interviews (https://dl.acm.org/doi/10.1145/3772318.3791918) but is
early-stage. Provenance: report → 5.2.

**AI competitive analysis.** Useful to map landscapes and feature
categories at scale; validate claims against primary sources, don't ask it
to predict competitor strategy or finances (stale data), and explicitly
prompt for disconfirming evidence. Provenance: report → 5.3.

## Red-team material

Failure modes to attack our own process with (report → Parts 4, 1–3, 5):
- **Confirmation bias** (NN/g,
  https://www.nngroup.com/articles/confirmation-bias-ux/): leading
  questions, selective synthesis, stopping at "enough" supporting evidence.
  Remedy: require interviewers to document disconfirming evidence.
- **HiPPO / loudest-user capture** (Kaushik): executive opinion or
  articulate power users displace the median user. Remedy: split what users
  say from what behavioral data shows; sample median users deliberately.
- **Feature request laundering:** "I need CSV export" recorded and built
  verbatim, with no why. Requests are problem signals, not specifications.
  Variant: backlog hoarding as fake product-market-fit evidence.
- **Over-segmentation:** too many personas → mediocre for everyone; small
  samples → N=1 personas; big samples → vivid outliers. Heuristic: 1–2
  primary roles max pre-product-market fit.
- **Method-specific traps:** assumption personas cited as evidence; story
  maps forced onto non-linear products; impact maps without a measurable
  Why; Must-have inflation in MoSCoW; Reach gaming and false precision
  (47.2 vs 44.8) in RICE; WSJF denominator gaming; stale Kano categories;
  smoke tests read as product validation; AI-fabricated quotes (~30%) and
  sycophantic synthetic users taken as research.
