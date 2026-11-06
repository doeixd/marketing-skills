# SMS/MMS/WhatsApp and text marketing: strategy, creative, consent and operations

Reviewed 2026-11-06. Use [SMS Workflow 9C](../workflows/09c-sms-text-and-messaging-marketing.md), [SMS Creative/Compliance Brief](../templates/sms-campaign-and-compliance-brief.md), [Lifecycle 9D](../workflows/09d-cross-channel-lifecycle-and-segmentation.md), [Shopify Lifecycle 9A](../workflows/09a-shopify-lifecycle-retention.md), and [Email Consent](email-deliverability-consent-and-reputation.md).

## 1. SMS is a high-interruption channel

A text is personal and attention-demanding. Use for **meaningful, timely, authorized** information: genuinely relevant restock, helpful scheduled event reminder, eligible abandoned checkout assist, verified time-limited offer, practical postpurchase support or service update. If a campaign is generic content with no time relevance, a less interruptive email or owned resource may be preferable.

Distinguish **marketing SMS**, **transactional service notification**, **authentication/OTP**, **human conversation**, **MMS** (media cost/availability), **RCS**, and **WhatsApp Business** (platform templates, session/opt-in rules). Rules and sending permissions differ by channel and country. A phone number used for shipping notifications is not automatically permission to receive promotions.

## 2. US legal and carrier compliance: verify current rules

