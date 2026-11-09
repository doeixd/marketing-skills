# Workflow 8F — Shopify / Etsy / Amazon ETL: extract → model → reconcile → publish

**Trigger:** Integrate Shopify, Etsy or Amazon Seller Central; automate CSV/API order exports; merge listings, SKUs, ad spend and settlements; build data warehouse, incremental ingestion, webhooks, marketplace profit and catalog metrics.

**Position:** Commerce data specialist within [8D](08d-marketing-data-pipelines-and-measurement.md). Read [commerce sources](../references/commerce-data-shopify-etsy-amazon.md), [ETL engineering](../references/marketing-data-engineering-and-etl.md), [2026 API changes](../references/2026-platform-data-api-updates.md) and [pipeline contract](../templates/marketplace-extraction-and-reconciliation-contract.md).

## 0. Decide question, grain and source authority

Identify merchant accounts and stores, markets and currencies, product/variant catalog truth, business metric (paid orders, recognized net sales, payouts, margin, returns), permitted access, reporting dates/timezones, expected freshness, daily volume, dependencies, run cost and data-retention policy. Etsy/Amazon are third-party marketplaces: their customer/order data must **not** automatically be used for off-market customer lists. Record terms and approval before sharing beyond permitted fulfillment/analytics purposes.

## 1. Build an API/report inventory by source

- **Shopify Admin GraphQL:** products/variants, orders, transactions/adjustments, inventory where available; check scopes and protected-customer-data eligibility. For backfills use GraphQL bulk operations and resulting JSONL; in API versions **2026-01+**, up to **five concurrent bulk queries per app/shop** are supported; older versions have different limits. Use authenticated webhooks for latency and periodic reconciliation for missed events.
- **Etsy Open API v3:** authenticate via OAuth scopes under correct **Seller App vs Personal vs Commercial** access. Pull receipts/transactions/listings/inventory. Etsy now supports order, listing and inventory webhooks (including `order.paid`, `order.canceled`, `listing.updated`, `inventory.updated`); verify signatures, dedup delivery IDs and replay on retry. Obey 429 `retry-after`, QPS/QPD. Do not assume Shopify-like checkout pixels or rights over Etsy buyer data.
- **Amazon SP-API:** register app and seller authorization, regional marketplace IDs, least-privilege roles and current data protection policy; use Orders, Reports, Notifications (SQS/EventBridge), Data Kiosk where eligible, fees/settlement and refund reporting with versioned source semantics. Reports and notifications are not the same as Seller Central order fact; use actual completion status and reconciliation. **Amazon Ads API** and **Amazon Attribution** require separate advertising authorization and report definitions; Amazon Attribution tags measure off-Amazon tactics leading to Amazon.
- **Other sources** (BigCommerce, Etsy Ads, Google Ads/Meta Ads, email/CRM, shipping platforms) can fit same contract, but don't invent a supported endpoint or assume permissions.

## 2. Design ingest and replay

Per connector: auth refresh and secret storage; mode (bulk query, cursor/offset, webhook, report job, daily file), initial backfill, incremental watermark, maximum tolerated lag, endpoint quotas, `retry-after` and jitter, dead-letter/quarantine, schema evolution, source response checksums, cost and owner. Commit watermark **after durable successful load**, not after first page or webhook acknowledgment. Preserve source IDs, account scope and `source_updated_at`, raw payload version and `ingested_at`. Re-query edit/refund lookback, handle tombstones and replay safely.

**Webhook → queue → fetch authoritative record → upsert** when notification lacks complete source facts. Webhooks may be duplicated, delayed or out of order. A nightly full/rolling reconciliation remains necessary.

## 3. Stage and normalize without collapsing identities

Proposed source-scoped canonical keys:
- Order: `(channel, account_id, marketplace_id_or_shop_id, source_order_id)`.
- Line: order key + immutable source line/transaction identifier.
- Adjustment: `source + account + adjustment_id` with event time and sign.
- SKU crosswalk: `source listing/variant/ASIN/FNSKU/merchant_sku → canonical variant` with validity interval and bundle quantity/pack mapping.

Never join orders across marketplaces by shared display order number, email, ASIN alone or SKU alone. Distinguish Amazon ASIN from seller SKU; Etsy listing from purchasable product variation; Shopify product from variant. Avoid duplicating order totals when joining multiple line items to spend by day.

## 4. Financial and marketing marts

Separate `fct_order`, `fct_line`, `fct_adjustment`, `fct_settlement`, `fct_spend`, `dim_product_bridge`, `dim_campaign` and UTM/source mapping. Compare metrics with **same grain, status, time zone, currency and tax/shipping/refund convention**. Report marketplace fees/settlement cutoffs separately from placed-order time; payouts are not gross sales. For actual margin require real COGS, shipping and commissions; missing cost should be `unknown`, not zero. Advertising attributed conversions are separate reported events and do not provide unique ledger order IDs by default.

## 5. QA: reconciliation and failure modes

Run [source contract](../templates/marketplace-extraction-and-reconciliation-contract.md) checks: duplicate keys, orphan lines/adjustments, invalid currency, impossible quantity, missing identifiers, stale source watermarks, partial page/report, refunded order not corrected, negative ledger signs, SKU bundle mismatch, source totals by date/currency and repeat-run idempotency. QA store-level absolute/relative variances with known report timing and source status. Preserve historical version/lineage and alert on lateness.

**Deliver:** extraction architecture and scopes, raw/staging/mart schema, sample SQL/data validation, watermark/retry plan, reconciliation matrix, deployment cost/rollback/alerts and an evidence-qualified first decision. No real customer records, write scopes, catalog mutation or audience exports without express approval.
