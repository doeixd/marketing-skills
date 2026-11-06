# Shopify acquisition: Google Shopping, Performance Max, Meta catalog ads and measurement

Reviewed 2026-11-06. Use [Shopify Ads Workflow 05I](../workflows/05i-shopify-shopping-ads-and-tracking.md), [Feed/Tracking QA](../templates/shopify-merchant-feed-and-pixel-qa.md), [Google Search 5G](../workflows/05g-paid-search-google-ads.md) and [Meta creative 6](../workflows/06-creative-production.md).

## Catalog integrity precedes shopping automation

Shopify products/variants, Google & YouTube channel/Google Merchant Center, Facebook & Instagram by Meta and catalog ads must agree on **actual identifiers, variant attributes, brand, condition, price/currency, availability, product images, categories, shipping, returns and destination**. Check sync status, rejected products, GTIN/MPN/brand when legitimate, apparel/accessory requirements, locale, market and policy. Never invent identifiers or misrepresent stock to force approval.

Distinguish:
- **Google free listings / Shopping / Performance Max**: product feed plus Google Ads/Merchant Center, with account eligibility, goal, assets and budget.
- **Google Search keyword campaigns**: query-targeted responsive search ads and landing pages (see [5G](../workflows/05g-paid-search-google-ads.md)).
- **Meta dynamic/catalog ads**: pixel/catalog/commerce configuration and authorized brand/product creative; check pixel-to-product identity matching and audience permissions.
- **Organic Shop and social commerce**: availability and checkout behavior depend on account, country and channel.
- **Other channels**: Pinterest, TikTok Shop, marketplace and affiliates require their own source-of-truth feed/eligibility; don't assume Shopify compatibility guarantees approved listings.

**Performance Max** spans multiple Google inventories, not exclusively keyword Search. A feed-only or asset-creative PMax configuration has different reach/controls; verify current live settings. Do not declare "PMax always better" or use it without reliable conversions and margin/return constraints. Google brand and nonbrand acquisition differ; evaluate incrementality where possible.

## Shopify Web Pixels and privacy

Shopify's [Web Pixels](https://shopify.dev/docs/api/web-pixels-api) run in sandboxed contexts using customer events and respect privacy configurations; app pixels and custom pixels differ. Inspect configured pixel integrations and event sources before adding snippets. Map `product_viewed`, `product_added_to_cart`, `checkout_started`, `checkout_completed` and relevant customer events to actual Google Ads, GA4, Meta and platform goals; **do not assume all events fire under each consent setting/channel**.

Audit **event_id / transaction_id deduplication**, currency/value, tax/shipping inclusion, order edits, refunds, timezone, server-side/CAPI double counting, checkout domain and conversion windows. Shopify orders are source of truth for sales; ads attribute some sales and can double-count overlap. Report coverage limitations, avoid leaking customer PII through URLs/pixels, and never install tracking without consent/owner permission.

## Profit and performance

Calculate SKU/category and channel **contribution economics** first; price, discounted sale revenue and profit differ. Check channel cost plus production/creator costs, promotion impact, return/cancellation rate, branded demand overlap and campaign scope. A high attributed ROAS doesn't establish incremental profit.

Use diagnostics:
- Disapproved product → inspect exact field mismatch/policy/merchant settings; fix original Shopify catalog first.
- Ads spend but no orders → search/query/buyer fit, product feeds, creative, landing, tracking, stock and price.
- High clicks low conversions → check expectation mismatch, PDP evidence, checkout and real costs.
- Products missing in market → Shopify Markets availability + channel sync, not automatically keyword choice.
- Pixel mismatch → confirm same variants/ids and event identifiers across store/catalog/platforms.
- Purchase counts exceed real orders → dedupe, attribution/cross-channel overlap, conversion action settings.
- Campaign "wins" but margin declines → product-mix/discount/returns and incremental contribution.

**Output:** channel/feed inventory, rejected/eligible SKU list, exact mismatch fixes, approved campaign/job, event map, spending guardrails, creative assets and experiment agenda. Changes to live feeds, pixels, ad budgets or campaigns require explicit authorization.

## Sources

- [Shopify Google & YouTube channel requirements](https://help.shopify.com/en/manual/online-sales-channels/marketplaces/google/requirements)
- [Google Merchant Center product data specification](https://support.google.com/merchants/answer/7052112)
- [Google merchant product structured data](https://developers.google.com/search/docs/appearance/structured-data/product)
- [Shopify Web Pixels API](https://shopify.dev/docs/api/web-pixels-api)
- [Shopify Facebook & Instagram by Meta](https://help.shopify.com/en/manual/online-sales-channels/facebook-instagram-by-meta)
- [Google Performance Max guidance](https://support.google.com/google-ads/answer/10724817)
- [Meta catalog ads documentation](https://www.facebook.com/business/ads/catalog-ads)
