# Changelog

## 5.10.0 — 2026-11-09

- Added a behavior eval suite (`evals/`, 41 cases: 21 routing, 4 no-trigger, 6 no-fabrication, 7 guardrail, 3 quality) for `claude plugin eval`, a portable `evals/evals.json` copy inside the skill, a structure test, a manually triggered CI workflow and a plugin manifest.
- Description changes driven by eval failures: now triggers on responding to bad reviews, complaints and reputation problems, and on adding surveys, pop-ups, timers, urgency or tracking scripts to a site.
- Corrected facts after checking sources: Google's review policy wording (no mention of kiosks; on-premises pressure, staff quotas, selective solicitation and incentives confirmed), TikTok GMV Max status and learning figure, the July 2025 vacatur of the FTC click-to-cancel rule, the Business Profile Q&A retirement timeline, and the Amazon title-limit wording.

## 5.9.0 — 2026-11-09

- Added `references/landing-page-design-and-copy.md`, compiled from NN/g and Baymard research, practitioner frameworks (Dry, Gardner, Wiebe, Laja, MECLABS, LIFT), the Unbounce benchmark, the FTC native advertising guide, WCAG/European Accessibility Act and Core Web Vitals, with evidence-quality labels and a list of related agent skills.
- Rewrote Workflow 4D to cover page-type choice, first-screen drafting and tests, design direction, confirmation page, pre-launch testing and reviews of existing pages.
- Added `templates/landing-page-review-scorecard.md` and `examples/landing-page-brief-example.md`; expanded the landing page brief; aligned the HTML skeleton with the worked example.
- Extended `check_page_meta.py` with heading-order, button-text, exit-link, image-dimension, lazy-hero, blocking-script, input-type and reading-level warnings, with tests.
- Linked the landing page material from 4A, 5K, the CRO reference, the routing guide and sources.

## 5.8.0 — 2026-11-09

- Added twelve workflows: 0 quickstart, 4C pricing, 4D landing page build, 5L other paid platforms (TikTok, Pinterest, YouTube/Demand Gen, LinkedIn, Microsoft), 5M marketplace listings and ads, 5N local marketing, 5O B2B/SaaS demand generation, 5P media plan and budget, 7A launch plan, 8H review cadence, 9F advocacy and reputation, 9G subscription retention.
- Added references: paid platforms beyond Meta and Google Search; reviews, referrals, loyalty and reputation (FTC 16 CFR 465, platform review policies, response guide, severity matrix); privacy, consent and data protection (GDPR/ePrivacy, US state laws, GPC); marketing glossary.
- Added templates (media plan, launch plan, landing page brief, advocacy and reputation plan) and examples (filled-in context file, media plan JSON, landing page HTML skeleton).
- Added validators `check_media_plan.py`, `check_context_file.py` and `check_page_meta.py` with 14 tests and CI steps.
- Rewrote the skill description for all business types; principle 16 now covers genuine reviews; principle 19 points to the privacy reference. Time-sensitive platform and legal facts are dated and marked where they come from third-party reports.

## 5.7.0 — 2026-11-09

- Added Workflow 5K (Meta Ads campaign setup and optimization), `references/meta-ads-campaign-setup-and-signal-quality.md` and `templates/meta-ads-campaign-blueprint.md`, built from an ecommerce operator's field tips and checked against Meta, Google and practitioner sources. They cover objective and event choice, learning-phase volume, Pixel/CAPI dedup and match quality, geography controls, custom/lookalike tests, ROAS/CAC/CLV vs platform reporting, recordings, exit surveys, comment moderation, and Marketing API/Composio access with write gates.
- Broadened principle 14 from paid search to all paid media; routed 5K from SKILL.md, WORKFLOWS.md and the routing guide.
- Launch QA now requires comment and visitor-behavior monitoring; the CRO reference names recording tools and bans back-button hijacking (Google spam policy, enforced June 15, 2026).

## 5.6.0 — 2026-11-09

