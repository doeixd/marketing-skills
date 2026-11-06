# Customer RFM, cohort retention, contribution and action plan

Use [Customer Analytics 8C](../workflows/08c-customer-segmentation-rfm-and-clv.md).

## Question, unit and safe data
- Decision: better messaging, repeat, product strategy, spend or customer experience?
- Customer entity and actual product category purchase cycle:
- Order/CRM data source, coverage, lookback, currency/timezone, known missing guest orders:
- Cancel/refund/test-order exclusion and contribution convention:
- Privacy-safe join key (no raw names/emails/phones needed for aggregate output):
- Marketing consent and preference source **separate by channel**:
- Cohort period and observation cutoff (younger cohorts not equally mature):

## RFM definition
- R = days since last valid order, reference date:
- F = distinct eligible orders during lookback:
- M = net realized **revenue or contribution**, choose one:
- Threshold/quantile method and handling ties/small samples:
- Category-specific "normal" purchase cycle and censoring:
- Known data quality issues, coverage and exclusions:

## Cohort and segment results
| Segment/cohort | Exact inclusion rule | Eligible people and observation time | R/F/M or repeat data | Real net contribution | Contact permission by channel | What is hypothesized |
|---|---|---|---|---|---|---|

## Customer-specific treatment
| Segment and need | Useful intervention | Trigger/exit/frequency | Email vs SMS actual consent | Cost/offer economics | Primary incremental KPI | Test or no-action rationale |
|---|---|---|---|---|---|---|

## Value modeling
- Historical observed cumulative contribution per original cohort member:
- Projected CLV model? Required data, assumptions, horizon, discount rate, uncertainty and validation:
- Risk of survivorship, selection, small sample, leaked future data:
- Actual margin/returns/retention vs ESP attributed purchases:
- Decisions, owners and next data needed:
