# Marketing OS

**Version 5.5 — an evidence-grounded marketing operating system, creative director and Meta ad-writing Agent Skill.**

A reusable [Agent Skills](https://agentskills.io/specification) package for understanding brands, offerings, markets, and buyers, then planning discovery, conversion and growth across organic search, AI answer engines, paid advertising, and customer experiences. It combines marketing fundamentals, JTBD research, competitive positioning, brand memory, perceived value and pricing, ethical persuasion and signaling, genuine objections, creative concepts, and experiments.

> **Core philosophy:** Think about **why customers would choose the offering**, **what else they could choose**, **what makes the promise believable**, **what prevents purchase**, and **whether copy is even the best intervention**. Then write selective, compelling ads.

## New in v5.5: Source-verified data integration, tracking and audience activation

Builds on the existing v5.4 data-pipeline foundation with **implementation-grade** source-specific instructions and offline structural validation.

- [8E Event and Conversion Instrumentation](workflows/08e-event-instrumentation-and-conversion-qa.md): Shopify Web Pixel/consent, Meta Pixel+CAPI event identity and dedup, GA4 Measurement Protocol and value/transaction IDs, Google Ads Data Manager offline conversions and observed QA.
- [8F Marketplace ETL and Finance Reconciliation](workflows/08f-marketplace-etl-and-reconciliation.md): Shopify Admin GraphQL bulk and webhook ingestion, Etsy v3 orders/listings/inventory webhooks, Amazon SP-API/Ads/Attribution sources, scoped keys, backfills, retries, SKU bridges, payments/adjustments and money/fee reports.
- [8G Audiences, Datasets, Reverse ETL and UTM Governance](workflows/08g-audience-activation-and-utm-governance.md): Meta datasets versus audience objects, source/purpose-specific consent, marketplace buyer restrictions, Google Customer Match, deletion/opt-out propagation, click IDs, stable campaign tags and cost-import joins.
- [Current November 2026 Platform API Notes](references/2026-platform-data-api-updates.md): Shopify 2026-01 concurrent bulk query limits, expanded Etsy webhook domains, Amazon SP-API rate limits, GA4 Measurement Protocol, Google Consent Mode v2, post-June-2026 Data Manager guidance and Meta CAPI dedup rules.
- [Campaign UTMs and Identity Reference](references/campaign-utm-and-identity-governance.md): source/merchant/grain identity, allowed click IDs, external campaign URL rules, avoiding PII in parameters, marketplace vs DTC permissions.
- Reusable [Event/destination/consent QA matrix](templates/event-destination-and-consent-matrix.md), [marketplace extraction and reconciliation contract](templates/marketplace-extraction-and-reconciliation-contract.md), and [audience/suppression brief](templates/audience-activation-and-suppression-brief.md).
- A [synthetic JSON pipeline manifest](examples/marketing-data-pipeline-manifest.json), [Python structural QA](scripts/check_marketing_data_plan.py) and tests check identifiers, purchase mapping, Meta browser/server event IDs, UTM privacy, activation readiness and marketplace audience restrictions.

**Important:** A passing JSON linter is not proof of a lawful consent state, real Shopify/Google/Meta/Etsy/Amazon API authorization, successful event delivery or financial reconciliation. No live account or customer data was touched.

## New in v5.4: Marketing data, ETL, Meta/GA4 measurement, audiences and marketplace analytics

This expansion gives the skill an engineering and measurement layer: **Shopify/Etsy/Amazon seller APIs and reports → source-scoped, reliable ETL → canonical orders, variants, refunds and fees → GA4/Meta/Google collection and attribution → reconciliation, data quality, governed audiences and experimentation**. It keeps order ledgers, observed analytics, platform-attributed results and incremental effects distinct.

- [Workflow 8D: Data Pipelines and Measurement](workflows/08d-marketing-data-pipelines-and-measurement.md): a decision-to-architecture-to-QA specialist with explicit consent, auth, approval and release gates.
- [Data engineering and ETL reference](references/marketing-data-engineering-and-etl.md): source contracts, idempotent ingestion, backfills, CDC/snapshots, canonical warehouse grain, data quality and monitoring.
- [GA4/Meta/UTM measurement guide](references/measurement-pixels-ga4-and-attribution.md): GA4 ecommerce + BigQuery + Measurement Protocol, Shopify Web Pixels, Meta dataset/Pixel/CAPI deduplication, GTM, consent, UTM naming and Google Ads offline measurement.
- [Commerce API reference](references/commerce-data-shopify-etsy-amazon.md): Shopify GraphQL Bulk and webhooks, Etsy Open API v3, Amazon SP-API/Reports/Data Kiosk/Amazon Attribution, SKU mapping, marketplace tracking limitations and financial reconciliation.
- [Audience, identity and reverse ETL](references/audiences-identity-and-reverse-etl.md): customer segmentation, first-party eligibility, suppression and deletion propagation, audience diagnostics and policy-safe syncs.
- [Curated data skills and resources](references/marketing-data-tools-skills-and-resources.md): dbt's official agent skills, RudderStack maintained skills, Shopify technical skills, marketing analytics tracking skills, Dataslayer, Airbyte, dlt, Meltano, dbt, DuckDB, GTM server-side and primary platform docs, with tool-selection guidance and caveats.
- [Pipeline implementation blueprint](templates/marketing-data-pipeline-blueprint.md), [event/UTM plan and QA](templates/marketing-event-tracking-and-utm-plan.md), [worked multi-marketplace example](examples/multichannel-marketing-data-pipeline.md).

**Guardrails:** no fabricated live metrics or accesses, no invented customer identity joins, no marketplace buyer-list export for retargeting without permission, no sensitive PII in UTMs, no server-side consent bypass, and no modifying live tagging, audiences or spend without approval. Review platform API versions and rules at implementation time.

## New in v5.3: Email, SMS, lifecycle, customer analytics and causal measurement

Marketing OS now supports **campaign strategy and copy, deliverability and consent audits, text marketing, cross-channel lifecycle orchestration, event/KPI design, RFM/cohorts/CLV, attribution and incremental lift experiments**.

- [Marketing Analytics 8A](workflows/08a-marketing-analytics-and-measurement.md) and [analytics reference](references/marketing-analytics-data-model-and-reporting.md): trustworthy GA4/Shopify/CRM/ESP metrics, event integrity and [KPI dictionary](templates/marketing-measurement-and-kpi-dictionary.md).
- [Attribution and Incrementality 8B](workflows/08b-attribution-incrementality-and-experiments.md) and [causal reference](references/attribution-incrementality-experimentation-and-mmm.md): platform credit versus impact, eligible holdouts, geo tests, MMM/GeoX and [experiment plan](templates/marketing-attribution-and-incrementality-plan.md).
- [Customer RFM/Cohorts 8C](workflows/08c-customer-segmentation-rfm-and-clv.md) and [segmentation research](references/customer-analytics-segmentation-rfm-and-clv.md): net value, real purchase cycles and [segment treatment brief](templates/customer-rfm-cohort-and-segment-plan.md).
- [Email Marketing 9B](workflows/09b-email-marketing-campaigns-and-copy.md) and [copy/strategy guide](references/email-marketing-strategy-copy-and-creative.md): newsletters, welcome/checkout/postpurchase, subject/preheader/hero/CTA and [creative brief](templates/email-campaign-and-creative-brief.md).
- [SMS/Text Marketing 9C](workflows/09c-sms-text-and-messaging-marketing.md) and [SMS/consent guide](references/sms-text-marketing-and-compliance.md): separate opt-in, A2P/carrier/STOP/HELP, quiet hours, costs, content and [SMS brief](templates/sms-campaign-and-compliance-brief.md).
- [Lifecycle Orchestration 9D](workflows/09d-cross-channel-lifecycle-and-segmentation.md) and [journey guide](references/lifecycle-orchestration-and-channel-governance.md): customer state, channel choice, suppressions, trigger/exit logic and [journey matrix](templates/cross-channel-lifecycle-journey-map.md).
- [Deliverability 9E](workflows/09e-email-deliverability-and-list-health.md) and [sender research](references/email-deliverability-consent-and-reputation.md): SPF/DKIM/DMARC, Gmail bulk one-click unsubscribe, list hygiene and [sender audit](templates/email-deliverability-and-consent-audit.md).
- [Agent skills and resources index](references/email-sms-analytics-skills-and-resources.md): Corey Haines, Rebecca Rae's Klaviyo/GA4/Braze, specialist email skills, official Google/Shopify/Twilio/FCC/FTC sources.
- [Worked ecommerce lifecycle example](examples/email-sms-ecommerce-lifecycle-example.md), [analytics/holdout example](examples/marketing-analytics-cohort-decision-example.md), and [messaging plan structural checker](scripts/check_messaging_plan.py).

**Guardrails:** US CAN-SPAM commercial email does not universally require prior opt-in; ESP rules and other jurisdictions may be stricter. SMS marketing commonly needs separate, stronger permission. **Email permission ≠ SMS permission.** Apple Mail Privacy Protection distorts opens; ESP-attributed sales do not prove incremental revenue. No live sends, contact uploads, tracking changes or automation activations without explicit authorization.

## New in v5.2: Shopify and ecommerce operating system

The new Shopify expansion connects **verified catalog/variant/brand data → buyer jobs → collection/PDP merchandising → Shopify SEO/Markets → conversion and checkout → Google/Meta Shopping feeds and Web Pixel analytics → consented lifecycle marketing → net contribution and experiments**.

- [Shopify Store Diagnosis 1B](workflows/01b-shopify-ecommerce-diagnosis.md) and [commerce economics](references/shopify-ecommerce-strategy-and-economics.md): storewide profitability, assortment, customer journey, traffic/channel quality, Shopify plan/theme/Markets, data integrity and prioritized growth roadmap.
- [Shopify Catalog and Merchandising 3B](workflows/03b-shopify-catalog-and-merchandising.md) and [catalog reference](references/shopify-catalog-merchandising-and-data.md): accurate products/variants, buyer-focused collections, Search & Discovery, metafields/metaobjects, titles, bullets, imagery and merchandising.
- [Shopify Ecommerce CRO 4B](workflows/04b-shopify-ecommerce-cro.md) and [CRO/checkout reference](references/shopify-ecommerce-cro-and-checkout.md): mobile collection/PDP/cart/checkout diagnosis, plan-eligible checkout customization, buyer trust, accurate policy/price, valid tests and contribution.
- [Shopify Ecommerce SEO 5H](workflows/05h-shopify-ecommerce-seo.md) and [Shopify SEO/Markets reference](references/shopify-ecommerce-seo-and-markets.md): search-intent pages, Shopify default SEO, canonical/facet/variant URLs, original descriptions, eligible merchant schema, localization and catalog availability.
- [Shopify Shopping/Meta Ads and Tracking 5I](workflows/05i-shopify-shopping-ads-and-tracking.md) and [feed/pixel reference](references/shopify-shopping-ads-feeds-and-attribution.md): Google & YouTube/Merchant Center, Shopping/PMax, Meta catalogs, product sync/IDs/stock, sandboxed Web Pixels, consent, deduplication and profit-oriented ads.
- [Shopify Promotions 5J](workflows/05j-shopify-ecommerce-promotions.md) and [seasonal/bundle reference](references/shopify-promotions-bundles-and-seasonal-campaigns.md): verified seasonal and gifting occasions, real discounts, bundle limitations, price/stock and shipping compatibility, campaign calendars and incremental contribution.
- [Shopify Lifecycle Retention 9A](workflows/09a-shopify-lifecycle-retention.md) and [lifecycle reference](references/shopify-lifecycle-retention-and-automation.md): Shopify Messaging, Flow, Forms, segments, welcome/cart/checkout/postpurchase/winback, customer consent and real cohort economics.
- [Technical storefront and analytics](references/shopify-theme-performance-and-measurement.md): Liquid/theme performance, app weight, Web Vitals, plan-specific checkout and Shopify's late-September 2026 sessions/conversion measurement change.
- [Curated ecommerce skills and resource library](references/shopify-ecommerce-skill-and-resource-library.md): Shopify's official developer agent skills, ecommerce/Shopify marketing skill libraries, Baymard usability, search/merchant, Klaviyo and cross-channel references. Skills vary in scope/maturity and are not automatically installed.
- [Store audit](templates/shopify-store-audit-and-roadmap.md), [product/collection brief](templates/shopify-product-collection-content-brief.md), [PDP CRO brief](templates/shopify-pdp-cro-brief.md), [SEO audit](templates/shopify-search-merchandising-audit.md), [merchant feed/pixel QA](templates/shopify-merchant-feed-and-pixel-qa.md), [lifecycle plan](templates/shopify-lifecycle-and-retention-plan.md) and [worked ecommerce example](examples/shopify-ecommerce-end-to-end.md).

**Guardrails:** no invented store metrics, product/variant facts, access, conversion lifts or merchant feed approvals; no live store edits, ad spending, theme publishing or customer messaging without explicit approval. A merchant's Shopify plan, installed apps, consent settings and real reports control which changes are feasible.

## New in v5.1: Promotion, social media, creator partnerships, PR and Google Ads

This release adds a coordinated **promotion operating system**—not just more social post suggestions—plus detailed **Google Ads paid search planning, copy and campaign QA**.

- [Integrated promotion workflow 5C](workflows/05c-promotion-strategy-and-distribution.md) + [PESO strategy reference](references/promotion-fundamentals-and-integrated-distribution.md): set audience and communication purpose, coordinate paid/earned/shared/owned media, choose real distribution and commercial success measures.
- [Organic social and hooks 5D](workflows/05d-social-content-hooks-and-community.md) + [social reference](references/social-media-strategy-hooks-and-community.md): platform-native Instagram, TikTok, YouTube, LinkedIn, community response, content pillars, truthful hooks, caption/storyboards and repeatable calendars.
- [Micro-influencer and collaborations 5E](workflows/05e-creators-influencers-and-collaborations.md) + [partner reference](references/influencers-collaborations-and-community-partnerships.md): partner discovery/vetting, UGC vs endorsement, gifted/paid disclosures, licenses, Meta Partnership Ads, TikTok Spark Ads, sponsorships and affiliate economics.
- [PR / earned media / newswires 5F](workflows/05f-pr-earned-media-and-press-releases.md) + [newsroom reference](references/pr-press-releases-newswires-and-earned-media.md): newsworthiness gate, truthful press release, editorial-specific pitch, press kit, direct outreach and paid wire comparison. Distribution/syndication does not guarantee independent editorial pickup.
- [Google Ads paid search 5G](workflows/05g-paid-search-google-ads.md) + [complete search research guide](references/paid-search-google-ads-fundamentals.md): intent/keyword research, semantic match/negative keywords, campaign structure, brand-vs-nonbrand, bidding, primary/qualified conversion data, 2026 AI Max expansion, ad assets, RSA copy, landing quality, policy/geo settings, experiments and profit-oriented diagnostics.
- [Paid promotion and measurement](references/paid-social-amplification-and-promotion-measurement.md), [campaign brief](templates/promotion-campaign-brief.md), [social hook calendar](templates/social-content-and-hooks-calendar.md), [creator agreement input](templates/creator-and-collaboration-brief.md), [press/pitch kit](templates/pr-newsroom-and-pitch.md), [promotion outcome review](templates/promotion-outcomes-review.md).
- [Google Search campaign blueprint](templates/google-ads-search-campaign-blueprint.md), [RSA copy/asset sheet](templates/google-search-rsa-and-assets.md), [experiment/optimization brief](templates/google-ads-optimization-and-experiments.md), [fictional worked campaign](examples/google-ads-search-campaign-example.md), and a [structural RSA copy checker](scripts/check_search_ads.py) with tests.

The new sections distinguish **official platform rules from practitioner/guru heuristics**, **truly earned media from sponsored promotion**, and **platform-reported activity from customer/business value**. No live publishing, outreach, partner commitment or spend without approval.

## New in v5.0: Marketing OS identity

Renamed from **Meta Ad Copy Strategist** to **Marketing OS** (`marketing-os`) to reflect the full marketing operating system: brand and offering research, positioning, messaging, SEO/AEO/CRO, Meta creative and advertising, measurement, and growth. Installation paths and validation configuration have been updated; all existing workflows remain.

## New in v4.3: SEO, AEO and CRO foundations + workflows

The skill now covers **the full discovery-to-conversion path**, connecting brand and offering knowledge with organic search, AI answers and purchase experience:

- [SEO Workflow 5A](workflows/05a-seo-and-organic-search.md) and [SEO reference](references/seo-fundamentals-and-ecommerce.md): buyer search intent, index/crawl/JS rendering, site architecture, page copy, merchant product/offer schema and feeds, technical/mobile UX, Search Console and results.
- [AEO Workflow 5B](workflows/05b-aeo-ai-search-visibility.md) and [AI answer reference](references/aeo-generative-search-and-citations.md): reliable first-party answers, entity/product correctness, Google AI Search requirements, Bing Copilot citations and honest reporting limitations. No guaranteed inclusion or special llms.txt requirement.
- [CRO Workflow 4A](workflows/04a-conversion-rate-optimization.md) and [CRO reference](references/cro-research-and-experimentation.md): mobile product-page usability, price/trust/shipping/returns, checkout/form funnel issues, business outcome quality, statistically responsible experiments and guardrails.
- [Search and conversion audit](templates/search-and-conversion-audit.md), [CRO experiment brief](templates/cro-experiment-brief.md), [worked research-to-sale example](examples/seo-aeo-cro-from-offering.md), and an updated [annotated source library](references/sources.md).

**Core distinction:** SEO helps potential buyers find appropriate pages; AEO concerns useful, accurate answers and measurable citation surfaces; CRO reduces obstacles to making an informed, commercially valuable decision. They share the same verified product/brand evidence. These are optional specialist workflows within the original nine-stage system.

## New in v4.2: Offering discovery → buyer value → full marketing plan

The [Offering Discovery Workflow 1A](workflows/01a-offering-discovery-and-marketing-plan.md) investigates a **specific product, service, software tool, subscription or bundle** holistically: what is delivered, who buys or uses it, buying occasions, desired outcomes (including aesthetic or emotional desires), alternatives/status quo, features and buyer benefits, actual limitations, objections, assurances, pricing and economics, credible proof, brand fit and voice. It turns that research into a product-specific positioning proposal, evidence-backed selling-point bullets, short/long descriptions, headline and support-line banks, Meta ad concepts/visuals, product-page fixes, channel recommendations and testable go-to-market priorities.

- [Workflow 1A](workflows/01a-offering-discovery-and-marketing-plan.md) — questions → evidence → diagnosis → decisions → marketing outputs.
- [Research and planning framework](references/offering-research-and-marketing-planning.md) — JTBD, Strategyzer, alternatives-first positioning, service 7Ps, truthful assurances and offer economics.
- [Offering intake](templates/offering-discovery-intake.md) · [Dossier/marketing plan template](templates/offering-dossier-and-marketing-plan.md) · [Worked physical-product and service examples](examples/offering-discovery-to-marketing-plan.md).

Brand discovery is **optional when sufficient approved brand context exists**; otherwise gather a light brand scan or run 3A. The offering workflow is an optional sub-workflow of Stage 1, not an additional mandatory stage.

## New in v4.1: brand discovery → voice → reusable copy

The new [Brand Discovery Workflow 3A](workflows/03a-brand-discovery-and-messaging.md) investigates what a brand **claims**, **demonstrates**, and what buyers **perceive**. It analyzes brand perspective, personality, customer desires, selling points, verified advantages, tone, phrase patterns and limitations, then turns the findings into a coherent [message and copy library](templates/brand-messaging-library.md): benefit bullets, product descriptions, headlines, Meta primary texts and supporting descriptions, hooks, CTAs and channel-specific variants. The process includes a [discovery interview template](templates/brand-discovery-intake.md), a [voice/copywriting research guide](references/brand-voice-and-copy-system.md), and a [worked example](examples/brand-discovery-to-copy.md). No invented founder story, customer quotes, exclusive benefits, or fake scarcity.

## New in v4: creative direction, Instagram/Reels native formats and QA

The workflow now travels **from customer reason → creative concept → visual communication → platform-native production → validated ad draft**. The system knows how to ask for missing real footage instead of inventing product details, creator praise or offers.

- **Visual creative direction:** exact hero subject, framing, lighting, color fidelity, scale, layout, text hierarchy and recognizable brand cues. [Visual guide](references/visual-direction.md).
- **Platform-specific playbooks:** Feed 4:5, Stories/Reels 9:16, carousel 1:1, safe-zone templates, field visibility, and Meta's automated creative variations. [Placement playbook](references/meta-placement-playbook.md).
- **Reels scripts/communication:** native-feeling hooks, demos, unboxing, try-ons, `POV`, `GRWM`, voiceovers, audio, captions and sequential storytelling without forced slang or fabricated experiences. [Video](references/video-storytelling.md) · [Language/idioms](references/platform-idioms-and-voice.md).
- **Creator UGC/partnership rights:** authorized creator use, real testimonials, paid-audio licensing, clear paid endorsements and honest script direction. [Creator guide](references/creator-partnerships-and-rights.md).
- **Reviews and safeguards:** human QA, eight-dimension creative rubric, launch hard stops, product/visual integrity and additional creative-manifest linter. [Scorecard](templates/creative-review-scorecard.md) · [Linter](scripts/check_creative.py).
- **Production outputs:** [Creative director's brief](templates/creative-direction-brief.md), [storyboard/shot list](templates/shot-list-and-storyboard.md), [Reels example](examples/reels-creative-direction.md), and [example manifest](examples/creative-manifest.json).

These guidelines are current as of **November 6, 2026** and are not immutable Meta specifications. Live Ads Manager previews, rights and approval always win over a generalized reference.

## What is new in v3: executable marketing workflows

The package now answers **"what do we need to understand, what do we do with the answer, and what comes next?"** across product selection, research, positioning, offer, advertising, launch, measurement and growth.

- Start with the [**Marketing Operating System**](WORKFLOWS.md): a nine-workflow route map, inputs/outputs, readiness gates, decision tables and recurring operating rhythm.
- Use nine focused [**workflow runbooks**](workflows/01-commercial-diagnosis.md) for commercial diagnosis, buyer research, positioning/brand, offer/store readiness, channel strategy, creative production, launch QA, measurement/experimentation and retention/scaling.
- Use [**operating brief**](templates/operating-brief.md), [**creative brief**](templates/creative-production-brief.md) and [**experiment decision log**](templates/experiment-decision-log.md) to pass findings from one workflow into the next.
- Read a [**worked research-to-sales example**](examples/workflow-from-research-to-sales.md) with concrete buyer hypotheses, creative angles, economic boundaries, and reasons to fix a product page instead of rewriting copy.

The system is modular: a quick ad-copy request still takes a short route. A diagnosis can recommend **not spending on ads** until a product, price, checkout, inventory or tracking problem is addressed.

## What's improved in v2

- **Marketing diagnosis before copy:** separates message issues from product, pricing, distribution, landing-page, brand, demand and measurement problems.
- **A real positioning process:** alternatives → differentiated capabilities → value → best-fit customer circumstances → category; includes category expectations and trade-offs.
- **Brand strategy:** Keller's brand associations and Ehrenberg-Bass's mental/physical availability, category entry points and distinctive assets. Ads can vary by angle without abandoning brand recognition.
- **Customer psychology:** buyer versus user/recipient, JTBD, four switching forces, buying occasions, non-linear exploration/evaluation and decision friction.
- **Persuasion and credibility:** ELM, persuasion knowledge, ethical Cialdini, quality/trust/identity signaling and Fogg's motivation–ability–prompt model.
- **Product value and price:** benefit ladders, total perceived sacrifice, risk reduction and truthful handling of real drawbacks.
- **Better measurement:** brand-building versus short-term activation, ad-concept testing, commercial outcomes, brand measures and causal cautions.
- **Practical references:** linked research notes, an expanded source index, a strategic brief template and a full end-to-end diagnosis example.

## How it works

```text
Actual product & campaign facts
            ↓
Buyer situation, desired progress and alternatives
            ↓
Product benefit, perceived value, objections and weaknesses
            ↓
Competitive positioning + brand identity / buying cues
            ↓
Trust and persuasion mechanism + claim proof
            ↓
Creative concepts → shot/storyboard → brand cues → formats
            ↓
Distinct Meta ad fields and placement-specific assets
            ↓
Policy review, skeptical-buyer audit, landing-page match
            ↓
Controlled learning and strategic revision
```

A quick copy-edit request takes a shorter route; the skill does **not** require a full strategy report every time.

## Install

Install from the published `doeixd/marketing-skills` repository with a compatible Agent Skills installer:

```bash
npx skills add doeixd/marketing-skills --skill marketing-os
```

Or download the ZIP, unpack it and copy the full directory to your tool's agent skills folder, for example:

```bash
mkdir -p .agents/skills
cp -R marketing-os .agents/skills/marketing-os
```

For Claude Code, the local folder can be `.claude/skills/marketing-os/`. See your tool's specific installation instructions. The skill lives at `skills/marketing-os/` inside [doeixd/marketing-skills](https://github.com/doeixd/marketing-skills).

## Example prompts

> Plan a promotion strategy for this product using social content, paid distribution, relevant creators and possible PR. Find the real buyer story, write hooks and build a realistic content and outreach calendar without inventing news or endorsements.

> Research and plan a Google Search Ads campaign: keyword intent groups, positive/negative match strategies, bidding, verified conversions, RSAs/headlines, sitelinks, landing-page checks, AI Max controls, spend safeguards and what to test.

> Diagnose whether my product-page and Meta ad conversion problem comes from weak copy, a confusing offer, buyer uncertainty or product-market mismatch. Give me evidence gaps and a test plan.

> Research how buyers choose this product, including buying occasions, actual alternatives, feature-to-benefit ladders, brand cues, emotional motives and real drawbacks; then write three distinct ad concepts.

> Investigate this product or service end-to-end. Discover exactly what is sold, the customers and situations it serves, motivations and drawbacks, alternatives, positioning, feature-benefit proof, pricing, assurances and the best plan to market it. Generate a reusable copy bank with bullets, descriptions, headlines, Meta ad concepts and what should be fixed before launching.

> Discover this brand from its website, products, reviews and existing marketing. Explain what makes it special, its actual voice and perspective, the claims it can support and customer reservations; create a reusable copy bank with benefit bullets, headlines, descriptions and Meta ad units.

> Develop a positioning strategy for my brand: category expectations, points of parity/difference, best-fit customers, distinctive assets, category entry points and value to communicate in ads.

> Write Facebook Feed and Instagram Feed primary text/headline/description combinations that preserve our brand identity while testing gifting, aesthetic and product-led angles.

> These are my campaign results. Separate what is actually known from causal guesses; tell me whether to fix landing-page UX, change positioning or test new creative.

> Give me a 9:16 Instagram Reels storyboard for this SKU, with exact shots, overlay text, voiceover, brand cue, muted-viewing check, rights constraints, and a 4:5 Feed cut. Distinguish facts from buyer hypotheses.

> I want to sell this new product. Run the marketing workflow from commercial viability through customer research, positioning, offer, channel selection, ad concepts, launch QA and measurement. Label unknowns and tell me when ads are not the next move.

## Reference library

| Document | When to read |
|---|---|
| [Email marketing strategy and copy](references/email-marketing-strategy-copy-and-creative.md) | Subject, preheader, creative, subscriber value and campaigns |
| [Email deliverability and permission](references/email-deliverability-consent-and-reputation.md) | Sender authentication, Gmail requirements, CAN-SPAM and opt-out |
| [SMS/text marketing](references/sms-text-marketing-and-compliance.md) | TCPA/carrier/consent, STOP and timely messaging |
| [Cross-channel lifecycle](references/lifecycle-orchestration-and-channel-governance.md) | Channel collision, customer state, trigger and suppression |
| [Marketing analytics](references/marketing-analytics-data-model-and-reporting.md) | Tracking, GA4/Shopify/CRM truth, KPI definitions and dashboards |
| [Attribution and incrementality](references/attribution-incrementality-experimentation-and-mmm.md) | Holdouts, MMM, geo testing and profit effects |
| [Customer analytics, RFM, CLV](references/customer-analytics-segmentation-rfm-and-clv.md) | Cohorts, realistic segments and customer value |
| [Email/SMS/analytics skills and resources](references/email-sms-analytics-skills-and-resources.md) | Curated agent skills, official docs and limitations |
| [Shopify commerce strategy and economics](references/shopify-ecommerce-strategy-and-economics.md) | Profit, assortment, store health and commerce roadmap |
| [Shopify catalog and merchandising](references/shopify-catalog-merchandising-and-data.md) | Variants, collections, Search & Discovery, metafields and accurate copy |
| [Shopify ecommerce SEO and Markets](references/shopify-ecommerce-seo-and-markets.md) | Product/collection discovery, schema and international store search |
| [Shopify CRO/checkout](references/shopify-ecommerce-cro-and-checkout.md) | PDP/cart/checkout usability, plan-specific extensions and experiments |
| [2026 official data API change notes](references/2026-platform-data-api-updates.md) | Shopify, Etsy, Amazon, GA4, Google Data Manager and Meta Pixel/CAPI details |
| [Campaign UTM and identity governance](references/campaign-utm-and-identity-governance.md) | Source-specific customer/product IDs, URL tracking, consent and audience permissions |
| [Marketing data engineering / ETL](references/marketing-data-engineering-and-etl.md) | Data pipelines, idempotency, backfills, warehouses, source reconciliation and QA |
| [Meta Pixel/CAPI, GA4/BigQuery, GTM and UTM tracking](references/measurement-pixels-ga4-and-attribution.md) | Event contracts, conversion deduplication, consent, attribution, Measurement Protocol |
| [Shopify/Etsy/Amazon data integrations](references/commerce-data-shopify-etsy-amazon.md) | Seller APIs, marketplace limits, financial events and cross-channel product ID bridge |
| [Audiences / identity / reverse ETL](references/audiences-identity-and-reverse-etl.md) | Meta datasets vs audiences, first-party customer segments and governed activation |
| [Data tools and agent skills](references/marketing-data-tools-skills-and-resources.md) | dbt, RudderStack, Airbyte, dlt, official API docs and curated agent skill repositories |
| [Shopify Shopping/Meta feeds and pixels](references/shopify-shopping-ads-feeds-and-attribution.md) | Merchant sync, ads/product data, Web Pixels, events and contribution |
| [Shopify lifecycle and retention](references/shopify-lifecycle-retention-and-automation.md) | Messaging/Flow, segments, consent and customer lifetime |
| [Shopify promotions and seasonal campaigns](references/shopify-promotions-bundles-and-seasonal-campaigns.md) | Discount classes/stacking, bundles, gift occasions, fulfillment and margin |
| [Shopify performance and measurement](references/shopify-theme-performance-and-measurement.md) | Liquid/theme/app performance, analytics and safe rollout |
| [Ecommerce skills/resources](references/shopify-ecommerce-skill-and-resource-library.md) | Official Shopify developer skills and audited third-party workflow examples |
| [SEO fundamentals and ecommerce](references/seo-fundamentals-and-ecommerce.md) | Technical eligibility, buyer intent, architecture, on-page copy and product search features |
| [AEO / AI search citations](references/aeo-generative-search-and-citations.md) | Google AI Search requirements, question-first information and citation measurement limits |
| [CRO and experimentation](references/cro-research-and-experimentation.md) | Buyer friction, store funnels, data integrity and trustworthy A/B testing |
| [Promotion / PESO fundamentals](references/promotion-fundamentals-and-integrated-distribution.md) | Coordinating paid/earned/shared/owned distribution, guru frameworks and communication measurement |
| [Social strategy, hooks and community](references/social-media-strategy-hooks-and-community.md) | Native platform idioms, useful hooks, editorial planning, engagement and response |
| [Influencers, UGC, collaborations](references/influencers-collaborations-and-community-partnerships.md) | Vetting, nano/micro fit, gifting/sponsorship, FTC disclosures, license/affiliate economics |
| [PR, releases and newswires](references/pr-press-releases-newswires-and-earned-media.md) | Newsworthiness, editorial pitches, press kit, paid syndication and outcome evaluation |
| [Paid promotion measurement](references/paid-social-amplification-and-promotion-measurement.md) | Paid creative, platform roles, budget and conversion/brand value |
| [Google Ads paid search](references/paid-search-google-ads-fundamentals.md) | Keywords, match types, negatives, conversion goals, bidding, RSAs, AI Max, experiments |
| [Marketing fundamentals](references/marketing-fundamentals.md) | Diagnose the broader business and marketing system |
| [Buyer research](references/buyer-research.md) | JTBD, buyer situations, customer language and evidence |
| [Market positioning](references/market-positioning.md) | Alternatives, capabilities, value, best-fit customers, category |
| [Brand strategy](references/brand-strategy.md) | Brand equity, distinctiveness, category entry points and memory |
| [Brand voice and copy system](references/brand-voice-and-copy-system.md) | Discover the real voice, differentiate identity from perception, distill into reusable phrasing |
| [Product value and pricing](references/product-value-and-pricing.md) | Feature–benefit ladders, total sacrifice and price concerns |
| [Persuasion and signaling](references/persuasion-and-signaling.md) | ELM, Cialdini, PKM, quality signals and buyer decision barriers |
| [Positioning and objections](references/positioning-and-objections.md) | Objection matrices, benefits and drawbacks |
| [Creative strategy](references/creative-strategy.md) | Translate buyer motives into distinct visual promises and creative territories |
| [Visual direction](references/visual-direction.md) | Frame, camera, typography, product fidelity, brand cues and review language |
| [Meta placement playbook](references/meta-placement-playbook.md) | 4:5 / 9:16 / carousel, safe zones, Reels/Stories/Feed, automated enhancements |
| [Video storytelling](references/video-storytelling.md) | Reels story types, hooks, short-video scripts, audio and captions |
| [Instagram/platform idioms](references/platform-idioms-and-voice.md) | POV, GRWM, unboxing, natural diction and multi-channel communication |
| [Creator partnerships & rights](references/creator-partnerships-and-rights.md) | FTC disclosures, permissions, licenses and authentic creator direction |
| [Creative quality control](references/creative-quality-control.md) | QA gates, eight-item scorecard, systematic revision |
| [Meta fields](references/meta-fields.md) | Primary text, headlines, description, CTA and placement logic |
| [Compliance](references/compliance.md) | Policy risks and claim verification |
| [Marketing effectiveness](references/marketing-effectiveness.md) | Brand vs activation and measurement horizons |
| [Testing and learning](references/testing-and-learning.md) | Creative experiments, campaign metrics and learning records |
| [Quality rubric](references/quality-rubric.md) | Skeptical buyer and editorial review |
| [Annotated sources](references/sources.md) | Primary research, Meta and open-source skill links |

## Operational workflows

See [the complete workflow guide](WORKFLOWS.md), which links to nine core stage runbooks **plus optional offering discovery (1A), Shopify diagnosis (1B), brand discovery (3A), Shopify catalog (3B), CRO (4A/4B), SEO (5A/5H), AEO (5B), promotion/social/creators/PR (5C–5F), Google Ads (5G), Shopify ads/feed tracking (5I) and Shopify lifecycle (9A), analytics/attribution/cohorts (8A–8C) and email/SMS/orchestration/deliverability (9B–9E)**, decision gates, and the source-backed operating loop.

## Templates and examples

- [Event/destination/consent QA matrix](templates/event-destination-and-consent-matrix.md), [marketplace ETL/reconciliation contract](templates/marketplace-extraction-and-reconciliation-contract.md), [audience/UTM activation brief](templates/audience-activation-and-suppression-brief.md), [sample pipeline manifest](examples/marketing-data-pipeline-manifest.json) and [validator](scripts/check_marketing_data_plan.py).

- [Email campaign brief](templates/email-campaign-and-creative-brief.md), [sender/consent audit](templates/email-deliverability-and-consent-audit.md), [SMS creative/permission brief](templates/sms-campaign-and-compliance-brief.md), [cross-channel journey map](templates/cross-channel-lifecycle-journey-map.md).
- [Marketing KPI dictionary](templates/marketing-measurement-and-kpi-dictionary.md), [incrementality experiment plan](templates/marketing-attribution-and-incrementality-plan.md), [RFM/cohort segments](templates/customer-rfm-cohort-and-segment-plan.md), [campaign performance review](templates/marketing-campaign-performance-review.md).
- [Ecommerce lifecycle example](examples/email-sms-ecommerce-lifecycle-example.md), [holdout/analytics example](examples/marketing-analytics-cohort-decision-example.md), [draft fixture](examples/messaging-plan-draft.json) and [checker](scripts/check_messaging_plan.py).

- [Shopify seasonal/bundle promotion brief](templates/shopify-ecommerce-promotion-brief.md)
- [Shopify store audit](templates/shopify-store-audit-and-roadmap.md), [collection/PDP content](templates/shopify-product-collection-content-brief.md), [Shopify CRO brief](templates/shopify-pdp-cro-brief.md), [SEO/merchandising audit](templates/shopify-search-merchandising-audit.md), [feed and pixel QA](templates/shopify-merchant-feed-and-pixel-qa.md), [lifecycle plan](templates/shopify-lifecycle-and-retention-plan.md) and [Shopify ecommerce worked example](examples/shopify-ecommerce-end-to-end.md)

- [Integrated promotion brief](templates/promotion-campaign-brief.md), [social hooks/calendar](templates/social-content-and-hooks-calendar.md), [creator collaboration brief](templates/creator-and-collaboration-brief.md), [press release/pitch kit](templates/pr-newsroom-and-pitch.md), [promotion review](templates/promotion-outcomes-review.md), and [promotion example](examples/promotion-from-research-to-distribution.md)
- [Google Ads Search blueprint](templates/google-ads-search-campaign-blueprint.md), [RSA creative asset sheet](templates/google-search-rsa-and-assets.md), [optimization/experiment brief](templates/google-ads-optimization-and-experiments.md), and [worked campaign](examples/google-ads-search-campaign-example.md)

- [Search and conversion audit](templates/search-and-conversion-audit.md), [CRO experiment brief](templates/cro-experiment-brief.md), [SEO/AEO/CRO worked example](examples/seo-aeo-cro-from-offering.md)

- [Brand discovery intake](templates/brand-discovery-intake.md), [messaging library template](templates/brand-messaging-library.md), and [worked example](examples/brand-discovery-to-copy.md)
- [Product and campaign intake](templates/intake.md)
- [Strategic marketing brief](templates/strategy-brief.md)
- [Output and example JSON contract](templates/output-format.md)
- [Simple vintage ring copy example](examples/vintage-ring.md)
- [End-to-end marketing diagnosis](examples/strategic-diagnosis.md)
- [Machine-readable example ad variants](examples/ad-variants.json)
- [Commercial operating brief](templates/operating-brief.md)
- [Ad concept and production brief](templates/creative-production-brief.md)
- [Experiment/decision log](templates/experiment-decision-log.md)
- [Research-to-sales workflow example](examples/workflow-from-research-to-sales.md)
- [Creative direction brief](templates/creative-direction-brief.md), [shot list](templates/shot-list-and-storyboard.md), and [creative review scorecard](templates/creative-review-scorecard.md)
- [Reels direction example](examples/reels-creative-direction.md) and [planned creative manifest](examples/creative-manifest.json)

All example products, buyer motives and ads are **illustrative**; do not treat them as real customer interviews, verified product claims or proven winners.

## Validation

```bash
python3 scripts/check_copy.py examples/ad-variants.json
python3 scripts/check_creative.py examples/creative-manifest.json
python3 scripts/check_search_ads.py examples/google-search-rsa-draft.json
python3 scripts/check_messaging_plan.py examples/messaging-plan-draft.json
python3 scripts/check_marketing_data_plan.py examples/marketing-data-pipeline-manifest.json
python3 scripts/check_links.py
python3 -m unittest discover -s tests -v
```

The copy and creative linters check structural issues, advisory lengths, planned dimensions/safe-zone overlaps and release metadata. It **does not** verify factual claims, brand effectiveness, buyer motives, Meta policy approval or advertising performance. Meta placement guides and current account previews take precedence over stale character-length rules.

## Boundaries

Read-only analysis and draft generation are the default. This skill does **not** authorize campaign publishing, changes to spend or ad account modifications. Sensitive-attribute targeting assumptions, fabricated scarcity, endorsements or claims, and misleading comparisons are prohibited by the skill. It is independent of, and not endorsed by, Meta.

License: [MIT](LICENSE).