- Reduced SKILL.md from ~48.7 KB (~12k tokens) to ~14 KB (~3.5k tokens) to fit the Agent Skills activation-tier budget. Moved the 11-step reasoning chain to `references/core-reasoning-chain.md` and the detailed routing rules/depth table to `references/routing-guide.md` verbatim, and replaced the routing prose with a one-row-per-workflow router table plus a done-checklist.
- Rewrote the frontmatter description as "what it does + when to use it" (826 chars) instead of a keyword list.
- Added a persistent marketing context file (`templates/marketing-context.md` → `.marketing-context/brand-truth.md`) with status-labeled rows, a claim register, freshness and approval rules; wired it into SKILL.md, WORKFLOWS.md and workflows 1A/3A.
- Added `[NEEDS INPUT]` / `[NEEDS HUMAN REVIEW]` conventions; `check_copy.py` now errors on unresolved markers in copy fields.
- Added principle 20 (read-only by default; per-action human confirmation for external writes).
- Added `scripts/check_skill_spec.py` (spec + budget + routing + orphan checks), tests, and a CI step.
- Added practitioner frameworks with guardrails: AIDA/PAS/ACCA/4 Cs table and ARC-E copy brief (brand voice reference), competitor teardown (positioning reference, linked from Workflow 3), a mechanism note for solution-aware buyers, a master asset → per-platform transformation pipeline with LinkedIn/X/video/carousel/email constraints, hook/setup/payoff/CTA beats, and programmatic video guidance (Remotion, HyperFrames).
- Added `references/content-grounding-and-production-tools.md`: read-only vs write boundary, transcript/Readwise grounding, Search Console/GA4 MCP options, pre-publication checks, and a comparison with other marketing-skill repos. Tool names were verified on 2026-11-09; unverifiable names from external suggestions were omitted.
- Added `docs/skill-architecture.md` (maintainer guide: disclosure tiers, frontmatter including client-specific extensions, writing rules, roadmap with phase status).

## 5.5.0 — 2026-11-09

- Built on v5.4's existing ETL/GA4/Meta/Shopify/Etsy/Amazon work with three focused implementation workflows: **8E first-party event instrumentation**, **8F marketplace ETL/financial reconciliation**, and **8G audiences, datasets, reverse ETL and UTM governance**.
- Added primary-source-verified November 2026 API notes for Shopify 2026-01 bulk-query concurrency, Etsy v3 order/listing/inventory webhooks and rate limits, Amazon SP-API/Ads/Attribution boundaries, GA4 Measurement Protocol and Consent Mode v2, Google Data Manager API after June 2026 upload restrictions, and Meta Pixel/CAPI dedup fields.
- Added identity/campaign UTM governance reference, event destination/consent mapping, marketplace ingestion and reconciliation contract, and audience activation/suppression brief.
- Added synthetic multi-marketplace source→event→audience→campaign URL JSON manifest and an offline Python preflight validator with ten regression tests. Checks structural correctness, source-scoped keys, browser/server Meta event IDs, purchase values, sensitive URL parameters, activation approvals and marketplace restricted-data gates.
- Wired specialists, revised source index, templates, README and CI without replacing core Marketing OS or granting access to customer, ads, or store data.
- Validation scripts and documents are guides only; no live pixel edits, customer data ingestion, audience upload, ad spend or tracking changes.


## 5.4.0 — 2026-11-06

- Added Stage **8D Marketing Data Pipelines and Measurement** integrating attribution/analytics engineering with the existing marketing operating system, plus implementation blueprint, event/UTM QA plan and hypothetical Shopify/Etsy/Amazon pipeline example.
- Researched and added separate references for **ETL/ELT and warehouse contracts; Meta datasets, Pixel/CAPI dedup and conversion QA; GA4 ecommerce, Measurement Protocol, BigQuery, GTM and consent mode; Amazon SP-API/Attribution and Etsy v3 API; SKU/order reconciliation; audience identity, suppression and reverse ETL**.
- Curated and classified **real agent skills** from dbt Labs, RudderStack, Shopify, Corey Haines and Dataslayer plus Airbyte, dlt, Meltano, dbt, DuckDB, Great Expectations, official APIs and learning resources. External skills are optional references, not automatically installed.
- Added governance for marketplace buyer data, source-scoped identities, data quality, event deduplication, privacy and activation approval; linked the data specialist into Meta/Shopify ads and measurement routes.


## 5.3.0 — 2026-11-06

- Added seven specialist workflows: **Analytics 8A**, **Attribution/Incrementality 8B**, **Customer RFM/Cohorts/CLV 8C**, **Email Marketing 9B**, **SMS/Text Marketing 9C**, **Cross-Channel Lifecycle 9D**, **Email Deliverability/List Health 9E**.
- Added eight research references on email creative, sender authentication/Gmail bulk rules/consent, SMS/TCPA/carriers/STOP, GA4/Shopify metric integrity, cohort/RFM/CLV, attribution/holdouts/Meridian MMM, lifecycle/flow collisions and open-source marketing skills.
- Added eight production and analytical templates (email, sender, SMS, lifecycle, KPI/event dictionary, attribution experiment, cohorts, performance review), two worked examples, and a deterministic email/SMS draft-manifest checker with tests.
- Integrated specialists into Marketing OS routing, Stage 8/9 and Shopify lifecycle handoffs, source bibliography, README and CI validation.
- Emphasized **email consent is not SMS consent**, differences between US CAN-SPAM, ESP/receiver and other jurisdictions, one-click unsubscribe/Gmail deliverability, Apple MPP open-rate artifacts, attribution vs incremental profit and explicit approval for every live send or data mutation.


