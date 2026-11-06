# Workflow 3B — Shopify product and collection intelligence → merchandising → copy

**Trigger:** Product title/description rewrite across a Shopify catalog, reorganize collections, filters and search, variant confusion, upsell/cross-sell, product data/metafield work, low category findability, import prep or merchandise campaign.

**Place:** Stage 3 specialist. Start from [Offering Discovery 1A](01a-offering-discovery-and-marketing-plan.md) and [Brand/voice 3A](03a-brand-discovery-and-messaging.md); read [catalog guide](../references/shopify-catalog-merchandising-and-data.md) and use [product/collection content brief](../templates/shopify-product-collection-content-brief.md).

## 0. Identify catalog scope and source of truth

Shop domain, actual SKU/variant/bundle, source CSV/JSON or admin data, real product page/images, brand rules, market/language, customer questions, collection taxonomy, filter needs and destination constraints. Compare official Shopify product/variant state with stale CSV/vendor data, not the other way around. Mark unavailable source fields.

## 1. Product and variant fact map

Collect `product id/handle/title | variant SKU/options/id | barcode/GTIN if genuine | inventory/availability by market | price/currency | material/size/dimensions/attributes | validated claim ID | media/alt | shipping/returns/fit`. Do not claim variant-wide material/price/availability that differs by option.

Derive `feature → buyer consequence → benefit → proof → tradeoff`, with buyer job/occasion and real alternatives. Identify hero/top contributors, overstock, stockout risks and commercially unsuitable discount candidates only with actual economics.

## 2. Collection taxonomy, store search and discovery

Build intended customer hierarchy: category, occasion, style, material, fit, intent. Check Shopify collections, handles, merchandising/sort/stock, product cards, Search & Discovery filters, synonyms, results/no-results behavior, actual real onsite query types and navigation. A product without a findable path is a store discovery problem, not necessarily an external ad targeting problem.

Use structured metafields/metaobjects **only when definitions/values, theme bindings, translation and ownership are viable**. Normalize factual variant attributes before using as filters. Plan complementary recommendations around the current buyer's task; don't insert unrelated high-margin items.

## 3. Copy and creative from product truth

Produce catalog-specific titles that identify what is sold, useful short/long descriptions, 3–6 benefit bullets, verified specifications/fit/care/assurance, category page text and SEO titles/descriptions. Supply real product photography shot list, honest alt text describing what's visible and optional videos/size demonstrations. Respect original brand voice and real material claims; do not write generic "premium craftsmanship" for every item.

## 4. Channel/merchant consistency

Map Shopify data → product page → structured data → Google Merchant Center/Shop/Meta feed: name, SKU/variant identity, brand, identifiers, price, currency, stock, markets, shipping/returns. Surface mismatches and owner/sync setting. Coordinate [SEO 5H](05h-shopify-ecommerce-seo.md), [Ads 5I](05i-shopify-shopping-ads-and-tracking.md) and [CRO 4B](04b-shopify-ecommerce-cro.md).

## 5. Change planning and QA

For bulk edits give dry-run changed-row CSV / old→new diff, sample product/variant verification, rollback, redirect plan for handle changes, theme/metafield dependencies, backup and staged approval. Don't mutate inventory/prices/title/handle or launch feeds without user consent. Exclude speculative and unsupported claims.

**Deliverable:** structured catalog/collection audit, product/collection messaging, customer findability improvements, feed-ready fields, SEO/CRO handoff, measurable implementation and rollback.
