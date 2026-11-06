# Lifecycle orchestration: journeys, email + SMS choice, triggers, suppression and contact governance

Reviewed 2026-11-06. Use [Lifecycle Workflow 9D](../workflows/09d-cross-channel-lifecycle-and-segmentation.md), [Journey Matrix](../templates/cross-channel-lifecycle-journey-map.md), [Email 9B](../workflows/09b-email-marketing-campaigns-and-copy.md), [SMS 9C](../workflows/09c-sms-text-and-messaging-marketing.md), [Shopify 9A](../workflows/09a-shopify-lifecycle-retention.md), and [Analytics 8A](../workflows/08a-marketing-analytics-and-measurement.md).

## 1. Model a person’s actual journey instead of a batch schedule

Core loop: **trigger → eligible relationship/consent → helpful purpose → channel decision → content/proof → next action → response → exit/suppress → measured result**.

A contact may be eligible for transactional updates but not marketing; may consent to email but not SMS; may buy before an abandoned-checkout send; may be in active service recovery or refund. A coordinated system must make correct decisions rather than sending every campaign to everyone.

**Channel role**:
- Email: more room for explanation, product comparisons, editorial and visual assets, relatively low incremental delivery cost; still interruptive at excessive volume and subject to deliverability.
- SMS: more immediate and costly/intrusive; reserve for genuine value and separate permission. Transactional/marketing purposes and rules differ.
- Owned site/account and support: appropriate for nonconsented research/FAQ, privacy/preferences and sensitive concerns.
- Paid and organic ads: external reach but consent/targeting restrictions; don't use a customer’s email/SMS opt-in as a universal license for ad audience sharing.

## 2. Recommended priority and state machine

Example customer-state precedence (adapt to legal/business model):
1. **Safety/order/service**: send necessary lawful service notifications without promotional embellishment, according to actual classification.
2. **Opt-out, complaint, bounce, legal/privacy prohibition**: suppress corresponding marketing channel immediately; record source and propagate.
3. **Purchase/booking/refund/support case**: exit incompatible browse/cart campaigns; prioritize help over sales.
4. **Pending active lifecycle message**: send only if reason remains relevant and within frequency budget.
5. **Broadcast campaign**: eligible only after checking contact preference, recent sends, quiet hours, delivery/local market and product availability.
6. **Reengagement/sunset**: limited and respectful; stop after no interest or complaint.

For every automated journey define event, predicate, timing, fallback, dedupe, channel eligibility, **exit/stop conditions**, priority vs other flows, duration, owner, audit and rollback. Ensure the event stream is **idempotent** (order/checkout events may arrive twice) and purchase/postpurchase state overrides prior checkout. Log channel-specific consent changes and message send attempts. Do not turn a marketing opt-out into an account deletion request; manage privacy separately.

## 3. Lifecycle portfolio

| Moment | Real customer need | Candidate channel | Distinctive gate |
|---|---|---|---|
| Subscriber signup | Understand brand/value and promised content | Email welcome | Recorded valid channel permission and source |
| Active browsing | Understand product differences | Helpful guide/page, possibly consented email | Avoid surveillance tone, verify event eligibility |
| Cart/checkout | Remove a specific true objection | Consented email; occasionally SMS | Stop if purchase; avoid multi-platform duplicate recovery |
| Purchase | Confirmation and care | Genuine transactional channel | Do not mix aggressive sales into service notices |
| Fulfillment/usage | Delivery/care, ensure satisfaction | Service email and consented education | Only real product instructions and policy |
| Later complementary need | Real fit and occasion | Email; occasional consented SMS | Check time/stock, no fictitious replenishment |
| Lapsed engagement | Preferences and value | Limited email reengagement | Respect no response, avoid mass repetitive sends |
| Referral/advocacy | Useful recommendation with permission | Owned email/partner page | No incentivized positive review or unsolicited friend's number |

## 4. Contact pressure, preference and frequency

Build frequency budget `customer channel × rolling window × relative priority`; avoid hard-coded global cadence. Respect actual frequency promise in signup, recipients' preferences and platform limits. Track quiet hours using a trusted **recipient local timezone** or conservative fallback; do not infer timezone from an unverified phone country code alone.

A flow "collision matrix" should answer:
- Can two flows both start for the same event?
- Is a contact already in another automated series?
- Are they now a customer, returned item, or a support case?
- Are there overlapping email/SMS campaigns within a short period?
- Can send timing conflict with legal or requested quiet periods?
- Which event cancels or pauses another?
- Do unsubscribe, STOP and channel switch propagate to **all connected ESPs**?

## 5. Segment and experiment ethically

Use actual RFM, first/returning buyer, explicit preference, product need and customer state—not sensitive inferred identity. Send-time tests and discount experiments use stable eligible groups and business guardrails (contribution, unsubscribe, return/cancellation, spam). For SMS vs email, randomize among **recipients validly consented to both** so a consent difference doesn't masquerade as channel effectiveness. Ensure controls still receive required service and safety communications.

## 6. Platform implementation

Shopify Messaging/Flow, Klaviyo/Braze/Iterable/Attentive/Postscript/Twilio may implement different state/trigger and suppression semantics. **Do not assume an integration is configured**; inspect actual installed tools, settings and permissions. System of record for contact preferences and orders must be explicit. Deduplicate order IDs and cart IDs where supported, and include real variant/market availability at send time.

Deliver workflow/journey table, segment logic, provider-specific implementation notes, consent matrix, collision/suppression test cases, copy packs and measurement plan. Do not activate automation or send recipients without express authorization.

## 7. Sources

- [Shopify Messaging automations](https://help.shopify.com/en/manual/promoting-marketing/create-marketing/shopify-messaging/marketing-automations)
- [Shopify Flow triggers](https://help.shopify.com/en/manual/shopify-flow/reference/triggers)
- [FTC CAN-SPAM](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)
- [Gmail Sender Guidelines](https://support.google.com/mail/answer/81126)
- [Twilio Opt-Out](https://www.twilio.com/docs/messaging/tutorials/advanced-opt-out)
- [Klaviyo Analyst agent skill](https://github.com/thatrebeccarae/claude-marketing/blob/main/skills/klaviyo-analyst/SKILL.md)
