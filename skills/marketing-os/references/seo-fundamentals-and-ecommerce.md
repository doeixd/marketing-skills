# SEO fundamentals — discovery, crawling, relevance, architecture, and commerce

Reviewed: 2026-11-06. Read with [SEO workflow](../workflows/05a-seo-and-organic-search.md), [offering discovery](../workflows/01a-offering-discovery-and-marketing-plan.md), and [SEO/AEO/CRO audit template](../templates/search-and-conversion-audit.md).

## 1. Mental model and goals

**Search Engine Optimization (SEO)** helps a search engine discover, understand, index and appropriately present useful pages to people searching for relevant needs. It is *not* a promise to rank first, a fixed checklist of keyword placements, or a replacement for a competitive product and a usable website.

Distinguish **technical eligibility** (crawl/index/canonical), **topic and intent match** (what query/journey a page serves), **information quality** (first-hand knowledge, accurate evidence, clarity), **site architecture** (internal discovery/navigation), **search appearance** (titles/snippets/merchant formats), and **commercial outcome** (qualified visits, leads, sales and contribution). Measure separately.

Begin by asking:
- What does the buyer search *before* category awareness, during comparison, when ready to purchase, and after purchase?
- What type of page best answers that intent: guide, category, PDP, service page, comparison, FAQ, location page, original tool, support?
- What first-party knowledge, measurements, examples or expertise can this business contribute that is not already commodity content?
- Is a useful page *actually present*, indexable, internally linked, fast enough, and honest?
- What happens after a search visitor lands there?

## 2. Crawl, render, index, canonicalize

Audit site evidence before recommending a fix:
1. HTTP status and meaningful redirects, robots.txt, robots meta/X-Robots-Tag, canonical signals, noindex and staging protections.
2. Discoverability from navigational/internal HTML anchors (`<a href>`), categories, breadcrumbs, relevant guides and XML sitemaps. Sitemap submission is a discovery aid, not an indexing guarantee.
3. Canonical rules and duplication across filtering/facets, pagination, tracking URLs, near-identical product variants, out-of-stock pages, multi-currency and locale pages.
4. If JavaScript-rendered, check **raw HTML vs rendered DOM**. Google can render JavaScript but rendering has extra steps; server-side/pre-rendered critical text, links and product structured data can improve robustness across crawlers. Ensure SPA routes return meaningful HTTP status codes; avoid accidental soft 404s.
5. Check mobile layout, accessibility, internal search/navigation, and Core Web Vitals in **field data**: LCP <= 2.5s, INP <= 200ms, CLS <= 0.1 at 75th percentile (as of review; measure mobile/desktop separately). These are experience signals, not a ranking guarantee or proxy for conversion.

