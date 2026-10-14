---
title: "Seed: product sunset and end-of-life"
status: reference
date: 2026-06-10
tags: [research, seed, provenance]
---

# Seed: product sunset and end-of-life

Distilled from `_inbox/software-eol-best-practices.md` (Perplexity
research, imported 2026-06-10). Everything reworded; provenance is
"report → section"; primary-source links (RFCs, regulator guidance,
vendor EOL pages) kept where given. This feeds the book's differentiator
chapter — the only prior Ch. 08 source is one playbook, so **[checklist:
corroborates/extends]** tags map items to its sunset checklist (export
paths, deletion by retention class, credential revocation, vendor
termination, archive, final retrospective).

## Ch. 01 — Understand: kill criteria at inception

**Pre-registered kill criteria.** Set quantitative kill thresholds at
launch, before sunk costs create attachment. Report's SaaS example: < 500
MAU at 18 months with no growth; < $10K MRR at 24 months; margin < 40%
two consecutive quarters; > 3 tickets per customer per quarter; loss of
ICP fit. Revisit annually — the discipline is having the threshold, not
freezing it. **FLAG: decision-table candidate.** Source:
https://www.pragmaticinstitute.com/resources/articles/product/sunsetting-a-product/
— report → §1, §9.

**Margin, not user count, controls.** Combine customer profile, full-cost
margin, strategic alignment, and competitive landscape. Case: a "200
users only" product charged $20,000/seat and was highly profitable; the
shutdown was reversed. **FLAG: decision-table candidate.** The five
common triggers: low adoption, strategic misalignment, bad unit
economics, quality debt, M&A rationalization. Same source — report → §1.

## Ch. 02 — Design: design-for-sunset architecture choices

**Export-as-a-feature from day one.** Self-service customer export
(JSON/CSV/XML + schema docs + checksums) as a product feature, tested
continuously — silently broken export pipelines are catastrophic at
shutdown; the report's single highest-leverage investment. Pair with open
data models (a plain `SELECT *` dump should be useful without proprietary
decoding) and idempotent, reversible migrations so the final move to
archive is routine. **[checklist: corroborates — export paths]**
Report → §7, §9.

**Avoid lock-in both ways.** Standard SQL over proprietary stores, vendor
services behind internal interfaces, containerized workloads, everything
version-controlled with a handover path; unanticipated cloud-migration
spend added 14% to project costs in 2024. Run periodic "exit drills".
https://selleo.com/blog/what-is-vendor-lock-in-in-cloud-computing ,
https://www.superblocks.com/blog/vendor-lock — report → §7.

**Lock-in vs lock-out.** Lock-out (losing access to your own data) is
categorically worse than lock-in (costly migration); design so no
customer ever experiences lock-out. Frame for the Ch. 02 data layer.
https://www.veeam.com/blog/vendor-lock-in-vs-lock-out-data-portability-insights.html
— report → §7.

**Write the shutdown runbook at launch.** Pre-register export-vs-delete
data categories, the shutdown email template, third parties holding
customer data, and the regulatory checklist — cheap at launch, expensive
under pressure. **[checklist: extends — makes the whole checklist a
launch artifact]** Report → §7, Conclusion.

## Ch. 07 — Ship & Operate: deprecation and evolution

**Machine-readable deprecation signaling.** RFC 8594's `Sunset` header
(HTTP-date hint of removal) plus a `sunset` link relation; RFC 9745's
`Deprecation` header covers the earlier "deprecated but supported" stage.
Use all three headers from announcement day, paired with active outreach.
Sources: https://datatracker.ietf.org/doc/html/rfc8594 ,
https://zuplo.com/learning-center/http-deprecation-header — report → §4.

**Staged API sunset with brownouts.** Decision T-9 months; announcement,
Deprecation header, migration guide T-6; Sunset header + 15-minute weekly
brownouts T-3; escalating brownouts T-6 weeks; HTTP 410 at T-0. Six
months suits most integrators; 12 enterprise; 12–18 platform scale.
**FLAG: decision-table candidate** (phase × timing × action). Source:
https://zuplo.com/learning-center/how-to-sunset-an-api — report → §4.

**Return 410 Gone, not 404.** 410 is permanent and deliberate; clients
and monitors stop retrying. Body: message, migration link, replacement,
support contact. Report → §4.

