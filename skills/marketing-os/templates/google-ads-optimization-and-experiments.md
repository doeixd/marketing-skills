# Paid search audit, monitoring and experiments decision log

Use [Workflow 5G](../workflows/05g-paid-search-google-ads.md). Investigate first; do not reflexively change bids, budgets or keywords based on small or delayed samples.

## 1. Account and period
- Real Google Ads account / campaign, range, timezone and conversion lag:
- Revenue, margin, qualified lead definition, brand/nonbrand scope:
- Campaign status, current bidding and goal changes:
- Source-of-truth for Google Ads, GA4, store/CRM, actual refunds:
- AI Max matching/text/URL expansion, account changes in window:
- Missing report/visibility or permission limits:

## 2. Metrics and business decisions
| Segment (campaign/brand/keyword/term/device/geo/asset/page) | Spend | Impressions | Clicks/CTR | Real qualified conversions | Conversion value/net contribution | CPA/CAC/ROAS & business guardrail | Evidence caveat |
|---|---:|---:|---:|---:|---:|---|---|

- Primary vs secondary conversion actions and whether bidding targets them:
- Search Terms Report (may exclude low-volume/private queries) vs Search Terms Insights categories:
- Search partners vs Google Search when breakdown available:
- Geo presence vs interest; network, schedule and landing pages:
- Brand and existing demand cannibalization risk:
- Mobile checkout/lead follow-up, quality and return effects:

## 3. Search term and negative decisions
| Observed search/query theme | Match/source/campaign | Spend/conversions | Offer/job relevance | Negative or add keyword? | Risk of blocking wanted traffic | Evidence/approval |
|---|---|---|---|---|---|---|

Never infer that every hidden query is a bad query; evaluate actual search insights and business outcomes. Account-wide negatives require high confidence.

## 4. Diagnostic alternatives
| Symptom | Hypothesis A | Competing hypothesis B | Best confirming data | Decision and confidence |
|---|---|---|---|---|
| High CTR, poor purchases | Ad misleads/weak landing | Wrong traffic/price/offer/tracking | | |
| Good Google ROAS, low profit | Low margin/returns | Branded demand attribution | | |
| Few impressions | Match/bid targets too restrictive | Policy/billing/geo/search demand | | |
| Lots of cheap leads | Bid targets form quantity | Sales team qualification/follow-up | | |

## 5. Experiment plan
- One business decision and user/search context:
- Control and treatment (keywords/match, ads, bidding, AI Max, landing):
- Explicit hypothesis/causal mechanism:
- Randomization or native Google campaign experiment method and scope:
- Budget guardrails, approved spend and traffic split:
- Correct conversion goal, denominator, baseline and minimum detectable economically meaningful effect:
- Power/sample plan, conversion delay, stopping rule and multiple tests:
- Quality and business guardrails: contribution, refunds, qualified lead rate, spend, complaints:
- Confounders: brand vs nonbrand, seasonality, promos, price, stock, geo and competitor activity:
- QA for tracking and sample/traffic allocation:

## 6. Results and decisions
| Outcome | Control | Treatment | Estimate and uncertainty | Guardrail | Status |
|---|---:|---:|---|---|---|

- Was experiment integrity verified?
- Actual business implication and alternative explanation:
- **Ship / iterate / revert / inconclusive**:
- Ads/landing/keyword/negative/AI Max update:
- Why we do **not** claim more than data establish:
- Next review and owner:
