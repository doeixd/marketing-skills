# Workflow 5I — Shopify ecommerce acquisition: Google Shopping/PMax, Meta catalogs, pixels and profit

**Trigger:** Shopify Google & YouTube/Meta channel marketing, Merchant Center disapprovals, catalog ads, Shopping/Performance Max, social commerce, product feed synchronization, conversion pixel tracking, advertising effectiveness or profitable scaling.

**Place:** Stage 5 specialist. Read [Shopify Shopping/feeds reference](../references/shopify-shopping-ads-feeds-and-attribution.md), [Google Search 5G](05g-paid-search-google-ads.md), [Meta creative](06-creative-production.md), [Paid/Promotion 5C](05c-promotion-strategy-and-distribution.md), [Shopify ecommerce economics](../references/shopify-ecommerce-strategy-and-economics.md). Complete [Merchant Feed and Pixel QA](../templates/shopify-merchant-feed-and-pixel-qa.md). When implementing Meta CAPI/datasets, GA4/BigQuery, UTM contracts, marketplace ETL or tracking QA, route to [Stage 8D](08d-marketing-data-pipelines-and-measurement.md) and its [tracking implementation reference](../references/measurement-pixels-ga4-and-attribution.md).

**Technical tracking handoff:** choose [8E](08e-event-instrumentation-and-conversion-qa.md) for Shopify Web Pixels, Meta Pixel/CAPI, GA4 ecommerce, Google Data Manager or conversion duplicates; [8F](08f-marketplace-etl-and-reconciliation.md) for multi-marketplace order/fee/feed pipelines; [8G](08g-audience-activation-and-utm-governance.md) for audience restrictions and UTM-to-cost-mart mapping. Measurement correctness and customer data permission come before new ad spend.

## 0. Decide the customer and business objective

Identify actual category/brand/variant, target market, purchase occasion, margin, stock, budget, first/returning demand, paid vs organic/Shopping intent, Shopify plan, active channels and product availability. Distinguish search query capture, catalog product discovery, Meta visual demand generation, retargeting and retention. Don't assume a multichannel campaign is better than a narrow one.

## 1. Verify catalog and market eligibility

Check Shopify product/variant ID/SKU/GTIN where applicable, product category, title, description, media rights, price/currency, availability, shipping/returns, market, Google/Meta sync state, merchant account verification and errors. Correct original source of truth first. Confirm whether Shopify Google & YouTube and Facebook & Instagram by Meta channels are actually installed; do not invent an account connection.

## 2. Conversion event and consent audit

Keep canonical paid/refunded Shopify orders, observed GA4 events and attributed Meta/Google conversions distinct. Inventory existing native/app/GTM/theme senders before adding duplicate purchase events. For paired Meta browser Pixel and server CAPI events, verify matching event names and shared browser `eventID` / server `event_id`; GA4 needs a stable purchase `transaction_id`. Verify consent under the actual regional/shop configuration. See [8D](08d-marketing-data-pipelines-and-measurement.md).

Map customer events and Shopify Web Pixels to GA4, Google Ads and Meta, dedupe purchase transaction IDs and server/browser sources, confirm values/currency/returns, consent/ad platforms' prerequisites and coverage. **Sandboxed Shopify pixel APIs are not unrestricted DOM access**. Reconcile reports with Shopify actual orders; note late-September-2026 session-metric changes and ad attribution overlaps. Separate primary purchase from secondary product view/add-to-cart.

## 3. Campaign architecture by buyer/intent

- **Google Shopping/PMax:** actual merchant feed and eligibility, category/brand/new buyer strategy, asset accuracy and inventory profitability; test PMax expansion with true conversion values and approved pages.
- **Google Search:** actual keyword/query theme and match/negative decisions, targeted landing, RSA with evidence-backed copy; [5G](05g-paid-search-google-ads.md).
- **Meta/Instagram catalog ads:** audience state, real images/variants, product-set relevance, creative overlay/format constraints, consent, product identity matching, brand cues and truthful CTA.
- **Organic/social commerce:** product tagging, local/account market eligibility, actual checkout destination and commercial terms.
- **Other channels:** Pinterest/TikTok/marketplace where relevant and properly connected; no assumptions about account capabilities.

Each campaign has `job → audience/query → product set → verified angle → asset → landing URL → measurement → spend boundary → owner`.

## 4. Define financial guardrails and creative tests

Calculate contribution after discounts, COGS, fulfillment, shipping, platform fees and returns, plus paid spend. Choose main KPI (incremental contribution or qualified orders, with justified proxies when needed); distinguish new vs known demand and margin-different product sets. Write 2–4 genuinely distinct creative hypotheses and the precise PDP/collection destination.

## 5. QA, launch and feedback

Check product disapprovals, URL redirects, live prices/stock, product variant sync, consent, checkout, asset licenses, AI creative enhancements, budgets, market, attribution and store operation capacity. Publish/change live feed settings or ad budgets only with approval. Monitor rejected products, spend anomalies, query/product fit, actual order quality and refunds. Suggest a measured pilot/holdout where feasible.

**Deliver:** feed error matrix, product-set strategy, event QA map, campaign brief/ad assets, landing readiness, economics and monitored launch/learning plan. If products are unbuyable/feeds mismatched/tracking invalid, fix before scaling.
