# Workflow 4B — Shopify ecommerce CRO: discovery → PDP → cart → checkout

**Trigger:** Store conversion weakness, "optimize Shopify product page", cart/checkout issues, mobile friction, paid traffic not converting, theme improvements, AB tests or customer confidence.

**Place:** Stage 4 specialist. Read [Shopify CRO guide](../references/shopify-ecommerce-cro-and-checkout.md), [general CRO 4A](04a-conversion-rate-optimization.md), [Shopify theme guide](../references/shopify-theme-performance-and-measurement.md), and use [PDP brief](../templates/shopify-pdp-cro-brief.md).

## 0. Evidence and plan gate

Verify exact store plan, theme vs headless, market, actual theme/access rights, time series/report definitions, user segments, customer service insights, costs/policies and store events. Note September 2026 session-measurement change. Without Shopify admin access, publicly observed UI problems are findings but internal funnel diagnosis remains **unverified**.

## 1. Walk real buyer tasks

Test mobile and desktop journeys from relevant ad/search → category/collection → product/variant → cart → checkout with approved testing (no unwanted charges). Evaluate promise match, product classification, real photos/scale/video, specs, variant selection, availability, delivery cost/time, size/care, return policy, reviews, payment and support. Document screenshots/page references when available, error reproduction and severity.

## 2. Classify blockers

**P0:** broken buying, false price/stock/policy, security/privacy, inaccessible essential CTA or invalid conversion event.
**P1:** actual user confusion: poor filtering/search, absent sizing/materials, contradictory ads, unexpected shipping/duties, app obstruction, slow/unstable mobile UI.
**P2:** uncertainty suitable for testing: hero hierarchy, feature-vs-benefit order, gallery sequencing, reassurance position, recommendation mix, bundle presentation.
Real limitations (bad quality/fit, high cost) require product/offer fixes rather than copy theater.

## 3. Shopify-specific implementation

Use Search & Discovery, collection/variant/metafield quality, theme sections and app blocks; inspect app performance and Liquid server output. **Checkout information/shipping/payment UI extensions generally require Shopify Plus**; standard brand editor and some thank-you/status extensions are available more broadly. Check actual plan before suggesting code. Do not recommend legacy checkout.liquid modifications as a universal tactic.

## 4. Draft and validate change

Deliver `issue → evidence → buyer job → exact page/section/Shopify surface → proposed copy/design/data diff → cost/effort → owner → guardrail`. For P0/P1 use correctness/usability QA. For P2 preregister randomized test with sufficient volume and stable assignment, purchase/contribution primary metric, returns/complaints/loading guardrails and stop rule. Don't invent lift estimates.

## 5. Follow-up and handoff

Compare real purchase, profitability, qualified intent and satisfaction with data limitations; don't declare a conversion gain from sessions/CVR before/after September 2026 without accounting for measurement definition. Update [offering](01a-offering-discovery-and-marketing-plan.md), [merchandising](03b-shopify-catalog-and-merchandising.md), [SEO](05h-shopify-ecommerce-seo.md), [paid channels](05i-shopify-shopping-ads-and-tracking.md).

**Stop:** no unsupported quality/policy claims, fake social proof, fabricated scarcity, deceptive subscriptions, unauthorized checkout/theme edits. Publishing requires user approval.