The US [TCPA](https://www.fcc.gov/general/telemarketing-and-robocalls) and FCC rules apply depending on how messages are sent and their purpose; **automated marketing texts commonly require prior express written consent**. Do not assert the same exact statutory rule for all human-sent service messages. In addition, many states have stricter **"mini-TCPA"** and quiet-hours rules, plus industry/carrier/CTIA requirements. Because litigation and rules have changed, verify 2026 effective dates with counsel/official sources.

**Consent proof for text marketing:** brand/sender and intended content, clear opt-in statement/form version, capture source, country/state, timestamp, method/phone number in secure systems, optional double opt-in as required by platform, and withdrawal method. **Email opt-in ≠ SMS opt-in**. Purchased lists/third-party "consent" should not be presumed transferable. Do not pre-check SMS opt-in or condition a purchase on accepting unrelated marketing; regulatory details vary. Preserve proof securely with access/retention policy.

**A2P registration:** US application-to-person messaging over US **10-digit long codes** typically requires registered business/brand and campaign via **A2P 10DLC**; toll-free verification and short codes have separate routes. [Twilio A2P registration](https://www.twilio.com/docs/messaging/compliance/a2p-10dlc/quickstart) describes a provider process; don't assume registration from merely owning a phone number. Shopify Messaging may manage infrastructure differently—verify merchant/provider readiness and countries, not copy a Twilio setup mechanically.

**Opt-out:** support recognized STOP/HELP and meaningful equivalents; ensure receiving systems honor requests and suppress future marketing across all tools. Twilio [Advanced Opt-Out](https://www.twilio.com/docs/messaging/tutorials/advanced-opt-out) documents reserved keyword behavior and cross-channel caveats; forwarding an unsubscribe to Shopify/Klaviyo/Postscript is an integration task, not automatic. Honor explicit revocations promptly and track current legal deadlines. The FCC adopted rule changes published October 2026, some effective **November 25, 2026**; because this is future relative to review, do not treat the pending provisions as already effective. See [Federal Register FCC rule](https://www.govinfo.gov/content/pkg/FR-2026-10-26/html/2026-21821.htm).

For UK, ICO PECR generally requires specific individual consent or qualifying soft opt-in for marketing email/text, with country/recipient distinctions; don't apply US standards globally.

**Quiet hours and frequency**: check recipient local timezone, state law, provider/campaign rules, store schedule and notification purpose. There is no safe single global send window. Never suggest a nighttime "urgent" campaign with invented urgency.

## 3. Compose text that deserves the interruption

A concise text has:
- **Identifiable brand/sender** immediately or clearly from sender ID/context;
- **Specific relevant reason** (real event/product/condition and verified promise);
- **Concrete value** (how to choose, useful deadline, actual offer, customer-help link);
- **Single action** and legitimate branded/trusted destination;
- **Accurate price/stock/conditions**; no generic "personal" insinuations about private behavior;
- **Opt-out instructions**, legally/platform appropriate, with understandable frequency/cost disclosures where required.

Character/encoding costs matter: GSM-7 **usually 160 single-segment characters**, UCS-2 often **70**, and concatenation lowers per-segment capacity; emojis, smart punctuation, and non-GSM symbols may change billing/length. Count with actual provider's encoding estimator; plain JS string length is **not** a substitute for GSM segment calculation. MMS and links have carrier restrictions and costs. Avoid suspicious URL shorteners or tracking links that conceal destinations. URL UTM tracking must not leak PII.

**Copy principles:** 1 intention per message; honest, conversational actual brand voice; no ALL-CAPS false alarm, fake "you left something," impersonation, fabricated scarcity, deceptive prize, or hidden fees. Messages can be genuinely helpful without a sale.

## 4. Lifecycle use cases and suppressions

| Scenario | Eligibility/trigger | Critical exclusion |
|---|---|---|
| Welcome | Actual separate SMS marketing opt-in | Already opted out, duplicate confirmation or region not served |
| Restock | Requested watch/consent and actual restored available SKU | Out of stock in customer's market, purchased already |
| Abandoned checkout | Verified eligible checkout + appropriate SMS permission and policy | Already purchased, frequency cap, sensitive/private products |
| Event/appointment | Real scheduled event and message purpose | Canceled/rescheduled; transactional vs promo classification |
| Seasonal sale | Real relevance, consent, real pricing/limits | Discount restrictions or shipping cutoff mismatch |
| Postpurchase care | Genuine ordered item and channel permitted | Shipping service text confused with advertising |
| Replenishment | Real product use and expected cycle, consent | No replenishment need / returned order |
| Winback | Appropriate relation and frequency, still valid permission | Repeated unanswered messages, complaint or opt-out |

Cross-channel priority: **do not blast email + SMS at the same moment by default**. Use buyer need, value of interruption, channel consent, frequency budgets, previous recent sends, purchase/suppression and fallback. Verify channel-specific unsubscribe across installed systems.

## 5. Operational tracking and ROI

Track actual **eligible opted-in audience**, send attempts, carrier acceptance, delivery receipts (not guaranteed actual reading), click signals with bot caveats, qualified sessions, actual orders/leads, margin per recipient, replies/complaints and STOP rate; account for **per-segment send fees**, number rental, compliance/registration, provider fees, creative production and discount cost.

SMS attributed revenue is often based on short lookback rules and can overlap with email/paid media/organic. **Holdouts at customer level**, when lawful and feasible, more directly estimate incremental impact. Avoid applying universal vendor CTR figures as business-specific expectations.

## 6. Platform/skills references

- [Shopify SMS requirements](https://help.shopify.com/en/manual/promoting-marketing/create-marketing/shopify-messaging/sms/requirements), [Shopify Messaging](https://help.shopify.com/en/manual/promoting-marketing/create-marketing/shopify-messaging)
- [Twilio A2P 10DLC](https://www.twilio.com/docs/messaging/compliance/a2p-10dlc/quickstart), [Opt-outs](https://www.twilio.com/docs/messaging/tutorials/advanced-opt-out)
- [FTC CAN-SPAM](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) (commercial **email**, not a replacement for TCPA review)
- [FCC/Federal Register Oct 26 2026 rule, later effective date](https://www.govinfo.gov/content/pkg/FR-2026-10-26/html/2026-21821.htm)
- [UK ICO PECR marketing email/text](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/)
- [Corey Haines SMS Skill](https://github.com/coreyhaines31/marketingskills) (`sms`) and [Klaviyo Analyst skill](https://github.com/thatrebeccarae/claude-marketing/blob/main/skills/klaviyo-analyst/SKILL.md).
