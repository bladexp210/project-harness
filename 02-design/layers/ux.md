---
title: UX Layer
chapter: 02
status: template
audience: [novice, seasoned, both]
tags: [design, layer, ux]
---

# UX Layer — how humans experience the software

## What this is

> [!TEACH] Teach
> The UX layer decides what using your software feels like: how fast it
> responds, who can physically operate it, how choices are presented, and —
> new since the classics were written — how AI behavior is communicated.
> It is designed per [[../01-understand/user-roles|user role]]: the roles and
> their contexts ("on a phone, mid-commute") are this layer's real inputs.
>
> One framing carries the whole file: **every UX heuristic resolves a named
> trade-off** — speed vs. depth, consistency vs. novelty, density vs.
> discoverability (`ux-heuristics-seed → cross-cutting`). The tables below
> state the trade-off and the failure condition, per
> [[ADR-005-failure-condition-convention|ADR-005]]; numbers are floors and
> thresholds you can test against, not vibes.

## Why it matters

> [!TEACH] Teach
> The other three layers are invisible when they work. This one *is* the
> product as far as users are concerned — and it is where evidence-free
> folklore ("7±2 menu items!") does the most quiet damage. The seeds for
> this file carry their own criticism sections; the failure conditions
> below preserve them.

## Decision 1 — Latency budgets

> [!TEACH] Teach
> The physics first, because it makes the budget non-negotiable: memory
> ~100 ns, SSD ~100 µs, datacenter round-trip ~500 µs, disk seek ~10 ms,
> transcontinental round-trip ~150 ms. Every ocean-crossing call your UI
> waits on spends 150 ms of the budget (`system-design-seed → latency
> numbers`). The perception thresholds the budget serves
> (`ux-heuristics-seed → 3.1, 3.2`):

| Wait | User perception | What to show | When NOT to apply |
| :---- | :---- | :---- | :---- |
| ≤ 100 ms | Instant | Nothing | — |
| ≤ 1 s | Noticed, flow intact | Subtle state change; no spinner (flicker reads as breakage) | — |
| 1–10 s | Patience draining | Skeleton screen for page/section loads; spinner for a single module | Skeletons on server-rendered pages or unknown output shapes |
| > 10 s | Attention gone | Progress bar with estimate — users abandon or double-submit without one | Non-blocking background work — don't make people watch it |

> [!TEACH] Teach
> Two levers from the other layers: **optimistic UI** — update before the
> server confirms when success rate exceeds ~95%, the action is reversible,
> and the latency is perceptible on a frequent action; **never** for
> financial, medical, or irreversible operations
> (`ux-heuristics-seed → 3.5`). And **consistency level as a UX choice** —
> users must see their own write (strong for "my profile"), but feeds can
> be eventual; pick per surface, decide in the [[data]] layer
> (`system-design-seed → consistency patterns`).

## Decision 2 — Accessibility, decided now

> [!TEACH] Teach
> **Claim:** WCAG 2.1 AA at design time, not retrofit. **Evidence:** AA is
> the level regulations reference (ADA, EN 301 549, Section 508); retrofits
> cost multiples (`ux-heuristics-seed → 1.3`;
> `company-framework-seed → accessibility`). The floors:

| Check | Floor |
| :---- | :---- |
| Contrast, normal text | 4.5:1 |
| Contrast, large text | 3:1 |
| Keyboard | Every critical flow fully operable, no pointer |
| Touch targets | 44×44 pt (iOS) / 48×48 dp (Material) / WCAG 2.2: 24 px fine pointer, 48 px touch |
| Errors | Identified in text — never color alone; pair red with an icon |
| Flashing | Nothing over 3×/second |

