# Shopify, Etsy and Amazon ingestion/reconciliation contract

Use [Marketplace ETL 8F](../workflows/08f-marketplace-etl-and-reconciliation.md).

## Objective and legal scope
- Business decision (margin, CAC, inventory, return/fee reconciliation):
- Shop/merchant account and permitted marketplace IDs/regions:
- Current source API/versions and accessible scopes, approvals/contract terms:
- Storage destination, restricted customer data handling, encryption/retention:
- Grain, timezone, currency exchange source and reporting frequency:
- Business owner, cost/SLA and response on API failures:

## Connector inventory
| System | Access/owner/market | Exact official API/report/webhook | Grain and key fields | Extraction backfill | Incremental cursor/notifications | Quota/429 behavior | Restrictions |
|---|---|---|---|---|---|---|---|
| Shopify GraphQL | | Bulk JSONL/order/refund/products | source, shop_id, order_id, line_id | | | API version bulk limit | |
| Etsy v3 | | Receipts/transactions/listings/order-listing-inventory webhooks | shop_id, receipt_id, transaction_id | | | retry-after + signature | |
| Amazon SP-API | | Orders/Reports/Data Kiosk/Notifications | seller_id, marketplace_id, AmazonOrderId | | | token bucket | |
| Amazon Ads/Attribution | | Separate account/report/tag API | ad profile, campaign, day | | | ad quota | |
| Other channels | | | | | | | |

## Data pipeline stages
```text
API / webhook / report → raw scoped immutable batch → staging typed rows → key/variant crosswalk
                         → fct_order + fct_line + fct_adjustment + fct_spend (different grains)
                         → reconciliation → profit/KPI marts → approved decisions
```

- Source keys and versioned schemas / raw location:
- Webhook signature verification and dedupe, authoritative refetch plan:
- Watermark and **durable checkpoint commit** after all pages loaded:
- Late edit/backfill lookback, deletes/erasure/tombstones, retries and dead letters:
- Product crosswalk (Shopify variant ↔ Etsy purchasable variation ↔ Amazon ASIN/seller SKU/bundle):
- Prevent fanout when joining order lines with campaign-day spend:
- Privileged credentials, log redaction, secret rotation and support ownership:

## Money / attribution definitions
| Metric | Source and real event/status | Tax/shipping/discount/refund convention | Grain/currency/timezone | Observed official total | Modeled total | Tolerance and caveat |
|---|---|---|---|---|---|---|
| Orders and net sales | | | | | | |
| Return and adjustments | | | | | | |
| Fees and settlement | | | | | | |
| Ad spend and platform-attributed conversions | | **not ledger revenue** | | | | |
| Contribution with COGS | | | | | | |

## QA and operational runbook
- [ ] Scoped keys unique; order lines attach to correct order.
- [ ] Re-running same page/webhook doesn't increase business totals.
- [ ] Missing costs are marked unknown, not zero.
- [ ] Cancel/refund/partial return updates historical facts appropriately.
- [ ] Daily count/sales/fees match comparable source definition, currency and timezone.
- [ ] Queues, 429/retry-after, partial pages, report expiry, cursor rollback and schema drift tested.
- [ ] Source auth/market restrictions and marketplace buyer-data prohibited uses respected.
- [ ] Freshness, error, money/row variance alerts configured.
- [ ] Restore/replay/rollback understood; owner approval before production write.
