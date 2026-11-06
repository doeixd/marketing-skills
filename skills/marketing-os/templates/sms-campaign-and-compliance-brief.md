# SMS/text marketing concept, provider and consent preflight

Use [SMS Workflow 9C](../workflows/09c-sms-text-and-messaging-marketing.md) and [SMS/Legal Reference](../references/sms-text-marketing-and-compliance.md).

## Why text?
- Specific timely customer job; why not email/site/support instead:
- Verified brand, product/offer, exact claim IDs and official URL:
- Geography and actual recipient timezone; state/local rules and quiet hours:
- Marketing vs genuine transactional/service classification:
- Audience, size and **separate SMS marketing consent** with proof/source date:
- Provider (Shopify Messaging/Klaviyo/Postscript/Attentive/Twilio etc), sending route and A2P/short/toll-free/WhatsApp readiness:
- Brand, country, sender registration and compliance/owner:
- Time/cost constraints, actual offer expiry and shipping/stock:
- Complaint/STOP source of truth and suppression sync:

## Candidate copy (distinct useful premises)
| Angle/occasion | Exact SMS draft (brand, value, verified URL, correct opt-out) | Real evidence | Encoding estimate/segments via provider | Expected buyer action | Approval |
|---|---|---|---|---|---|

**Do not assume 160 characters always means one SMS.** Check provider-calculated GSM-7 vs Unicode/UCS-2 segment count, embedded URLs, language, MMS costs and sender presentation.

## Automation / eligible send logic
| Trigger | Must be true (permission, market, state) | Exclusions (purchase, STOP, refund, service, frequency) | Delay/local time | Other channel priority | Exit/owner |
|---|---|---|---|---|---|

## Mandatory quality gates
- [ ] Jurisdiction-specific legal review appropriate to case; no blanket TCPA advice.
- [ ] SMS marketing opt-in evidenced separately from email; no bought/scraped phone list.
- [ ] Sender/A2P or alternative route approved by provider and carriers.
- [ ] STOP/HELP and other revocations tested; suppression propagated to connected tools.
- [ ] User-selected frequency, local quiet hours and real offers honored.
- [ ] Product availability, discount/expiration and destination valid.
- [ ] Message states actual brand; no false surveillance/limited stock/testimonial.
- [ ] Estimated total message segments/carrier/send fees; margin guardrail.
- [ ] Internal tests only until **explicit customer send approval**.

## Results review
- Eligible opt-ins, attempts, carrier delivered, clicks/qualified visits/orders:
- STOP rate, complaints, cost per segment, contribution, holdout if feasible:
- Actual value and uncertainty; stop/adjust decision:
