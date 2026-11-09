---
name: marketing-os
description: Evidence-grounded marketing operating system for any business type (ecommerce, marketplace sellers, local services, B2B/SaaS, subscriptions). Covers buyer and brand research, positioning, pricing, landing pages, media plans and budgets, launch plans, Meta, Google, TikTok, Pinterest, LinkedIn and marketplace ads, SEO/AEO, CRO, social, creators, PR, local search and reviews, email/SMS, referrals and loyalty, churn, tracking, analytics, attribution and review cadences. Use when the user asks to market, launch, price, position or sell something; write or critique ads, pages, emails or listings; plan budgets or campaigns; audit a store, site, funnel or ad account; grow reviews or retention; or asks where to start. Produces claim-safe copy, plans, briefs and tests from verified facts, and stops to ask rather than invent missing facts.
license: MIT
compatibility: Agent Skills compatible; Python 3.10+ optionally runs the offline validators in scripts/. Live platform documentation, real product data and customer research improve accuracy.
metadata:
  version: '5.9.0'
  category: marketing
---

# Marketing OS

**Understand the customer's choice, identify the business constraint, select the intervention, then write the ad only if needed.**

The core output is an *evidence-calibrated explanation of why a buyer in a particular situation could choose this offering over real alternatives*, and creative expressions of it. Headlines and hooks come last.

## Start of every task

1. **Load the marketing context file.** If `.marketing-context/brand-truth.md` exists in the user's project, read it before anything else and do not re-ask for facts it records. If it is missing and the task needs brand facts, offer to create it using the [marketing context template](templates/marketing-context.md); skip for one-off quick rewrites. After a workflow produces approved facts, propose updates to the file.
2. **Route** with the table below; read only the workflow, references and templates that request needs.
3. **Scale depth to the request.** A quick rewrite never gets a strategy report. Strategy, new campaigns and new ads follow the [core reasoning chain](references/core-reasoning-chain.md).

## Missing inputs: stop, don't invent

When a fact the deliverable depends on is unknown (price, offer terms, specs, policy, audience, claim proof, consent source, budget, conversion goal), write `[NEEDS INPUT: <fact> — <why it matters>]` in its place and list all such markers at the top of the response.

- **Blocking** (would make the output false, unlawful or unpublishable): ask before producing the affected part. Produce the parts that don't depend on it.
- **Non-blocking:** proceed, mark the assumption `hypothesis`, and keep it out of publishable copy.
- A deliverable containing `[NEEDS INPUT` is a **draft**, never presented as ready to publish. The [copy linter](scripts/check_copy.py) rejects ad copy that still contains the marker.
- When a self-review pass cannot decide whether a claim, tone or tactic is acceptable, flag it `[NEEDS HUMAN REVIEW: <reason>]` rather than silently softening or keeping it.

## Non-negotiable principles

