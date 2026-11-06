# Email/SMS customer journey, state machine, consent and collisions

Use [Lifecycle 9D](../workflows/09d-cross-channel-lifecycle-and-segmentation.md).

## Context
- Brand/offering, actual purchase/usage cycle and buyer needs:
- Source system for orders, consent by channel, CRM customer identity, product inventory:
- Installed Shopify/ESP/SMS providers, scopes and automation owners:
- Geography, privacy/compliance requirements, contact preference promises:
- Campaign frequency budget, local timezone/quiet-hour policy:
- Transactional/service vs marketing classification:

## Trigger/eligibility and exit matrix
| Journey/event | Source/event_id and state | Audience/real buyer need | Email eligibility and proof | SMS eligibility and proof | Timing/priority | Exit/suppression | Accurate offer/message | Business KPI |
|---|---|---|---|---|---|---|---|---|

## Flow collision matrix
| Flow A | Flow B | When both eligible | Priority/hold/suppress rule | Owner | QA case |
|---|---|---|---|---|---|

## Minimal state pseudocode
```text
on customer_event:
  identify lawful customer/market and deduplicate event
  update order, refund, customer-service and channel-consent states
  if marketing opted out/unknown for channel -> do not send marketing there
  if order completed -> cancel incompatible checkout/browse recovery
  if unresolved support/refund -> prioritize service and review marketing
  if local quiet period, frequency exceeded or other active flow -> queue/cancel per policy
  else choose highest-relevance valid message/recipient channel
  recheck state and catalog at actual send time
  record decision, consent source, send ID and outcome (no PII in logs)
```

## Test scenarios
- [ ] Buyer opts into email only and doesn't receive marketing SMS.
- [ ] Buyer responds STOP before queued SMS; all connected sender paths suppress.
- [ ] Person purchases while abandoned checkout message waiting; no recovery send.
- [ ] Duplicate events do not trigger double sending.
- [ ] Refund/service dispute changes sales eligibility.
- [ ] Two email flows + one SMS don't bypass frequency/priority.
- [ ] Local timezone and active discount/stock condition checked at delivery.
- [ ] Missing product name, locale or personalization has harmless fallback.
- [ ] Internal test profiles only; production activation explicitly approved.

## Outcome and learning
| Journey | Eligible population | Actual messages | Clicks/visits | Orders/net contribution | Complaint/STOP | Incremental control | Decision |
|---|---|---|---|---|---|---|---|
