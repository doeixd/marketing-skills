# Workflow 8A — Marketing analytics: business question → event contract → dashboard → decision

**Trigger:** User wants ecommerce/marketing analytics, KPI dashboard, GA4, Shopify reports, campaign report, tracking plan, marketing data export, data-driven decisions, anomaly diagnosis, funnel metrics or data quality audit.

**Place:** Specialist within [Stage 8](08-measure-diagnose-experiment.md). Read [Analytics Fundamentals](../references/marketing-analytics-data-model-and-reporting.md), [KPI Dictionary](../templates/marketing-measurement-and-kpi-dictionary.md), [Performance Review](../templates/marketing-campaign-performance-review.md); use [Attribution 8B](08b-attribution-incrementality-and-experiments.md), [Cohorts/RFM 8C](08c-customer-segmentation-rfm-and-clv.md) and [Shopify 1B](01b-shopify-ecommerce-diagnosis.md) when relevant.

## 0. Ask what decision is needed

Define specific owner decision and commercial/brand goal: increase qualified leads, validate organic acquisition, allocate paid budget, improve PDP conversion, retain profitable customers, or evaluate promotion. Specify period, market, store/CRM ground truth, current data and tool access. Do not claim live access to Shopify, Google Analytics, ESP or ad platforms without verifying. If files are provided, read them; if not, request necessary narrow exports **only when critical**.

## 1. Create exact metric dictionary

For every decision define `KPI | numerator | denominator | time window | identity/unit | source | currency | status | guardrails`. Prioritize completed orders/qualified leads, realized net contribution and retention when available. Diagnostic metrics may include qualified traffic, funnel events, email delivered/clicks, SMS STOP, search intent, media spend and costs. In particular:
- Conversion rates can change when **denominator definitions** change (Shopify September 2026 session update).
- Google Analytics **key events** and Google Ads **conversions** can have different attribution and count definitions.
- Pixel/ESP platform credited revenue can overlap across channels.
- Gross orders/revenue don't establish margin or additional buyers.

## 2. Audit collection and identity

Map actual `purchase/refund/lead/status/qualified` events and customer/order IDs. Check duplicate purchase events, test orders, currency, taxes/shipping/discounts, late events, consent coverage, source/medium/campaign UTM naming, GCLID/link redirects, server/browser dedupe and checkout domain. Pseudonymize where possible and never export full customer email/phone histories as an ordinary analysis prerequisite.

Compare order ledger to GA4 and platform event reports for same timeframe and definition. Document missing or modeled conversions and data delay. Do not diagnose performance before noting serious discrepancies.

## 3. Segment meaningful buyer/business decisions

Use product/market/category, channel intent (brand/nonbrand), device, new/returning, actual cohorts and permissions, margin and refund type. Avoid low-sample segment fishing and sensitive trait inference. For customer RFM/cohorts use [8C](08c-customer-segmentation-rfm-and-clv.md); for email/SMS, distinguish send eligibility and channel list growth from raw customer counts.

## 4. Build analysis/report

Use [KPI Dictionary](../templates/marketing-measurement-and-kpi-dictionary.md) and [Performance Review](../templates/marketing-campaign-performance-review.md). Include business pulse, acquisition spend/qualified demand, funnel, email/SMS lifecycle, cohort retention, experiment evidence, alerts and integrity checks. Every chart/table should display **period, source, denominator and caveats**, and avoid double-summing attributed revenue.

If data supports it, use GA4/Shopify extracts/BigQuery; do not invent SQL output. Define anomalies relative to actual baseline, promotions, seasonality and tracking releases. Prefer plain-language actionable findings over a maximal dashboard.

## 5. Choose intervention vs experiment

Prioritize broken tracking or checkout, unsupported claims, costly sending/compliance errors. If evidence suggests a buyer decision problem, route to [Offering 1A](01a-offering-discovery-and-marketing-plan.md), [CRO 4A](04a-conversion-rate-optimization.md) or [Shopify 4B](04b-shopify-ecommerce-cro.md). For channel effectiveness use [8B](08b-attribution-incrementality-and-experiments.md). For customer groups use [8C](08c-customer-segmentation-rfm-and-clv.md). Propose test or operations fix with owner and business guardrails.

**Deliver:** a source-linked metric dictionary, integrity/coverage notes, measured baseline and evidence-qualified diagnosis, a prioritized recommendation, dashboard/report schema, and review cadence. No invented metrics, notional "20% improvement", unauthorized tracking changes or disclosure of raw PII.