> [!TEACH] Teach
> Fitts's Law backs the target floors: acquisition time grows with distance
> and shrinks with size — big, near primary actions; smaller, farther
> destructive ones. Screen space is zero-sum; the floors force the
> prioritization (`ux-heuristics-seed → 1.4`).
>
> **Failure condition — compliance theatre:** automated checkers catch only
> a fraction of real barriers, and compliance is not usability. Automated
> checks gate commits; a human using a keyboard and a screen reader tests
> the critical flows before ship (`red-team-seed → a11y`). Use accessible
> component libraries rather than inventing primitives — and define every
> component's states up front: default, hover, focus, disabled, loading,
> error (`company-framework-seed`).

## Decision 3 — Design system: adopt or build?

| Your situation | Approach | When NOT to apply |
| :---- | :---- | :---- |
| Small team, first product, no dedicated owner | Adopt a library (Radix, Material UI, shadcn/ui, Chakra) | — this is the book's default |
| Strong brand requirements | Adopt + customize via design tokens | Brand needs are one logo and a color — just theme it |
| Multi-product, multi-team, cross-platform | Custom system pays back | No named owner — bespoke systems decay without one |

> [!TEACH] Teach
> `ux-heuristics-seed → 2.1`
>
> **Design tokens from the first sprint** — named color/spacing/type/motion
> values shared by design tool and code; retrofitting costs 3–5× upfront.
> **Failure condition:** a tiny single-page tool (tokens are ceremony), or
> tokens without naming governance (confusion with extra steps)
> (`ux-heuristics-seed → 2.2`). Hold three consistencies, in order of
> visibility: visual (same token values), functional (same pattern for the
> same action class — all destructive actions confirm), external (platform
> conventions users import from other apps). Break one only with measured
> evidence of harm and a universally applied replacement
> (`ux-heuristics-seed → 2.3`).

## Decision 4 — Structure: choices, depth, forms, states

> [!TEACH] Teach
> - **Hick's Law, bounded:** decision time grows with equally likely
>   options — keep 1–5 differentiated choices where speed matters; group or
>   disclose larger sets. **When NOT to apply:** deliberative decisions,
>   strong-intent users (they scan), long lists (recognition, not
>   decision); and it *never* justifies deep navigation — depth compounds
>   decisions (`ux-heuristics-seed → 1.5`).
> - **Breadth beats depth:** seven top-level categories beat three levels
>   of three. Cap navigation at 2–3 levels; a needed fourth usually means
>   the structure mirrors your org chart, not user thinking
>   (`ux-heuristics-seed → 4.1`).
> - **The 7±2 myth, retired:** Miller disowned the number; working memory
>   is closer to 4 (Cowan 2001). Chunk what users must *memorize*; never
>   cap visible navigation with it — screens are recognition
>   (`ux-heuristics-seed → 1.6`).
> - **Progressive disclosure** when under ~20–30% of users need a feature
>   in the primary flow — one action away, not buried. **When NOT:** hidden
>   info needed *alongside* visible info, or navigation (keep nav flat and
>   labeled) (`ux-heuristics-seed → 4.2`).
> - **Forms:** single column; validate on blur, not per keystroke
>   (exception: password-strength meters); errors inline below the field,
>   human-readable, non-blaming; prevent errors with pickers, masks,
>   constrained inputs (`ux-heuristics-seed → 4.3`).
> - **Empty, error, offline are designed states, not accidents.** An empty
>   state is onboarding: say why it's empty, offer the filling action,
>   distinguish "no data yet" from "filter matched nothing". Offline is a
>   state, not an error: indicate passively, queue actions for sync,
>   distinguish "you're offline" from "server down"
>   (`ux-heuristics-seed → 3.3–3.6`).
>
> For review, two checklists earn their keep — use before ship or after major UI
> changes:

| Checklist | Pass when | Failure condition |
| :---- | :---- | :---- |
| **Nielsen 10 heuristics** | 3–5 expert reviewers; ~40–75% of usability issues surfaced without users | Domain mental-model gaps — needs contextual inquiry |
| **Norman six principles** | Every interaction failure mapped to visibility, feedback, affordance, mapping, constraint, or consistency | Complex dashboards with learned patterns only |

