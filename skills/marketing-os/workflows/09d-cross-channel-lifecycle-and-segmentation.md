# Workflow 9D — Email + SMS + onsite lifecycle orchestration and suppression

**Trigger:** Customer journey mapping, welcome/cart/postpurchase/winback workflows across channels, marketing automation stack, channel priority, trigger collisions, list/consent unification, segmentation-driven messaging or "build a full lifecycle system."

**Place:** Stage 9 orchestration. Read [Lifecycle Reference](../references/lifecycle-orchestration-and-channel-governance.md), [Customer Analytics 8C](08c-customer-segmentation-rfm-and-clv.md), [Email 9B](09b-email-marketing-campaigns-and-copy.md), [SMS 9C](09c-sms-text-and-messaging-marketing.md), [Shopify 9A](09a-shopify-lifecycle-retention.md) and [Journey Map](../templates/cross-channel-lifecycle-journey-map.md).

## 0. Map actual business/customer state

Identify purchase and product cycle, brand/offer, actual events and catalog, current ESP and Shopify/customer tools, **channel-specific** consent and opt-out, geography, source of truth, order/refund/support events, customer preferences, budget and capacity. Don't presume Braze/Klaviyo/Twilio or Flow exists.

## 1. Build explicit journey state machine

Create `event/trigger → who is eligible → exclusion → channel choice → wait window → message content/CTA → cancellation condition → measurement` for signup, browse, cart/checkout, purchase, fulfillment, care, next occasion, replenishment where real, winback and sunset. Use idempotent event IDs, stable customer key, observed order state and clear authority. Avoid "buy now" if order completed or refunded, and avoid selling into unresolved service disputes.

## 2. Give communication channels distinct jobs

Email for explanation/product breadth; SMS only with separate permission and material timely value; service/transactional messages separated from marketing. Enforce cross-channel pressure (per-day/week campaign budget suited to audience rather than imaginary universal rules), local send windows, active-flow precedence, no duplicate provider sequences and immediate suppression sync.

Develop segment×channel×journey matrix with exact opt-in proof, eligible size, goal, copy strategy, product/policy evidence and owner. Do not infer sensitive customer state from product browsing.

## 3. Design tests and rollout plan

For each branch define sample internal test accounts, no-send control, timing/reentry protection, item/currency/market substitution, unsubscribe changes, purchase-after-queue edge case, refunds, international eligibility, missing dynamic variables and email vs SMS collision. Keep transactional notices unimpeded. Send tests only to authorized internal/test recipients.

## 4. Evaluate customer and business quality

Report actual eligible audience, unique receives by channel, unsubscribes/STOP and complaints, real qualified purchases/contribution/retention, contact costs, observed vs incremental gains with holdouts where feasible. Segment by lifecycle and product cycles, not arbitrary vendor dashboard defaults.

**Deliver:** [Journey Map](../templates/cross-channel-lifecycle-journey-map.md), state/trigger contracts, consent/priority matrix, creative briefs, data/QA plan, controlled rollout and monitoring owner. **All real automation activation and customer communications require explicit user approval.**
