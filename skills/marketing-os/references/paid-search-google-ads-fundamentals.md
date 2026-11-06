# Paid search and Google Ads: comprehensive strategy, campaign engineering, copy and optimization

**Reviewed:** 2026-11-06. Use with [Paid Search Workflow 5G](../workflows/05g-paid-search-google-ads.md), [campaign blueprint](../templates/google-ads-search-campaign-blueprint.md), [RSA creative template](../templates/google-search-rsa-and-assets.md), and [search experiment/diagnosis](../templates/google-ads-optimization-and-experiments.md). These are planning materials: account permissions and user authorization are required before actual Google Ads actions.

## 1. Where paid search fits the marketing system

Search ads intercept **expressed demand**: a person types or speaks a question, product category, problem, brand, comparison, local need or purchase query. A paid listing is an opportunity to help their choice—not proof that they'll purchase. Brand awareness and organic SEO can create/sustain demand; paid search captures and may expand it. Don't treat Google Ads as a replacement for positioning, product fit, trust, delivery or checkout.

The fundamental chain is `real buyer situation → search terms / intent → relevant offer → advertising claim → landing page proof → measured qualified outcome → economic decision`.

Start with [brand 3A](../workflows/03a-brand-discovery-and-messaging.md), [offering 1A](../workflows/01a-offering-discovery-and-marketing-plan.md), [buyer discovery 2](../workflows/02-buyer-discovery.md), [positioning 3](../workflows/03-positioning-and-brand.md), [offer/CRO 4/4A](../workflows/04a-conversion-rate-optimization.md) and [measurement 8](../workflows/08-measure-diagnose-experiment.md). A "buy now" query may require specs, inventory and prices; a "what is..." query might be better served by educational organic content and a different bidding objective.

## 2. Buyer search jobs, intent and query map

Research actual demand using **Google Keyword Planner**, Search Console, onsite search, customer support, sales language, real product names, observed search terms (for existing campaigns), user interviews and SERP/competitor evidence. Keyword Planner estimates volume, competition and costs; forecasts are uncertain and dependent on budget, bids, seasonality and account quality. Never invent search volumes, CPC or competitor spending.

Cluster by **commercial job** rather than demographic persona alone:
- **Brand navigation**: [brand], [brand product], model; protect proper name and assess organic cannibalization/incrementality.
- **Product category and attributes**: "vintage patterned ring", "sterling silver..." only if real material/offer fits.
- **Problem/desire/solution**: high-intent requests such as "custom ring sizing", "online payroll service" with truthful capability.
- **Comparison**: "X vs Y", reviews, alternatives; use accurate, permitted comparisons.
- **High purchase/action intent**: "buy", "book", "quote", "near me" only if location/scope matches.
- **Research/education**: how-to, examples, meaning; may be more suitable for SEO/lead magnets or lower priority for paid.
- **Support/jobs/careers/free/DIY**: potential exclusions **only where irrelevant**, not automatic globally.
- **Competitor terms**: weigh legal, brand, relevance, actual value and landing-page fit; trademark policy does not mean all competitor bidding is forbidden or endorsed.

For each query theme create `term / seed | source | intent and buyer | expected decision | match type choice | landing URL | negative-risk | cost forecast & uncertainty | brand/offer fit | priority`. Include actual status quo and alternative products: irrelevant traffic is usually a strategic mismatch, not just a negative-keyword problem.

## 3. Keyword match types and negatives: current semantics

**Positive match types:** `[exact]`, `"phrase"`, `broad` all include close variants/intent variants. Exact ≠ literal string match; phrase ≠ always a strict phrase substring; broad uses more contextual signals and may expand meaning. Exact/phrase provide additional matching constraints. Broad + conversion-based Smart Bidding can be powerful when reliable signals exist; it also increases the need to inspect search intent, page quality, and unintended matches. Google recommends AI Max/Smart Bidding, but recommendations are vendor guidance and must be tested against business objectives.

**Negative keywords:** negative broad/phrase/exact do **not** behave like positive matching. Negatives generally don't automatically cover synonyms and plurals the same way positive keywords do; explicitly check variants. Review [Google negative keyword documentation](https://support.google.com/google-ads/answer/2453972). Build *conceptual exclusion lists* only after examining actual offer fit. Do **not** exclude "free," "cheap," "how to," "jobs" or competitors blindly; some may be valuable for certain products/segments.

Use [Search Terms Report](https://support.google.com/google-ads/answer/2472708) and [Search Terms Insights](https://support.google.com/google-ads/answer/11386930) separately. Reported queries have **privacy/volume thresholds** and may be incomplete; Search Terms Insights clusters hidden terms, not a literal full list. Track waste with denominator/spend and date, not 1 irrelevant search anecdote. Add valuable new themes, test negatives cautiously, and inspect expansion by campaign/ad group.

## 4. Structure, segmentation, campaign settings

Use Google's hierarchy: **account → campaigns → ad groups → keywords/search-term matching + responsive search ads (RSAs) + assets → landing page**. Campaigns hold geo, budget, bidding, networks, goals; ad groups should group meaningfully aligned search intent/landing promises. An individual keyword per ad group (SKAG) isn't a universal requirement in semantic matching. Avoid hundreds of near-identical micro-campaigns with insufficient conversion signal.

Separate when a *real decision* requires it: brand vs nonbrand reporting/targets, geographic availability, product economics or category, budget, policy, service lead value, unique language/service area, distinct offer or landing page. Don't split for cosmetic reasons. Include exact **campaign naming, owner, job, bid objective, geo, search partners on/off, network, devices/ad schedule policy, daily budget, exclusions and URLs**.

**Geo options:** default may include people in, regularly in, **or interested in** target area; review actual presence vs interest selection for local services. Language settings, audience segments, demographics, observation/targeting modes, customer lists, schedule and search partners need a current-account check. Avoid guessing Google defaults and silently opting into expansion.

**Ads assets:** sitelinks (real internal destinations), callouts (accurate benefits/policies), structured snippets (actual classes/products), logo/business name, image assets, call/location if truly available, prices/promotions only with verified terms. Ad assets aren't mandatory universal counts; choose useful verified assets. See [Google Ads asset guide](https://support.google.com/google-ads/answer/7331111) and [sitelink recommendations](https://support.google.com/google-ads/answer/12073962).

## 5. Conversion goals, measurement and data quality **before bidding**

Define what the business really wants:
- Ecommerce: purchase, net order value, quantity, returns/cancellations, contribution if supported.
- Lead gen: *qualified* leads, meetings held, proposals and **closed-won revenue**, not merely form opens.
- Subscription: paid activation, retained users, churn and recurring gross margin, with actual observation horizon.
- Local business: verified phone contact, bookings that show, paid appointments, not phantom phone taps.

Audit Google Ads conversion actions, **primary vs secondary**, account-default vs campaign-specific custom goals (custom goals can include secondary actions in bidding; inspect exact configuration). Never accidentally optimize toward pageview/add-to-cart while reporting purchase efficiency. Check tag firing, deduplication, transaction IDs, currency, values, conversion count (one/every), attribution windows, time zones, enhanced conversions consent and identity data policies.

For leads: capture CRM outcome quality and import offline qualified stages with legitimate consent/security. **2026 platform migration:** Google documentation states offline conversion/enhanced-conversions-for-leads uploads are moving to **Data Manager API** starting June 15, 2026; historical examples using Google Ads API upload methods may be deprecated/restricted. Verify live Data Manager integration, compatibility and allowlisting; never implement an old endpoint based only on an older tutorial. See [enhanced conversions for leads](https://support.google.com/google-ads/answer/15713840) and [Data Manager](https://support.google.com/google-ads/answer/15707550).

For privacy and consent, consult actual geography, consent management and Google requirements. Ad scripts, tags and offline imports must not collect/upload user data without authorization. Preserve GCLID and appropriate attribution where supported; diagnose redirects/cross-domain redirects that remove tracking.

## 6. Economics: bid and budget decisions

Calculate `price × gross or contribution margin – variable fees/returns/fulfillment – ad cost` at the business level. Distinguish sales ROAS (revenue/ad spend) from actual *margin/profit* and incremental lift.

Useful boundaries:
- `break_even_CAC ≈ net contribution before marketing per incremental order`, subject to fixed-cost and customer-value assumptions.
- `break_even_ROAS (on revenue) ≈ 1 / contribution_margin_rate` when a single common margin applies; true value varies by order/returns.
- `expected_CPC_ceiling ≈ conversion_rate × economically acceptable CAC`, **scenario**, not a vendor promise; uncertainty in each input.
- For leads: `allowable_CPL ≈ qualified-lead-to-sale_rate × allowable CAC`; use actually realized qualified close rate, not form count.
- Set feasible budget based on **learning volume, risk tolerance, capacity and margin**, not arbitrary formula such as "$10/day for everyone."

Use Google's bid strategies intentionally: **Maximize clicks** for reach/diagnostic click goals only with cost/traffic-quality controls; **Maximize conversions** / **Target CPA** for sufficiently reliable quality conversion events; **Maximize conversion value** / **Target ROAS** for meaningful conversion values and sufficient data; **Target impression share** for a deliberate visibility objective. In 2026, Target CPA and Target ROAS UI labels are transitioning to standalone strategies while behavior remains similar—verify account UI. Smart Bidding can spend the budget without profitability if targets/values are wrong. Avoid making frequent reactive changes within learning/conversion lag.

Compare branded/non-branded and prospecting/returning appropriately; attribution of brand-search conversions may cannibalize organic or direct demand. For large spend, use controlled tests or incrementality methods.

## 7. RSA copywriting and search-ad creative

Current responsive search ad (RSA) format: **up to 15 headlines** (commonly 30 characters each) and **4 descriptions** (commonly 90 characters each); final URL and optional display paths, with Google combining assets dynamically. Verify **live local/account rules** and count carefully, including Unicode characters; dynamic insertion can affect rendering. Google guidance suggests diverse unique assets (several keyword-relevant, several benefit/proof/brand/CTA) and **not** 15 near-identical keyword synonyms.

Write from the [offering dossier](../templates/offering-dossier-and-marketing-plan.md), *not* keyword insertion alone. Build a **message matrix**:
- **Category/query fit**: "Vintage-Inspired Rings", "[Service] for [actual industry]".
- **Feature/value**: verified meaningful capability, scope, materials, quality evidence, pricing.
- **Difference/position**: buyer-valued true advantage over realistic alternative (not fabricated "only"/"best").
- **Proof/assurance**: returns, warranty, real reviews, demos, support, actual process and eligibility.
- **Buyer situation**: gift consideration, high-intent purchase, comparison, local need.
- **Brand**: official name and distinctive assets, not generic "Shop Now" alone.
- **CTA**: view styles, check availability, get quote, compare, book, learn.
- **Description**: adds useful detail/qualification, not a duplicate headline.

**Combination safety:** Assets can appear in different combinations/order/length; each must be intelligible and accurate alone. Don't make one description qualify a misleading absolute in a headline. Pin only for actual ordering/legal/brand requirements; pinning reduces flexibility and may be bypassed under **AI Max Final URL expansion**, so check account settings. Display paths are descriptive path text, not permission to mislead about destination.

Use **sitelinks** to actual relevant pages: product/category, sizing/returns, pricing, case studies/FAQ, contact. Fill descriptions where real; callout/structured snippet facts require proof. Promo/price assets reflect current actual terms. Avoid keyword stuffing, excessive punctuation, trademarks used deceptively, clickbait, unsubstantiated absolutes and false urgency. Review [Google Advertising Policies](https://support.google.com/adspolicy/answer/6008942) and [RSA guide](https://support.google.com/google-ads/answer/6167122).

Ad Strength may guide missing/variety, but **Ad Strength and Quality Score are NOT business KPIs**; Quality Score is not directly used as an auction input. Improve measured conversions, business contribution and customer experience, not arbitrary scores. [Quality Score documentation](https://support.google.com/google-ads/answer/6167118).

## 8. AI Max for Search (2026), automated assets and control

**AI Max** is an optimization layer for Search, not a new campaign type; in April 2026 it moved beyond beta. It can expand query matching beyond explicit keywords, generate/adjust text and choose landing URLs through **Final URL expansion**. Upgrading DSA/automatic assets in September 2026 may change campaign behavior. Explicitly record:
- AI Max enabled? Search Term Matching enabled at ad group? Brand inclusions/exclusions and location-of-interest controls.
- Text customization enabled? Which generated assets are actually approved? Can they claim unverified features?
- Final URL expansion enabled? **Exact allowed/excluded URL destinations**, tracking template, policy/price mismatch and accidental lead to support/career page.
- **Pinned RSA assets may be ignored** when URL expansion or URL inclusions are active. For legally necessary disclosure, Google offers text-disclaimer assets (where supported) and configuration checks; do not rely on pinning alone.
- What does search-term/match-source reporting actually reveal? Some terms hidden by privacy limits.
- Search campaign vs Performance Max vs Shopping and new AI ad inventory: not equivalent; decide overlap, brand protection and eligibility. Google reports AI Max average improvements using its internal aggregate, not a forecast for this specific advertiser.

**Decision:** propose a controlled pilot with correct conversion tracking, URL and claim controls, brand/negative protections, actual baseline and stop conditions. Avoid enabling automated expansions without reviewing **every eligible page and claim**.

Official guides: [AI Max working model](https://support.google.com/google-ads/answer/15910187), [AI Max controls](https://support.google.com/google-ads/answer/15910366), [Final URL expansion](https://support.google.com/google-ads/answer/16230205), [2026 changes](https://business.google.com/us/accelerate/announcements/dsa-upgrade-to-ai-max-2026/).

## 9. Search-term hygiene and optimization loop

Before interpreting results, reconcile **Google Ads vs GA4 vs store/CRM** (time windows, consent, attribution, currency, incomplete conversions and refunds). Segment brand/nonbrand, theme/ad group, true search term (available), device, geo, network, time and landing page.

Diagnosis:
- Spend no qualified leads/sales → query relevance/negative exclusions, poor offer/landing, broken tracking or inappropriate bidding.
- High CTR poor CVR → intriguing but wrong promise, price/policy issue, informational intent or low-fit traffic.
- Many leads few sales → wrong conversion goals, low qualification, follow-up delays, delivery/scope mismatch.
- Limited delivery → policy status, billing, bid/target restrictiveness, search volume, approvals, geolocation or campaign settings.
- High CPC → auction context, competitors, relevance, landing, device/geo; no simplistic "higher Quality Score directly reduces CPC" guarantee.
- Good attributed ROAS poor net profit → margin, shipping, returns, brand cannibalization, attribution overlap or promotion costs.
- Search term drift → negatives, semantic match expansion, AI Max controls and page associations.
- Good organic search results → investigate whether paid brand traffic creates incrementality or just captures what would have happened anyway.

Daily/early checks: spend spikes, disapprovals, broken URLs, grossly irrelevant terms, tracking, inventory, key negatives, budgets; **avoid daily major bidding changes** without evidence. Weekly: query themes/negatives, ad and landing assets, qualified outcomes, device/geo, margin. Monthly/after sufficient volume: experiments, net contribution, incrementality and expansion decisions. Don't use fixed day counts as substitute for conversion lag and sample power.

## 10. Research, tests and practitioner perspectives

**Official evidence:** [Keyword Planner](https://support.google.com/google-ads/answer/7337243), [keyword matching](https://support.google.com/google-ads/answer/14996023), [negatives](https://support.google.com/google-ads/answer/2453972), [Search Terms](https://support.google.com/google-ads/answer/2472708), [Search Terms Insights](https://support.google.com/google-ads/answer/11386930), [RSAs](https://support.google.com/google-ads/answer/7684791), [conversion goals](https://support.google.com/google-ads/answer/11461796), [Smart Bidding](https://support.google.com/google-ads/answer/14697340), [experiments](https://support.google.com/google-ads/answer/10683687), [Google Ads API campaign setup](https://developers.google.com/google-ads/api/docs/campaigns/search-campaigns/getting-started). Official vendor "best practices" can reflect product incentives; test financial value for your account.

**Practitioner/agent-workflow sources:** [Corey Haines Marketing Skills](https://github.com/coreyhaines31/marketingskills) (`ads`, `ad-creative`, `conversion-tracking`, `analytics`, `attribution`, `competitors`, `cro`, `ab-testing`). [Brad Geddes / Adalysis](https://adalysis.com/blog/) specializes in search-ad testing/quality and account audits; [Frederick Vallaeys / Optmyzr](https://www.optmyzr.com/blog/) discusses automation and PPC management; [Kirk Williams / ZATO Marketing](https://zatomarketing.com/blog/) gives Shopping/search strategic commentary; [Search Engine Land PPC](https://searchengineland.com/library/channel/ppc) offers changing-platform discussions. **Practitioner heuristics aren't platform rules or causal proof.** Only adopt a tactic where it matches actual customer/job/account evidence and compliance.

## 11. Production and approval gates

Every campaign recommendation includes: `goal | brand & offer | actual economics | query/job evidence | campaign/ad group | keywords/match | negatives | geo & network | bidding/conversion goals | RSA/assets | landing & tracking | AI expansion/URL controls | budget | approvals | measurement & next check`.

**Hard stops:** missing claim proof, forbidden product/landing mismatch, unverified conversion goals/transaction values, unsafe keyword targeting or consent, false deadlines/discounts, unclear budgets, broken purchase, critical policy issue. Draft in paused state if using API. User authorization is required before creating/activating ads or spending money.
