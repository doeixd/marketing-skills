# First-party event and destination implementation matrix

Use [Tracking Workflow 8E](../workflows/08e-event-instrumentation-and-conversion-qa.md) and [2026 API Source Notes](../references/2026-platform-data-api-updates.md). **Draft only: no live tracking modification or user-data sharing is authorized.**

## Business/technical inventory
- Merchant brand, Shopify shop, active theme/headless, checkout and market:
- Existing Shopify pixel apps, custom pixels, GTM web/server, Meta native channel, Google channel, CRM/CAPI integration:
- Meta dataset/pixel and ad account, GA4 stream, Google Ads conversion account and Google Data Manager:
- Consent manager / Shopify customerPrivacy and geo modes; signed-off legal purpose:
- Canonical order source (payment/paid/refunds) and event creation authority:
- Current sender duplicate risk and owners:

## Event → destination mapping
| Moment | Canonical action/trigger | Shopify event/webhook | GA4 event and items/value/currency | Meta event and product content IDs | Google Ads/DM goal | Stable event ID / order ID | Actual consent gate | Source and QA |
|---|---|---|---|---|---|---|---|---|
| View product | | product_viewed | view_item | ViewContent | | | | |
| Add item | | product_added_to_cart | add_to_cart | AddToCart | | | | |
| Checkout start | | checkout_started | begin_checkout | InitiateCheckout | | | | |
| Purchase/paid order | | checkout_completed vs paid ledger | purchase | Purchase | | | | |
| Refund / edit | | Admin order/transaction adjustment | refund | no fresh Purchase | adjustment | | | |

## Pixel/CAPI and identity rules
- Browser vs server sender name, event ID generation/storage, exact matching event name:
- Same action: share event ID; new action: distinct ID; replay: ID stable:
- Meta Event Match Quality and Test Events/dedup results **observed**, not assumed:
- GA4 Measurement Protocol real client/session identity source and validation:
- GA4 value = items price×quantity, shipping/tax separate by current spec:
- Google Data Manager conversion action, event/audience type, `validateOnly` QA and async status:
- Google Consent Mode v2 `ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization` vs Shopify consent flags:
- Real product/variant ID → Meta Catalog → Merchant Center/GA4 item ID mapping:
- Avoid PII in URLs/logs, minimum approved hashed identity and deletion policy:

## Test matrix
| Case | Expected (per real consent/policy) | Observed | Evidence / system | Pass / known gap | Fix owner |
|---|---|---|---|---|---|
| Consent denied/granted/changed | | | | | |
| Mobile Safari / ITP / adblock | | | | | |
| Same browser+server Purchase | | | | | |
| Two separate purchases | | | | | |
| Retry + partial refund | | | | | |
| GA4 MP validation/DebugView | | | | | |
| Meta Test Events/dedup | | | | | |
| Data Manager validation/async upload | | | | | |
| Country / currency / variant | | | | | |
| UTM and approved click-ID redirect | | | | | |

## Release
- Draft changes/owner and rollback:
- Merchant/legal/brand approval, event correctness and consent verification:
- **No live publishing without explicit authorization**:
- Monitor delayed/missing events, duplicate anomalies, actual orders and attribution separately:
