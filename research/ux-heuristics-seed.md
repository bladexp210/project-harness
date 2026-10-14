---
title: "Seed: UX/UI decision heuristics"
status: reference
date: 2026-06-10
tags: [research, seed, provenance]
---

# Seed: UX/UI decision heuristics

Distilled from the Perplexity report in `_inbox/UX & UI Design Decision
Heuristics  An Evidence-Based Guide for AI-Assisted Software
Development.md`. Everything is reworded; provenance is "report → section",
keeping the report's primary-source links where they matter. Items marked
**[DECISION-TABLE CANDIDATE]** carry hard thresholds and should become
markdown decision tables in the book.

## Ch. 02 — ux layer

**Nielsen's 10 heuristics as a review checklist.** Run every interface
past the ten classics; 3–5 expert evaluators surface roughly 40–75% of
usability problems without recruiting users. Does NOT catch
domain-specific mental-model mismatches (needs contextual inquiry);
minimalism means removing the irrelevant, not needed complexity.
Evidence: https://www.nngroup.com/articles/ten-usability-heuristics/
Provenance: report → 1.1.

**Norman's six principles as a diagnostic.** Trace any interaction
failure to visibility, feedback, affordance, mapping, constraints, or
consistency — an unclicked button is a visibility problem, a silent form
a feedback problem. Less clean in complex dashboards with learned
patterns. Evidence: Norman, *The Design of Everyday Things* (1988);
https://www.heurio.co/don-norman-principles-of-design
Provenance: report → 1.2.

**WCAG 2.1 AA as the accessibility floor.** Hit Level AA: 4.5:1 contrast
for normal text, 3:1 for large, full keyboard operability, consistent
navigation, text-based error identification, no flashing over 3x/second.
AA is what regulations (ADA, EN 301 549, Section 508) reference. AAA is
not universally achievable; compliance is not usability.
**[DECISION-TABLE CANDIDATE: contrast ratios, flash limits.]** Evidence:
https://www.w3.org/TR/WCAG21/ — Provenance: report → 1.3.

**Fitts's Law and touch targets.** Acquisition time grows with distance
and shrinks with target size: make important targets big and near.
Floors: iOS 44×44pt, Material 48×48dp, WCAG 2.2 24×24 CSS px (fine
pointer) / 48×48 (touch). Does NOT apply to slow deliberate movement or
scroll/read interactions; screen space is zero-sum, so prioritize (big
primary CTAs, smaller farther destructive actions). **[DECISION-TABLE
CANDIDATE: target size minimums per platform.]** Evidence: Fitts 1954;
https://www.nngroup.com/articles/touch-target-size/
Provenance: report → 1.4.

**Hick's Law: fewer options per decision point.** Decision time grows
logarithmically with equally likely choices; keep 1–5 differentiated
options where speed matters, categorize or disclose larger sets. Does
NOT apply to complex deliberative choices, strong-intent users (they
scan), or long lists (recognition, not decision). Never justifies deep
navigation — depth compounds decisions. **[DECISION-TABLE CANDIDATE:
1–5 option threshold.]** Evidence: Hick 1952, Iyengar & Lepper 2000;
https://lawsofux.com/hicks-law/ — Provenance: report → 1.5.

**Chunk, but don't worship 7±2.** Group related information into
meaningful clusters; that is the real rule. The "7±2 menu items" reading
of Miller is a myth — visible screen items are recognition, not recall.
Chunk what users must memorize; never cap navigation with it. Critique:
https://stephaniewalter.design/blog/your-menu-doesnt-need-millers-7-plus-minus-2-rule/
Provenance: report → 1.6.

