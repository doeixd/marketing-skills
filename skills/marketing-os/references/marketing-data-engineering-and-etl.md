# Marketing data engineering: ETL/ELT, pipelines, reliability and canonical models

**Reviewed 2026-11-06.** Use for marketing data warehouses, API ingestion, historical backfills, attribution marts, marketplace reconciliation, feed pipelines, identity joins and reporting reliability. Pair with [measurement](measurement-pixels-ga4-and-attribution.md), [commerce integrations](commerce-data-shopify-etsy-amazon.md), [audience activation](audiences-identity-and-reverse-etl.md), [tools/skills](marketing-data-tools-skills-and-resources.md), and [Workflow 8D](../workflows/08d-marketing-data-pipelines-and-measurement.md).

## Start from decisions, not a stack diagram

Define which decision the pipeline enables (gross margin by channel, cost per new customer, cohort LTV, orders missing from GA4, campaigns causing profitable *incremental* sales), the accountable owner, expected grain/freshness, canonical definitions, latency tolerance and authorized data access. **An extraction is not an insight.** Define outputs/SLAs before choosing tools.

Distinguish four pipelines:
1. **Behavioral event collection** (web/app/checkout, browser pixels, server endpoints) for funnel and platform optimization.
2. **Business-system ETL/ELT** (Shopify/Etsy/Amazon orders, transactions, refunds, products, costs, inventory) for commercial truth.
3. **Ad/analytics reporting ingestion** (Meta/Google/Amazon Ads, GA4, Search Console, email provider) for *reported* spend and attributed performance.
4. **Activation/reverse ETL** (permissioned segments, offline conversions, audiences, catalog updates) for feeding approved outputs back to tools. A warehouse table does not authorize uploading customer details.

## Architecture: small first, scale deliberately

```text
Shopify GraphQL + webhooks ──┐
Etsy v3 receipts + reports ──┼──> raw immutable extracts ──> staging ──> canonical commerce marts ─┐
Amazon SP-API reports ───────┘            |                    |                              |
GA4 BigQuery / Data API ──────────────────┤                    └── events/session marts ────────┤
Meta / Google / Amazon Ads reports ───────┤                                                   ├──> KPI views / QA / decisions
Email/SMS, CRM, costs, returns ───────────┘                campaign mapping / reconciliation ──┘
                                                                               |
                                                     approved, consent-filtered reverse ETL only
```

**Choose:** scheduled CSV/API sync + SQLite/DuckDB/Postgres for smaller merchants; Airbyte/dlt/Meltano or well-tested TypeScript workers for extraction; Postgres/BigQuery/Snowflake for multi-source/history; dbt or typed SQL for modeled transformations; orchestration with cron/workflows/Dagster/Prefect where monitoring and retries justify the cost. These are options, not prerequisites. Prefer stable managed native integrations where they actually meet event coverage and cost requirements. Distinguish CDC (record changes), webhooks (notifications) and periodic full reconciliation: webhooks can be late, out of order or missing.

## Ingestion contract (per connector)

Record: `source_system`, `account_id`, `source_record_id`, `entity_type`, `source_created_at`, `source_updated_at`, `extracted_at`, `batch_id`, `cursor`, `schema_version`, `raw_payload_location`, `ingestion_status`. Scope every ID by account/store and source; do not assume IDs unique across channels. Store timezone-aware instants in UTC while preserving store timezone and original source-local reporting date. Track local currency and conversion rate source/date where comparisons require it.

- **Auth:** least-privilege OAuth/service credentials, refresh rotation, secret manager, redacted logs, tenant isolation and approved protected-customer-data scopes.
- **Pagination/backfills:** cursor/offset and time-window pagination as supported; retain checkpoints only after durable successful commits; backfill bounded intervals and requery a lookback window for edits.
- **Rate limits:** obey platform-specific headers, dynamic quotas and retry-after; exponential backoff with jitter; circuit breakers; never guess fixed quotas.
- **Idempotence:** stage first, `MERGE`/upsert by stable source+account+ID (and version when needed); retain event IDs and processed webhook IDs; retries cannot create new sales.
- **Updates/deletes:** refunds, edits, cancellations, disputes, backorders, GDPR erasures and deleted catalog items change historical values. Use update timestamps, webhook reconciliation, tombstones and/or snapshots. Never treat append-only orders as unchangeable.
- **Historical replay:** version raw records and transformation logic; support deterministic reprocessing with a clear effective date, not silent report rewrites.
- **Failure isolation:** quarantine malformed records with redacted error details, preserve a dead-letter path, alert on sustained errors, track partial vs complete batches.

