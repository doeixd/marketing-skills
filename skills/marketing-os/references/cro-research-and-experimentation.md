# CRO — commercial diagnosis, user evidence, testing and conversion quality

Reviewed 2026-11-06. Use with [CRO workflow](../workflows/04a-conversion-rate-optimization.md), [offer and conversion](../workflows/04-offer-and-conversion.md), and [measurement/experimentation](../workflows/08-measure-diagnose-experiment.md).

## 1. CRO is not button-color optimization

**Conversion Rate Optimization (CRO)** is a research-driven process for improving the rate at which appropriate visitors complete a meaningful goal, while protecting customer trust, product fit, margin and downstream quality. Improving signups that never activate, purchases that are mostly refunded, or leads that never qualify is **not necessarily business growth**.

The central question is: **where does a willing, qualified buyer encounter avoidable uncertainty, effort, confusion or mismatch?** Treat conversion as the result of traffic quality × relevance × trust × offer attractiveness × usable flow × operational readiness. These are hypotheses, not a literal mathematical causal decomposition.

**Optimize for the commercial outcome:** net contribution, completed purchases, qualified leads, retained customers or meaningful activation. Conversion rate, CTR, bounce, scroll or add-to-cart are diagnostic measures, not sufficient success metrics on their own.

## 2. Evidence-first diagnosis

