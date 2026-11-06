# Data-driven marketing foundations: measurement design, trustworthy events and decision reporting

Reviewed 2026-11-06. Use [Analytics Workflow 8A](../workflows/08a-marketing-analytics-and-measurement.md), [Measurement Dictionary](../templates/marketing-measurement-and-kpi-dictionary.md), [Campaign Decision Report](../templates/marketing-campaign-performance-review.md), [Attribution 8B](../workflows/08b-attribution-incrementality-and-experiments.md) and [Customer Analytics 8C](../workflows/08c-customer-segmentation-rfm-and-clv.md).

## 1. Ask what decision the data must support

Marketing analytics is the practice of measuring changes in customer/business outcomes **with explicit definitions, denominators, data quality and uncertainty**. A dashboard is a tool for deciding—not a substitute for a testable question.

Write a `decision → hypothesis → necessary outcome → acceptable proxy → source / event → unit of analysis → segment → expected latency → review rule` before choosing charts, tools or attribution models. Examples:
- Should we spend more on nonbrand Search? Outcome: incremental qualified contribution; diagnostics: relevant clicks, new buyers and valid orders.
- Which product pages are losing interested buyers? Outcome: verified purchases/returns; diagnostics: accurate view→cart→checkout funnel, UX evidence.
- Does winback email create extra purchases? Outcome: incremental contribution per eligible recipient; diagnostic: ESP delivery/click, randomized holdout.
- Which buyers might respond to replenishment? Outcome: relevant true repurchase, not a fabricated generic 30-day cycle.

## 2. Source hierarchy and reconciliation

Define **authoritative source** for each fact:
- **Commerce/CRM**: completed orders, refunds/cancellations, products, fulfilled/returned state, realized margin, qualified leads and closed revenue.
- **Web/app analytics (e.g. GA4)**: acquisition sessions and event journeys within consent/identity coverage.
- **Ad/ESP platform**: media spend, sends and attributed results **under its own windows and methodology**.
- **Search Console/platform visibility**: queries/impressions/clicks under platform reporting rules.
- **Customer research**: usability, actual motivations, satisfaction and service problems, not reducible to pixels.

**Reconciliation checklist**: store vs GA4 purchase counts and value; same reporting date and timezone; refunds/discount/tax/shipping definition; order ID dedupe; consent/modeling vs measured events; cross-domain checkout; checkout attribution redirects; test orders/bots; ESP and ads double claiming revenue; currency conversion; product variant ID; email/SMS campaign tags.

**Shopify's September 2026 session measurement update** creates denominator discontinuities: check [Shopify documented changes](https://help.shopify.com/en/manual/reports-and-analytics/discrepancies/session-measurement-update) before interpreting historical conversion-rate jumps.

## 3. Event data contracts

Design a documented schema with:
- Event name and **business meaning**, emit timing, trigger/entry source, event version and owner;
- Stable `event_id` for dedupe, `transaction_id` for purchase/refund linkage, `occurred_at` timezone and `ingested_at` for late events;
- Object IDs (product/variant/sku) consistently mapped to catalog and actual orders;
- Consent/privacy status and jurisdiction **where legally and technically allowed** (no casual profile PII leak to ad/URL);
- Campaign `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term` where relevant, naming taxonomy and internal link exceptions;
- Revenue, tax, shipping, discounts, currency, **net/refunded amount**, contribution estimate with clear profit-accounting policy;
- Primary conversion vs intermediate events; identity joining with lawful first-party IDs and permissions.

For GA4 ecommerce events use documented recommended `view_item`, `add_to_cart`, `begin_checkout`, `purchase`, `refund`, `items`, `transaction_id`, `value`, `currency`; [Google Ecommerce Measurement](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce). Event semantics and GA4 default reporting can differ from Shopify reports and Google Ads conversions; do not silently equate them.

**Example minimal event rows (fictional)**:
`event_id,occurred_at,event_name,subject_key,order_id,product_variant_id,value,currency,consent_state,utm_campaign,source_system`.
`subject_key` can be pseudonymous and need not be an actual email/phone. Analytics tools and ad destinations must not receive prohibited PII. Store raw customer identifiers only when needed, lawfully and securely.

## 4. KPIs: exact numerator/denominator/meaning

| Metric | Operational definition (adapt and write down) | Misinterpretations |
|---|---|---|
| Purchase conversion rate | Completed eligible orders / eligible sessions or visitors **per chosen system** | Different session definitions; repeat visits/identity/consent |
| Average order value (AOV) | Chosen net/gross order revenue / completed orders | Discounts, refunds, tax/shipping inclusions |
| Contribution before marketing | Net realized sales minus variable COGS, fulfillment, processing, return costs | ROAS ≠ profit; fixed costs different |
| Customer acquisition cost (CAC) | Relevant acquisition cost / *new* qualified buyers, with attribution/incrementality caveat | Mixed retargeting or existing buyers |
| Revenue per delivered email | ESP-attributed revenue / delivered messages (platform view) | Not incremental revenue per contact |
| Incremental contribution per eligible contact | (Treatment − valid control outcome) / relevant eligible population | Needs randomized/stable control and cost |
| Email click rate | Unique clickers / delivered (or other documented provider definition) | Link scanners, duplicate clicks, definitions |
| SMS opt-out rate | Unique opt-outs / delivered or sent (define system) | Channel/period cohort differences |
| Gross customer value | Observed cumulative order revenues / customer cohort | Ignores margin/returns/causal acquisition |
| Qualified lead rate | Leads passing an agreed CRM stage / relevant lead denominator | Sales cycle delay, qualification changes |

No "average click rate" or vendor benchmark can replace a store's actual customer and economics baseline. GA4's [key event vs Ads conversion distinctions](https://support.google.com/analytics/answer/13965727) and account attribution choices matter.

## 5. Dashboard design and analytical queries

Default dashboard sections:
1. **Business pulse**: realized orders, net sales, contribution, new vs repeat, returns/service and seasonality.
2. **Demand and acquisition**: channel spend and relevant traffic by device/market/intent, brand/nonbrand and campaign.
3. **Buyer decision funnel**: product views, add-to-cart, checkout, purchase (consistent eligible users and events).
4. **Lifecycle**: eligible audience, campaigns vs automations, sends, deliverability, unsubscribes, clicks, conversion quality and held-out lift.
5. **Cohorts**: first purchase month, repeat rate, margin by cohort and LTV limits.
6. **Experiments**: changes, assignment, MDE/sample, confidence/uncertainty and business decision.
7. **Data quality**: event coverage, missing IDs, duplicates, failed sync, platform attribution deltas and red flags.

Choose **trend and relevant denominators** over eye-catching totals. Annotate promotions, pricing, tracking/tag changes and store updates. Slice only where sample supports interpretation and privacy thresholds permit; don't turn 40 microsegments into misleading "statistical insights."

GA4 BigQuery export and Shopify/CRM data warehouse may support joined analysis; verify **real integration and data availability**, data retention and account access. Use BigQuery SQL or comparable tools if present; don't claim that a sample query has been run without access. Avoid sending raw customer PII to an LLM when aggregated/pseudonymous metrics suffice.

## 6. Forecasting vs causal knowledge

Descriptive reports answer **what happened**. Predictive models answer **what may happen under assumptions**. A/B tests, geo experiments and calibrated MMM attempt to answer **what changed because of marketing**, with model design limitations. **Last-click attribution is descriptive credit allocation, not causality.**

For forecast or anomaly analysis state observed baseline, window, seasonality, data completeness, model/hypothesis, likely error and decision sensitivity. Do not invent confidence intervals or causal certainty when no experiment exists. Track policy and technical changes over time.

## 7. Sources

- [Google Analytics ecommerce events](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce)
- [Google Analytics key events and conversions](https://support.google.com/analytics/answer/13965727)
- [GA4 BigQuery export](https://support.google.com/analytics/answer/9358801)
- [Shopify marketing reports / attribution options](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/marketing-reports)
- [Shopify Session Measurement Update 2026](https://help.shopify.com/en/manual/reports-and-analytics/discrepancies/session-measurement-update)
- [Google Meridian MMM](https://developers.google.com/meridian/mmm)
- [Corey Haines Analytics/Attribution Skills](https://github.com/coreyhaines31/marketingskills)