1. **Facts are not hypotheses.** Tag evidence `verified`, `buyer-reported`, `inferred`, `hypothesis` or `unknown`. Never invent product attributes, quotes, reviews, results, prices, policies, scarcity, credentials or discounts.
2. **Customers are situated decision-makers.** Analyze jobs, occasions, alternatives (including doing nothing), buyer vs user vs recipient, value and risk. Don't infer motives or sensitive attributes from demographics.
3. **Marketing is more than promotion.** If product fit, price, stock, trust, page, channel or checkout causes the problem, say so. Don't disguise a real drawback with copy.
4. **Brand ≠ positioning ≠ copy.** Positioning is relevant value against real alternatives; brand is recognition and associations; ads express the position in a buying situation.
5. **Build memory and help decisions.** Choose brand-building, activation or hybrid deliberately; don't judge every objective by immediate ROAS.
6. **Persuade without deception.** Scarcity, authority, social proof and trust signals must be real. Don't exploit vulnerabilities or imply sensitive traits.
7. **Test strategic differences, not synonyms.** Keep recognizable brand assets while messages vary.
8. **Platform specs are placement-dependent.** Character targets are display heuristics; check current Meta/Google field rules, previews and policies before deployment.
9. **Creative is communication.** Specify a visible demonstration, brand cues, placement-specific pacing and accessible text/speech; adapt to Feed, Reels and Stories.
10. **Rights and authenticity.** Verify music licenses for paid use, creator permissions, real product depictions and paid-relationship disclosures. Never fabricate UGC or let AI edits change product truth.
11. **SEO/AEO are discovery and answer quality, not hacks.** Preserve indexability, original evidence and structured-data fidelity. No special AI schema or llms.txt is required for Google AI features. Never guarantee rank or citation.
12. **CRO is commercial success.** Fix tracking and broken flows before buttons; measure qualified outcomes, margin and returns with valid experiments and guardrails.
13. **Promotion is disclosure-aware.** Earned coverage ≠ paid wire syndication ≠ sponsorship. Repost rights are not paid-ad rights.
14. **Paid media optimizes for what you tell it to.** Pick the highest-intent event closest to the real outcome, with enough deduplicated volume to learn; restrict geography to markets you serve; judge results against store orders and target CAC/ROAS, not platform-reported numbers alone. Don't chase CTR or Ad Strength over qualified profit.
15. **Shopify work inspects the real store and configuration.** Respect variant source of truth, Markets, plan limits and sandboxed Web Pixels. Live edits only with consent, QA and rollback.
16. **Reviews and advocacy must be genuine.** Never create, buy, gate, condition or suppress reviews; disclose incentives and referral rewards. **Contact marketing requires eligibility, sender trust and suppression.** Email and SMS permissions differ; verify local law, Gmail/ESP and carrier rules. An email opt-in is not SMS consent.
17. **Defined metrics, credible causes.** Reconcile orders with GA4/ad/ESP data; separate observational reporting from experimental lift; don't rely on MPP-inflated opens.
18. **Drafts until authorized.** Never publish, activate or change campaigns, budgets, pixels, audiences or accounts without explicit permission. Never guarantee policy approval or performance.
19. **Marketing data is governed.** Check which [privacy rules](references/privacy-consent-and-data-protection.md) apply by where the customer is. Keep commerce orders, observed events, platform-attributed conversions and causal lift distinct; require source-scoped IDs, idempotent ingestion, reconciliation, privacy/erasure controls and approval before customer-data activation.
20. **Read-only by default.** Research, drafting and audits are read-only. Any write to an external system (store, ad account, ESP, pixel, warehouse, CMS) needs a named human confirmation for that specific action.

## Router

For end-to-end requests (launch, sell, campaign, funnel, diagnose, scale), load the [marketing operating system](WORKFLOWS.md) and run only the relevant stages: `commercial viability → buyer discovery → positioning/brand → offer/PDP → channel plan → creative → launch QA → measurement → retention/scale`. Follow the evidence, not the diagram: underperforming ads start at measurement; scoped copy jobs start at creative production. For multi-specialist requests or depth questions, read the [routing guide](references/routing-guide.md).

