# Workflow 8D — Marketing data pipelines, measurement, attribution and audiences

**Trigger:** data/ETL/ELT pipelines; Meta datasets, Pixel or Conversions API; GA4/BigQuery/GTM; UTMs; marketplace Shopify/Etsy/Amazon sales; ads reporting; conversion discrepancies; audience/CRM segmentation; reverse ETL; analytics warehouse or BI dashboards.

**Role:** Stage 8 specialist serving commerce diagnosis, paid search, Shopping/Meta, SEO/CRO, creative measurement and retention. Start with [ETL](../references/marketing-data-engineering-and-etl.md), [measurement implementation](../references/measurement-pixels-ga4-and-attribution.md), [marketplaces](../references/commerce-data-shopify-etsy-amazon.md), [audiences](../references/audiences-identity-and-reverse-etl.md) and [curated tools/skills](../references/marketing-data-tools-skills-and-resources.md). Use [pipeline blueprint](../templates/marketing-data-pipeline-blueprint.md) and [event + UTM plan](../templates/marketing-event-tracking-and-utm-plan.md).

**Implementation branches (2026):** [8E First-party Pixels/Conversion QA](08e-event-instrumentation-and-conversion-qa.md), [8F Marketplace ETL/Reconciliation](08f-marketplace-etl-and-reconciliation.md) and [8G Audiences/Reverse ETL/UTM Governance](08g-audience-activation-and-utm-governance.md). The latest [verified platform API updates](../references/2026-platform-data-api-updates.md) cover Shopify 2026-01 bulk concurrency, expanded Etsy webhooks, Amazon report/API boundaries, GA4 Measurement Protocol, Google Ads Data Manager and Meta CAPI dedup. Use the [data plan manifest checker](../scripts/check_marketing_data_plan.py) for an offline structural preflight; it does not test actual permissions or API acceptance.

## 0. Establish the decision, facts and access

Ask what specific question must be answerable (e.g., which campaigns profitably acquire *new* customers, where conversion tracking is broken, why reported purchases exceed store orders). Record business owner, region/currencies, the destination/action it will inform, required freshness and available account permissions. Distinguish **observed from inferred** store data. Inventory channels, store(s), existing pixel apps/integrations, data warehouse, consent manager, reporting APIs, tracking history and current costs. Do not request or expose secrets in a report.

**Gate:** no data access/consent? Produce a design plus exact evidence requests, never pretend a production extract ran.

## 1. Define a source-of-truth and event contract

For each metric define grain, source, timestamp semantics, status, refund behavior, shipping/tax/discount convention, currency and owner. Separate actual orders/settlements, GA4 behavioral events, Meta/Google attributed conversions and experiment-based lift. Catalog product/variant identity and campaign IDs must be stable across channels. Choose a canonical event plan and source-of-truth matrix. Identify all potential duplicate senders before installing new tags.

**Gate:** no agreed business definition of revenue/conversion? Resolve definition before a dashboard.

## 2. Map collection and extraction

Choose the **smallest fit-for-purpose** implementation:
- existing approved native integrations and simple export for modest scope;
- scheduled API/CSV ETL for marketplace order/revenue and paid ad reports;
- Shopify Web Pixel app/custom event subscriptions + native channels when properly consented;
- GA4 client tracking + optional valid Measurement Protocol and BigQuery export;
- Meta browser Pixel + **server CAPI with shared event ID** if configured and lawful; never add duplicates blindly;
- Amazon/Etsy seller APIs where authorized, with marketplace-specific permissions, rate limits and data restrictions.

Produce a diagram from each origin to each destination. Separate **API permissions needed** from those actually granted. Don't confuse an ads account with a pixel/dataset or an ad report with a customer/order system.

## 3. Build/review data ingestion and transformation

Specify paging/cursor, backfill and lookback, schema versions, retry-after/backoff, idempotent keys, webhook signature validation, error quarantine, source record provenance and cost. Store raw audit history safely; normalize staged records into canonical product, order, line, adjustments, spend and permitted events. Build SKU/ID bridge for Shopify/Etsy/Amazon. Distinguish order_created, paid, refunded and financial ledger events. Use incremental `MERGE` or history snapshots where required.

**Gate:** rows fail uniqueness, identity scope, consent classification or money reconciliation? Stop downstream publication/activation.

## 4. Implement QA and attribution checks

Test actual staging conditions and permitted event flows:
1. Consent denied/granted with regional cases, mobile/browser/privacy blockers, checkout completion and sandbox context.
2. One test purchase -> one canonical order; Meta browser+CAPI share same `event_name` and stable `event_id`; GA4 purchase has `transaction_id`; revenue/currency values agree with defined convention.
3. Verify source event arrival in Shopify Web Pixel/Meta Test Events/GA4 DebugView or permitted server diagnostics.
4. Use stable UTM campaign taxonomy and check redirects and auto-tag IDs; avoid splitting campaigns by casing.
5. Compare daily order ledger to warehouse; report separately attributed ads conversion totals, conversion windows, lateness, view-through, timezone and data loss.
6. Run row-level schema/privacy checks and aggregate freshness/completeness checks, plus staged backfill and rerun.

**Gate:** incomplete or misleading data? Label it, repair and retest before optimizing budgets/bidding. Never invent match-rate numbers or promise exact UI parity.

## 5. Design governed activation only when justified

For Meta audiences/datasets, Google offline/enhanced conversions, Shopify segments, email/SMS or CDP sync: document first-party provenance, lawful purpose, platform restrictions, exclusions, unsubscribe/erasure propagation, refresh, consent state, owner approval, test mode and stopping conditions. Hashing fields is not permission to share them. Marketplace purchase records are not automatically available for cross-platform remarketing.

## 6. Deliver a decision-ready package

Output:
- [Pipeline design](../templates/marketing-data-pipeline-blueprint.md) with current state, target architecture, integration/permission/owner map, field/ID mapping, versioning and cost.
- [Tracking plan](../templates/marketing-event-tracking-and-utm-plan.md) with real event triggers, pixel/GA4 mappings, UTMs and consent.
- QA report: test cases, expected vs actual, source reconciliation, duplicate/blocked event findings and severity.
- Metric dictionary: clearly separate ledger sales, GA4 events, ad-platform attribution, margin and causal lift.
- Prioritized tickets by **data integrity risk × business consequence × effort**, rollback, monitoring, authorized writes and next evaluation.

**Stop conditions:** missing data ownership/permission; privacy or platform policy conflict; possible PII disclosure; live purchase event duplicated; materially unreconciled sales; missing spend authorization. All live pixel, CAPI, audience, data-share and account changes require explicit approval.

## Example

See [Shopify/Etsy/Amazon source-to-dashboard walkthrough](../examples/multichannel-marketing-data-pipeline.md) for a hypothetical implementation and reconciliation test. Integrate findings into [Stage 8 measurement](08-measure-diagnose-experiment.md), [Shopify Ads 5I](05i-shopify-shopping-ads-and-tracking.md) and [Lifecycle 9A](09a-shopify-lifecycle-retention.md).
