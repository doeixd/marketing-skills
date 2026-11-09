# Workflow 8G — Audiences, datasets, reverse ETL and campaign/UTM governance

**Trigger:** Meta datasets or audiences, customer list upload, Custom Audience/Lookalike, Google Customer Match, Google Ads Data Manager, CRM→ads sync, suppression/exclusion audiences, UTM taxonomy or first-party conversion activation.

**Position:** Activation specialist under [8D](08d-marketing-data-pipelines-and-measurement.md), from [Analytics 8A](08a-marketing-analytics-and-measurement.md) and [Customer Segmentation 8C](08c-customer-segmentation-rfm-and-clv.md). Read [audiences and reverse ETL](../references/audiences-identity-and-reverse-etl.md), [2026 API changes](../references/2026-platform-data-api-updates.md), [UTM governance](../references/campaign-utm-and-identity-governance.md), [Audience Activation Brief](../templates/audience-activation-and-suppression-brief.md).

## 0. Start with buyer relevance and lawful purpose

Clarify **why this audience** and what customer decision/benefit it serves, and distinguish **dataset/event source** (e.g., Meta Pixel/CAPI) from **Custom Audience** (targeting eligibility), **seed/lookalike** (model audience), **ad group** (delivery configuration) and **warehouse segment** (analytical classification). Buyer research/brand value come first; having customer emails does not imply a legitimate remarketing purpose.

## 1. Verify first-party provenance and restricted sources

Maintain `identity source → data origin/relationship → lawful basis → marketing/ads consent by purpose/geo → platform product terms → retention/deletion → permitted destination`. A purchaser on Etsy or Amazon is not automatically a direct-to-consumer advertising contact: marketplace terms can restrict use even when technically available. Hashing a contact field is **not** anonymization or permission to transmit it. Sensitive-category restrictions, minors, health/financial status, protected traits and customer deactivation requests require specialized legal/platform review.

For email/SMS communication: separate permission from audience sharing/ads; an opted-in email address doesn't necessarily authorize a Meta Customer List. Retargeting on-site visitors also needs consent/configuration appropriate to jurisdiction and channel.

## 2. Define and qualify audience logic

`Audience name/ID | business purpose | exact inclusion/exclusion logic | source timestamps | consent eligibility | expected size | destination | refresh | deletion SLA | controls | owner`. Candidate segments from real events: product viewed but **not bought** (where permitted), recent genuine buyer for retention, historical customer suppression, category interests from actual opt-ins, high-contribution cohort with lawful use. Do not infer sensitive motivations from purchase records or assert that Lookalikes guarantee similar profitable buyers.

Apply opt-out and right-to-delete **before materialization** and at every sync; remove stale/withdrawn members. Avoid relying on a static positive list that never retracts unsubscribed users. Use account/platform audience policies and membership minimums as **live-check items** because they change.

## 3. Decide activation method and Google/Meta specifics

- **Meta datasets:** collect events via Pixel/CAPI and optionally applicable offline integration; event forwarding and Custom Audience creation are separate controls/permissions. Evaluate match quality only from authorized permitted identifiers and correct event IDs. Never switch off old pixel/CAPI until actual sender inventory and dependencies reviewed.
- **Meta Customer Lists / Custom Audiences:** eligible permissioned first-party list with deletion/refresh policy, no unauthorized marketplace contacts; API/Ads Manager access and platform terms review.
- **Google Ads Customer Match / offline conversions:** choose **Data Manager API** for new 2026 integrations. Validate event uploads (`validateOnly`), monitor async status, conversion adjustments; audience uploads and events have distinct schemas/consent. Review any restricted ad category, account eligibility and ad personalization controls.
- **Shopify/email lists:** a Shopify segment is not intrinsically a cross-platform ad audience; check consent and integration permissions. Never use raw hashed contacts in URL/query parameters.
- **Data warehouse reverse ETL:** no direct raw PII copying into chat output, logs, public buckets, shared sheets or loosely protected automation platforms.

## 4. Campaign/UTM contract

Use consistent `utm_source`, `utm_medium`, `utm_campaign`; optional `utm_id`, `utm_content`, `utm_term`, with a governed dictionary for *each actual platform*. Preserve landing/redirect parameters, authorized click IDs and autofilled ad tags. Never write contacts, coupon recipients, email, phone, address or secrets into URLs. For Amazon-target campaigns, Amazon Attribution tags are a separate mechanism; don't substitute arbitrary website UTMs. For Etsy-target ads, Etsy's marketplace reporting doesn't expose the same first-party site events.

Validate links, campaign IDs, case, encoding and network/cost import compatibility. Cross-platform GA4 data import requires exact case-sensitive campaign source/medium mapping; review Google requirements before unifying "fb", "facebook" and "meta".

## 5. QA and business evaluation

Dry-run eligible population, consent/opt-out exclusion, destination account, segment size, false inclusions, refresh/deletion and no-eligible-data scenario. In sandbox/test mode verify **actual membership and suppressed removals**, not just an "upload succeeded" status. Maintain audit of audience versions/changes and owner approvals.

Measure qualified reach/cost, net new buyer/contribution, suppression effectiveness, complaint/privacy metrics and incrementality where feasible. Reconcile audience population and upload errors without exposing customer identities.

**Stop:** unknown permission/source, protected/marketplace data, suppressed customer, unclear retention, unreviewed hashing/PII, invalid consent state, missing user authorization. **No live audience upload, segment activation, ad delivery or data sharing without explicit approval.**
