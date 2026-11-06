# Ecommerce and marketplace data: Shopify, Etsy, Amazon and cross-channel joins

**Reviewed 2026-11-06.** Use with [ETL](marketing-data-engineering-and-etl.md), [measurement](measurement-pixels-ga4-and-attribution.md) and [Workflow 8D](../workflows/08d-marketing-data-pipelines-and-measurement.md). A Shopify-managed site can collect its own web events; an Etsy/Amazon marketplace storefront is controlled by that platform. Do not recommend installing arbitrary Meta Pixel or GA4 checkout code on marketplace pages.

## Shopify: source of truth and extraction

- Use **Admin GraphQL API** for current supported products, variants, orders, customers, refunds, fulfillment, inventory and transactions, with access scopes and versioned schema. For large exports use [bulk query operations](https://shopify.dev/docs/apps/build/apis/graphql-admin/bulk-operations/queries); account for asynchronous result availability, JSONL parent-child relationships and partial failures. Track API versions and per-merchant scopes.
- Webhook notifications plus periodic reconciliation are complementary. Authenticate webhook signatures, idempotently process delivery IDs/order revisions, handle out-of-order/missed events and have backfill. Don't infer cancellation/refunds from order creation alone.
- Separate order placed date, payment state, financial events, order edits, tax, discounts, shipping, return and fulfillment dates; build an explicit metric for gross/net/realized contribution. Verify how gift cards, tips, duties, shipping refunds and marketplace channel orders are represented.
- Public storefront Web Pixels concern browser behavior; Admin order API and payment details concern commercial records. Never send raw protected Shopify customer data to arbitrary pixels. Use [Shopify Web Pixels](https://shopify.dev/docs/api/web-pixels-api) and [privacy](https://shopify.dev/docs/api/customer-privacy).
- Govern variant/SKU/item ID joins between catalog, Meta Content IDs and Google Merchant feeds, including product vs variant IDs and bundle mappings. Maintain historical mapping if SKU/title changes.

## Etsy: Etsy Open API v3, receipts and limitations

- Use [Etsy Open API v3](https://developer.etsy.com/), [API reference](https://developer.etsy.com/documentation/reference) and [authentication](https://developer.etsy.com/documentation/essentials/authentication/). Authorized seller endpoints provide shop receipts/order transactions, listings/inventory and shop information; confirm endpoint scopes such as `transactions_r`, app access and OAuth grants before extraction.
- Follow [QPS/QPD rate limits](https://developers.etsy.com/documentation/essentials/rate-limits/) with retry and progressive backfill. Use Etsy receipt and transaction IDs with shop ID to dedupe; preserve currency, refunds/cancellations and listing/variation references.
- Distinguish Etsy Stats, Ads reporting, payout/payment-account figures and receipt order totals: platform reporting, fees, offsite-ads fees, refunds and booked dates will differ. Model each money flow separately rather than multiplying unit price by quantity and calling it net payout.
- Etsy's [merchant GA4 setup instructions](https://help.etsy.com/hc/en-us/articles/360000337967-How-to-Use-Google-Analytics-for-Your-Etsy-Shop) describe a platform-provided integration; verify current availability/coverage. Do **not** claim merchants can run arbitrary scripts, Meta pixel/CAPI or browser-level identity tracking throughout Etsy checkout.
- Seller-side API/order access is **not** blanket permission to export buyer emails to ad audiences or contact customers for unrelated marketing. Review Etsy policies, applicable law, consent and permitted purposes; default to aggregate analytics.

## Amazon: seller operations vs ads analytics

- Use Amazon [SP-API](https://developer-docs.amazon/sp-api/docs/connecting-to-the-selling-partner-api) for authorized seller records; [Reports API](https://developer-docs.amazon/sp-api/docs/reports-api) for asynchronous report requests/downloads, and [Data Kiosk](https://developer-docs.amazon/sp-api/lang-en_US/docs/data-kiosk-api) for eligible GraphQL seller sales and traffic measures. [Orders API](https://developer-docs.amazon/sp-api/docs/orders-api-v0) and Financial Events/Finances where needed; confirm up-to-date roles, schemas, regional access and release notes.
- Model `seller_account + marketplace_id + AmazonOrderId`, ASIN + seller SKU + fulfillment type (FBA/FBM) and per-order/fee/return financial events. Sales/traffic report `ordered units` are not payouts; conversion denominators vary by report. Data Kiosk reports may have time-window/grain limits.
- Protected buyer PII may require Amazon [Restricted Data Token](https://developer-docs.amazon/sp-api/lang-US/docs/authorization-with-the-restricted-data-token) and special role/security requirements. Do not obtain/expose PII unless justified and authorized.
- Amazon Ads reporting is a **separate** measurement/API surface from SP-API. [Amazon Attribution](https://advertising.amazon.com/en-us/solutions/products/amazon-attribution/) measures eligible *off-Amazon traffic* driven to Amazon using specific attribution tags, not a general-purpose first-party pixel on Amazon checkout. Check eligibility, available metrics and attribution windows; do not assume UTMs in an Amazon URL grant GA4 access to order conversion.
- Track settlement date, currency, marketplace, promotions, refunds, storage/FBA/referral fees and reported ad spend separately before true contribution reporting.

## Cross-channel join discipline

Use a product identifier bridge, not fuzzy product title alone: `canonical_product_id → [shopify variant gid, sku, gtin] / [etsy shop/listing/variation] / [amazon marketplace, ASIN, seller_sku]`. Store effective-dated mapping and flags for ambiguous bundles, merged items or name changes. Each platform retains its own order, customer and transaction namespaces. **Never automatically infer that a buyer on Etsy/Amazon is the same person as a Shopify buyer by similar names/emails or identity lookups**; such joins require lawful, permitted purposes and documented evidence.

Comparable net revenue and marketing margin require a definition sheet: source currency, tax inclusion, shipping income/costs, promotions, platform commissions, payment fees, ad costs, returns, COGS, fulfillment, customer support, referral commissions, FX rates, cost allocation. Warn when fees are estimates or settlement timing lags.

## Recommended reconciliation

For each platform separately compare `orders_count, units, gross_merchandise_value, discounts, cancellations, refunds, net_revenue, fees, settlements` over the *same* source-defined date, status, currency and timezone. Only then roll up channels. For marketing comparison preserve distinct paid attribution reports and campaign tagging; avoid reconciling marketplace ad conversion rows to Shopify orders as if IDs shared a common meaning.

**Output:** access/scope matrix, connector method, field mapping, ID bridge, metric definitions, quality checks, approval list, and “not observable” limitations.