Start with:
1. **Business/analytics integrity:** compare store/CRM orders with GA4 events and ad platform reporting; check duplicate events, time-zone differences, source attribution, refunds, chargebacks, consent, bot traffic and broken pixels. Never conclude a page failed from unreliable data.
2. **Funnel breakdown:** channel/query/campaign → landing-page arrival → product/offer comprehension → variant/quote selection → add-to-cart/form → checkout/lead submission → purchase → fulfillment, retention, refunds. Segment by mobile/desktop, new/returning, intent, country, inventory and relevant product category without p-hacking.
3. **Qualitative evidence:** usability task observation, customer support, site search, real objections, customer interviews, consented surveys, accessibility review, QA on devices/browsers; recordings/heatmaps (e.g. PostHog, Microsoft Clarity, Hotjar) are privacy-controlled clues (mask inputs, honor consent) rather than a stand-in for user research; for paid traffic, watch recordings segmented by campaign/UTM to see what ad visitors look at and where they leave. Ask non-buyers why with exit-intent, scroll-depth or one-question on-page surveys and post-purchase "what almost stopped you?" questions. **Never hijack the back button** or trap navigation: it angers visitors and is a [Google Search spam-policy violation](https://developers.google.com/search/blog/2026/04/back-button-hijacking) enforced from June 15, 2026.
4. **Page/offering reality:** ad/search promise vs product page, missing product facts, wrong hero/scale, opaque price/shipping/returns, unavailable variants, slow rendering, form errors, account walls.
5. **Competing explanations:** wrong traffic, seasonality, promotions, stock, platform delivery, measurement error, price and actual customer fit—not automatically "weak copy."

Use [Baymard's Product Page UX research](https://baymard.com/research/product-page) and [Checkout UX research](https://baymard.com/research/checkout-usability). Their benchmarking describes common friction among sampled sites, **not a guarantee** that a specific fix lifts conversion by a particular percentage.

Page-level structure, copy, forms, design and pre-launch tests are covered in the [landing page reference](landing-page-design-and-copy.md).

## 3. Fundamental user experience tests

| Decision stage | Questions to verify | Potential intervention |
|---|---|---|
| Arrival | Is the right product/offer visible and congruent with the ad/query? | Correct message match, actual offer availability |
| Comprehension | Can a first-time buyer state what this is, for whom, why useful and what's included? | Clear headline, short benefit summary, visuals |
| Evaluation | Can they compare variants, materials, scope, dimensions, performance, alternatives? | Real photos, specification table, comparisons |
| Trust/risk | Are policies, authenticity, shipping, security, warranties and contact visible and credible? | Surface real terms, genuine reviews, support |
| Price/cost | Do fees, taxes, delivery or terms surprise? | Cost transparency, clear policy and total price |
| Action | Is CTA explicit, variant choice possible, button functional, mobile layout usable? | UX/technical fixes and accessibility |
| Checkout/form | Is forced account creation, unnecessary data, confusing field behavior or error recovery blocking? | Guest checkout where viable, simpler forms, adaptive errors |
| Post-conversion | Does the delivered product match promise? What are cancellations, returns and quality? | Better pre-sale qualification, ops/product improvements |

Baymard's [2025 checkout findings](https://baymard.com/blog/current-state-of-checkout-ux) include guest checkout prominence, delivery dates, form labels and helpful error messaging. [2026 product-page findings](https://baymard.com/research-articles/current-state-ecommerce-product-page-ux) identify substantive PDP opportunity, especially on mobile. Use the actual research details rather than treating benchmark percentages as your site's projected lift.

## 4. Services, SaaS and lead generation

A service landing page must clarify **who it serves, actual scope/deliverables, process, timeline, price/range if available, proof and contact or booking next step**. Measure qualified contacts, show rates, opportunity creation, close rate and delivery quality, not raw forms alone.

For SaaS: distinguish trial signup → activation → retained use → paid conversion. Lower signup friction can increase low-fit accounts; check activation and downstream value. Demonstrate actual product, integrations and limits, and avoid fabricated logos/case studies.

## 5. Behavioral design without dark patterns

Reduce uncertainty, improve clarity and facilitate desired action; **never** manipulate with fake urgency, hidden subscriptions, prechecked add-ons, coercive consent, misleading prices, disguised buttons, frictionful cancellation or fictitious endorsements. A "persuasive" page should still allow the user to decline easily. Accessible design is part of CRO, not an optional extra.

Relevant [Nielsen Norman Group product pages](https://www.nngroup.com/reports/ecommerce-ux-product-pages-including-reviews/) and [trust/credibility research](https://www.nngroup.com/reports/ecommerce-ux-trust-and-credibility/) emphasize adequate detail, reviews, pricing, accurate media and trustworthy policies. More persuasive copy cannot repair a bad or unviable offer.

## 6. Prioritize interventions by evidence, leverage and effort

Use `issue → evidence/confidence → affected buyer/step → expected commercial mechanism → fix/test → owner → measurement`.

**P0:** broken purchase, invalid tracking, unsupported claim, prohibited product, out-of-stock promoted item, wrong price, security/privacy or major accessibility blocker.

**P1:** clear friction affecting high-intent visitors: contradictory ad/PDP, missing required specs, surprise shipping, variant errors, unclear CTA, poor mobile usability.

**P2:** uncertain improvements and optimization opportunities requiring experiment: messaging prominence, layout, visual sequencing, explanation length, reassurance placement, comparison presentations.

Prioritize *fixing defects* when obvious rather than demanding an A/B test to see whether checkout should work. An impact/effort/confidence score is a planning heuristic, not a scientifically validated lift estimate.

## 7. Design experiments that can answer a question

Before launch pre-register:
- Hypothesis explaining **mechanism** and target population, rather than "version B will win".
- Unit randomized (visitor/account/session); assignment, exposure, contamination/crossover, returning-user consistency and rollout guardrails.
- Primary **commercial outcome** and denominator; secondary/diagnostic metrics; **guardrails** (margin, returns, latency, complaints, accessibility, fairness).
- Baseline and minimum detectable effect; realistic sample size/power/time to collect a business-relevant signal.
- Planned analysis/decision rule, confidence interval or Bayesian criterion consistent with chosen method.
- Seasonality, promotion, channel-mix shifts, stock/price changes, new variants, multiple testing and sample-ratio mismatch (SRM) checks.
- Responsible data handling and accessibility review.

**Don't** peek repeatedly and stop at the first unadjusted `p < 0.05`; don't infer causality from a before/after screenshot, platform ROAS, or cherry-picked cohorts. If not enough volume for a controlled experiment, use usability observation, clearer baseline measures and explicitly labeled directional evidence. A/B testing can fail to answer business questions when users are not randomly assigned, exposure is mismeasured or sample size is too low.

## 8. Post-test decision loop

Record `hypothesis → change → experimental setup → raw data/quality checks → result + uncertainty → guardrail outcomes → decision (ship/iterate/stop/inconclusive) → follow-up`.

Compare end-to-end outcomes, not only clickthrough. A page variant can raise add-to-cart yet lower net contribution or raise returns; avoid calling that a win without considering business goals.

Monitor after shipping: test results may fail to generalize across seasons, segments, device changes or other offers. Watch for instrumentation drift and guardrail deterioration.

## 9. Measurement and tools

- Store/CRM transactions and refunds; server-verified revenue where appropriate.
- GA4 or comparable event analytics; events tied to business steps and consent/privacy rules.
- Search Console for search-side queries/pages/clicks to connect user intent to landing outcomes.
- Product-page/checkout usability tests and functional QA (including keyboard/screen reader).
- Real-user Web Vitals; see [web.dev metrics](https://web.dev/articles/vitals) for LCP, INP and CLS.
- Experiment platform or a trustworthy assignment/analysis service; check SRM and denominator integrity.
- [Corey Haines Marketing Skills](https://github.com/coreyhaines31/marketingskills): `cro`, `signup`, `onboarding`, `analytics`, `conversion-tracking`, `ab-testing` — useful agent workflow examples, not proof that tactics work.
- [Baymard Product Page UX](https://baymard.com/research/product-page), [Checkout UX](https://baymard.com/research/checkout-usability) and [2025 checkout practices](https://baymard.com/blog/current-state-of-checkout-ux).
- [Nielsen Norman Group Product Pages](https://www.nngroup.com/reports/ecommerce-ux-product-pages-including-reviews/), [Trust and Credibility](https://www.nngroup.com/reports/ecommerce-ux-trust-and-credibility/).
- [Google Search Console + GA4](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console).
