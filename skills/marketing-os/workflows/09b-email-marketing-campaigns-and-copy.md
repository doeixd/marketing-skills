# Workflow 9B — Email marketing strategy → creative → campaign/flow → measurement

**Trigger:** Promotional newsletter, ecommerce email campaign, subject/preheader, welcome series, product launch or offer, email copy, abandoned cart, postpurchase, segmentation, email strategy, engagement or underperforming email sales.

**Place:** Stage 9 specialist. Read [Email Strategy/Copy](../references/email-marketing-strategy-copy-and-creative.md), [Email Deliverability](../references/email-deliverability-consent-and-reputation.md), [Email Campaign Brief](../templates/email-campaign-and-creative-brief.md), [Brand 3A](03a-brand-discovery-and-messaging.md), [Offering 1A](01a-offering-discovery-and-marketing-plan.md), [Analytics 8A](08a-marketing-analytics-and-measurement.md), [Deliverability 9E](09e-email-deliverability-and-list-health.md). For Shopify use [9A](09a-shopify-lifecycle-retention.md); for cross-channel flows [9D](09d-cross-channel-lifecycle-and-segmentation.md).

## 0. Context and guardrails

Identify actual brand voice, offering/product variants, customer purchase occasions, recipient relationship and *legal basis/ESP platform eligibility*, current list sources and marketing permissions, jurisdiction/market, email provider, business goal, recent performance, actual offer/discount/stock, destination and sender domain. A list export is not proof of opt-in or live email delivery. Choose transactional vs marketing with proper primary purpose; ensure product truth and compliant sender contact details.

## 1. Select audience, outcome and email job

Map `segment/actual eligibility → buyer context → existing alternatives/questions → one useful takeaway → credible evidence → CTA/landing → expected commercial/brand outcome`. Define campaign vs automation, subscriber expectation and send timing. Consider whether helpful editorial, real product information, comparison or customer-care messaging serves audience better than discounting. Assess purchase/retention economics and current frequency pressure.

## 2. Compose strategic variants

From the actual brand/offering evidence, propose **distinct creative hypotheses**, not ten clickbait synonyms. For each create:
- Subject with accurate promise + complementary preheader;
- Recognizable sender and possible reply handling;
- Clear opening/hero product or insight, brand cue and substantive body;
- Real proof, honest qualification, relevant actual policies and accessible images/alt;
- One main CTA and matching verified destination;
- Correct commercial footer, unsubscribe/preferences and physical address fields **supplied by the business** (never invent).
- Optional plain-text alternative, mobile layout/rendering direction and actual dynamic-variable fallbacks.

Use [Email Campaign and Creative Brief](../templates/email-campaign-and-creative-brief.md). If asked for a multi-email series, specify **separate purpose and actual time/exit logic for each touch**, not a repetitive "just following up" chain.

## 3. Deliverability and sender/list QA

Route to [9E](09e-email-deliverability-and-list-health.md). Check SPF/DKIM/DMARC (and bulk sender requirements where relevant), From domain, complaints/bounces/unsubscribes, list sources, opt-out propagation, rendering/links and frequency. **Open rate is unreliable** due to Apple MPP, so do not declare a subject winner only from opens.

## 4. Automation and collision QA

Check actual trigger and eligibility (browse vs cart vs checkout), postpurchase/refund/opt-out and other flow suppressions, frequency, no-email/quiet restrictions, product/market availability and flow priority. Avoid duplicated welcome, recovery and postpurchase sends across Shopify Messaging, Klaviyo and other ESPs. For SMS coordination see [9D](09d-cross-channel-lifecycle-and-segmentation.md).

## 5. Measure and learn

Record delivered/clicks/bounces/complaints/opt-out, qualified traffic, actual product/order/lead outcome, realized contribution, segment and date. Distinguish ESP-attributed revenue from incremental benefit; for meaningful strategic uncertainty propose eligible recipient holdout or A/B with one outcome and guardrails. Compare performance against store/segment history not generic vendor benchmark.

**Deliver:** audience/eligibility rationale; campaign or flow logic, full copy (subject/preheader/body/CTA), creative/layout and landing notes; sender/legal/deliverability QA; experiment/reporting plan; approval checklist. **No send/schedule/automation activation without user approval.**