> [!TEACH] Teach
> Nielsen's 10 and Norman's six are the diagnostic vocabulary — an unclicked
> button is a *visibility* problem, a silent form a *feedback* problem.
> **Failure condition:** expert review only finds what experts know to look
> for; it does not catch domain mental-model mismatches — that takes
> watching real users (`ux-heuristics-seed → 1.1, 1.2`).

## Decision 5 — AI in the product

> [!TEACH] Teach
> AI output breaks the deterministic assumption behind every rule above,
> so it gets its own discipline (`ux-heuristics-seed → 5.x`, drawing on
> Google PAIR, Microsoft HAX, Apple HIG):
>
> - **First: should this be AI?** AI fits repetition beyond human
>   throughput or pattern recognition beyond human capacity. **When NOT:**
>   anywhere a deterministic rule suffices — users form their mental model
>   of your AI in 2–3 interactions, and miscalibration cascades.
> - **Set expectations before first use:** make clear what the system can
>   do and *how well* — the two HAX guidelines with the strongest
>   validation. Lead onboarding with a strong result on the most common
>   high-quality use case; the first output sets the trust baseline.
> - **Never style probabilistic output with the visual confidence of
>   verified content.** Users over-trust early, then collapse to
>   under-trust at the first failure. Show confidence where output is
>   acted on unverified — visual cues and source attribution over raw
>   percentages (an uncalibrated "82%" on everything destroys the signal).
> - **Always provide override:** a reachable path to correct, undo, or
>   disable AI behavior; never change behavior silently. Make AI errors as
>   cheap to fix as the original action.
>
> How much autonomy, by stakes × reversibility
> (`ux-heuristics-seed → 5.6`):

| Stakes | Reversible? | Pattern | When NOT to apply |
| :---- | :---- | :---- | :---- |
| Low | Yes | Automate; optimistic UI; quiet undo | — |
| Medium | Yes | Act + micro-confirmation | Confirmations so frequent they train blind clicking |
| High | Partly | Review queue *before* the AI acts | Queue items averaging > ~60 s — reviewers start rubber-stamping |
| High | No | No AI autonomy | — |

> [!TEACH] Teach
> Always offer a fast "talk to a human" escape hatch; its absence costs
> trust in the whole product, not just the AI feature.

## A caveat on all of the above

> [!TEACH] Teach
> The evidence base behind UX research has limits the other layers' sources
> don't: convenience samples, stated preferences instead of behavior, and
> findings that never expire ("the 5-user rule" was never a guaranteed
> floor — discovery rates vary widely with task scope)
> (`red-team-seed → ux ammunition`; `ux-heuristics-seed → red-team`).
> Treat every rule here as a strong prior, and your own users — watched,
> not surveyed — as the data that updates it.

> [!NOTE] Ask your AI agent
> "Here are my user roles with their contexts, and my must-have use
> cases. For each role: propose a latency budget per key screen, the
> WCAG-relevant constraints from their context, and where the
> stakes × reversibility table forbids AI autonomy. Challenge me where my
> use cases imply a wait over 1 second."

---

## Template — your UX layer

### Per-role decisions

| Role | Context constraint | Latency budget (key flow) | Accessibility notes |
| :---- | :---- | :---- | :---- |
| [Shopper] | [phone, mid-commute] | [≤ 1 s to product page] | [touch targets, glare contrast] |

### Decisions made

| # | Decision | Choice | Failure condition you accepted | ADR |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Latency budgets + loading patterns | [per table above] | | |
| 2 | Accessibility floor + human test plan | [WCAG 2.1 AA + who tests] | [automated checks alone = theatre] | |
| 3 | Design system | [adopt / customize / build + owner] | | [[ADR-NNN]] |
| 4 | Navigation depth + disclosure rules | [e.g., 2 levels max] | | |
| 5 | AI autonomy per use case | [stakes × reversibility row each] | | |

### Component states checklist

Every interactive component defines: default · hover · focus · disabled ·
loading · error — at design time, in the design tool and the code.
