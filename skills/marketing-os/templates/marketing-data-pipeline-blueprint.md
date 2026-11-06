# Marketing data pipeline implementation blueprint

**Use with [Workflow 8D](../workflows/08d-marketing-data-pipelines-and-measurement.md).** Do not populate missing real data with invented values.

## Business decision and definition

- Decision owner / date / target go-live:
- Business question and exact decision this data informs:
- Current answer and confidence / why inadequate:
- Required sources and stores (with authorized account scope):
- Granularity: order, order line, event, campaign-day, SKU-day, cohort, etc.:
- Freshness / historical coverage / currency / locale / source timezone:
- Canonical `order`, `purchase`, `net revenue`, `margin`, `new customer`, `attribution` definitions:
- What must NOT be inferred or joined across platforms:

## Architecture and source contracts

| Source system | Business object/API/report | Access/scopes + owner | Key/grain | Cursor/backfill | Data sensitivity | Schedule/SLA | Destination |
|---|---|---|---|---|---|---|---|
| Shopify | Admin GraphQL orders + adjustments; Bulk as needed | Verify | store + order/line ID | updated_at/lookback | Protected fields | TBD | raw/staging |
| Etsy | OAuth v3 receipts/transactions | Verify seller grant | shop + receipt/transaction ID | paging + requery | Restricted seller data | TBD | raw/staging |
| Amazon | SP-API reports/Data Kiosk | Verify role/region | seller + marketplace + order | report periods | RDT for restricted ops | TBD | raw/staging |
| GA4 | BigQuery export / Data API | Verify property | stream/event ID | daily/intraday | Event identifiers | TBD | events |
| Ads | Meta/Google/Amazon Ads reporting | Verify ad accounts | account + campaign/ad + day | overlapping date windows | Campaign-level | TBD | spend/attribution |

Delete irrelevant rows and add observed connectors; this is an illustrative inventory.

```text
[sources] → [raw retained securely] → [staging with stable IDs] → [canonical facts/dims] → [QA/reconciliation] → [BI/decisions]
                                                                             └─> [consented, explicitly approved activation]
```

## Mapping and checks

| Output field / metric | Source field | Grain and unit | Transformation and exclusions | Acceptance test |
|---|---|---|---|---|
| canonical_order_id | source order ID + source/store namespace | order | unique, immutable | unique+not-null |
| paid_net_sales | source line/adjustments | order/line/currency | documented tax/shipping/refund policy | reconcile with platform |
| campaign_id | ads platform internal ID + platform/account | campaign | names may change | no ambiguous joins |
| variant_link | source-native variant/listing/ASIN/SKU mapping | effective-dated relation | explicitly mark uncertain bundles | orphan/collision counts |
| total_ad_spend | platform reporting export | account-day-currency | use aligned dates, statuses and attribution settings | UI comparison within policy |

## Security, failure recovery, monitoring

- Auth/rotation/least-privilege ownership; approved sensitive-field allowlist:
- Consent/legal basis/data processing purpose; geographic restrictions; deletion propagation:
- Paging/cursor checkpoint durability; pagination sample; API rate-limit/429 strategy:
- Idempotency key and upsert logic; webhook signature + retries:
- Test fixtures, late updates, refunds/cancellations, replay/snapshot design:
- Missing/duplicate event tests, null/unique/relationship/schema validation:
- Last-successful timestamp, max lag, source-vs-warehouse totals, alert owner and severity:
- Cost estimate (API/hosting/warehouse/maintenance) and buy-vs-build decision:
- Rollback, backfill/reconciliation runbook, data retention and decommission plan:
- Authorization required for live writes, data sharing and ad audience activation:

## Release gate

- [ ] Owner and permissions verified
- [ ] Canonical definitions approved
- [ ] Consent/data restrictions enforced
- [ ] Sample backfill and replay passes
- [ ] No material duplicate/missing orders
- [ ] Test orders/refunds and currency handling reconcile
- [ ] Alerts and rollback tested
- [ ] All outbound activation destinations separately approved
- [ ] Report clearly labels platform attribution, observed sales and incrementality