## Canonical grain and modeling

Recommended marts (adapt to business reality):
- `dim_channel`, `dim_campaign`, `dim_product_variant`, `dim_store`, `dim_calendar`, `dim_customer_pseudonymous` (only if lawful and necessary).
- `fct_order`: one record per `(source, store, order_id)`, with status, order date, currency, gross, discounts, tax, shipping charged, refunds, fees, net recognized sales by *explicit* convention.
- `fct_order_line`: one per `(source, store, order_id, line_id)`, joined to canonical SKU/variant mapping, quantity, unit price, discounts, returns and COGS evidence.
- `fct_order_adjustment`: money events (refund, return, edit, payout adjustment) with unique IDs, timestamps and signs.
- `fct_ad_daily`: per platform/account/date/campaign/ad and attribution window if provided; spend/clicks/impressions; platform-attributed conversions **not** canonical orders.
- `fct_event`: per authorized tracking event ID; event time, ingestion time, identity/session keys, UTM/click ids where permitted, consent state, order reference for valid purchases.
- `bridge_product_identifier`: Shopify variant ID/SKU/GTIN, Etsy listing/transaction IDs, Amazon ASIN/SKU and feed `item_id`; make many-to-one and variant/multipack collisions explicit.
- `fct_inventory_snapshot`, `fct_email_engagement`, `fct_customer_cohort` only when there is a decision requiring them.

**Never add rows of different grain and call the result revenue.** Taxes/shipping/discounts can be included differently by Shopify, Etsy, Amazon, GA4, Meta and Google Ads. Document each metric's scope, exclusion of test/canceled orders, refund timing, timezone, payment-vs-placed date, currency, gross-vs-net status, fees and currency exchange. Define denominator for conversion rate (GA4 sessions, Shopify sessions and ad clicks are different).

## Warehouse quality and operations

Test both at row and aggregate level:
- **Contracts:** required fields and types, unique+not-null keys, accepted state/currency values, referential integrity, PII restrictions and schema drift.
- **Freshness/completeness:** max lag, expected page/batch count, watermark advancement, backfill coverage, required platform partitions.
- **Financial reconciliation:** source orders/revenue/adjustments by store-local day and currency vs canonical marts, with documented tolerances and source report latency.
- **Event quality:** funnel event coverage by browser/platform/consent, invalid payload rates, missing `transaction_id`, purchase event duplicates, consent denial behavior, UTM completeness and landing redirects.
- **Monitoring:** extraction success, last complete data date, retries/429s, delayed webhook age, error budgets, cost of API/warehouse, alerts and runbook. For ad spend, compare delivered export totals against UI in the same date, timezone, breakdown, currency and attribution settings.
- **Data contracts:** owner, sensitivity classification, lawful processing purpose, schema/test fixtures, retention/deletion rules and downstream consumers. Restrict raw customer data and avoid copying it into analytics/ad platforms.

A passing pipeline is **not** evidence of correct attribution or an incremental impact. Use experiment/holdout, geo tests or model-based analysis only with explicit assumptions. Diagnostics are not proofs.

## Example release gates

Before a production sync: approved scopes; sampled historical export; primary key + duplicate tests; retry/backfill; schema-change behavior; unsubscribe/erase propagation where applicable; source reconciliation; alerting; and rollback. Before changing bidding/creative from the resulting report, check sample size, attribution settings, margin, lag and independent commerce records.

## Sources

- [dbt incremental/snapshot guidance](https://docs.getdbt.com/best-practices/how-we-handle-cdc/2-choosing-incremental-or-snapshots) — updating rows vs historical states, key tests and freshness.
- [dlt verified sources](https://dlthub.com/docs/dlt-ecosystem/verified-sources) — inspect available connector scope and API versions.
- [Airbyte connector directory](https://docs.airbyte.com/integrations) — vendor-maintained sync coverage and deployment options.
- [Shopify GraphQL bulk query](https://shopify.dev/docs/apps/build/apis/graphql-admin/bulk-operations/queries) — large-volume exports and completion lifecycle.
- [Google Analytics BigQuery schema](https://support.google.com/analytics/answer/7029846) — event-table schema and important source attribution limits.
- [Great Expectations](https://docs.greatexpectations.io/docs/core/introduction/) — data validation approaches.
