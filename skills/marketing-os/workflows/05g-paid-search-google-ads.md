# Workflow 5G — Paid search / Google Ads: demand → keywords → campaign → conversion → learning

**Trigger:** Google Ads/Search Ads/PPC campaign setup, keyword research, keyword selection, ad groups, responsive search ad copy, negative keywords, bids, AI Max, CPA/ROAS, account audit, underperforming paid search, branded search testing, Google Ads creative or optimization.

**Place:** Optional specialist within [Stage 5 Channels](05-channel-and-campaign.md), complementary to [SEO 5A](05a-seo-and-organic-search.md) and [Promotion 5C](05c-promotion-strategy-and-distribution.md). Load [Paid Search Reference](../references/paid-search-google-ads-fundamentals.md), [Brand 3A](03a-brand-discovery-and-messaging.md), [Offering 1A](01a-offering-discovery-and-marketing-plan.md), [Buyer 2](02-buyer-discovery.md), [CRO 4A](04a-conversion-rate-optimization.md), [Measurement 8](08-measure-diagnose-experiment.md). Produce [campaign blueprint](../templates/google-ads-search-campaign-blueprint.md), [RSA assets](../templates/google-search-rsa-and-assets.md), and [diagnosis/experiment](../templates/google-ads-optimization-and-experiments.md).

## 0. Confirm the commercial decision

Ask who should search, *why now*, what real product/service they can buy, brand, geographic/service availability, budget, profit/qualified lead economics, current account and landing status. Goal: product purchases, qualified leads, bookings, revenue/value/profit, deliberate brand visibility, or exploratory demand—not "more clicks" by default. Use actual brand voice, unique value/proof, competitive alternatives and drawbacks; never jump from a list of keywords to unsubstantiated claims.

**Deliverable:** 1-sentence campaign objective + target buyer search situations + commercial threshold (or explicit missing inputs).

## 1. Audit readiness and attribution first

Verify sales/lead funnel; website responsive and truthful, actual price/policies/capacity; conversion action with correct business value; ad tags and consent, transaction-ID deduplication, destination loading, checkout/form, Google Ads–GA4–store/CRM reconciliation, primary vs secondary conversions and campaign goals. For services, decide whether form submits are only interim and plan importing **qualified** and won CRM events via current Google Data Manager as applicable.

**Stop** spending on the assumption that "Google's conversions" represent quality if tracking counts page views, duplicates or unqualified contacts. If no account metrics available, outline verification steps rather than pretend they passed.

## 2. Research query demand and buyer intent

Source seeds from the offering dossier, official catalog, customer language, Google Keyword Planner, GSC, site search, actual Search Terms Report/Insights, SERP/competitors. Cluster by:
- Brand/proprietary product/model;
- High-intent transactional/category;
- Specific features/service + location;
- Comparison and alternative, competitor (careful);
- Problem/solution, how-to/research with a separate purpose;
- Clearly irrelevant informational, jobs/support/DIY/other meanings to evaluate as negatives.

Record **source, geography/date, intended buyer/job, priority, forecast estimates and uncertainty**, keyword match type and landing. Don't invent volume/CPC, and avoid splitting every minor synonym.

## 3. Plan campaign, ad group and exclusions

Structure by **intent, landing page, commercial objective, geo and margin differences**. Separate brand/nonbrand when helpful to avoid mixing easy branded orders with incremental category acquisition. Build tightly relevant but not needless one-keyword groups. Document:
- Campaign name, objective, budget, bid strategy and conversion goals;
- Geo option **presence vs presence-or-interest**, language behavior, ad schedule, devices, network/search partners, policy;
- Search terms/keyword list with broad/phrase/exact and semantic limits;
- Negatives at appropriate account/shared/campaign/ad-group scope. Negative matches differ from positive; verify variants and avoid blocking valuable queries;
- AI Max search-term matching, text customization, Final URL expansion, URL/brand controls explicitly on/off; compare PMax/Shopping overlap.
- Primary destination and correct canonical/product page.

See [keyword and campaign blueprint](../templates/google-ads-search-campaign-blueprint.md).

## 4. Budget and bidding

Compute actual net contribution / qualified close rate; set max acceptable CAC, CPA, CPL or minimum contribution ROAS where data allow. If unknown, model scenarios without claiming known profitability. Choose Maximize Conversions/Target CPA or conversion value/Target ROAS according to *reliable* outcomes; use clicks/impression share only when those are genuinely intended and quality safeguards exist. Check conversion lag, current bidding data and stability before target changes.

Don't automatically select broad match, AI Max, exact-only or SKAGs as universal best practices. Broad/AI Max may expose additional demand with adequate signals and controls; test versus baseline. "Google recommends" ≠ "profitable for your account."

## 5. Map search language to differentiated creative

