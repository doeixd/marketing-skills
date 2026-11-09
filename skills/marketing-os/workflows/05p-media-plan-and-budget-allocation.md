# Workflow 5P — Media plan and budget allocation: economics → channel roles → split → forecast → reallocation rules

**Trigger:** "How much should I spend?", "How do I split the budget?", annual/quarterly/campaign budget planning, what to cut or scale, forecasting results, or several channel workflows producing plans that must fit one budget.

**Place:** Sits across [Stage 5](05-channel-and-campaign.md): it turns channel roles into money and expected outcomes. Feeds the channel specialists (5A–5O) and is reviewed in [8H](08h-marketing-review-cadence.md). Output: a [media plan](../templates/media-plan-and-budget.md); a JSON version can be checked with the [media plan validator](../scripts/check_media_plan.py) ([example](../examples/media-plan.json)).

## 1. Derive the budget from economics, not from a round number

- **Allowable CAC** = contribution margin per customer over the chosen horizon (first order, or CLV to N months) × the share you are willing to reinvest. State the horizon and payback period.
- **Bottom-up budget** = target new customers × expected CAC, per channel. **Top-down cross-check** = marketing as a share of revenue (blended MER). If the two disagree widely, the target or the CAC assumption is wrong.
- Missing margin, CLV or cash-payback tolerance → `[NEEDS INPUT]`; do not recommend a scale-up without them.

## 2. Give every channel a job and a minimum viable budget

Record `channel | role (create demand / capture demand / convert / retain) | audience and markets | optimization event | expected cost per event | minimum viable budget | primary KPI | countermetric`.

- **Minimum viable budget:** a conversion-optimized ad set needs roughly 50 optimization events a week to learn (see [5K](05k-meta-ads-campaign-setup-and-optimization.md)). `weekly budget ÷ expected cost per event ÷ number of ad sets ≥ ~50`. A channel funded below its minimum teaches nothing; fund fewer channels properly.
- Capture existing demand (search, marketplace, email to customers) before paying to create new demand, unless the goal is deliberately brand-building.
- Include production, tools, creator fees and agency costs, not only media.

## 3. Split deliberately

- A common practitioner heuristic is roughly **70% proven, 20% promising, 10% experimental**. It is a starting point, not evidence. New businesses have nothing proven: treat the whole budget as a sequence of tests.
- Decide the **brand vs activation** balance on purpose ([marketing effectiveness](../references/marketing-effectiveness.md)); activation-only plans tend to harvest demand without rebuilding it.
- Keep a **measurement reserve**: budget or audience held back for holdouts, geo tests or lift studies ([8B](08b-attribution-incrementality-and-experiments.md)).
- Avoid concentrating nearly everything in one platform without acknowledging the dependency risk.

## 4. Forecast as ranges with stated assumptions

For each channel give **low / base / high** for spend, conversions, CAC and revenue, with each assumption labeled `verified` (own history), `inferred` (benchmarks) or `hypothesis`. Benchmarks from other businesses are weak evidence. Model **diminishing returns**: judge the next dollar by *marginal* CAC, not the channel's average. Account for seasonality, stock, lead time and creative capacity.

## 5. Set reallocation rules before launch

Write down in advance: the review cadence, the minimum data needed before judging a channel (spend, time, conversions), the thresholds that trigger scale / hold / cut, the maximum budget change per step (large jumps can reset platform learning), and who approves changes. Pacing: planned vs actual spend by week.

## 6. Approve and hand off

The plan is a draft until the budget owner approves it. Spend caps are set in each account by the owner. Hand each line to its channel workflow, and the whole plan to [8H review cadence](08h-marketing-review-cadence.md).

**Stop conditions:** no margin or CAC target; total budget below the minimum viable budget of any single channel (say so, and route to the [quickstart](00-quickstart-first-30-days.md) table of no-budget options); tracking that cannot attribute conversions to channels at all.
