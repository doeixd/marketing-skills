# Shopify product catalog, merchandising, taxonomy and product copy

Reviewed: 2026-11-06. Use [Merchandising Workflow 03B](../workflows/03b-shopify-catalog-and-merchandising.md) and [Product/Collection Brief](../templates/shopify-product-collection-content-brief.md).

## Source of truth → usable product information

Map **parent product vs actual variants vs bundles**, correct titles/handles/SKUs, vendor/brand, product taxonomy/category, tags, options, attributes, materials/dimensions/compatibility, colors/sizes, inventory, available-to-sell by location/market, shipping, returns, imagery and rights. Prefer a structured schema of facts, not invented category stereotypes.

Shopify product and variant data power many surfaces: PDP/collection pages, Search & Discovery filters, Google Merchant Center, Meta catalog, Shop, email, SEO snippets, paid ads and support. Avoid marketing claims that are true for one variant but false for another. Store qualified attribute/benefit proof and availability by the correct product/variant. Treat claims like "waterproof", "handmade" or origin as regulated/factual and require substantiation.

**Metafields and metaobjects** allow reusable structured data that themes can render through compatible dynamic sources. Use them for verified specs, care, fit, FAQ, collection attributes and brand storytelling when appropriate—not as an excuse to duplicate every text field. Plan definitions, types, localization, source of truth, import/export QA, theme connections, ownership and access controls. Avoid attaching contradictory facts in Shopify, Google, Meta and old CSVs.

## Collection/PLP merchandising

Check:
1. Collections map to meaningful buyer tasks, occasions and distinguishable product types—not simply internal warehouse categories.
2. Navigation, breadcrumbs, collection titles/descriptions, useful filtering, sorting and search. Filters should use normalized factual categories and attributes.
3. Mobile product cards show real product, consistent photo, name, price, meaningful variant/availability and appropriate on-card signal (only if true).
4. Search & Discovery: configured filters, synonym groups, results visibility and related/complementary recommendations where supported; use real onsite search queries and zero-results.
5. Catalog availability: broken filters, out-of-stock dominance, duplicate variant cards, confusing bundles, wrong prices, inaccessible product links.
6. Cross-sells: complements to the current purchase, not random high-margin items. Bundle value and inventory/fulfillment must be truthful.
7. Seasonality/gifting: curate where buyer buying occasions justify it; don't create hundreds of near-duplicate seasonal collections.

Distinguish indexable main collections from filter/facet URLs that may create duplication or crawl traps; investigate current canonical/robots behavior and business value before forcing technical overrides.

## PDP copy and information

A product page should answer **what it is, who it suits, how it looks/works, options, exact fit/material, what arrives, total price, delivery, return risk, proof and action**. Copy framework:
- Category/product-forward title; descriptive 1–2 sentence opening in actual brand voice.
- 3–6 prioritized feature→buyer benefit bullets, not generic adjectives.
- Variant-specific product facts, dimensions, materials, sizing guide, care and compatibility.
- Real closeups/scale/context/video or demo, no fabricated image review or usage.
- Actual policy/assurance, trust evidence and honest limitations.
- FAQ drawn from real support questions, relevant cross-sells and CTA.

Use [Offering 1A](../workflows/01a-offering-discovery-and-marketing-plan.md) to derive buyer reasons and factual claim IDs. Optimize for buyer comprehension and organic search intent jointly, not an arbitrary word count.

## Bulk imports and governance

When proposing CSV/API/ETL: map sources, keys, variants, options, unique handles, images, collections, taxonomy and metafields; dry-run a subset, verify data consistency and diffs, preserve rollback, check deleted/archived products and redirects, honor Shopify API limits/scopes. Never propose editing dozens of live products without snapshot and explicit permission.

**Output:** category architecture, catalog integrity findings, variant/mapping rules, prioritization by impact, product/collection briefs, copy bank, collection merchandising plan, feed mapping and QA.

Sources: [Shopify Liquid product object](https://shopify.dev/docs/api/liquid/objects/product), [Search & Discovery](https://help.shopify.com/en/manual/online-store/storefront-search), [Search & Discovery filters](https://help.shopify.com/en/manual/online-store/storefront-search/search-and-discovery-filters), [Metaobject dynamic sources](https://help.shopify.com/en/manual/custom-data/metaobjects/connecting-to-your-online-store/connecting-metaobjects), [Shopify Bundles](https://help.shopify.com/en/manual/products/bundles/shopify-bundles), [Google Merchant spec](https://support.google.com/merchants/answer/7052112).