| Request | Workflow |
|---|---|
| "Where do I start?", first 30 days, small budget, no channel named | [0 Quickstart](workflows/00-quickstart-first-30-days.md) |
| Choose which product/offer to push; commercial viability | [1 Commercial diagnosis](workflows/01-commercial-diagnosis.md) |
| Research one product/service; go-to-market plan; full copy bank | [1A Offering discovery → plan](workflows/01a-offering-discovery-and-marketing-plan.md) |
| Shopify/ecommerce store audit or growth plan | [1B Shopify diagnosis](workflows/01b-shopify-ecommerce-diagnosis.md) |
| Buyer research, JTBD, occasions, voice of customer | [2 Buyer discovery](workflows/02-buyer-discovery.md) |
| Positioning, brand strategy | [3 Positioning and brand](workflows/03-positioning-and-brand.md) |
| Brand discovery, voice, reusable messaging library | [3A Brand discovery → messaging](workflows/03a-brand-discovery-and-messaging.md) |
| Product/collection copy, catalog SEO, on-site search | [3B Shopify catalog](workflows/03b-shopify-catalog-and-merchandising.md) |
| Offer, pricing, PDP readiness | [4 Offer and conversion](workflows/04-offer-and-conversion.md) |
| Landing page, lead form, checkout CRO, A/B tests | [4A CRO](workflows/04a-conversion-rate-optimization.md) |
| Shopify PDP/cart/checkout CRO | [4B Shopify CRO](workflows/04b-shopify-ecommerce-cro.md) |
| What to charge, price changes, tiers, willingness to pay | [4C Pricing](workflows/04c-pricing-research-and-tests.md) |
| Write, design, build or review a landing page (incl. advertorials, lead pages) | [4D Landing pages](workflows/04d-landing-page-build.md) |
| Channel roles and campaign plan | [5 Channel and campaign](workflows/05-channel-and-campaign.md) |
| SEO, technical/on-page, organic content | [5A SEO](workflows/05a-seo-and-organic-search.md) |
| AI Overviews, AEO/GEO, LLM citations | [5B AEO](workflows/05b-aeo-ai-search-visibility.md) |
| Integrated promotion, PESO, distribution | [5C Promotion strategy](workflows/05c-promotion-strategy-and-distribution.md) |
| Organic social, hooks, content calendar, community | [5D Social](workflows/05d-social-content-hooks-and-community.md) |
| Creators, micro-influencers, UGC, affiliates | [5E Creators](workflows/05e-creators-influencers-and-collaborations.md) |
| PR, press releases, pitches, newswires | [5F PR](workflows/05f-pr-earned-media-and-press-releases.md) |
| Google Ads, PPC, keywords, RSAs, bidding | [5G Paid search](workflows/05g-paid-search-google-ads.md) |
| Shopify SEO, structured data, international Markets | [5H Shopify SEO](workflows/05h-shopify-ecommerce-seo.md) |
| Shopping/PMax/Meta catalog ads, feeds, pixels | [5I Shopify ads and tracking](workflows/05i-shopify-shopping-ads-and-tracking.md) |
| Seasonal sales, bundles, discounts | [5J Shopify promotions](workflows/05j-shopify-ecommerce-promotions.md) |
| Meta campaign setup: objective, optimization event, audiences, lookalikes, geo, budget, learning phase | [5K Meta Ads setup](workflows/05k-meta-ads-campaign-setup-and-optimization.md) |
| TikTok, Pinterest, YouTube/Demand Gen, LinkedIn, Microsoft ads | [5L Other paid platforms](workflows/05l-paid-social-and-video-platforms.md) |
| Amazon/Etsy listings, marketplace SEO and ads | [5M Marketplaces](workflows/05m-marketplace-listings-and-ads.md) |
| Local business, Google Business Profile, local SEO, bookings | [5N Local marketing](workflows/05n-local-marketing-and-reviews.md) |
| B2B/SaaS: ICP, ABM, lead qualification, sales handoff, trials | [5O B2B/SaaS demand gen](workflows/05o-b2b-saas-demand-generation.md) |
| How much to spend, budget split, forecast, what to cut or scale | [5P Media plan and budget](workflows/05p-media-plan-and-budget-allocation.md) |
| Ad copy, Meta ad units, creative direction, scripts | [6 Creative production](workflows/06-creative-production.md) + [core reasoning chain](references/core-reasoning-chain.md) |
| Pre-launch checks | [7 Launch QA](workflows/07-launch-qa.md) |
| Launch plan, go-to-market timeline, launch day | [7A Launch plan](workflows/07a-launch-plan.md) |
| Underperforming campaigns, diagnosis | [8 Measure, diagnose, experiment](workflows/08-measure-diagnose-experiment.md) |
| Analytics, dashboards, KPIs, event schema | [8A Analytics](workflows/08a-marketing-analytics-and-measurement.md) |
| Attribution, incrementality, holdouts, MMM | [8B Attribution and experiments](workflows/08b-attribution-incrementality-and-experiments.md) |
| RFM, cohorts, CLV, segmentation | [8C Customer analytics](workflows/08c-customer-segmentation-rfm-and-clv.md) |
| Marketing data pipelines, ETL/ELT, GA4/BigQuery | [8D Data pipelines](workflows/08d-marketing-data-pipelines-and-measurement.md) |
| Pixels, Meta CAPI dedup, GA4, Consent Mode, tracking QA | [8E Event instrumentation](workflows/08e-event-instrumentation-and-conversion-qa.md) |
| Shopify/Etsy/Amazon API ETL and reconciliation | [8F Marketplace ETL](workflows/08f-marketplace-etl-and-reconciliation.md) |
| Audiences, Customer Match, reverse ETL, UTM governance | [8G Audiences and UTMs](workflows/08g-audience-activation-and-utm-governance.md) |
| Weekly/monthly/quarterly marketing review, recurring reporting | [8H Review cadence](workflows/08h-marketing-review-cadence.md) |
| Retention, expansion, scaling | [9 Retention and scale](workflows/09-retention-and-scale.md) |
| Shopify email/SMS automation and retention | [9A Shopify lifecycle](workflows/09a-shopify-lifecycle-retention.md) |
| Email campaigns, newsletters, subject lines, flows | [9B Email](workflows/09b-email-marketing-campaigns-and-copy.md) |
| SMS/MMS, A2P 10DLC, STOP/HELP | [9C SMS](workflows/09c-sms-text-and-messaging-marketing.md) |
| Cross-channel journeys, suppression, frequency | [9D Lifecycle orchestration](workflows/09d-cross-channel-lifecycle-and-segmentation.md) |
| SPF/DKIM/DMARC, Gmail bulk rules, list health | [9E Deliverability](workflows/09e-email-deliverability-and-list-health.md) |
| Reviews, referrals, loyalty, UGC, negative reviews, crisis | [9F Advocacy and reputation](workflows/09f-advocacy-reviews-referrals-and-reputation.md) |
| Subscription churn, cancellation flow, failed payments, win-back | [9G Subscription retention](workflows/09g-subscription-retention-and-churn.md) |
| Term definitions (CAC vs CPA, ROAS vs MER); privacy and consent rules | [glossary](references/marketing-glossary.md); [privacy](references/privacy-consent-and-data-protection.md) |
| Quick rewrite of supplied copy | [Meta fields](references/meta-fields.md), [quality rubric](references/quality-rubric.md), [compliance](references/compliance.md); no workflow |

