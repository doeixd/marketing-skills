# Campaign UTM, first-party identity and click attribution governance

**Reviewed:** 2026-11-09. Use with [Workflow 8G](../workflows/08g-audience-activation-and-utm-governance.md), [Event Tracking/UTM Plan](../templates/marketing-event-tracking-and-utm-plan.md), [Audience Brief](../templates/audience-activation-and-suppression-brief.md), [Analytics 8A](../workflows/08a-marketing-analytics-and-measurement.md) and [2026 platform changes](2026-platform-data-api-updates.md).

## 1. Separate the kinds of identities

Do not collapse them into a single "customer ID":
- **Purchase key:** source+merchant/store+order ID, represents commercial fact.
- **Line/variant/product ID:** source-specific inventory and catalog fact, may map to a canonical SKU with an effective date, pack size and exceptions.
- **Visitor/client/session ID:** device/session analytics identity, coverage depends on consent and browser.
- **Ad click IDs:** e.g. permitted Google `gclid`, `gbraid`, `wbraid`, Meta `fbclid` or `fbc` derived from correct first-party context; distinct from company person ID.
- **Campaign identity:** platform account + immutable campaign/ad/ad set ID where exposed, joined to approved UTM nomenclature and report date.
- **Recipient/audience ID:** legal first-party or platform-specific consented/authorized identity, possibly hashed on destination; data protection rules apply.
- **Etsy/Amazon marketplace account and order IDs:** cannot automatically be joined to DTC contact identities for remarketing.

**A canonical key is not permission to merge identities**, and a missing match is not a data-error if privacy choices disallow it. Preserve source scoping, provenance and purpose-based access policies. Treat hashing as pseudonymization, not consent or irreversible anonymization.

## 2. UTM conventions (proposal, not a universal GA4 preset)

| Field | Governance | Example |
|---|---|---|
| `utm_source` | Specific actual publisher/platform, lowercase and stable | `instagram`, `facebook`, `newsletter` |
| `utm_medium` | Small controlled channel dictionary | `paid_social`, `email`, `paid_search`, `organic_social` |
| `utm_campaign` | Stable initiative slug or exact platform campaign name, avoid renaming | `holiday_gifts_2026` |
| `utm_id` | Stable campaign ID when importing cost data | `meta_238123` |
| `utm_content` | Actual creative/variant identifier, not PII | `reel_product_closeup_02` |
| `utm_term` | Query/keyword theme where permitted | `vintage_style_ring` |

These are proposed strings; **GA4 default channel grouping may not classify arbitrary custom medium names as intended**. Validate live channel grouping or create a documented custom grouping. Cost import joins require exact source/medium/campaign fields with consistent case. Do not automatically use `utm_campaign={{campaign.name}}` where source names can change without a versioning policy.

**UTM source is not event source:** the campaign source may be "facebook" while the purchase event is emitted by Shopify/GTM/CAPI. Don't confuse UTM attribution with cross-channel conversion credit, nor infer a purchase came from a campaign merely because a final URL included its tags.

## 3. URL construction, redirects and storage

- Decide tagging conventions per final destination (Shopify site, article, external landing, marketplace page); do not tag internal navigational links with UTMs as they can override acquisition attribution.
- Add properly URL-encoded query parameters with existing `?` or `&`, respect fragments, distinguish first touch vs session source and preserve approved click IDs through 301/302, single-page routes, checkout/cross-domain transitions.
- Validate no duplicate UTM parameter with different values; document source/medium case and business naming normalization rather than silently rewriting all links.
- PII includes user email/phone/name, postal details and secret access tokens: never place these in URL, UTM or public tracking logs.
- Ensure campaign landing URL displays actual offer and matches correct country, catalog availability, language/currency and product variant.

## 4. Staging and identity mapping

Use `dim_campaign_mapping(account_id, platform_campaign_id, valid_from, valid_to, utm_*, is_active)`, retaining changes in platform naming. Build ad spend marts at **account+campaign+date+currency+attribution settings** and never fan out one campaign-day spend across multiple order lines without a deliberate allocation rule.

For events and commerce, use scoped `event_id`, `order_id` and consent state. A customer may receive email and later convert through a paid ad; neither UTM nor platform last click proves causation. Keep warehouse measured events distinct from modeled/attributed conversions.

## 5. Audience lifecycle and exclusions

A warehouse audience segment needs actual business purpose, source and legal eligibility, refresh cadence, retention and suppression/erasure handling. Upload/ad activity must be reviewed by authorized owner. **Avoid assuming email marketing opt-in covers paid ad targeting**. List inclusion/exclusion should be derived from current source-of-truth event and preference states and re-evaluated on every run.

For customer match and offline conversions in late 2026, prefer Google's **Data Manager API**; distinguish audience membership from event ingestion. Meta dataset event diagnostics and audience member eligibility aren't interchangeable concepts. Avoid optimizing high-EMQ scores without checking privacy and customer experience.

## 6. Measurement and validation

Tests: normalized UTM examples across Google/Meta/email, valid URLs and no PII; redirects; paid click-ID passthrough as allowed; source/medium/campaign exact matching and import contract; ad campaign ID lineage; purchase dedup and order reconciliation; consent change and audience removal; traffic from marketplaces without GA4 browser coverage.

Data review outputs must display **business orders vs measured events vs attributed conversions vs lift** separately. This distinction is central to Marketing OS.

### Primary sources

- [GA4 custom campaign URLs](https://support.google.com/analytics/answer/10917952)
- [GA4 campaign-data import](https://support.google.com/analytics/answer/10071305)
- [Google Consent Mode](https://developers.google.com/tag-platform/security/guides/consent)
- [Google Data Manager](https://developers.google.com/data-manager/api/devguides)
- [Amazon Attribution](https://advertising.amazon.com/en-us/solutions/products/amazon-attribution/)
- [Etsy Open API](https://developer.etsy.com/)