Use [Google Search Console](https://developers.google.com/search/docs/monitor-debug/search-console-start) and [Google JS SEO documentation](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics). No GSC access? State that visibility/indexation cannot be confirmed by speculation; inspect what is publicly visible and request a crawl or exports.

## 3. Search intent, architecture and content planning

Create an **intent → question → page → proof → CTA → next-page** map. Distinguish informational, problem-solving, comparison, transactional, local, brand, and after-sales intents. Use query evidence, onsite search, customer-support questions, purchase occasions and real competitor result types; don't equate estimated volume with commercial value.

Design a logical hierarchy:
- Home / about / brand facts
- Collections and categories (browse, filter, compare)
- Product detail pages for purchasable SKUs/variants
- Services/capabilities and proof or case studies
- Original guides and comparisons responding to real questions
- Support/FAQ, policy, sizing, returns and delivery information
- Local pages only for genuine staffed/served locations; avoid doorway pages

Use descriptive URLs and anchors; links should help both users and crawlers navigate. Ensure each page has a **distinct purpose** and clear relationships. Keyword cannibalization is not automatically a problem when pages serve different intents; unnecessary near-duplicate pages should be consolidated, improved or removed based on evidence, not a universal "one keyword one URL" rule.

## 4. On-page communication

For each key page review:
- Accurate main title and H1 identifying the product/topic; concise useful opening and recognizable brand.
- Prominent value proposition, relevant specifications, use context, real limitations and purchase/lead next step.
- Sections answering searchers' actual questions with first-hand evidence, photography, demos, comparison tables, dates, sources and honest authorship.
- Images with honest alt text describing content, appropriate file size/loading and accessible UX.
- Internal links to related choice/help content.
- Unique, descriptive `<title>` and useful meta description; **Google may rewrite the search title and snippet** from other page content. No fixed universal character cutoff; don't keyword-stuff.
- No fabricated expertise, mass-produced filler, rehashed competitor pages, automatic fake review stars, or unsupported FAQs.

The best SEO copy is also useful **post-click**: a title promising something the PDP does not deliver harms buyer expectations. See [Google helpful content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) and [title](https://developers.google.com/search/docs/appearance/title-link) / [snippet](https://developers.google.com/search/docs/appearance/snippet) documentation.

## 5. Product SEO and Google merchant ecosystem

For physical products, prioritize **complete product truth**:
- Product name, identifiable model/variant, photos, dimensions/materials, correct price/currency, availability, shipping, returns, identifiers (GTIN, MPN, brand when valid), and real review/rating data.
- `Product` / `Offer` JSON-LD on **eligible single-product or variant pages**; do not put merchant-listing markup on category grids merely because they contain many products. Consult Google's [merchant listing specification](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing) for exact required/recommended properties.
- Consider [Merchant Center and feeds](https://developers.google.com/search/docs/appearance/structured-data/product), ensuring on-page facts, structured data and feed values agree; pricing or stock mismatch can prevent rich appearance.
- Product variants, multi-currency, delivery and return policies require current type-specific documentation.
- Test with [Google Rich Results Test](https://search.google.com/test/rich-results), monitor Search Console and actual rich-result eligibility. **Valid schema never guarantees enhanced appearance.**
- Do **not** invent reviews, rating counts, prices, stock or third-party product testing.

For services and software: focus on category/solution pages, verifiable process, audience fit, pricing/scope, examples, case studies and actual FAQs. Apply only structured data types supported for the content and relevant search experiences; schema.org existence does **not** imply Google rich-result support.

## 6. Page experience and business outcomes

Landing pages, PDPs and site navigation are marketing assets. Audit from mobile first: product identification, photography/scale, value, selection controls, price and costs, delivery/policies, trust, clear purchase action, error handling, accessibility and speed.

Search CTR can be improved by clearer title and snippet copy, but **higher CTR alone is not a win** if traffic is poorly matched and does not buy. Use query/page segmentation and combine GSC impressions/clicks with GA4/store conversions (privacy, consent and attribution caveats). Measure net contribution, qualified leads and customer outcomes. See [CRO reference](cro-research-and-experimentation.md).

## 7. Technical and content audit decision matrix

| Observation | Investigate first | Possible action |
|---|---|---|
| Important pages missing from index | Status, robots/noindex, canonical, internal links, rendering, duplication | Technical fix, canonical/page consolidation |
| High impressions, low relevant clicks | Query intent, SERP titles/snippets, competitor alternatives, page mismatch | Better title, page promise and appropriate content |
| Clicks but no purchases | Landing relevance, wrong traffic, price, availability, friction, broken tracking | CRO diagnosis rather than blanket keyword stuffing |
| Multiple similar thin pages | Unique intent, real user value, redundancy | Improve/consolidate; avoid scaled content abuse |
| Product snippet/rich result absent | Actual merchant eligibility, schema, feed/page consistency | Validate markup and catalog data |
| Many irrelevant visits | Search intent mismatch or page topic | Reposition pages/queries, improve targeting and navigation |
| JS site content inaccessible | Raw HTML, rendered DOM, bot access and links | SSR/pre-render critical content; test crawler output |

## 8. Sources and further study

- [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Google Search Essentials and Spam Policies](https://developers.google.com/search/docs/essentials/spam-policies)
- [Google Helpful, Reliable, People-First Content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google JavaScript SEO Basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [Google Title Links](https://developers.google.com/search/docs/appearance/title-link) and [Search Snippets](https://developers.google.com/search/docs/appearance/snippet)
- [Google Product Structured Data](https://developers.google.com/search/docs/appearance/structured-data/product) and [Merchant Listing](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)
- [Google Structured Data Introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Web.dev Core Web Vitals](https://web.dev/articles/vitals)
- [Google Search Console + Analytics](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)
- [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)
- Open-source AI patterns: [Corey Haines Marketing Skills](https://github.com/coreyhaines31/marketingskills) (`seo-audit`, `site-architecture`, `schema`, `programmatic-seo`, `product-marketing`); consider as design references, not authoritative ranking facts.