**Adopt vs. build a design system.** Small team, first product, no
dedicated owner → adopt an existing library (Material UI, Radix, Chakra,
shadcn/ui). Strong brand needs → existing library customized via tokens.
Multi-product, multi-team, cross-platform → custom pays back. Without a
named owner, bespoke systems decay. **[DECISION-TABLE CANDIDATE: the
report's condition → approach table.]** Provenance: report → 2.1.

**Design tokens from the first sprint.** Abstract color, spacing, type,
shadow, and motion into named tokens shared by Figma and code;
retrofitting costs 3–5× upfront implementation. NOT for tiny single-page
tools; tokens without naming governance create confusion. Evidence: Brad
Frost, https://bradfrost.com/blog/post/extending-atomic-design/
Provenance: report → 2.2.

**Three layers of consistency.** Visual (same token values), functional
(same pattern for the same action class, e.g. all destructive actions
confirm), and external (platform conventions users import from other
apps). Break only with measured evidence of harm AND universal
application of the replacement. Provenance: report → 2.3.

**Latency perception thresholds.** ≤100ms feels instant (no indicator);
~1s is noticed but doesn't break flow (subtle state change, no spinner);
10s is the attention limit (progress indicator with estimate mandatory —
users abandon or double-submit). NOT for non-blocking background work.
**[DECISION-TABLE CANDIDATE: 0.1s/1s/10s table.]** Evidence: Nielsen;
https://www.nngroup.com/articles/response-times-3-important-limits/
Provenance: report → 3.1.

**Loading pattern selection.** Under 1s: nothing (avoid flicker). 1–10s
full page/section: skeleton screen matching final layout (wave animation
reads fastest; bare frames read as broken); single module: spinner. Over
10s or any file operation: progress bar with estimate. Skeletons do NOT
belong on server-rendered pages or unknown output structure.
**[DECISION-TABLE CANDIDATE: duration × content → pattern.]** Evidence:
https://www.nngroup.com/articles/skeleton-screens/ — report → 3.2.

**Empty, error, and offline states.** An empty state is onboarding:
explain why it's empty, offer the filling action, distinguish "never had
data" from "filter returned nothing". Errors: explicit, human-readable,
actionable, non-blaming — no tooltips, no modals for inline validation,
no summary-only display; translate technical codes. Offline is a state,
not an error: indicate connectivity passively, queue actions for sync,
distinguish "offline" from "server unavailable". Evidence: NN/g;
https://www.nngroup.com/articles/errors-forms-design-guidelines/
Provenance: report → 3.3, 3.4, 3.6.

**Optimistic UI.** Update before server confirmation when backend
success exceeds ~95%, the action is reversible, and latency is
perceptible (>200ms) on a frequent action — with rollback as easy as the
original action. NOT for financial/medical/irreversible operations,
frequently-failing validation, or step-dependent workflows.
**[DECISION-TABLE CANDIDATE: 95% success / 200ms thresholds.]**
Provenance: report → 3.5.

**Breadth over depth in navigation.** Seven top-level categories beat
three nested three deep: depth forces users to hold a hierarchy model.
Cap at 2–3 levels; a needed 4th usually means the IA mirrors the org
chart, not user thinking. Navigation fails on weak "information scent".
Evidence: Pirolli & Card;
https://www.nngroup.com/articles/information-scent/ — report → 4.1.

**Progressive disclosure.** Show only what the current step needs; defer
advanced features behind one action when fewer than ~20–30% of users
need them in the primary flow. NOT when hidden information is needed
alongside visible information, nor for navigation (prefer flat,
well-labeled nav). **[DECISION-TABLE CANDIDATE: ~30% threshold.]**
Evidence: NN/g; https://www.nngroup.com/articles/progressive-disclosure/
Provenance: report → 4.2.

**Form design rules.** Single column; validate on blur, not keystroke;
errors inline below the field; never red alone — pair with an icon (a
WCAG AA requirement); prevent errors with masks, pickers, constrained
inputs; success indicators only where they carry signal. Exceptions: 1–2
field forms can be multi-column; keystroke validation suits
password-strength meters. Evidence: NN/g;
https://www.nngroup.com/articles/errors-forms-design-guidelines/
Provenance: report → 4.3.

## Ch. 01 — Understand (user research and validation)

**The 5-user rule, correctly scoped.** Five users uncover ~85% of
usability problems — for qualitative, single-audience testing only. It
answers "what is broken and why", never completion rates or satisfaction
(quantitative work needs 40+ participants). Run rounds per persona;
prefer 3 rounds of 5 with fixes between over one batch of 15.
**[DECISION-TABLE CANDIDATE: 5 vs. 40 users; qual vs. quant.]**
Evidence: Nielsen & Landauer 1993;
https://www.nngroup.com/articles/5-test-users-qual-quant/
Provenance: report → 6.1.

**A/B vs. qualitative.** A/B tests measure direction and magnitude on a
KPI but cannot explain why; qualitative testing generates the hypotheses
A/B then measures. A/B needs ~1,000+ users per variant; it fails on
low-traffic products and small segments (e.g. screen-reader users).
**[DECISION-TABLE CANDIDATE: question type → method.]** Evidence:
https://www.nngroup.com/articles/ab-testing/ — Provenance: report → 6.2.

**Card sorting and tree testing for IA validation.** Card sorts expose
users' mental categories; tree testing audits an existing hierarchy via
task success without visual cues. Evidence:
https://www.nngroup.com/articles/card-sorting-definition/
Provenance: report → 4.1.

**Accessibility audits: automate, then verify by hand.** In a 2021 UK
government study the best automated tool caught only 40% of seeded
barriers; the worst, 13%. Use automated tools (axe, WAVE) first-pass,
plus one manual round with assistive-tech users per major release — only
humans can judge whether alt text is accurate. **[DECISION-TABLE
CANDIDATE: 13–40% detection figures.]** Provenance: report → 1.3, 6.3.

## Ch. 05 — Build (AI-product UX)

**Probabilistic outputs need different visual treatment.** AI breaks the
deterministic assumption behind Norman/Nielsen. Never style probabilistic
output with the same visual confidence as verified content — users
over-trust early, then collapse to under-trust after the first failure.
Provenance: report → 5.1.

**Ask "should this be AI?" first.** AI fits repetitive tasks beyond
human throughput or pattern recognition beyond human capacity; NOT
anywhere a deterministic rule suffices. Users form a mental model of the
AI in 2–3 interactions and miscalibration cascades — set expectations
before first use, calibrate trust to actual accuracy (confidence
signals, source attribution, transparent failures), build visible
correction loops. Evidence: Google PAIR;
https://pair.withgoogle.com/guidebook/ — Provenance: report → 5.2.

**Microsoft HAX guidelines.** Eighteen guidelines validated in a 2019
CHI study; the two game-changers: make clear what the system CAN do, and
how WELL it does it. Also: make AI errors as cheap to fix as the
original action, scope responses when uncertain, explain on demand,
never change behavior silently. Evidence: Amershi et al., CHI 2019;
https://www.microsoft.com/en-us/haxtoolkit/ — Provenance: report → 5.3.

**Apple HIG on ML, plus confidence display.** Always provide a reachable
path to override or disable AI behavior. Show confidence explicitly in
medical/legal/financial/safety contexts and wherever output is acted on
unverified; prefer visual cues and source attribution over raw
percentages; progressive-disclose the "why". Avoid uncalibrated
percentages (a flat "82%" on everything destroys the signal) and visual
parity between AI and human-verified content. Evidence:
https://developer.apple.com/design/Human-Interface-Guidelines/machine-learning
— Provenance: report → 5.4, 5.5.

**Human-in-the-loop by stakes × reversibility.** Low + reversible:
automate, optimistic UI, quiet undo. Medium + reversible:
micro-confirmation. High + low reversibility: review queue before the AI
acts. High + irreversible: no AI autonomy. Queues over ~60 seconds per
item get skipped. Always offer a fast "talk to a human" escape hatch —
its absence costs trust in the whole product. **[DECISION-TABLE
CANDIDATE: stakes × reversibility → pattern; 60s limit.]**
Provenance: report → 5.6.

**AI onboarding: result first, explanation second.** Lead with a
compelling output on the most common high-quality use case; the first AI
output sets the trust baseline for the whole product. Provenance:
report → 5.7.

## Cross-cutting

Every heuristic in the report resolves a named trade-off (speed vs.
depth, consistency vs. novelty, load vs. discoverability). The book's
layer files should state the trade-off each rule resolves, not just the
rule; the report's Part VII quick-reference table is a model for the
book's decision-table format. Provenance: report → 7.

## Red-team material

Criticisms the report preserves, kept intact. Miller's 7±2: Miller
disowned the number ("allegory", "pernicious, Pythagorean coincidence"),
Cowan (2001) revised working memory to ~4, and capping menus with it
hurts experts (report → 1.6). A 2024 critique says the 5-user rule "was
never a rule for qualitative research" as a guaranteed floor — discovery
rates vary widely with task scope
(https://saeidehbakhshi.substack.com/p/the-five-user-rule-was-never-a-rule;
report → 6.1). Heuristic evaluation finds only what experts already know
to look for (1.1). Hick's Law is misapplied to long lists and to justify
deep hierarchies it argues against (1.5). Pie menus win on Fitts's math
but lose on familiarity (1.4). Minimalism is misused to strip needed
content (1.1). Compliance is not usability; automated checkers catch as
little as 13% of real barriers, and W3C concedes WCAG 3.0 must become
technology-agnostic (1.3, 6.3).
