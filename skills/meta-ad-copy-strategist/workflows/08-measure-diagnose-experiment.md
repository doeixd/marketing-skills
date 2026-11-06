# Workflow 8 — Diagnose performance, choose interventions, test and learn

**Trigger:** Campaign live, revenue lower than expected, ROI weak, tests need review, or results are surprisingly strong.

## A. Check data quality before forming a causal story

Reconcile ad platform events with commerce order totals and net sales (accounting for time window, click/view attribution, currency, taxes, duplicates, refunds, cancellations and discounts). Inspect major traffic sources, inventory, promotions and seasonality. **Attributed sales are not necessarily incremental sales**; a reliable causal claim requires appropriate comparison or lift/holdout design. Small-sample results should often be called directional or inconclusive.

## B. Follow the actual customer journey, not a single metric

| Observation | Candidate causes (not proven) | Best next evidence | Action to consider |
|---|---|---|---|
| Little delivery/reach | Approval, budget, account/targeting limits, competition | Delivery errors, spend, placements | Verify campaign configuration, do not rewrite copy by default |
| Reach but weak relevant engagement | Inappropriate occasion, creative, offer or brand relevance | Creative view/engagement by format; qualitative feedback | Test a meaningfully different concept |
| Clicks but few landing-page views | Slow/broken page, accidental clicks, redirects, measurement issue | Link test, load times, analytics consistency | Fix link/site/tracking |
| Visits but poor product engagement | Message mismatch, wrong product, opaque value | Session/PDP usability, source-by-page | Match ad promise to PDP; improve product evidence |
| Product views but low adds to cart | Price/value, fit, availability, trust, weak interest | Customer questions, variant selection, product reviews | Improve info, imagery, price/offer or product |
| Adds to cart but few checkouts | Shipping/fees, cart UX, purchasing commitment | Cart behavior, stated fees, funnel data | Fix offer/cart and transparent delivery |
| Checkout starts but few orders | Payments, shipping restrictions, friction, unexpected costs | Test purchase, checkout errors | Repair checkout and policy clarity |
| Orders but poor contribution | Acquisition cost, discounting, returns, low AOV, costs | Net order profit, returns cohorts | Fix economics and offer/product selection |
| Strong short-term results, weak scale | New reach harder, constrained stock, saturation, overlap | Incremental reach, cohort economics, frequency/context | Test new buying situations and inventory capacity |
| Good platform ROAS, weak total sales lift | Attribution overlap, cannibalization, organic substitution | Holdout/incrementality design where feasible | Reconsider allocation and causal claims |

**Never assert any one explanation solely from a funnel ratio**. Segment at the product, offer and traffic-source level when samples allow.

## C. Choose interventions by expected business leverage

Prioritize: (1) hard blockers and customer harm, (2) data integrity, (3) unit economics and high-friction page issues, (4) positioning/creative tests, (5) channel and budget allocation, (6) expansion. Use `impact × evidence × reversibility ÷ cost/effort` as a qualitative prioritization aid, not fake numerical precision.

## D. Experiment design

For each proposed change write `observation → hypothesis → competing explanation → intervention → control → primary metric → guardrails → decision rule`. Where possible, randomize and change only the variable being tested. If there is insufficient volume, report weaker evidence instead of declaring a winner. Track both effectiveness and unwanted outcomes: returns, discount dependency, refund rate, support load or damaged brand trust.

**Example** (hypothetical): Low add-to-cart rate on ring PDP; support asks about size. Hypothesis: clear on-page sizing information reduces uncertainty. Alternative: buyers simply dislike price or style. Improve the guide; compare controlled purchase behavior when feasible; track size-related returns. Don't automatically rewrite a headline.

## E. Decision matrix

| Evidence | Decision | Next step |
|---|---|---|
| Credible lift in *profitable* outcomes, no harmful guardrail regression | Keep / expand cautiously | Re-check capacity and incremental scale |
| Stronger engagement only, no business outcome improvement | Reconsider | Ask whether the creative brings the wrong visitor |
| Significant decline or real customer harm | Stop/fix | Investigate defect and document learning |
| Inconclusive / low sample / confounded | Continue or redesign if justified | Don't proclaim a winner; collect better evidence |
| Product/page issue overwhelmingly supported | Fix system before more ads | Route to [offer/PDP workflow](04-offer-and-conversion.md) |

Use [the experiment log](../templates/experiment-decision-log.md), [marketing effectiveness](../references/marketing-effectiveness.md) and [testing guide](../references/testing-and-learning.md). Meta provides [A/B, creative, conversion-lift and brand-lift study training](https://formedia.facebookblueprint.com/student/path/219763-ab-test-conversion-brand-lift-course). Google's [attribution-vs-incrementality explanation](https://support.google.com/google-ads/answer/14102450?hl=en) clarifies the underlying causal distinction (not Meta-specific tool availability).

**Handoff:** observed outcomes + validated learning → [customer research](02-buyer-discovery.md), [creative](06-creative-production.md), [offer](04-offer-and-conversion.md), or [retention/scale](09-retention-and-scale.md).
