# Workflow 5K — Meta Ads campaign setup: objective → signal → audiences → launch → learning

**Trigger:** Setting up or auditing Facebook/Instagram ad campaigns: objective or performance-goal choice, conversion event selection, "learning limited", audiences and lookalikes, geo targeting, budget structure, Advantage+ campaigns, ROAS/CAC questions, underperforming Meta campaigns, ad comment issues, or connecting an agent to the Meta Marketing API.

**Place:** Optional specialist within [Stage 5 Channels](05-channel-and-campaign.md). Ad copy and creative come from [Workflow 6](06-creative-production.md); tracking implementation from [8E](08e-event-instrumentation-and-conversion-qa.md); customer-list activation from [8G](08g-audience-activation-and-utm-governance.md). Load the [Meta Ads setup reference](../references/meta-ads-campaign-setup-and-signal-quality.md) and the [marketing context file](../templates/marketing-context.md). Output: a [campaign blueprint](../templates/meta-ads-campaign-blueprint.md).

## 0. Confirm the outcome and economics

Name the business outcome (purchase, qualified lead, booking), sellable markets, margin, and the **target CAC/ROAS derived from contribution margin and CLV**. If those are unknown, write `[NEEDS INPUT]` and don't recommend scaling.

**Deliverable:** one-line goal + target CAC or ROAS (or the missing inputs).

## 1. Verify the signal before spending

Check Pixel + Conversions API on key events, `event_id` deduplication, customer-information parameters (with consent), purchase value/currency accuracy, and that Meta purchases reconcile with store orders. **Broken or duplicated tracking is a hard stop** for conversion optimization; route to [8E](08e-event-instrumentation-and-conversion-qa.md).

**Deliverable:** signal checklist with pass/fail and evidence (Events Manager screenshots or exports the user provides).

## 2. Choose the objective, performance goal and optimization event

Choose the highest-intent event closest to the real goal (purchase or value for ecommerce; qualified lead over raw lead). Then run the volume check: will each ad set reach about 50 optimization events per week at the planned budget? If not, consolidate, adjust budget, or document a temporary step-up-funnel event with a plan to move back to purchase.

**Deliverable:** objective, goal, event, attribution setting, volume math and rationale.

## 3. Set hard constraints and audience inputs

Locations limited to where you actually sell, ship and support; exclusions (recent purchasers, current customers for acquisition); age and language only where they're true requirements. Audience hypotheses: broad/Advantage+ audience vs consented first-party custom-audience lookalikes at a few scales, built from the best-customer seed. Treat suggestion-only inputs as hints.

**Deliverable:** controls table + audience test matrix (hypothesis, seed, scale, budget share).

## 4. Structure, budget and creative

Use few ad sets with enough budget each to exit learning; give each concept from [Workflow 6](06-creative-production.md) a distinct hypothesis; review Advantage+ creative enhancements ([launch QA](07-launch-qa.md)). Spend caps go in the account, set by the owner.

**Deliverable:** campaign/ad set/ad structure, daily or lifetime budgets, creative-to-hypothesis map, UTM scheme ([governance](../references/campaign-utm-and-identity-governance.md)).

The destination decides much of the result: the page must continue the ad's promise and look ([message and design match](../references/landing-page-design-and-copy.md#1-what-a-landing-page-is-for)). Choose product page, landing page or labeled advertorial deliberately ([4D](04d-landing-page-build.md)).

## 5. Launch with authorization, then monitor

Run [Workflow 7](07-launch-qa.md). Nothing is published without explicit approval. During delivery: check comments daily, watch spend vs limits and learning status, review session recordings and on-page exit/intercept survey answers (no back-button hijacking), and avoid significant edits that reset learning without a reason.

## 6. Evaluate against business truth

Report Meta-attributed results **next to** store orders, new-customer counts, blended ROAS/CAC and contribution. Large budget calls get an [incrementality test](08b-attribution-incrementality-and-experiments.md). Log decisions in the [experiment decision log](../templates/experiment-decision-log.md) and hand off to [Workflow 8](08-measure-diagnose-experiment.md).

**Stop conditions:** unreliable or duplicated conversion data; no defined target CAC/ROAS for a scaling decision; budget too small to reach any usable optimization signal (say so and recommend alternatives); offer, stock or landing-page problems that ads can't fix.
