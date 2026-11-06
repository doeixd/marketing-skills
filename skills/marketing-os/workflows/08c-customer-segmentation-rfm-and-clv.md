# Workflow 8C — Customer analytics: RFM, cohorts, meaningful segmentation and CLV

**Trigger:** User wants customer segmentation, RFM, cohort retention, lifetime value, churn risk, repeat revenue, VIP/value audience, behavioral clustering, purchase cycle or personalized campaigns.

**Place:** Stage 8 specialist. Read [Customer Analytics](../references/customer-analytics-segmentation-rfm-and-clv.md), [Segmentation Brief](../templates/customer-rfm-cohort-and-segment-plan.md), [Analytics 8A](08a-marketing-analytics-and-measurement.md), [Lifecycle 9D](09d-cross-channel-lifecycle-and-segmentation.md) and [Shopify Lifecycle 9A](09a-shopify-lifecycle-retention.md).

## 0. Define action and eligibility before model

Ask what business decision segment must change (promotion, welcome, replenishment, onboarding, support, CAC or product strategy), real category buying cycle, time horizon and source orders/permissions. Segment people only on lawfully available, relevant facts and avoid sensitive inferences. If no customer data is connected, provide data contract and hypotheses; do not invent segments sizes or financial outcomes.

## 1. Clean order/customer records

Source of truth: paid/fulfilled order state, unique order ID, secure customer key, date/time/currency, refunds/cancellations, net contribution or net revenue, actual product/category, market and any available channel permissions. Exclude test/duplicate/fraudulent orders based on documented rules. Preserve anonymous/guest coverage caveats and effects of identity merging. Do not require raw PII to calculate aggregate cohort outputs.

## 2. Calculate RFM from actual business cycle

Recency days since last eligible order; Frequency count distinct eligible orders in explicit window; Monetary net revenue or contribution (say which) in window. Choose thresholds by observed distribution and category: quintiles may fail with tied or sparse histories. Label segments with customer **behaviors**, not personalities: recent-first, active-repeat, high realized contribution, inactive beyond realistic cycle, support/refund cohort, legitimate product interest. Assign no marketing channel unless separately permitted.

## 3. Create cohorts and value observations

First-order month or signup/activation cohort, month since entry, original population denominator, repeated purchase/return/retained value; align observation windows and label younger cohort censoring. Historical cumulative value ≠ predicted lifetime value. For predicted CLV provide assumptions, uncertainty, calibration and validation; do not infer 5-year value from two months' orders.

## 4. Translate segment into helpful treatment

Write `segment | definition/size | evidence | buyer job | communication/offer | allowed channel | frequency/suppression | economic hypothesis | test/guardrails`. For jewelry or infrequent categories, "lapsed" may be normal; use help/gifting opportunities, not fake replenishment. Prefer holdout tests within each eligible segment for incremental impact where feasible.

**Deliver:** documented definitions, reproducible aggregation logic, segment/cohort tables with source/coverage, restrained CLV interpretation, customer-safe treatment plan and follow-up test. No personal secret leakage, fake data, invented predictive scores or unauthorized audience upload.
