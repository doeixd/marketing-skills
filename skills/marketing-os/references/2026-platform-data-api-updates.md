# 2026 source-verified marketing data API implementation notes

**Reviewed:** 2026-11-09. This document supplements [Marketing ETL](marketing-data-engineering-and-etl.md), [Measurement/Meta/GA4](measurement-pixels-ga4-and-attribution.md), [Commerce sources](commerce-data-shopify-etsy-amazon.md) and [Audience activation](audiences-identity-and-reverse-etl.md). Platform/API rules change: verify the **actual account and API version** immediately before production. No code here conveys permission to install tags, import protected records or upload audiences.

## Shopify Admin GraphQL bulk operations

Official: [Bulk operations](https://shopify.dev/docs/apps/build/apis/graphql-admin/bulk-operations/queries), [Web Pixels API](https://shopify.dev/docs/api/web-pixels-api), [Web pixels and consent](https://shopify.dev/docs/apps/build/marketing/pixels), [Shopify Customer Privacy](https://shopify.dev/docs/api/web-pixels-api/standard-api/customerprivacy).

- For API **2026-01 and later**, Shopify allows **up to five concurrent bulk query operations per app/shop**. Previous versions allowed one bulk operation of each type per shop at a time. Do not hardcode older concurrency assumptions or launch five requests against a shop/version not verified.
- A bulk query is asynchronous: create operation → observe completion/partial failure → retrieve JSONL before expiry → parse parents/children carefully → reconcile selected count/status → advance checkpoint **after committed staging**. A bulk query does not imply the exported file is a stable order ledger: orders can be edited/refunded after extraction.
- Shopify App Pixels use a **strict sandbox**, Custom Pixels a **lax sandbox**. Subscribe to supported customer events; DOM scraping is not a supported App Pixel strategy. Consent may gate/pause/replay callbacks. Server pixels remain governed by customer privacy, and enrichment depends on applicable settings. `checkout_completed` and webhook order payment status must be reconciled rather than counted as a common money fact.
- Check actual app permissions, protected customer data access, GraphQL throttling and webhook authenticity. Don't treat a public Shopify PDP as admin access.

## Etsy Open API v3

Official: [API homepage/access types](https://developer.etsy.com/), [Webhooks](https://developer.etsy.com/documentation/essentials/webhooks/), [Rate limits](https://developer.etsy.com/documentation/essentials/rate-limits/).

- **Seller Apps** cover the developer's own shop, while **Personal Apps** and separately approved **Commercial Access** cover third-party seller integrations, subject to Etsy review, approved OAuth authorization and endpoint scopes.
- Etsy now lists webhook domains **order, listing and inventory**, e.g. `order.paid`, `order.canceled`, `order.shipped`, `listing.updated`, `inventory.updated`, `inventory.out_of_stock`. Verify exact documented payload/event versions and signature using Etsy's current verification instructions. A delivery may retry; deduplicate by provider delivery/message identity and refetch authoritative receipt/listing when necessary.
- Order **receipt**, **transaction/line** and **listing/product variant** are distinct objects. Seller SKU/name alone is not a reliable cross-shop primary key. Keep source/shop/record scope.
- Etsy `429` includes `retry-after`; obey estimated wait, quota scopes and exponential backoff. Use reconciliation windows to repair missing event notifications. **Never copy Etsy buyer identities into independent remarketing audiences without platform permission and lawful basis.**

## Amazon SP-API, Seller Central and advertising

Official: [SP-API onboarding](https://developer-docs.amazon.com/sp-api/docs/onboarding-overview), [SP-API release notes](https://developer-docs.amazon/sp-api/docs/sp-api-release-notes), [Reports API](https://developer-docs.amazon/sp-api/docs/reports-api), [Usage plans/rate limits](https://developer-docs.amazon/sp-api/lang-en_en/docs/usage-plans-and-rate-limits), [Amazon Attribution](https://advertising.amazon.com/en-us/solutions/products/amazon-attribution/), [Amazon Attribution API](https://advertising.amazon.com/API/docs/en-us/amazon-attribution/get-started).

- SP-API access needs developer/app, seller authorization, permitted roles, regional marketplace IDs and relevant data protection rules. Reports and Data Kiosk can supply different order, returns, inventory, traffic and sales grains. Notifications can arrive via SQS/EventBridge; they aren't a complete ledger. Check report requests, processing status, download lifetime and source timestamps.
- SP-API uses per-operation/account/application token-bucket usage plans; **do not assume global fixed requests/minute**. Use exposed current quotas where available, handle throttles and retry safely.
- Amazon **Seller orders**, **Amazon Ads performance**, **Amazon Attribution tags** and **settlement/payments** are distinct source families with separate credentials, time zones, conversion windows and metric meanings. Amazon Attribution reports non-Amazon campaign effect **on Amazon** for eligible advertisers; it is not a substitute for UTM-based website GA4 traffic nor evidence of causal lift.
- Amazon August 2026 SP-API release notes include a Promotions API and related report mapping IDs. Use only when the seller/market/report type is actually eligible; don't assume a planned feature is present.
- Buyer/PII data has additional contractual restrictions. Avoid identifying buyers across marketplace and DTC stores using emails or name/address just because APIs return them.

## Google Analytics 4 collection and server-side events

Official: [GA4 Measurement Protocol](https://developers.google.com/analytics/devguides/collection/protocol/ga4), [MP reference](https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference), [recommended ecommerce events](https://developers.google.com/analytics/devguides/collection/ga4/reference/events), [Consent Mode v2](https://developers.google.com/tag-platform/security/guides/consent), [server-side consent](https://developers.google.com/tag-platform/tag-manager/server-side/consent-mode).

- GA4 Measurement Protocol **supplements** gtag/GTM/Firebase tagging; server-only MP cannot be presumed to provide equivalent session/attribution. A web event needs actual `measurement_id` and **matching** `client_id`; session reporting benefits from real session metadata. An MP request can contain up to 25 events; validate with Google's strict-validation path. Do not guess a client ID or invent an attribution session.
- For GA4 purchase, use real `transaction_id`, `items`, currency, and `value` equal to sum of item prices × quantity **excluding tax and shipping** (reported separately). Consistent naming, value definitions and valid source/identity are more important than sending every possible event.
- Google Consent Mode v2 distinguishes `ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization`; mode is **not** a consent manager or general legal permission. Advanced Mode may transmit consent-limited cookieless signals depending on legal/CMP and configuration, so don't claim "denied means no network request" or "server-side bypasses consent."
- GA4 BigQuery event-level exports and GA4 UI are **not guaranteed to agree** due to modeling, identity, latency and report filters. Audit `event_timestamp` (microseconds), event date with timezone, `items` arrays, source/medium/campaign attribution, and data delay.

## Google Ads / Google Data Manager 2026

Official: [Data Manager API](https://developers.google.com/data-manager/api/devguides), [offline conversions](https://developers.google.com/data-manager/api/devguides/events/google-ads/offline), [Google Ads API deprecations](https://developers.google.com/google-ads/api/docs/deprecations).

- **June 15, 2026** restricted legacy `UploadClickConversions` for Google Ads API clients without earlier offline upload activity; developer-token-based access was separately sunset in **September 2026**. For **new offline conversion/enhanced-conversions-for-leads integrations, choose Data Manager API**.
- Data Manager distinguishes event ingestion from audience membership. Validate with `validateOnly`, then inspect asynchronous request diagnostics and conversion adjustments. Include actual permitted identifiers; hashing first-party contact data does not create legal permission.
- Primary vs secondary conversion action and values matter for bidding. A valid upload request does not prove that a conversion was credited, matched or profitable. Reconcile with real CRM stages, consent and transaction IDs.

## Meta Pixel, Conversions API and datasets

Official: [Meta Conversions API deduplication](https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events), [Server event fields](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event), [Meta event diagnostics](https://www.facebook.com/business/help/1541268312717919). Some Meta docs require signed-in access; verify live schema/business product UI.

- Use the **same action's** `event_name` and `event_id` for browser Pixel and server CAPI. `event_time` is Unix seconds, and other required fields include `action_source` and permitted matching details. Different purchases need different IDs; retries of one purchase reuse the same ID. Do not assume `fbp`/email alone guarantees dedup.
- "Dataset", "Pixel", "offline event" and "Custom Audience" refer to different objects/capabilities. Destination type, consent and platform permissions must be explicit.
- Meta Event Match Quality is a destination diagnostic, not an ethical excuse to collect additional identities, and higher EMQ isn't causally equal to incremental sales. Data-set acceptance/attribution and warehouse ledger sales must be reported separately.

## Campaign tags and URL privacy

Official: [GA4 UTM custom URL setup](https://support.google.com/analytics/answer/10917952), [GA4 campaign-data imports](https://support.google.com/analytics/answer/10071305).

- At minimum maintain governed `utm_source`, `utm_medium`, `utm_campaign`; include stable `utm_id` when joins to ad-cost imports require it, plus `utm_content` and `utm_term` as useful. Google recommends distinct source per platform (e.g. Facebook versus Instagram) and consistent medium definitions; document the business taxonomy.
- Data-import joins can be **case-sensitive**; `Facebook` ≠ `facebook`. Test redirect and checkout domain preservation, Google auto-tagging and platform-specific URL macros. Never put contact PII, tokens, phone numbers or customer IDs in URLs.
- Amazon Attribution tags must be created using Amazon's eligible advertiser workflow; arbitrary UTMs do not grant Amazon conversion reporting.

**QA rule:** A reviewed document is a starting point, not evidence the connector was installed, a tracking test passed, any customer consented, or a marketplace supplied access.