## 5.2.0 — 2026-11-06

- Added Shopify-specific operating system specialists: **Store Diagnosis 1B**, **Catalog & Merchandising 3B**, **Shopify CRO/Checkout 4B**, **Shopify Ecommerce SEO/Markets 5H**, **Shopping/Meta Feeds and Web Pixel Tracking 5I**, **Lifecycle/Retention 9A**.
- Added original research references for Shopify economics, product/variant catalog and Search & Discovery, collection/PDP usability, ecommerce technical SEO and Markets, Google/Meta catalog campaigns, Web Pixels and consent, Liquid/theme performance, Shopify Messaging/Flow and cohort retention.
- Added **curated ecommerce/Shopify agent skills and resources**: Shopify official AI Toolkit and developer skills, merchant-oriented store audit skills, ecommerce skill collections, Corey Haines marketing skills, Baymard, NN/g, Google Merchant and Klaviyo; documented maturity/licensing/official-vs-practitioner differences.
- Added Shopify **Promotions 5J** for seasonal/gifting, bundle and discount design with plan/stacking/stock checks, margin models, coordinated media and no fabricated urgency.
- Added seven reusable merchant-facing audit, PDP/collection, SEO, pixel/feed, promotion and lifecycle templates plus a source- and caveat-labeled worked example.
- Integrated Shopify branches into Marketing OS main routing and existing commerce/channel/retention/creative handoffs. Special attention to checkout plan eligibility, Web Pixel sandbox/consent and Shopify Sep 2026 session analytics changes.
- Required source-linked product facts, approved store mutations, realistic campaign economics and qualified business outcomes.


## 5.1.0 — 2026-11-06

- Added optional Stage 5 specialists: **5C integrated promotion**, **5D organic social/hooks/community**, **5E influencers, UGC and collaborations**, **5F earned PR, press releases and newswires**, and **5G Google Ads paid search**.
- Added source-based research references covering PESO, brand/promotion fundamentals, platform-native short-video and hooks, partnership vetting/FTC disclosure/rights, public relations/newsworthiness/wire limits, and paid distribution/business outcomes.
- Added comprehensive Google Search Ads guide: buying/query intent, Keyword Planner, match types and negatives, account architecture, lead/sales conversion integrity, 2026 Smart Bidding/AI Max and Data Manager changes, RSA assets, quality diagnostics, experiments and commercial safeguards.
- Added reusable promotion, content, partnership, newsroom, search campaign, RSA copy and optimization templates plus worked physical-product/service examples.
- Added structural Google RSA JSON checker and tests for headline/description lengths, distinct assets, brand cues and publication prerequisites; wired into CI and skill routing.
- Reinforced explicit approval before publishing, spending, outreach or committing to creator/newswire services.


## 5.0.0 — 2026-11-06

- Renamed skill from **Meta Ad Copy Strategist** (`meta-ad-copy-strategist`) to **Marketing OS** (`marketing-os`), reflecting its full brand, offering, acquisition, SEO/AEO/CRO, creative, measurement and growth capabilities.
- Moved the skill to `skills/marketing-os/`; updated Agent Skills frontmatter, installation instructions, repository links and GitHub Actions validation paths. Existing playbooks and reference materials are preserved.


## 4.3.0 — 2026-11-06

- Added **SEO 5A**, **AEO/AI-answer visibility 5B**, and **CRO 4A** as optional specialist workflows within the nine-stage marketing system.
- Added in-depth research guides for technical/ecommerce SEO, search intent and content, structured data, merchant product feeds, Google/Bing AI visibility, citation measurement, conversion usability, attribution quality and controlled experimentation.
- Linked current official Google Search Central, Bing Webmaster, web.dev, Baymard, Nielsen Norman Group and open-source AI skill references. Clarified that Google AI Search does not need special AI schema/llms.txt or guarantee citations.
- Added a search/answer/conversion audit, experiment brief and worked offering-level example; integrated search and conversion into skill routing, product/channel/offer handoffs and CI checks.


## 4.2.0 — 2026-11-06

