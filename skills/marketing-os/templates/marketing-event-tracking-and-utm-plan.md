# Event tracking, campaign UTMs, Meta dataset and audience QA plan

**Use with [Workflow 8D](../workflows/08d-marketing-data-pipelines-and-measurement.md) and [measurement reference](../references/measurement-pixels-ga4-and-attribution.md).**

## Property and integrations inventory

- Site/store, Shopify Markets/countries, checkout behavior and current plugins:
- Shopify Customer Privacy/CMP, default consent and regional testing:
- GA4 property + data streams, Google tag/GTM and Ads conversion action IDs:
- Meta Business Portfolio, **dataset/pixel** ID, connected ad accounts, CAPI partner and catalog:
- Existing native vs theme vs GTM vs app event senders; duplicate risks:
- Authorized source access and privacy owner:

## Canonical event matrix

| Business trigger | Real source event | GA4 | Meta | Required values and stable IDs | Consent / sender | QA observation |
|---|---|---|---|---|---|---|
| Product PDP viewed | Shopify `product_viewed` | `view_item` | `ViewContent` | variant/item ID, currency | Verify region | |
| Item added to cart | Shopify `product_added_to_cart` | `add_to_cart` | `AddToCart` | qty, price, content_ids | Verify region | |
| Checkout started | Shopify `checkout_started` | `begin_checkout` | `InitiateCheckout` | cart value vs purchase value | Verify region | |
| Purchase completed | Shopify `checkout_completed` **and verified paid order state** | `purchase` | `Purchase` | order/transaction_id; event ID paired browser/server; item value/currency | Verify region | |
| Order refund | Authenticated commerce records | `refund` if implemented | ledger/report adjustment | original order ID, amount, item qty | Not a new sale | |

**Dedupe contract:** choose a stable conversion `event_id` generated once per real checkout for Meta Pixel browser `eventID` and server CAPI `event_id` of the same `event_name`. GA4 `transaction_id` uses true stable order transaction identifier. They are different APIs; document both. Check actual checkout-completed semantics before equating with paid settlement.

## UTM naming and QA

| Field | Controlled pattern | Example |
|---|---|---|
| `utm_source` | lowercase platform/publisher | `facebook` |
| `utm_medium` | agreed channel vocabulary | `paid_social` |
| `utm_campaign` | stable lowercase campaign slug | `holiday_gifts_2026` |
| `utm_id` | optional immutable campaign ID | `meta_campaign_123` |
| `utm_content` | stable ad/creative identifier | `video_03` |
| `utm_term` | optional keyword/ad set marker | `gift_for_mom` |

Test both original and redirected final URLs for preservation, URL encoding, casing and parameter collisions. Do not manually overwrite Google Ads click tracking/auto-tag IDs; use approved dynamic platform macros only after verifying their current syntax. Never add PII to parameters. For Amazon-destination campaigns, use platform-supported **Amazon Attribution tags** where eligible; a UTM is not equivalent.

## Observed test matrix

| Test | Expected | Observed | Pass / issue | Screenshot/log reference |
|---|---|---|---|---|
| Region A, consent denied, product view and checkout | Respect current consent configuration | | | |
| Region A, consent granted | Correct collection and IDs | | | |
| Mobile Safari / browser with privacy restrictions | Known measurement gaps documented | | | |
| One test paid order | 1 ledger order; 1 canonical purchase; expected GA4/Meta mappings | | | |
| Meta Pixel and CAPI same checkout | Shared ID, same event name; Events Manager shows no double count | | | |
| Partial refund / cancellation | Ledger and recognized revenue adjust | | | |
| 302/301 landing redirect | UTMs and permitted click IDs preserved | | | |
| Email unsub / opt-out or erasure request | Audience activation suppresses/deletes as required | | | |
| Pixel/product feed | Variant content IDs match catalog | | | |

## Release and reporting

- Verification links/results in GA4 DebugView/Tag Assistant, Meta Test Events/Diagnostics and Shopify tests:
- Reporting definitions and lag/attribution setting differences:
- Acceptance thresholds determined by merchant baseline and actual platform reporting:
- Event owner, next audit date, incident response and rollback:
- Explicit authorized publish/modify approval: **not granted by this template**.
