# Workflow 8B — Marketing attribution → incremental impact → valid experimentation

**Trigger:** ROAS/ROI across channels, "did email/SMS cause these orders?", attribution model comparison, lift study, Google/Meta/Shopify discrepancies, email holdout, testing strategy, geo experiments, marketing mix modeling, budget allocation, causal analysis.

**Place:** Stage 8 specialist with [Attribution/Incrementality Reference](../references/attribution-incrementality-experimentation-and-mmm.md), [Experiment Plan](../templates/marketing-attribution-and-incrementality-plan.md), [Analytics 8A](08a-marketing-analytics-and-measurement.md), [Customer 8C](08c-customer-segmentation-rfm-and-clv.md). General tests: [Stage 8](08-measure-diagnose-experiment.md).

## 0. Separate credit from causality

Clarify whether user needs **descriptive attribution**, **real incremental effect**, or **aggregate MMM allocation**. Record goal, time horizon, spend and opportunity cost, available measurement, market, consent and reporting differences. Never sum Google + Meta + ESP "attributed orders" as separate sales.

## 1. Reconcile data and identify decision

List actual store/CRM orders, returns and margin as business truth, compared with GA4/Google Ads/Meta/Klaviyo/Shopify credit models and windows. Identify channel overlaps, new vs repeat demand, brand cannibalization, time zones, platform modeling and missing interactions. Explain which analysis is possible with real data, not an imaginary tool connection.

## 2. Select measurement method to fit scale

- **Person-level randomized holdout** for promotional emails, SMS and comparable audience treatments where eligibility and consent are valid. Never withhold required order/security notices.
- **Campaign or landing A/B** for real creative/UX uncertainty; not to test broken code or compliance.
- **Platform lift test** where eligibility and provider access permit; declare platform limitations.
- **Geo randomized or quasi-experimental study** for broader paid impact, with matching, spillover, seasonal and inventory safeguards.
- **MMM** (e.g. Meridian/GeoX) for large enough multi-channel historical datasets; report assumptions, calibration, sensitivity and uncertainty. Not warranted for small/noisy datasets.

## 3. Pre-register the design

Write [Experiment Plan](../templates/marketing-attribution-and-incrementality-plan.md): treatment vs control, randomization unit, eligible audience/market, exclusions, actual objective **per eligible customer** or contribution, discount/message costs, MDE/power/runtime given data, conversion delay, primary metric, quality guardrails, SRM/contamination and decision rule. SMS-email channel experiments must compare among people **consented to both**; no synthetic "holdout" composed of non-subscribers.

## 4. QA and run *only with authorization*

Check assignment remains stable, all systems respect control (no other ESP re-sending campaign), tracking and order dedupe, legal/service messages unaffected, spend/sender caps, rollback and data access. No campaign/send/experiment activation or budget change without user approval.

## 5. Evaluate and decide

Check SRM and integrity first, then compare outcomes with uncertainty (confidence/credible intervals per actual design). Calculate **net contribution lift after send/discount/media cost**, not just clicks or attributed sales. Analyze guardrails (unsubscribe/complaints, returns, customer satisfaction) and possible alternative causes.

**Deliver:** one clear answer to the decision with what is known vs unsupported, measurement method/plan, result (if actual data), and ship/iterate/stop/inconclusive recommendation. No fake causal claims from platform dashboards.
