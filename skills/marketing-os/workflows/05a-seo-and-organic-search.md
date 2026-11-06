# Workflow 5A — SEO discovery → page plan → optimization → measurement

**Trigger:** Search visibility is weak, product pages aren't found, new site/collection/service launch, content strategy needed, ecommerce technical audit, search traffic doesn't convert, or an offering needs an organic discovery plan.

**Position:** An optional sub-workflow of [Stage 5 channel planning](05-channel-and-campaign.md), informed by [Offering Discovery 1A](01a-offering-discovery-and-marketing-plan.md), [Buyer Discovery 2](02-buyer-discovery.md), [Brand Discovery 3A](03a-brand-discovery-and-messaging.md), [SEO research](../references/seo-fundamentals-and-ecommerce.md) and [CRO 4A](04a-conversion-rate-optimization.md).

**Output:** prioritized `intent → page → proof → on-page action → conversion destination → KPI` plan, technical findings with severity/evidence, original content briefs, ready-to-review page copy/metadata and measurement plan. Use [Search & Conversion Audit](../templates/search-and-conversion-audit.md).

## 0. Scope and evidence access
- Confirm domain, geography, language, product/service scope, business goal, page types, CMS/framework and current source-of-truth brand/offering facts.
- If available inspect Google Search Console (GSC), Bing Webmaster Tools, analytics and commerce/CRM performance **with permission**. Never claim current indexing, traffic or rankings without evidence. For public-only scans distinguish observable HTML from search-platform status.
- Determine which commercial outcomes matter: qualified visits, sales contribution, leads or retention. Set baseline and period with known caveats.

## 1. Buyer questions and search opportunity
- Begin with *situations and intent*—problem, category, alternative comparison, shopping, branded navigation, after-sales troubleshooting and local search where genuinely relevant.
- Gather real queries from GSC, site search, product reviews, support, sales, customer interviews and live result pages. Estimated keyword volume is imperfect; avoid imaginary search volumes.
- Map `question/intent | buying stage | buyer | expected SERP format | existing page | desired page | proof | actual conversion path`.
- Evaluate business relevance, ability to satisfy the intent uniquely, content gaps, real competitors and appropriate next step; don't create a page for every keyword synonym.

## 2. Technical eligibility and discoverability
Inspect actual evidence:
1. URL HTTP status, robots, noindex, canonicalization, redirects, sitemaps and indexing errors.
2. Site architecture, HTML links, category/PDP access, breadcrumbs, orphan pages, faceted navigation, product variations, duplicate URLs and pagination.
3. Raw HTML versus rendered content, especially on JavaScript sites; bots have different rendering support. Check SSR/pre-rendering and route status for critical product content.
4. Titles, meta descriptions, main heading, language/locale, relevant image alt text, media and readable text.
5. Mobile usability, accessibility and field Core Web Vitals (LCP/INP/CLS). Avoid declaring performance from one lab run alone.
6. For stores, validate Product/Offer structured data and Merchant Center feed against actual SKU name, price, stock, variants, shipping/returns and page text; check Google Rich Results Test and documented feature eligibility.

Classify: **P0 eligibility/blocking**, **P1 strong commercial user friction**, **P2 content/architecture opportunity**, **P3 cosmetic/low-confidence**. A sitemap or schema error might be low priority if the page is already properly discovered or the schema doesn't qualify for a supported result.

## 3. Build page-specific search and persuasion briefs
For each priority page decide:
- Specific intent; page type; unique reader question; whether to improve existing page instead of creating another.
- One honest category+benefit proposition, evidence/first-hand value, comparisons and relevant FAQ.
- Accurate title/H1/meta description (Google can rewrite title links/snippets; these are suggestions, not hard limits or guaranteed CTR lifts).
- Internal anchor links/navigation and related next-step content.
- Clear product features, actual price, availability, images/scale, genuine reviews/policies, CTA and landing-page consistency.
- Optional eligible schema plan, verified attributes and review/check process. Do not invent ratings or rich-result eligibility.
- Brand style from 3A and offering claim register from 1A.

**Deliverable:** page brief and copy drafts with source IDs, implementation owner and approval. No mass AI-generated near-duplicate pages or copied competitor content; prioritize first-party utility.

## 4. Prioritize and implement
- Fix P0 crawl/index/canonical/product price mismatches and broken pages before new content.
- Improve highest-intent, highest-opportunity existing pages when evidence supports them.
- Build category/service guides, comparisons and resources when they add meaningful unique value.
- Create/update relevant structured data and product feeds after source-of-truth verification.
- Coordinate with [CRO 4A](04a-conversion-rate-optimization.md): search traffic quality and page persuasion must both be evaluated.

## 5. Measure and learn
Use GSC queries/pages/impressions/clicks, coverage/indexing status, actual product/lead outcomes, real user Web Vitals and segmentation by intent/device/market. Observe changes with sufficient time for crawl and ranking fluctuations. Changes in clicks do not automatically prove causation; control for seasonal demand, ranking/SERP changes, catalog changes and brand campaigns.

Record `finding → evidence → technical/content action → date → result and uncertainty → next step`. For user requests focused on AI citations, branch to [AEO 5B](05b-aeo-ai-search-visibility.md) without abandoning SEO fundamentals.

**Stop conditions:** indexing unknown but asserted; proposed fabricated product information, keyword-stuffed pages, deceptive reviews, scaled low-value SEO content, unapproved production changes. Publishing requires owner approval.

**Source backing:** [Google SEO guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), [JS SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics), [helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), [product rich results](https://developers.google.com/search/docs/appearance/structured-data/product), [Search Console](https://developers.google.com/search/docs/monitor-debug/search-console-start), [Core Web Vitals](https://web.dev/articles/vitals).