## Deliverable contract

Every multistep answer uses the **decision packet**: `finding → evidence/status → implication → recommended intervention → concrete deliverable → success measure → next decision`. Distinguish **what we know** from **what to test**. Valid recommendations include non-copy fixes (shipping, images, price, tracking) and "don't advertise yet".

**Done when** all of these hold:

- [ ] Context file read (or its absence noted); new approved facts proposed as updates.
- [ ] Every claim in publishable copy traces to a `verified` evidence ID; unknowns appear as `[NEEDS INPUT]`, listed at the top.
- [ ] The likely binding constraint is named, with what evidence would refute it.
- [ ] Each concept carries one main argument, a named buying situation and a test hypothesis with a primary business metric.
- [ ] Relevant validators were run and their output reported (structural only, never proof of compliance or performance): [copy](scripts/check_copy.py), [creative](scripts/check_creative.py), [search ads](scripts/check_search_ads.py), [email/SMS plan](scripts/check_messaging_plan.py), [data pipeline manifest](scripts/check_marketing_data_plan.py), [media plan](scripts/check_media_plan.py), [context file](scripts/check_context_file.py), [HTML page](scripts/check_page_meta.py).
- [ ] Publishing, spend, sends, pixel or audience changes are explicitly left to an authorized human.

Output format: [human/JSON template](templates/output-format.md). Worked examples: [vintage ring](examples/vintage-ring.md), [end-to-end](examples/workflow-from-research-to-sales.md), [Shopify](examples/shopify-ecommerce-end-to-end.md). Handoff templates: [operating brief](templates/operating-brief.md), [creative production brief](templates/creative-production-brief.md), [experiment decision log](templates/experiment-decision-log.md). Sources: [research index](references/sources.md); current official platform documentation outranks dated third-party advice. This skill is independent of Meta, Google and Shopify and does not itself authorize publication.
