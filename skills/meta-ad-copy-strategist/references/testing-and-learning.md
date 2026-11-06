# Testing positioning hypotheses and closing the feedback loop

The objective is not to make the AI produce more synonyms. It is to learn **which specific buyer motivation or objection-resolving proposition produces commercially valuable behavior**.

## 1. Two different optimization problems

**Copy refinements:** choose wording, length, sentence order, or headline variations within an angle. These can improve delivery without teaching much about underlying buyer desire.

**Positioning experiments:** compare distinct propositions (self-expression vs gifting vs product details vs reassurance vs verified offer). These test *why* a buyer might respond. Distinguish the experimental change from visual creative, product mix, audience, price and landing page.

Automated multi-text creative combinations can improve delivery but do **not** automatically give unbiased causal estimates for every text. Separate structured experiments when you need clean comparisons; if running normal ads, label conclusions observational.

## 2. Hypothesis template

> For buyers in [purchase situation], an ad emphasizing [distinct benefit / objection resolution] will improve [primary KPI] relative to [specific control] because [buyer motivation or friction]. We will consider the hypothesis supported if [predefined success criterion] under [comparable conditions], while checking [risks/confounders].

Don't promise a fixed uplift without evidence. Provide the test unit, campaign objective, start/end window, budget expectation if known, pre-specified KPIs, safeguards and stopping conditions. Don't invent significance, power or sample size from no baseline data.

## 3. Metrics by diagnosis

| Metric | Useful for | Limitations |
|---|---|---|
| Reach / impressions | Delivery and exposure context | Does not equal attention |
| Thumb-stop / video engagement | Creative opening and video fit | Not necessarily buyer qualification |
| CTR / outbound CTR | Attention and intent to click | Clickbait can increase it while reducing purchases |
| CPC | Cost of traffic | Cheap clicks can be low quality |
| Landing-page views | Whether traffic loads the destination | Doesn't establish product desire |
| Add-to-cart / checkout rate | Mid-funnel interest/friction | Attribution and funnel drop-off matters |
| Purchases / qualified leads | Goal-aligned conversion | Requires sufficient volume and tracking |
| CPA / cost per purchase | Cost efficiency | Averages may vary with mix/attribution |
| ROAS / gross profit contribution | Commercial value | ROAS ignores margin unless integrated |
| New-customer rate / incrementality | Business growth quality | Often requires more robust measurement |

For commerce, prefer purchases, contribution margin, new-customer acquisition or qualified actions over CTR alone. For branding campaigns, do not falsely substitute purchase ROAS for a properly chosen objective.

## 4. Experiment hygiene

- Write what changes: angle only, headline only, image only, or combination. A full-creative concept test can be practical but cannot isolate copy's contribution.
- Where possible, align offer, audience, attribution, placement, dates, budget and destination.
- Handle Meta delivery optimization and learning effects; not all ads receive equal exposure.
- Decide primary metric and key guardrails **before** results arrive.
- Check attribution windows, conversion tracking, pixel/CAPI quality, seasonality and promotions.
- Include denominators, raw conversions, spend and measurement window in summaries.
- Explain uncertainty. "Observed higher ROAS in this period" is different from "proved headline increased ROAS".
- If few purchases occur, treat conclusions as preliminary; plan a next test or research rather than declaring victory.
- Revisit offer/landing-page friction if clicks increase but purchases do not.

## 5. Learning record

Store one row per creative/angle plus the time window. Example columns:

`angle_id, campaign_id, ad_id, buyer_situation, proposition, objection, evidence_ids, copy_version, creative_version, audience, placement, landing_page, offer, start_date, end_date, spend, impressions, outbound_clicks, landing_page_views, purchases, purchase_value, profit_estimate, conversion_attribution_window, decision, caveats, next_test`

Record both wins and failures. Don't overfit to the latest one-off result. Prefer reusable patterns such as: "Gifting improved results for the November collection on static Feed creative, but the product/offer was changed simultaneously, so causal confidence remains low."

## 6. Example interpretation

If a style ad has 2% CTR but no attributed purchases while a straightforward features ad has 1.2% CTR and sales, do not proclaim the style ad superior because it attracted more traffic. Investigate purchases, value, sample size, delivery differences and attribution.

If an ad causes many sizing questions, the best intervention may be a clearer size chart and image rather than new ad language. If buyers don't believe a durability claim, gather evidence or remove it; don't use stronger adjectives.

## 7. Inspiration and actual evidence

The public [Meta Ad Library](https://www.facebook.com/ads/library/) can reveal competitor wording, positioning, offers and creative conventions. **It does not establish general commercial ads' actual purchase profitability or ROAS.** Duration in circulation is at best a weak clue, not proof of a winning ad.

## Further reading

- [Meta Blueprint — Designing A/B Tests, Creative Tests and Lift Studies](https://formedia.facebookblueprint.com/student/path/219763-ab-test-conversion-brand-lift-course)
- [Meta Blueprint — Ad Creative that Converts (May 2026)](https://www.facebookblueprint.com/student/activity/707402)
- [Wynter — Message testing](https://wynter.com/products/message-testing)
- [Jon Loomer — Creating A/B tests in Meta Experiments](https://www.jonloomer.com/how-to-create-an-a-b-test-in-meta-experiments/) — third-party practical walkthrough.


## 8. Brand and memory effects

For brand-building objectives, specify the buying occasion/category entry point and recognizable brand assets being linked in the ad. Use appropriately designed brand-lift, recognition or association measurements where available; do not claim memory improvement from CTR or creative appearance alone. Distinguish short-term response from long-term impact. Read [marketing effectiveness](marketing-effectiveness.md) and [brand strategy](brand-strategy.md).
