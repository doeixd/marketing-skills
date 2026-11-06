# Marketing measurement plan, event contract and KPI dictionary

Use [Analytics 8A](../workflows/08a-marketing-analytics-and-measurement.md).

## Decision and data accessibility
- Brand/store/service, primary profit/qualified outcome, actual owner and time period:
- Questions decisions this analysis will answer:
- Authorized connected sources (Shopify, CRM, GA4/BigQuery, Google/Meta Ads, Klaviyo/Shopify Messaging/SMS, GSC):
- What cannot be observed or is modeled:
- Consent, privacy, access and retention constraints:
- Site/store version changes, tracking releases, Shopify Sep 2026 session-definition change:

## KPI dictionary
| Metric | Business question | Exact numerator | Denominator and population | Date/timezone/window | Currency/tax/refund/fee convention | System of record | Known bias/gap | Decision boundary |
|---|---|---|---|---|---|---|---|---|

**Examples to define:** qualified/new orders, net realized revenue and contribution, qualified lead, visit→purchase by chosen system, first-to-second order, discount/return rates, email delivered and click rate, SMS STOP rate, attributed vs incremental campaign value.

## Event and identity data contract
| Event name | Business meaning and emission trigger | Source | Timestamp/timezone | event_id/dedupe key | customer/order/variant key | Parameters/versions | Consent/PII restrictions | Owner/test |
|---|---|---|---|---|---|---|---|---|

### Required checks
- [ ] Purchase dedupe and order ledger reconciliation.
- [ ] GA4 ecommerce `purchase`/`refund` `transaction_id`, `items`, `value` and `currency`.
- [ ] Lead qualification stage vs raw form submit; window/loss delay.
- [ ] Email/SMS sends have actual consent/eligibility; no false delivered/open events.
- [ ] Campaign/UTM naming taxonomy consistent; no PII in URL.
- [ ] Multi-platform credited sales **not summed** as distinct revenue.
- [ ] Refunds, test orders, cancellations, consent, time zones and missing coverage documented.
- [ ] Metric/report changes and device/market denominators annotated.
- [ ] Access to customer-level data follows privacy approvals.

## Reporting design
| Section | Chart/table | Grouping/segment | Business use | Baseline/refresh | Red flag/data coverage |
|---|---|---|---|---|---|
| Business pulse | | | | | |
| Acquisition | | | | | |
| PDP/checkout funnel | | | | | |
| Lifecycle | | | | | |
| Customer cohorts/RFM | | | | | |
| Tests/uncertainty | | | | | |
| Data quality | | | | | |

## Research/decision log
- Main finding, source and limitations:
- Competing explanation and evidence to collect:
- Fix vs experiment vs no action:
- Owner, approval and review date:
