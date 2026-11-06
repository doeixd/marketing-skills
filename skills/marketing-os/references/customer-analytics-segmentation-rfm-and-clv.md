# Customer analytics: RFM, cohorts, meaningful segmentation and customer value

Reviewed 2026-11-06. Use [Customer Analytics Workflow 8C](../workflows/08c-customer-segmentation-rfm-and-clv.md), [Segmentation Template](../templates/customer-rfm-cohort-and-segment-plan.md), [Lifecycle Orchestration 9D](../workflows/09d-cross-channel-lifecycle-and-segmentation.md) and [Analytics 8A](../workflows/08a-marketing-analytics-and-measurement.md).

## 1. Segments should change useful treatment, not just spreadsheet labels

Segments must answer **which buyers have different needs, motivations, constraints, response to a useful action or economics**. Source labels only from lawfully collected/available data. Priority:
1. **Lifecycle stage**: prospect, first purchase, active repeat, at-risk by actual category, naturally dormant, return/complaint.
2. **Product/job**: purchased category/material/size or intentionally selected interest, occasion where evidenced.
3. **Behavioral**: checkout stage, recent product research, service questions, verified engagement.
4. **Economic**: first-order contribution, cohort margin, actual realized return cost—not "VIP" based on gross spend alone.
5. **Preference/channel**: separately recorded email/SMS consent and chosen frequency/content, location/market for actual supply.

No automatic inference of health, race, religion, income, other protected/sensitive characteristics from products/marketing events; don't upload raw private data to external research tools.

## 2. RFM without treating it as a scientific personality type

**Recency** = time since last eligible completed purchase relative to a defined analysis date. **Frequency** = count of distinct eligible orders (not item quantity) in a stated lookback window. **Monetary** = net realized customer revenue or **contribution** over that window (clearly named). For returns/refunds, don't count reversed purchases as full positive value.

Procedure:
- Choose customer unit and date, relevant market and lookback (e.g., 12 months **only if** category cycle makes sense).
- Clean duplicates, canceled/test/fraud orders, returns, currencies and missing customer IDs.
- Compute R, F, M from actual order history; low recency is typically better, but distinguish product cycles.
- Quantile scores (e.g., 1–5) are **within this store and cohort**, not universal grades. Very small samples/tied counts may make quintiles invalid; use simple segments and report sizes.
- Label actionable groups: recent first buyer; repeat high-contribution; naturally infrequent gift buyer; dormant with documented repurchase potential; refund/service recovery; new subscriber only where contact consent exists.
- Separate **what is measured** from hypothesized "at risk" or "likely to respond" status.
- Design different interventions by actual job (care/education for new buyers; relevant replenishment where real; gift guide at seasonal occasion; no-message for complaint). Test suppression/control.

## 3. Cohorts and retention

Choose **first purchase month** or signup/activation month according to the question. Define monthly ages consistently, and measure retained customers, repeat order timing, net revenue and **contribution** per original cohort member. Avoid survivorship bias: do not compute "LTV" using only customers who repurchased.

For category-specific cadence, classify opportunities: replenishable items, one-time gifts, infrequent high-ticket products, subscription/service renewals. A 12-month dormant jewelry buyer isn't necessarily churned. Report censoring/immature cohorts—newer cohorts haven't had the same chance to purchase again.

## 4. CLV is a model, not a known fact for a new store

**Historical observed customer value** = sum realized net contribution for a defined cohort/period per original customer, with period specified. **Predicted CLV** requires repeat probabilities, future margin, acquisition cohort selection, returns, discounting, uncertainty and meaningful validation. Segment-specific "CLV" often extrapolates from biased data; don't justify high CAC with an imagined multiplier.

Simplified repeat simulation may be useful when its assumptions, intervals and sensitivity are explicit; never report a precise lifetime value without sufficient evidence. Compare **incremental retention** and actual cost of contacting/supplying customer, not just more email clicks.

## 5. Data models and pitfalls

The typical order table needs `customer_key,order_id,order_at,net_revenue,currency,contribution,refunded/canceled,status,market,product_categories`; join email/SMS permission data separately via secure approved identifiers. Distinguish account holder/guest order, multi-channel identities and merges. Deduplicate per order ID; explicitly handle timezone, multiple currencies and country-specific compliance.

Common biases: treat delayed purchases as churn, infer product preferences from one gift order, misuse open rates, mistake email clicker for incrementality, select only profitable existing customers for holdout and conclude email "caused" their value, use future order data in historical segmentation (data leakage). Document sampling, known gaps and uncertainty.

## 6. Turn insight into a plan

For each segment record `definition → population/time window → customer need → potential helpful content/offer → eligible contact channel → frequency/suppression → incremental metric → size/profit constraints`. Segments with no different treatment should often be collapsed.

**Output:** RFM/cohort definitions and tables, business-relevant groups, hypotheses, honest sample/CLV limitations, permitted lifecycle/paid audiences and experimental learning plan.

## 7. Sources

- [Shopify customer reports and analytics](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/customers-reports)
- [Shopify customer segmentation](https://help.shopify.com/en/manual/customers/customer-segmentation)
- [Klaviyo customer segmentation and reports](https://help.klaviyo.com/hc/en-us/articles/360044604591)
- [Klaviyo 2026 deliverability and benchmarks](https://help.klaviyo.com/hc/en-us/articles/115000201131)
- [General Marketing Analytics](marketing-analytics-data-model-and-reporting.md)
