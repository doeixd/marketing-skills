# Paid platforms beyond Meta and Google Search (reviewed 2026-11-09)

Used by [Workflow 5L](../workflows/05l-paid-social-and-video-platforms.md). Platform products, names and thresholds change often, and much of the public guidance is from vendors and agencies. Items marked *(reported)* come from third-party sources; confirm in the platform's own help center before relying on them.

## TikTok

- **Signal:** TikTok Pixel + Events API with deduplication; check match quality in Events Manager.
- **Campaign types:** **Smart+** automates targeting, bidding, budget and creative selection, similar in spirit to Meta's Advantage+. **Spark Ads** run an existing organic post (your own or a creator's, with their authorization code) as an ad and keep its engagement. **GMV Max** is the automated campaign type for TikTok Shop and has been the default and only supported campaign type for TikTok Shop Ads since July 2025 (TikTok help center); it optimizes total shop GMV including organic and affiliate content, so read its ROI as blended, not ad-only.
- **Learning:** TikTok's own figures vary by product: its LIVE Shopping help page says about 40 conversions per shop to exit learning, while third-party guides commonly cite about 50 per ad group per week. Check the delivery status instead of assuming, and avoid major edits in the first week.
- **Creative:** vertical, sound-on, fast to the point, creator-style. Creative wears out quickly, so plan a steady supply rather than one hero video. Only use sounds licensed for commercial use (the Commercial Music Library), never trending consumer audio.
- **Watch for:** click-heavy low-intent traffic when optimizing for clicks or views; attribution windows shorter than Meta's defaults; restricted categories.
- Docs: [TikTok Business Help Center](https://ads.tiktok.com/help/).

## Pinterest

- **Signal:** Pinterest Tag + Conversions API together (Pinterest reports better CPA and more attributed conversions than tag-only). Product IDs in events must match the catalog.
- **Campaign types:** **Performance+** campaigns automate targeting, bidding and creative. Pinterest's guidance: use Performance+ conversion or catalog-sales campaigns at roughly **50+ conversions a week**; below that, start with consideration.
- **Catalog:** complete product data, fix feed diagnostics starting with best sellers, fewer and deeper product groups.
- **Behavior:** people plan ahead and save ideas, so consideration is longer and seasonal content should go live well before the season. Shopping works better always-on than in short bursts. Pinterest suggests keeping about 10 or more active ads per ad group.
- **Creative:** vertical 2:3 images or video, product in a real context, readable text overlay, clear branding; it should look like an idea worth saving.
- Docs: [Pinterest Business: Performance+](https://business.pinterest.com/blog/pinterest-performance-plus-campaigns/), [shopping best practices](https://business.pinterest.com/blog/pinterest-shopping-ads-guide/).

## YouTube and Google Demand Gen

- **Demand Gen** campaigns run across YouTube (including Shorts), Discover and Gmail and replaced Video action campaigns in 2025. They sit between brand video and search: good for creating demand that search later captures.
- **Signal:** Google tag with enhanced conversions and, for leads, offline conversion import; Consent Mode v2 where required.
- **Creative:** supply horizontal, vertical and square video plus images; state the product and brand in the first seconds; assume skippable.
- **Measure** with search-volume and branded-search changes, lift studies or geo tests as well as attributed conversions; video is under-credited by last-click and over-credited by long view-through windows.
- Docs: [Google Ads Help: Demand Gen](https://support.google.com/google-ads/answer/13695777).

## LinkedIn

- **Use for** B2B where the buyer can be defined by company, industry, job function, seniority or an uploaded account list ([5O](../workflows/05o-b2b-saas-demand-generation.md)). Costs per click and per lead are typically high, so it suits high contract values.
- **Signal:** Insight Tag + Conversions API; send CRM stages (qualified lead, opportunity) back as offline conversions and optimize to those rather than raw form fills.
- **Formats:** sponsored content (single image, document, video), Lead Gen Forms (higher volume, lower intent than site forms; qualify with questions), Conversation Ads, and Thought Leader Ads that sponsor a real employee's post with their consent.
- **Controls:** company-size and seniority filters, exclusions for customers, competitors and job-seekers; keep audiences large enough to deliver (LinkedIn requires at least 300 matched members).
- Docs: [LinkedIn Marketing Solutions Help](https://www.linkedin.com/help/lms).

## Microsoft Advertising

- **Use for** extending search that already works on Google: similar intent, usually lower volume and often lower CPCs, with an audience that skews older and desktop.
- **Setup:** Google Ads campaigns can be imported, but review bids, budgets, negative keywords, locations, extensions and conversion goals after import; not everything maps exactly. Recurring imports can overwrite manual changes.
- **Signal:** UET tag with consent mode (Microsoft requires consent signals for EEA/UK traffic) and offline conversion import.
- **Extras:** LinkedIn profile targeting (company, industry, job function) as a bid modifier on search; audience ads across Microsoft properties.
- Docs: [Microsoft Advertising Help](https://help.ads.microsoft.com/).

## Sources and limits

- Pinterest figures are Pinterest's own reported results. TikTok GMV Max status is from TikTok's [Product Shopping Ads help page](https://ads.tiktok.com/help/article/considerations-for-product-shopping-ads) and the learning figure from its [LIVE Shopping budget page](https://ads.tiktok.com/help/article/best-practices-for-setting-a-live-shopping-ads-budget); other TikTok details are from third-party summaries ([Journify](https://www.journify.io/resources/tiktok-ads-not-optimizing/), [Supermetrics release note](https://docs.supermetrics.com/docs/tiktok-ads-smart-ads-and-gmv-max-campaign-reporting-august-10-2026-1)).
- No platform's reported ROAS is a measure of incremental sales. Platform availability and ad policies vary by country.
