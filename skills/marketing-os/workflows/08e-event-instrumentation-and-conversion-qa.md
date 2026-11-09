# Workflow 8E — First-party event instrumentation: Shopify → Meta / GA4 / Google Ads

**Trigger:** Meta Pixel, Conversions API, datasets, duplicate purchases, event match quality, Shopify pixel, GA4 ecommerce events, server GTM, Google Data Manager, enhanced conversions, consent mode, or tracking not matching store orders.

**Position:** Implementation specialist under [8D Marketing Pipelines](08d-marketing-data-pipelines-and-measurement.md). Read [2026 integration rules](../references/2026-platform-data-api-updates.md), [Meta/GA4 measurement](../references/measurement-pixels-ga4-and-attribution.md), [privacy and audiences](../references/audiences-identity-and-reverse-etl.md); produce [Event and Consent Implementation Matrix](../templates/event-destination-and-consent-matrix.md), [tracking/UTM plan](../templates/marketing-event-tracking-and-utm-plan.md) and validated [manifest](../examples/marketing-data-pipeline-manifest.json).

## 0. Inventory before changing anything

Identify platform and account (Shopify store and plan, Meta Business/advertising account/dataset ID, GA4 property/web stream, Google Ads conversion customer), current native channel apps, pixels/custom pixels, GTM containers, CAPI gateway, server-side tag/worker, consent manager, billing, event sources and region. For every **Purchase**, ask **who fires it** (Shopify app, old theme script, GTM, browser Pixel, server CAPI, CRM). An extra code snippet can double-report conversions. Determine source-of-truth order ID, actual paid state, identity policies, API access and real observation dates.

## 1. Create an event contract, not a copied pixel snippet

For each business action define **semantic trigger**, event version, store/market and source, raw event identifier, stable canonical `event_id`, time, currency/value convention, products/variants, order ID, first-party identifiers if legitimately available, and consent purposes. Explicitly map names: Shopify `product_viewed` → GA4 `view_item` → Meta `ViewContent`; Shopify `checkout_completed` → GA4 `purchase` → Meta `Purchase`. A Shopify checkout event isn't the same as a settled/payment/refund ledger row: reconcile statuses before reporting. Store the canonical event ID at event creation; retries use **the same ID** and a new independent purchase uses a different ID.

Use true first-party catalog IDs to map product variant → GA4 item and Meta `content_ids` / catalog items. Diagnose feed match errors separately from customer event match quality.

## 2. Implement Shopify collection using platform-supported access

Shopify App Pixels run in strict sandboxes and Custom Pixels in lax sandboxes; use supported `analytics.subscribe` and event payloads—not DOM scraping or arbitrary checkout injection. Set actual scopes `write_pixels`/`read_customer_events` if building an app extension. Review the native Google & YouTube / Facebook & Instagram integrations before adding another integration. Shopify consent gating may delay/replay allowed events; app pixels and server pixels remain subject to its privacy settings. Inspect Shopify Network Intelligence/enrichment settings where applicable, rather than assuming customer data augmentation is enabled.

## 3. Plan destination-specific transports and identity

**Meta:** decide browser Pixel only, server Conversions API only, or both. For the *same* action, browser and server must share exact `event_name` and `event_id` for dedup; Meta API fields include `event_time` (Unix seconds), `action_source`, approved matching identifiers, value/currency where relevant. Verify in Meta Events Manager Test Events/Diagnostics, event match quality and observed dedup. Do not infer better data quality from high event volume. Meta datasets may collect online and offline data, but permissions and event semantics differ.

**GA4:** match Google-recommended ecommerce `event_name`, `items`, `transaction_id`, `value` and `currency` to actual event; `value` excludes shipping/tax as separately defined in Google's reference. Use Measurement Protocol to **augment** existing tagging and retained `client_id`/session where lawfully available; don't invent client IDs to make sessions. Validate using Google's validation server and compare DebugView/BigQuery with orders. Consent Mode has `ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization` as distinct signals; mode is not itself a CMP or a blanket permission to transfer data.

**Google Ads:** use correct purchase/qualified lead goal and conversion action, not arbitrary GA4 intermediate event. In 2026 choose **Data Manager API** for new enhanced-conversions-for-leads/offline conversion integrations; validate with `validateOnly`, review asynchronous ingestion status and adjustments. The Google Ads API `UploadClickConversions` legacy route has access restrictions. Do not conflate GA4 Measurement Protocol, Data Manager API and Google Ads conversion upload.

## 4. QA matrix and safety

Test **consent denied, granted and changed** per applicable region/platform, adblock/ITP limitations, duplicate browser+server sender, one real authorized test purchase, two distinct purchases, replay, refund, subscription cancel, mobile checkout, product variant/catalog mismatch, cross-domain redirect/UTM/click ID loss, and delayed events. Observe source/destination logs and transaction IDs without exposing customer PII.

Assertions: one **canonical** purchase per order/action by agreed rule, source/target IDs stable, correct money/timezone, expected destination coverage (not imagined 100% parity), no event leaking across prohibited consent states, no audience activation without permission. Collect evidence in [matrix](../templates/event-destination-and-consent-matrix.md).

## 5. Publish only as an approved controlled change

Provide sender inventory and topology, exact implementation edits, contract, test cases/observations, known reporting limitations, rollback and data minimization/security controls. Configure disabled/test destinations first. Require explicit merchant approval before changing live pixels, sharing customer data, enabling Enhanced Conversions or uploading events. Hand off meaningful observed outcomes to [Analytics 8A](08a-marketing-analytics-and-measurement.md) and [Attribution 8B](08b-attribution-incrementality-and-experiments.md).
