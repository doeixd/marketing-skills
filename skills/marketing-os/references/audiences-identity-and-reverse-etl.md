# Audiences, identity, Meta datasets and reverse ETL

**Reviewed 2026-11-06.** Use for first-party segmentation, remarketing, audience exclusions, suppression lists, CRM conversion uploads, Shopify customer segments, server-side event routing and warehouse-to-platform activation. Always pair with [tracking](measurement-pixels-ga4-and-attribution.md), [ETL](marketing-data-engineering-and-etl.md) and applicable policy.

## Separate datasets, events, audiences and activation

- **Dataset/event source**: Meta event collection surface used for measurement and optimization (may receive Pixel and Conversions API events).
- **Website Custom Audience**: people eligible for remarketing based on allowed website interactions, configuration and policies; audience size and coverage depend on matched and allowed signals.
- **Customer-list Custom Audience**: platform-matched first-party identifiers uploaded through a permitted interface and subject to terms, provenance and consent. Hashing is **not** anonymization or permission.
- **Lookalike / Advantage-type expansion / interest or broader targeting**: different platform products, eligibility and controls. Verify live settings; a customer segment is not automatically a targeting instruction.
- **Shopify customer segment**: dynamic merchant records selected by ShopifyQL and store-owned customer fields; not equivalent to a Meta dataset or GA4 audience.
- **GA4 audience / Google Ads Customer Match**: distinct identity, eligibility, consent, refresh, retention and linked-account requirements.

## Segment from an actual decision

Define one objective per segment with inclusion, exclusion, lookback, recency, frequency and measurement:
- Past buyers of product family A, excluding refunded or already reordered purchases, for relevant replenishment or accessory campaigns.
- First-time buyers with clear category interest, **only when lawful and supported by consent**.
- Checkout abandoners where permitted; exclude recent purchasers; do not assume an abandoned session contains an identifiable or contactable customer.
- Qualified lead converted offline, to improve **conversion measurement** without necessarily retargeting them.
- High-value customer cohort for aggregate LTV/retention analysis before contemplating ad lookalikes.

For each segment document: named owner; source table and grain; canonical rules; retention; refresh interval; match field eligibility; minimum size/policy rules; consent/legal basis; suppression and deletion propagation; activation destination; experiment/holdout; success metric. Don't target or exclude people on unlawfully inferred sensitive attributes; heed Meta's special ad categories and platform restrictions.

## Identity and matching

Use deterministic source-scoped commerce IDs for orders. For people, avoid a universal inferred identity graph built from platform marketplace exports. Within legitimately held first-party properties, use documented opt-in identity merges with retention and separation. Prefer pseudonymous, purpose-limited keys and aggregated cohorts for analysis. A hashed email/phone remains personal data in many regimes. Never use a consumer marketplace buyer export to create ad audiences absent documented platform authorization, customer permission and legal review.

Meta match signals may include browser identifiers, permitted customer information and `external_id`; use only actual collected values in approved contexts with correct normalization and hashing as required. Do not fabricate `_fbc`, `_fbp`, click identifiers or past consent. Restrict data exposure in logs, dashboards and third-party tools.

## Reverse ETL operational design

```text
lawful customer source → normalized customer/consent model → segment query → eligibility and exclusion gate
 → signed-off activation spec → encrypted permitted mapping → platform API/upload → delivery diagnostics
                 ↑                                             |
        unsubscribe/erasure updates <──── refresh/removal/reconciliation <──────┘
```

A robust sync supports idempotent upserts, platform rate limits, change detection, deletions/removals and suppression refresh, with encrypted transit and secret handling. Track count of eligible rows, sent records, accepted rows, platform match/usable size (when exposed), fresh/expired records, rejects and cost. Never interpret upload acceptance as successful matching or a measurable lift. For a pilot prefer aggregation first or a holdout with an agreed unit of randomization. Review inferred vs observed eligibility.

**Critical stop conditions:** ambiguous data ownership, insufficient marketing consent, unresolved deletion request, platform policy mismatch, sensitive traits, export to unrelated advertising accounts, inaccessible unsubscribe status, data breach risk, or account access not approved.

## Routing and governance

- For Shopify retention and known customers, prefer built-in [Shopify segments](https://help.shopify.com/en/manual/customers/customer-segmentation), Shopify Messaging/Flow and approved direct channels where suitable before costly CDP plumbing.
- For Meta Pixel/CAPI remarketing, audit event source, data quality, ownership, eligible events, audience configuration and consent. Use [Meta Blueprint data-source training](https://www.facebookblueprint.com/student/path/211560-tracking-events-course).
- For Google offline uploads/Customer Match, read [Google's first-party customer data policy](https://business.google.com/us/accelerate/resources/articles/customer-data-policies/) and [conversion upload docs](https://developers.google.com/google-ads/api/docs/conversions/upload-offline); avoid treating a campaign click ID as blanket permission to send user data.
- For warehouse activation/CDP evaluation, inspect [RudderStack's current source/destination coverage](https://www.rudderstack.com/docs/destinations/overview/) and consent/data governance features; commercial availability and feature permissions differ. Other providers' reverse ETL and CDP products are optional substitutes, not required technology.

**Deliver:** segment definition and audience policy checklist, consent lineage, dry-run counts, sync design, removal plan, QA observations, approved activation and causal measurement plan.
