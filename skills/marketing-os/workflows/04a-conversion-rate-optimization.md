# Workflow 4A — CRO diagnosis → friction/offer fixes → experiments → profitable conversion

**Trigger:** High traffic but few purchases, cart abandonment, unqualified leads, weak signup→activation, landing-page request, mismatched ads/SEO, poor form completion, product page/trust questions or conversion optimization research.

**Position:** Optional deep-dive under [Stage 4 Offer/Conversion](04-offer-and-conversion.md) and feeds [Stage 8 Measurement](08-measure-diagnose-experiment.md). Use [CRO reference](../references/cro-research-and-experimentation.md), [Offering 1A](01a-offering-discovery-and-marketing-plan.md), [Buyer Discovery 2](02-buyer-discovery.md), and [CRO Experiment Brief](../templates/cro-experiment-brief.md).

**Goal:** improve **qualified** customer success, not just click-to-cart or form volume.

For a single page, score it with the [landing page review scorecard](../templates/landing-page-review-scorecard.md) and the [landing page reference](../references/landing-page-design-and-copy.md); to build a replacement use [4D](04d-landing-page-build.md).

## 0. Goal, definition and data quality
- Specify the true conversion event (completed purchase, profitable order, qualified lead, appointment attended, activation or retained customer), metric denominator, reporting dates and relevant traffic sources.
- Reconcile store/CRM outcomes with GA4/pixel/session data. Check currency, tax/shipping, duplicate events, consent, bot traffic, seasonality, refunds and model attribution. Don't treat marketing platform ROAS as net incremental profit.
- If tracking appears broken, fix measurement before diagnosing copy with suspect conversion rates.

## 1. Map actual user and buying journey
`ad/search/organic → landing → product/offer comprehension → evaluation → variant/quote → cart/form → checkout/submission → fulfillment/activation`.

For each step ask:
- Did we attract the *right person with an honest promise*, or merely a click?
- Can a newcomer immediately tell what it is, who it suits and why it is desirable?
- What is included? What specs/limits/price/shipping/returns/terms matter for this buyer?
- What fears or objections remain unresolved? Is reassurance truthful?
- Can they complete the desired action on mobile, by keyboard, with assistive technology?
- Are form requirements, field validation, checkout login, delivery timing or payment errors creating avoidable friction?
- After purchase, are returns, disputes, activation and complaints rising?

Use actual funnel events **and** first-hand qualitative observations (usability tasks, customer feedback, support, on-site search, consent-respecting session recordings if available).

## 2. Diagnose the binding constraint
| Observed symptom | Competing hypotheses | Evidence to collect | Typical decision |
|---|---|---|---|
| Ads generate clicks, few landing views | Slow/broken page, redirects, accidental clicks, measurement | Mobile load, click path, pixels | Fix technical/traffic issue |
| Search traffic high, no purchase | Informational intent or weak offer/page, wrong geo | Search query mix, onsite behavior, interviews | Route to better page/intent; improve offer |
| PDP views, low cart actions | Unclear value, poor imagery, price, variants, trust | User task tests, objections, pricing comparisons | Clarify features, photos, assurances or price |
| Cart starts, checkout abandoned | Surprising fees, forced registration, errors, no payment option | Checkout QA, error logs, support | Fix UX/policy/checkout |
| Forms complete but leads unqualified | Promise/target mismatch, no qualification | CRM lead quality and sales calls | Correct copy, targeting and fit |
| Signups high, activation low | Onboarding or product mismatch | Activation cohorts, research | Fix onboarding and prospect expectations |
| Purchases rise but contribution falls | Discounts, fees, low-margin mix, returns | Net unit economics | Optimize business outcome, not vanity CR |

## 3. Fix first, then test meaningful uncertainty
- **P0 operational defects:** broken purchase, false price, no stock, security/consent issues, inaccessible critical action, unusable form. Repair and verify, rather than running A/B tests of known breakage.
- **P1 evidenced friction:** ambiguous value proposition, missing sizing/specs, real shipping/returns, unclear scope, nonfunctional selection, conflicting ad/PDP. Improve with source evidence and user testing.
- **P2 competing plausible designs:** visual order, CTA positioning, comparison format, social-proof placement, amount of detail. Develop testable hypotheses.

Respect user autonomy; avoid fake urgency, hidden recurring terms, obstructive cancellations, false social proof and deceptive consent. Do not "optimize" by hiding materially relevant drawbacks.

## 4. Create a controlled experiment when feasible
In [CRO experiment template](../templates/cro-experiment-brief.md) document:
- Buyer segment and decision moment, baseline, hypothesis and *mechanism*.
- Control and treatment descriptions, primary metric and denominator, business guardrails.
- Randomization unit (visitor/account), stable assignment, exposure and cross-device considerations.
- Minimum detectable effect, statistical power and sample requirements; expected runtime based on measured traffic, not guessed.
- SRM (sample-ratio mismatch), errors, latency, refunds, guardrails, multiple comparisons and planned stopping/analysis rule.
- What decision follows benefit, harm or inconclusive result.

No adequate sample? Use qualitative usability testing, task success measures, carefully monitored fixes and label before/after observations **noncausal**.

## 5. Evaluate, decide and monitor
- Check experiment integrity before outcome. Compare net revenue/contribution, qualified leads or retention; evaluate secondary and guardrail metrics.
- Report estimates *with uncertainty*; do not treat a `p < .05` claim as proof of a universal improvement.
- Decide ship/iterate/stop/inconclusive, document why, update product/brand claims and creative.
- Observe post-launch outcomes and traffic mix changes. A lift in add-to-cart with higher returns may be a net loss.
- Handoff to [Creative 6](06-creative-production.md), [SEO 5A](05a-seo-and-organic-search.md), [Offering 1A](01a-offering-discovery-and-marketing-plan.md) or [Measurement 8](08-measure-diagnose-experiment.md).

**Output:** prioritized CRO findings with buyer evidence, defects/fixes, experiment brief, page/offer copy recommendations, verification and learning plan. **Do not** recommend spending more on ads before critical conversion blockers are resolved.

**Sources:** [Baymard product page](https://baymard.com/research/product-page), [2026 product-page best practices](https://baymard.com/research-articles/current-state-ecommerce-product-page-ux), [checkout research](https://baymard.com/research/checkout-usability), [Nielsen Norman Group product page UX](https://www.nngroup.com/reports/ecommerce-ux-product-pages-including-reviews/), [trust research](https://www.nngroup.com/reports/ecommerce-ux-trust-and-credibility/).