- Added optional **Workflow 1A — Offering Discovery → Marketing Plan**, a research-to-decision playbook for one physical product, SaaS, service, subscription, bundle or other commercial offering.
- Added end-to-end mapping of actual deliverables, product features, benefits, Jobs-to-Be-Done, buyer roles, purchase occasions, competing alternatives, barriers, real drawbacks, pricing and economic constraints, honest assurances, creative proof and destination readiness.
- Added value-proposition and evidence traceability, customer choice and objections matrix, adaptive intake, full offering dossier, claim-safe copy library and prioritized channel/creative/experimentation plan.
- Added service-specific extensions (people/process/physical evidence, implementation scope and capacity) and illustrative product/service examples.
- Integrated offering workflow into skill routing, marketing operating system, discovery, offer and creative handoffs; added CI validation tests and source-backed reference links.


## 4.1.0 — 2026-11-06

- Added optional **Workflow 3A: Brand discovery → voice → messaging library**, before the existing positioning and creative-production stages.
- Added a structured, evidence-calibrated review of claimed, expressed and customer-perceived identity; brand purpose, perspective, goals, selling points, personality, category advantage and tradeoffs.
- Added a practical voice-discovery framework using real sample copy (pronouns, lexicon, syntax, rhythm, tone axes, claims and say/do-not-say examples).
- Added owner/customer discovery intake, cross-channel messaging library template, sources and worked example; compresses research into approved feature–benefit bullets, Meta primary text/headlines/descriptions, page copy, hooks, CTAs and scripts.
- Updated routing, positioning and marketing-system handoffs to use this step when brand understanding is missing. Added validation coverage for reference and template presence.

## 4.0.0 — 2026-11-06

- Added research-backed creative strategy, visual/art direction, placement specs and safe-zone caveats, Reels and Stories scripts, Instagram idioms, creator/UGC legal and rights safeguards, and creative QA guides.
- Extended creative-production and launch workflows with exact shot/visual communication planning, platform adaptations, legal/media rights, FTC disclosure and Advantage+ SAY/SHOW/SEND review.
- Added production brief, storyboard/shot list, reviewer scorecard, worked Reels concept, and structured creative manifest.
- Added optional creative manifest linter with 7 new tests covering aspect ratios, essential text overlays, brand cues, release approval and license gates; CI includes both linters.
- Expanded source bibliography with Meta Blueprint 2026, updated third-party Meta-spec audits, Kantar/Ipsos creative research, FTC and language science. Explicitly distinguish advisory specs from changing platform rules.


## 3.0.0 — 2026-11-06

- Introduced a **nine-stage modular marketing operating system** connecting market/customer understanding to actual sales, store conversion, ad production and retention actions.
- Added individual SOPs with trigger, questions, research/evidence needs, outputs, decision gates and handoffs: commercial/product, buyer/occasion, positioning/brand, offer/PDP, channel strategy, creative, launch QA, measurement/experiments and retention/scale.
- Added explicit unit-economics constraints (pre-ad contribution, allowable CPA and break-even ROAS), conversion bottleneck diagnostics, attribution-versus-incrementality caution and hard-stop publishing safeguards.
- Added actionable handoff templates for operating briefs, creative briefs and experimental decision logs, plus a complete hypothetical research-to-sales walkthrough.
- Updated `SKILL.md` routing to select appropriate workflows and output decision packets rather than defaulting to copy generation.
- Linked contemporary Meta Blueprint, product-page UX, category-entry-point and measurement education in the operating guide.

## 2.0.0 — 2026-11-06

- Introduced a **diagnosis-first** marketing workflow distinguishing communication problems from product, price, distribution, customer fit, website UX and measurement constraints.
- Added detailed research-backed references covering market positioning (April Dunford), brand equity and category entry points (Keller; Ehrenberg-Bass), perceived value/pricing (Zeithaml), persuasion and signaling (ELM, PKM, Cialdini, Fogg, Milgrom & Roberts), marketing effectiveness (Binet & Field), and non-linear buying journeys (Google).
- Expanded buyer research with buyer/user/recipient roles and exploration vs evaluation.
- Added strategic marketing brief and complete hypothetical diagnosis example.
- Integrated brand consistency, credible proof, category entry points and balanced brand/activation measurement into the writing workflow.
- Expanded source bibliography with primary references and limitations of each model.
- Clarified conditional installation instructions and conservative claim standards.

## 1.0.0 — 2026-11-06

- Initial evidence-first Meta ad copywriting skill with buyer research, objections, Meta field guidance, compliance, experiments and optional linter.