For each ad group decide `query intent → offer fit → primary payoff/position → proof/assurance → objection/qualification → final URL`. Write **responsive search ads** with a meaningful range of independently coherent 30-character headlines and 90-character descriptions (platform limits as of review), including actual brand, product/category, benefits, credible details, buyer situations, real policies and CTA. Aim for variety, not repetitive keyword insertion.

Create:
- 8–15 candidate headlines where useful; at least 3 to form an RSA; up to 4 descriptions, at least 2.
- Relevant true sitelinks, callouts, structured snippets, image/business/location/price/promotion assets only as applicable.
- Final URL and optional display paths; review combination order, truncated rendering, links and landing proof.
- If legal text must always appear, verify whether actual platform text-disclaimer assets or controlled configuration apply; AI Max URL expansion may override pins.
- Generate **2 genuinely different strategies/RSAs** where testing makes sense (one feature/fit, one trust/occasion), not identical synonyms.

Use [copy and asset template](../templates/google-search-rsa-and-assets.md). Run [RSA linter](../scripts/check_search_ads.py) for structural lengths/combinations and human truth review; tool output is not Google's policy approval.

## 6. Launch readiness and explicit authorization

Run [campaign blueprint QA](../templates/google-ads-search-campaign-blueprint.md):
- Approved advertiser/billing, budget ceiling, target market and campaign paused during configuration;
- Conversion events values/primary vs secondary/CRM quality validated;
- Query/negative strategy, geographic presence settings, partners, schedule;
- Ads, asset extensions, generated text, URL expansion, landing, mobile and rights tested;
- Keyword policy, ad/editorial/destination and brand/copyright compliance;
- Correct UTMs/GCLID, consent, URL redirects, canonical and page speed;
- Actual inventory/capacity and truthful policies; duplicate prevention;
- Experiment/monitoring plan, owners, review date, explicit user **approval to spend/publish**.

Drafts are **not live campaigns**. Do not create, enable, change spend or publish without user authorization.

## 7. Monitor, diagnose and improve

First check disapprovals, account status, spend pacing, query drift, eligible impressions, URL failures, tracking, conversions and stock. Search Terms Report is incomplete because of privacy thresholds; pair with Insights. Review asset performance **and** business outcomes.

| Symptom | Check before touching keywords/copy | Candidate next step |
|---|---|---|
| No impressions | Billing, policy, geo, low queries, restrictive bid target, negatives | Correct configuration/expectations |
| Lots of clicks, no orders | Query intent, mobile/PDP/cart, conversion action, price, trust | Fix landing/offer, search targeting or tracking |
| Spammy leads | Primary goal mistakenly form submit, irrelevant terms/geo | CRM qualified conversion import, tighten fit |
| High CTR, weak CVR | Promise mismatch, informational traffic, offer | Clarify ads, landing, negatives and CRO |
| Good reported ROAS, no profit | Return/refund, cost, brand cannibalization, margin, overlapping attribution | Measure net incremental contribution |
| Sudden irrelevant search terms | Broad/AI Max change, URL expansion, negatives | Inspect matching source and controls |
| Declining volume or higher CPA | Demand/auction change, policy, limited budget, saturation, conversion lag | Segment and test, not reactive daily bid switching |

Use [optimization/experiment template](../templates/google-ads-optimization-and-experiments.md) to log `observation → evidence → alternatives → hypothesis → change → business outcome & uncertainty → decision`.

## 8. Experiment strategically

Google Ads Search experiments/ad variations can compare campaign settings, bid/target strategies, matching, ads or landing pages where supported. Define *one* decision, baseline, power/realistic expected traffic, campaign split, experiment guardrails, seasonality, conversion delay, traffic overlap, SRM and prespecified success. When insufficient scale, do qualitative landing-page testing and limited-risk pilots labeled **inconclusive** rather than claim causal lift.

Review brand-search incremental lift where commercially important. Verify that a new "win" wasn't just a discount, traffic-mix shift or tracking change. Keep a decision log and periodically update brand/offering/SEO/CRO findings.

## 9. Deliverable contract

A completed agent response should contain:
1. **Campaign brief:** job, audiences/search intent, actual economics, main strategy, brand/offer proof, objective and missing facts.
2. **Keyword intent groups** with grounded candidates, match types, negative rationale, dated estimates where available and URLs.
3. **Campaign/ad group architecture** with geo, settings, budget, bidding and conversion goals.
4. **Production-ready draft copy**: RSA headline/description library, assets/sitelinks, distinct messaging angles and landing-match notes.
5. **Conversion implementation** and exact QA steps; explain unavailable account access.
6. **Launch checklist, risk gates and explicit sign-off** for spend.
7. **Monitoring and optimization plan** with business outcomes and how to test decisions.

Offer the [campaign blueprint](../templates/google-ads-search-campaign-blueprint.md), [RSA template](../templates/google-search-rsa-and-assets.md), [optimization brief](../templates/google-ads-optimization-and-experiments.md), and [worked examples](../examples/google-ads-search-campaign-example.md).

No claim of campaign creation, approval, live performance or account analytics without real tool access and confirmation.
