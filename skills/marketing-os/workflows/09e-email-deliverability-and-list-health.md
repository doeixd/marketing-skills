# Workflow 9E — Email sending identity, deliverability, consent and list health preflight

**Trigger:** Email marketing domain setup, authentication, SPF/DKIM/DMARC, Gmail bulk sender compliance, spam folder, bounces, low engagement, high complaints/unsubscribes, sender warming, unsubscribe issues or list migration.

**Place:** Stage 9 specialist. Read [Email Deliverability Reference](../references/email-deliverability-consent-and-reputation.md), [Audit Template](../templates/email-deliverability-and-consent-audit.md), [Email 9B](09b-email-marketing-campaigns-and-copy.md) and [Analytics 8A](08a-marketing-analytics-and-measurement.md).

## 0. Classify sending context

Get actual sender domain, ESP (Shopify Messaging, Klaviyo, Braze, etc.), sending IP shared/dedicated if known, Gmail recipient volume and other inbox providers, history of sending, permission source, marketing vs transactional class, geographic legal scope and available authenticated diagnostics. Public website domain does not prove DKIM/DMARC setup or compliance.

## 1. Verify authentication and provider policy

Check actual SPF/DKIM records and passing results, DMARC record and alignment, TLS/PTR/headers and provider's live compliance status. For roughly 5,000+ daily personal Gmail recipients under same primary domain check Gmail **bulk sender** SPF+DKIM+DMARC, From alignment, RFC 8058 one-click unsubscribe for marketing/subscribed messages, visible unsubscribe and Postmaster thresholds. These are required by provider when applicable; a `List-Unsubscribe` header alone is insufficient for one-click. Do not pretend that `p=none` DMARC prevents spoofing, though it can meet Gmail's minimum policy setting.

Check Yahoo/Microsoft/ESP requirements and current [Google sender FAQ](https://support.google.com/mail/answer/14229414). Provider deliverability varies over time.

## 2. Audit source/consent and suppression

List opt-in origins, legitimate allowed use by jurisdiction (CAN-SPAM vs stricter ESP/country), proof, unsubscribes, bounces/complaints, marketing suppression, acquired lists, duplicate sends and stale contacts. Ensure opt-outs propagate across active tools. US CAN-SPAM generally doesn't impose universal prior opt-in but requires other commercial email rules; use accurate legal distinction. Transactional/service streams are not a workaround for prohibited marketing.

## 3. Diagnose performance

Inspect actual Postmaster/ESP bounces, deferrals, complaints, domain reputation, click and unsubscribe trends; acknowledge Apple MPP open bias. If data absent, give checks, not "spam score 87%" guesses. Root causes may be DNS/auth, sudden list imports/volume, subscribers without expectation, irrelevant cadence, broken links or provider deliverability.

## 4. Prioritize remediations

P0 unwanted or unsubscribed marketing, absent required compliance/auth, serious complaints and spoofed sender. Pause affected campaigns and fix with owner. P1 list hygiene, frequency and segmentation, reliable preference links, technical rendering and accurate sender content. P2 sender ramp, creative content/format and engagement experiments. Never recommend "warm-up bots" that generate fake opens or bypass provider policies.

## 5. QA before send

Complete [Sender Audit](../templates/email-deliverability-and-consent-audit.md): actual DNS and provider status, opt-in/suppression, subject/headers, reply/from identity, required physical address, functional unsub and one-click if applicable, rendering, links, locale, test sends, complaints and monitoring owner.

**Deliver:** confirmed vs unknown compliance, risk-prioritized fixes, live verification instructions, stakeholder/legal approvals and allowed test plan. **Never modify DNS, export a contact list, or schedule/send marketing without explicit authorization.**
