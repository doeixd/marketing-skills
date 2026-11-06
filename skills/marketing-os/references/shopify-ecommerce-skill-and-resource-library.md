# Ecommerce agent skills, resources and reference patterns

**Research date:** 2026-11-06. Use with the [Shopify Store Diagnosis 1B](../workflows/01b-shopify-ecommerce-diagnosis.md) and [Shopify source library](shopify-ecommerce-strategy-and-economics.md). These external skills are **reference examples**, not automatically installed dependencies. Verify each repository's actual current content, maturity, license and tool prerequisites. Do not copy upstream instructions/code without license review.

## 1. Shopify's own developer agent skills — primary for implementation

**[Shopify/Shopify-AI-Toolkit](https://github.com/Shopify/Shopify-AI-Toolkit)**: Shopify-authored `shopify` skill routes Admin GraphQL, Liquid, Flow, ShopifyQL, Functions, checkout extensions, custom data, Hydrogen and CLI operations. Use for **implementation details**, not to infer whether a marketing change will improve sales.

**[Shopify/agent-skills](https://github.com/Shopify/agent-skills)**: specialized `shopify-liquid`, `shopify-admin`, `shopify-custom-data`, `shopify-functions`, `shopify-hydrogen`, `shopify-storefront-graphql` and checkout extension skill material. It describes documentation search/schema validation workflows; this Marketing OS should **look up current Shopify docs and validate API/theme artifacts**, not hallucinate Liquid fields, metafield types or APIs. Do not claim a local Shopify CLI/docs tool is installed unless confirmed.

**[benjaminsehl/liquid-skills](https://github.com/benjaminsehl/liquid-skills)**: third-party Liquid theme standards, accessibility and component patterns; useful supplementary examples, not official Shopify policy or permission to edit a live theme.

## 2. Merchant-oriented ecommerce agent skills

| Collection | Relevant skills and pattern | Maturity and use restriction |
|---|---|---|
| [proskillpacks/shopify-store-skills](https://github.com/proskillpacks/shopify-store-skills) | Narrow tasks: real-image alt text, policy-page contradictions, product-title cleanup, authentic review replies, agent-readiness QA; importable CSV/review sheets | Author describes real-store validation; verify claims and code yourself; no live write authorization |
| [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills) | `shopify-marketing`, `shopify-seo`, `shopify-conversion-optimization`, `shopify-email-flows`, `ecommerce-checkout-optimization`, `google-shopping-optimization`, `ecommerce-feed-management`, `ecommerce-growth-strategy`, `shopify-upsell-cross-sell`, `shopify-analytics-guide` | Wide catalog of templates; many marked **beta** and short/general. Inspect actual skill before treating as research or tested Shopify integration |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | General `seo-audit`, `cro`, `emails`, `ads`, `conversion-tracking`, `ab-testing`, `pricing`, `referrals`, `social` | Strong modular workflow patterns; not Shopify-specific implementation authority |
| [Shopify official skills](https://github.com/Shopify/agent-skills) | Theme/GraphQL/Flow/custom-data schema checking | Specialized technical skills; require appropriate environment/authorization |

**What Marketing OS should borrow as a design pattern:** narrow input/output contract, named evidence source, CSV/merchant-export compatibility, actual theme/plan check, claim-safe review stage, testable artifacts, no write without consent and shared brand/offering fact ledger. **What to reject:** "best Shopify app" without plan/cost proof, generic keyword stuffing, unsourced 2X conversion promises, imaginary sales data, copy-paste beta advice, invented customer reviews, risky production theme edits.

## 3. Shopify's official marketing and technical sources

- [Shopify Help Center marketing](https://help.shopify.com/en/manual/promoting-marketing/create-marketing) — current merchant setup and workflows.
- [Shopify theme performance](https://shopify.dev/docs/storefronts/themes/best-practices/performance) — Liquid-first SSR content, script/image priorities, performance checks.
- [Shopify Liquid Product object](https://shopify.dev/docs/api/liquid/objects/product) — product/variant rendering.
- [Shopify custom data and metaobjects](https://help.shopify.com/en/manual/custom-data/metaobjects/connecting-to-your-online-store/connecting-metaobjects) — structured reusable product facts.
- [Search & Discovery](https://help.shopify.com/en/manual/online-store/storefront-search) — catalog search, filters and recommendations.
- [Shopify international SEO/Markets](https://help.shopify.com/en/manual/markets/seo) — locales, translated URLs, hreflang and storefront availability.
- [Shopify Google & YouTube channel](https://help.shopify.com/en/manual/online-sales-channels/marketplaces/google/requirements) — Merchant Center sync eligibility and identifiers.
- [Shopify Web Pixels](https://shopify.dev/docs/api/web-pixels-api) — sandboxed events, consent and pixel limitations.
- [Shopify September 2026 analytics changes](https://help.shopify.com/en/manual/reports-and-analytics/discrepancies/session-measurement-update) — session/CVR denominator comparability.
- [Shopify checkout customization](https://help.shopify.com/en/manual/checkout-settings/checkout-customization) — Basic vs Plus checkout extension permissions.
- [Shopify Messaging automation](https://help.shopify.com/en/manual/promoting-marketing/create-marketing/shopify-messaging/marketing-automations) + [Shopify Flow triggers](https://help.shopify.com/en/manual/shopify-flow/reference/triggers) — real lifecycle automation availability.
- [Shopify customer segments / Forms / Messaging / Flow](https://help.shopify.com/en/manual/promoting-marketing/create-marketing/automation-tools) — segmentation and consented acquisition.
- [Shopify Autopilot](https://help.shopify.com/en/manual/promoting-marketing/autopilot) — optional merchant AI recommendations requiring real approval.

## 4. Independent usability, SEO, analytics and experimentation resources

- [Baymard ecommerce product page UX](https://baymard.com/research/product-page), [product list & filtering UX](https://baymard.com/research/ecommerce-product-lists), [onsite search UX](https://baymard.com/research/ecommerce-search), [checkout](https://baymard.com/research/checkout-usability): research-supported paths and friction patterns, not guaranteed lift for any store.
- [Nielsen Norman Group ecommerce trust & credibility](https://www.nngroup.com/reports/ecommerce-ux-trust-and-credibility/) and [ecommerce product pages](https://www.nngroup.com/reports/ecommerce-ux-product-pages-including-reviews/) — product information and buyer confidence.
- [Google Search Central ecommerce](https://developers.google.com/search/docs/specialty/ecommerce) and [Product structured data](https://developers.google.com/search/docs/appearance/structured-data/product) — merchant discovery requirements and platform limits.
- [Google Merchant product data spec](https://support.google.com/merchants/answer/7052112) — feed attribute rules, not a universal SEO checklist.
- [Google Web Vitals](https://web.dev/articles/vitals) — real-user performance.
- [Klaviyo ecommerce email education](https://www.klaviyo.com/blog/ecommerce-email-marketing) — useful lifecycle models, vendor perspective; validate with Shopify Messaging/installed ESP and consent.
- [Google Analytics ecommerce implementation](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce) — event schema and money-value consistency.
- [FTC endorsements/disclosures](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers) and [reviews/testimonials rule](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers) — genuine review/UGC and affiliate/social commerce safeguards.

## 5. Use these resources as an agent

1. Identify actual store structure, plan, theme, markets, channel apps, consent and available data.
2. Route marketing strategy to **Marketing OS**; route Shopify coding/schema specifics to **current official Shopify documentation and technical skills when tools exist**.
3. Take a snapshot and ground facts in product/variant, store settings, public pages and authorized exports.
4. Use narrow outputs: store audit, SKU feed matrix, PDP brief, collection query-intent map, lifecycle triggers, pixel event map or campaign plan.
5. Validate against business constraints, human perception, source evidence and live-eligible platform requirements.
6. Keep **recommendations** distinct from **changes performed**; no live mutation, app install, ad spend or message send without authorization.
7. Prefer fewer strong experiments/actions over exhaustive generic checklists.

### Skill library coverage gaps addressed by Marketing OS

Many third-party skills focus on a single task (title or policy checker) or only broad planning. Marketing OS should uniquely connect **verified Shopify catalog truth → buyer jobs → brand positioning → collection/PDP merchandising → organic search → Google/Meta feed advertising → consented lifecycle → margin and cohort outcomes**, plus evidence/approval and technical implementation handoffs. This is an architectural recommendation, not a claim that external authors lack other features.
