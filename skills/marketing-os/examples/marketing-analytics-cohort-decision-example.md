# Worked example — what data-driven marketing actually concludes

**Fictional numerical toy case.** Values are invented solely to demonstrate method, not observed Shopify/Klaviyo/Google performance or a benchmark. See [Analytics 8A](../workflows/08a-marketing-analytics-and-measurement.md), [Attribution 8B](../workflows/08b-attribution-incrementality-and-experiments.md), and [RFM 8C](../workflows/08c-customer-segmentation-rfm-and-clv.md).

## A. Email holdout: an attributed sale is not necessarily incremental

Assume equal-size randomized email-eligible groups, 1,000 customers each, valid consent/eligibility and mutually exclusive assignment. During a prespecified purchase observation period:
- Treatment: 60 unique customers buy, generating $1,500 *net contribution before messaging*.
- Control: 50 unique customers buy, generating $1,300 *net contribution before messaging*.
- Campaign sends cost $40 in total for treated contacts; no other differential cost (toy assumption).

**Observed purchase-rate difference:** 60/1000 − 50/1000 = **1 percentage point**, a 20% relative difference versus control's 5% baseline. **Observed contribution per eligible contact difference:** ($1,500−$40)/1000 − $1,300/1000 = **$0.16**. The data are too sparse to declare the effect statistically or commercially reliable without a prespecified power/uncertainty analysis and appropriate independence/measurement checks. Do **not** call this proof of +20% profit.

An ESP might attribute **all 60 purchases** to the treatment send under a lookback. The experiment instead asks what buyers did beyond the control baseline; this illustrates why credited revenue ≠ lift.

## B. RFM and cohorts: avoid one-size-fits-all churn

A customer who bought one holiday ring 11 months ago may be a normal infrequent/gift buyer, not "dormant and at risk". A customer who buys a consumable every 30 days may be meaningfully overdue after 90 days. Same recency, **different category and buyer job**. Segment by real history and purchase cycle, and verify customer preference before outreach.

Use `R = analysis date - last valid order`; `F = count distinct completed orders in a stated window`; `M = net revenue or contribution with refunds handled`. Tiny lists and tied F=1 distributions make quintiles misleading. Track cohorts from first purchase and compare customers with equal months of opportunity before inferring CLV.

## C. What a report should display

| Concept | Correct diagnostic question | Stronger evidence |
|---|---|---|
| High email opens | Is Apple Mail Privacy Protection inflating pixel loads? | Verified clicks and site actions |
| High revenue attributed to SMS | Would these customers buy anyway? | Customer-level holdout among lawful SMS subscribers |
| Shopify CVR changed suddenly after Sep 2026 | Did session measurement change? | Same-definition reconciliation and orders |
| Google Ads attributed purchases exceed store sales after adding Meta/email credits | Are platforms claiming overlapping journeys? | Single commerce order ledger and modeled windows |
| High click rate but lower margins | Does message/discount change who buys and what they buy? | SKU-level contribution, returns, experimental lift |

**Decision pattern:** not "send more, because dashboard revenue rose" but "fix instrumentation/eligibility, understand the buyer hypothesis, run appropriate controlled test and scale only if net contribution and customer experience support it." 
