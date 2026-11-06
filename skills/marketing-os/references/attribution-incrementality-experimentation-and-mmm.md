# Attribution, experimentation, incrementality and marketing mix modeling

Reviewed 2026-11-06. Use [Attribution Workflow 8B](../workflows/08b-attribution-incrementality-and-experiments.md), [Experiment Brief](../templates/marketing-attribution-and-incrementality-plan.md), [Analytics Reference](marketing-analytics-data-model-and-reporting.md), and [General Experiments 8](../workflows/08-measure-diagnose-experiment.md).

## 1. The three questions marketers often conflate

**Descriptive attribution:** "Which touches receive *credit* under a chosen rule?" Last-click, first-click, data-driven/multitouch and platform self-attribution allocate observed conversions. Every model sees a partial journey and can double-count across Google, Meta, Shopify and ESP. Example: a customer sees Meta, clicks Google Search, opens an email and buys; all three platforms may claim the same order. Their sum cannot be presented as incremental sales.

**Incrementality:** "What would have happened without this action?" Requires credible counterfactual via randomized holdout, geo-test, experiment or defensible causal design.

**Marketing Mix Modeling (MMM):** "What portion of aggregate outcomes can be associated with channel spend and external factors over time?" Models need sufficient volume/variation and assumptions; observational MMM is not automatic randomized proof. **Calibrate MMM with experiments** where feasible.

Choose method based on actual decision, scale, channel, technical feasibility, privacy, business risk, and available data.

## 2. Prioritize experiments before elaborate dashboards

| Decision | Suitable method | Limitations |
|---|---|---|
| New welcome email subject lines | Person-level A/B on *eligible* recipients, actual conversion/quality | Multiple tests, overlapping sends, false-open metrics |
| Does an abandoned-checkout sequence add profit? | Customer-level no-message/control holdout, with legally valid contact eligibility | Contamination from other campaigns, late orders |
| Does SMS improve on email alone? | Multi-arm randomized channel assignment among customers with **both** opt-ins | Selection bias if groups differ in consent |
| Does a paid channel create incremental revenue? | Platform conversion lift, customer/account holdout or geo experiment | Platform eligibility, interference, power, seasonality |
| Which paid channel should gain budget? | Geo experiments / calibrated MMM where spend and data support | Data density, effects across channels and cost |
| Checkout CTA layout | Valid storefront A/B experiment, randomized shopper | Stable assignment, eligibility, performance, simultaneous changes |

If a defect exists (broken checkout, false price, spam to unsubscribed users), **fix it** without testing whether harm converts.

## 3. Randomized email/SMS holdout design

Choose one **unit** (customer, account or household) and stable assignment before treatment; apply campaign eligibility and marketing permission before assignment. Define control "no marketing message" or standard message with legal/service communications unaffected; do not withhold required transactional/safety notices. Decide sample allocation, one primary outcome, denominator, period/lag and minimum economically meaningful effect **before** testing.

Check:
- Reproducibility and stable IDs, CRM/ESP sync and membership changes;
- Sample-ratio mismatch (SRM), balance, cross-exposure, frequency and control contamination;
- Exclusions and randomization effects; completed purchase, contribution and return quality;
- Consent/privacy and eligibility;
- Power; if volume too small, label test inconclusive rather than overstate 1 or 2 purchases;
- Multiple comparison and repeated peeking; choose analysis rule before results.

**Incremental lift per eligible contact** = `(treatment outcome / treatment eligible population) – (control outcome / control eligible population)` under comparability. For monetary tests specify `net contribution per recipient`, subtract message/discount/production cost and state when measured. Relative lift requires meaningful nonzero baseline. A confidence interval/power is essential for inference; raw observed gap isn't proof.

## 4. Geo incrementality and MMM

For media channels or campaigns, geography-based randomization/paired markets can compare outcomes under changes, controlling for trends in suitable untreated markets. Check matching, spillover, seasonal promotions, market-level budgets, inventory/service differences, measurement and time horizon; no naive before/after difference as "lift."

[Google Meridian](https://developers.google.com/meridian/mmm) is an open-source Bayesian MMM framework; as of September 2026, version 2.0 offers updated full-funnel analysis and geo experiment calibration. [Meridian GeoX](https://developers.google.com/meridian/geox) offers geo-based incrementality methods. These tools require sufficient modeled media/outcome data, technical expertise and careful diagnostics; **a small store with a month of sales should not receive a fake precise MMM forecast**.

Use RCTs/lift studies for short specific questions, meaningful dashboard/cohorts for ongoing operations, and MMM when data supports broad allocation. Model outputs aren't mandates for spend; use unit economics and real business constraints.

## 5. Attribution and reporting discipline

Document:
- Shopify/GA4/Google/Meta/Klaviyo conversion window and attribution model as actually configured;
- Net vs gross sale value, returns, order timestamp vs click timestamp and timezone;
- Deduplication across systems and how direct/branded demand is represented;
- Consent/privacy and modeled conversions;
- Channel/customer cohort overlaps, retargeting vs new customer role;
- **What is observational**, what is randomized, what remains unknown.

High ROAS, attributed revenue and "recovered cart" totals are **diagnostics**, not proof of added profit. If channel credited revenue surpasses store realized sales, first reconcile overlapping credit definitions rather than alleging accounting fraud.

## 6. Experiment library / prioritization

Maintain `experiment ID | decision | audience | unit | control | treatment | primary KPI | guardrails | power/MDE | planned duration | QA | results and uncertainty | decision/owner`.

Prioritize high-leverage uncertainties: channel incrementality, paid vs free acquisition, email/SMS contribution, frequency cap, offer value vs discount margin, product-page comprehension. Hypothesis and effect size should come from actual data; avoid a "top 10 A/B hacks" list.

## 7. Sources

- [Google Meridian MMM](https://developers.google.com/meridian/mmm) and [GeoX](https://developers.google.com/meridian/geox)
- [Shopify marketing attribution reports](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/marketing-reports)
- [GA4 conversion vs key event attribution](https://support.google.com/analytics/answer/13965727)
- [GA4 ecommerce event implementation](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce)
- [AMEC Integrated Evaluation Framework](https://amecorg.com/amecframework/)
- [Klaviyo reporting/attribution skill patterns](https://github.com/thatrebeccarae/claude-marketing/blob/main/skills/klaviyo-analyst/SKILL.md)
- [Corey Haines Attribution/AB Testing Skills](https://github.com/coreyhaines31/marketingskills)