**Cap concurrent versions at 2–3**, with sunset dates phasing out the
oldest and automated regression tests per version; Stripe's date-pinned
versioning is the alternative.
https://www.gravitee.io/blog/api-versioning-best-practices — report → §4.

**Notice norms scale with blast radius.** Feature removal 30 days; API
version retirement 90–180 days; product shutdown 6–12 months; enterprise
platform 12–24 months; Pliant's 6-month API floor is an emerging minimum.
Benchmarks: Microsoft Fixed Lifecycle = 5y mainstream + 5y extended
support, 12-month notice before security updates end
(https://learn.microsoft.com/en-us/lifecycle/policies/fixed); Atlassian =
2-year release support with LTS anchors, ~3-year platform wind-down
(https://www.atlassian.com/licensing/data-center-end-of-life); Google
Cloud ToS = contractual 12 months before discontinuation or breaking
changes (https://cloud.google.com/terms). **FLAG: decision-table
candidate** (tier × notice). Report → §2, §9.

## Ch. 08 — Sunset

**Staged exit gates.** Design freeze → last-time buy → last ship → end
of support → end of life, reviewed quarterly by finance, product,
engineering, compliance — visible migration checkpoints for customers.
**FLAG: decision-table candidate.** Source:
https://gocious.com/blog/how-to-sunset-a-product-in-manufacturing-with-examples
— report → §1.

**Legal floors.** No US federal shutdown-notice statute — obligations
come from contracts (30/60/90-day clauses), deception statutes, good
faith. EU and Australia: mid-term shutdown triggers proportional refunds.
Put shutdown notice in the ToS itself, with survival clauses covering
vendor-initiated shutdown. Report → §3.

**GDPR Article 20 export.** Machine-readable formats (CSV/JSON/XML yes,
proprietary binaries no), direct transmission on request, no hindrance,
one-month response (+1 complex). The export window must span the full
notice period plus a 30-day post-shutdown tail; closing without one
violates Article 20. Article 17 erasure runs concurrently: one month, no
fee, legal holds excepted. Compliant export = open formats, context
metadata, self-service, tail window, confirmation receipt. **[checklist:
corroborates — export paths; extends — 30-day tail + five-point spec]**
Sources: https://gdpr-info.eu/art-20-gdpr/ ,
https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/right-to-data-portability/
— report → §3.

**Refunds: proactive, not claims-based.** Refund remaining prepaid value
with no customer action, self-service paths for one-time purchases, claim
deadline ~90 days post-shutdown (Stadia refunded all hardware and content
proactively). https://www.termsfeed.com/blog/saas-refund-policy/ ,
https://www.cnet.com/tech/gaming/google-stadia-is-shutting-down-in-2023-all-purchases-to-be-refunded/
— report → §3.

**Migration support minimums.** Guide published with the announcement,
exports importable by named alternatives, no degradation before EOL, a
named migration contact. — §3.

**Phased decommissioning.** Discovery (inventory, dependency map, data
classification, regulatory mapping, cost baseline) → archival design
(hot/cold tiers, WORM immutability, validated retrieval, tested retention
rules) → cutover (UAT sign-off, extraction reconciled by row count and
checksum, audited access termination, ordered deprovisioning, license
cancellation) → governance (retention dashboard, monthly log reviews,
quarterly retrieval drills, annual rule review, 3-year integrity audit).
**FLAG: decision-table candidate.** **[checklist: corroborates — archive,
vendor termination; extends — governance cadence]** Source:
https://www.archondatastore.com/blog/application-decommissioning-retirement/
— report → §5.

**Deletion by retention class.** Some laws force deletion, others force
retention, simultaneously: SOX financials 7y; FLSA payroll 3y; IRS tax
7y; HIPAA medical 6y; banking 5–10y; audit logs 1–3y; GDPR personal data
deleted once no legal basis remains. In doubt, keep and restrict access —
spoliation beats over-retention as a liability. **FLAG: decision-table
candidate.** **[checklist: corroborates — deletion by retention class]**
Report → §5.

**Credential revocation, tested not assumed.** Inventory every credential
(API keys, OAuth tokens, service accounts, deploy secrets, DB passwords,
TLS certs, SSH keys), map consumers, revoke at source, verify in logs in
every environment, rotate shared credentials first, cancel third-party
subscriptions; orphaned service accounts retain standing access forever.
**[checklist: corroborates — credential revocation, vendor termination]**
Sources: https://d3fend.mitre.org/technique/d3f:CredentialRevocation/ ,
https://nhimg.org/glossary/credential-revocation/ — report → §5.

**DNS and cert wind-down.** TTL to 300s 48h+ before shutdown; point DNS
at a 410/migration page rather than deleting; remove records after a
90-day tail; rotate out TLS certs; cancel the domain only after all
references update — expired product domains get squatted. **[checklist:
extends — concrete sequence]** Report → §5.

**Archive in preservation formats.** BagIt (RFC 8493, Library of
Congress-endorsed) packaging with manifest checksums; WARC (ISO 28500)
for web content; CSV + DDL + relationship JSON for relational data; PDF/A
for documents; gzipped JSON Lines + SHA-256 for audit logs; OAIS as
frame. **[checklist: corroborates — archive; extends — named formats]**
Sources: https://www.ietf.org/rfc/rfc8493.html ,
https://www.loc.gov/preservation/resources/rfs/webarchives.html — §5, §9.

**License and IP residue.** GPL/AGPL source obligations end with
distribution; cancel auto-renewing licenses after the dormancy window;
check whether licensed third-party data must be deleted; get IP
assignments signed before the team disperses. **[checklist: corroborates
— vendor termination]** Report → §5.

**Legal hold survives shutdown.** Litigation, investigations, or customer
disputes suspend deletion. Holds must be written, custodian-acknowledged,
technically enforced, re-reminded every 6 months, formally released; FRCP
37(e) sanctions failures. Held data goes into the archive, labeled and
access-controlled. Sources: https://www.opentext.com/what-is/legal-hold ,
https://csdisco.com/blog/legal-hold-best-practices-guide — report → §6.

**Internal comms precede external by 2+ weeks.** Exec briefing at
decision; legal/finance T-8 weeks; customer-facing teams and engineering
T-2 weeks (scripts, FAQ, escalations); all-hands on announcement day. A
support agent who doesn't know is the worst failure mode. — §6.

**Final retrospective within two weeks** of decommissioning. Cover:
hypotheses validated/falsified, whether kill criteria predicted the
outcome, technical legacy, customer-handling lessons, knowledge to
transfer, and how long the team held on past the kill threshold. Publish
the document, don't just hold the meeting. **[checklist: corroborates —
final retrospective; extends — six dimensions + 2-week timer]** Source:
https://www.christianstrunk.com/blog/post-mortem — report → §6.

**Knowledge preservation as a deliverable** with owner and deadline: ADRs
and post-mortem permanent; customer feedback 5y; support themes and
benchmarks 3y; runbooks until replaced; contracts 7y or per terms; DPAs
for relationship + limitations period. Store outside the product's own
infrastructure. **FLAG: decision-table candidate.** Report → §6.

## Red-team material / cautionary cases

**Vine (poorly handled).** ~90 days notice, no bulk export of creators'
own videos, no migration target, creators not consulted; the read-only
vine.co archive (itself killed 2019) met the letter, not the spirit, of
portability. Creator platforms carry a higher export bar. Source:
https://startupik.com/why-vine-shut-down-how-twitter-killed-one-of-the-most-influential-apps/
— report → §8.

**Google Stadia (mixed).** Full proactive refunds — but only 3.5 months
notice, no save-data portability, developers learning at the public
announcement, and shutdown rumors denied two months earlier. Money does
not repair short notice, lost data, or broken trust. Report → §8.

**Google Reader (cultural lesson).** ~3.5 months notice, framed as
"spring cleaning"; its users were RSS's infrastructure layer, so damage
exceeded what counts predicted ("Killed by Google" meme). Counter to
naive kill criteria: weigh strategic dependency, not user count. — §8.

**Heroku free tier (adequate, criticized).** 90 days notice, good FAQ,
upgrade paths — but inactive-account deletion began at 60 days, free
Postgres had no export, and the "fraud and abuse" framing rang false. 90
days is the practical floor; the missing export path is what people
remember. Report → §8.

**Parse's imperfections.** Even the best case (12 months, open-sourced
Parse Server, one-command DB migration, zero-downtime cutover) gave no
pre-announcement warning and no cushion for commercial apps. — §8.

**Trade-offs the chapter must not hide.** Ten-year support windows breed
migration procrastination that ESU programs monetize; rigid kill criteria
can be gamed or go stale; header-only API signaling fails without
outreach; post-shutdown export infrastructure costs real money;
open-sourcing a replacement is a major investment. Report → §2, §9.
