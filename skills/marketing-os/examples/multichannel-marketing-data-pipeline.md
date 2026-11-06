# Worked example — a multi-channel ecommerce measurement pipeline (hypothetical)

**Illustrative only:** no merchant access, API requests or real customer data. Use [Workflow 8D](../workflows/08d-marketing-data-pipelines-and-measurement.md), [pipeline blueprint](../templates/marketing-data-pipeline-blueprint.md) and [event/UTM plan](../templates/marketing-event-tracking-and-utm-plan.md).

## Business question

A jewelry merchant sells on Shopify, Etsy and Amazon. Meta reports 43 purchases for a week; GA4 reports 31; Shopify has 29 paid orders that week. The marketer asks, “Which Meta campaign should we scale?” **Do not scale on these numbers alone**: their units, attribution windows, statuses and scopes are different. Meta can credit conversions outside the Shopify placed-order count; some may be view-through or from differently selected dates. Etsy/Amazon orders should be compared separately.

## Data flow

1. Shopify GraphQL exports orders, line items, refunds, products/variants, transaction state and costs (when legitimately available), with periodic updates and idempotent upsert by `(shop_id, order_id)`. Consume authenticated webhook notifications and reconcile daily.
2. Etsy v3 authorized shop receipts and transactions are extracted and updated. Track `(shop_id, receipt_id, transaction_id)`; use the Etsy seller reports for fees/payouts; **no direct browser pixel access assumed**.
3. Amazon SP-API orders/reports and optional Data Kiosk sales/traffic ingest by `(seller_id, marketplace_id, AmazonOrderId)`; fee/return/report time grains are preserved; no Amazon customer PII in ad audiences.
4. GA4 BigQuery export is stored independently, with nested event/item arrays and transaction_id dedup check. Meta Ads, Google Ads and Amazon Ads campaign-day exports are kept in separate attribution facts; native metrics are not conflated with orders.
5. Build `dim_product_variant` with effective-dated `source_platform + source_id` links to canonical product. Build `fct_order` and `fct_order_line` with paid/refund lifecycle; `fct_ad_daily` for reported spend and conversions; `fct_event` for permitted web behavior.
6. Compare orders by source-local dates/currencies/statuses first. Publish KPI marts with clearly labeled `recognized_net_sales`, `ad_spend`, `platform_attributed_revenue` and `contribution_after_media` with COGS/fees only where known.

## Concrete failure investigation

**Hypothesis A — two Meta Purchase senders:** native Meta channel Pixel and another theme/GTM implementation both emit a Purchase; CAPI uses a new event ID unrelated to browser event. Audit sender inventory, event names/IDs and test Events Manager. Fix by keeping one controlled event pipeline and sharing event ID across browser/server. Do not delete integrations until their dependencies are inspected.

**Hypothesis B — reporting scopes don't match:** Meta ads report cross-device/view-through attribution with one time window; GA4 logs a different subset of client/server events and Shopify gives canonical paid orders by a different date. Record windows/date fields/currency, run a controlled paid test order and align what can be compared. **Do not promise exact parity.**

**Hypothesis C — marketplace joins:** a Shopify SKU and Amazon seller SKU happen to match but Amazon ASIN corresponds to a bundle. An unreviewed SKU join inflates product-level margin. Require effective-dated source ID mapping plus manual validation for bundles.

## Tests and decision gate

- One synthetic purchase and one partial refund processed twice from API retries should yield **one** order plus correct accumulated adjustment, not duplicate orders.
- One Meta Pixel and one CAPI observation of the same action should share exact event identity; a separate checkout should have a different event ID.
- An opt-out should suppress unpermitted tracking/activation, and replayed pipelines should respect deletion.
- Missing channel fees/COGS: display `unknown`, not $0, for margin.
- Once tracking/reconciliation pass, run a bounded creative/audience test with the same ledger-defined KPI and consider incrementality measurement. Only then choose budgets.
