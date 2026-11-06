# Worked example: Shopify-style ecommerce lifecycle, email + SMS and data integrity

**Entire scenario is fictional.** There is no real store, customer list, purchase data, consent, sender DNS, prices, margin, ESP, phone sender, Shopify integration or verified performance. This demonstrates *what to research and produce* before asking an owner to approve communication.

## 1. Offering and buyer need

An example retailer sells an ornate vintage-inspired ring. Known only within the fictional prompt: visual ornamental ring detail. **Unknown**: metal, size, delivery, stock, warranties, refunds, user preference and authentic brand personality. Potential decision situations: comparing expressive jewelry, seeking a style-conscious gift (hypotheses; not observed customer segments).

First actions: verify actual SKU/variant facts and policy, brand voice, email opt-in collection and separate SMS permissions, live product and buyer questions. No "hypoallergenic", "free shipping", "handmade", "perfect gift" or invented reviews.

## 2. Email: possible *drafts*, not approved sends

**Concept A — helpful product detail** (when list subscribers genuinely requested product/style emails):

**Subject:** A closer look at the pattern

**Preheader:** Explore the vintage-inspired detail before choosing.

**Opening:** "The details are part of the design. See this vintage-inspired patterned ring from a closer angle."

**Body:** "Explore the visible pattern and product photos. Check the product listing for confirmed options and fit details before making your choice."

**CTA:** "View the ring" → verified product page **required**.

**Concept B — buying guidance** (only if an authentic size guide and real policies exist):

**Subject:** Choosing a ring as a gift?

**Preheader:** Start with the recipient's style and the fit details.

**Opening:** "A good starting point is the kind of ring they'd choose for themselves." Link to an actual accurate size/fit guide, not a fictional return guarantee.

**Creative:** product closeup, on-hand scale image only if genuine; appropriate alt text and actual brand mark. A real message requires legitimate sender, address and unsubscribe/preference details supplied by owner. Do not fabricate.

## 3. SMS: assess suitability before writing

If a real customer **specifically subscribes to SMS marketing** and asks for a product restock alert, a concise authentic notification can be useful **after** actual SKU inventory changes. Example is *conditional*:

> "[Verified Brand]: The ring you asked about is available again in [your selected variant]. View it: [verified URL]. Reply STOP to opt out."

The agent should **not** send this message based only on email opt-in or a product page view. Send route, local time, actual availability, sender identity, STOP handling, discount rules and SMS segment charges all require verification. If none of these are known, recommend email or onsite guide instead.

## 4. Orchestration sketch (hypothetical)

| Trigger | Customer eligibility | Message | Exit/suppress |
|---|---|---|---|
| First email signup | Real opted-in or otherwise legally eligible marketing email contact | Helpful introduction to brand/catalog | Already unsubscribed, email blocked |
| Real product browse | Platform has lawful event + channel permission, not already purchased | Optional product info email | Bought item, returned item/support case, frequency cap |
| Checkout started, unfinished | Valid checkout state + channel permission + flow policy | Clarify verified size/delivery terms | Any completed order, recent recovery, complaint/opt-out |
| Postpurchase | Actual order | Transactional confirmation; separate permission-based education | Return/safety/service rules and channel classification |
| Later gift season | Real permission and useful relevant selection | Product/collection guide | Sold-out, uninterested, purchase or suppressed |
| Verified SMS restock request | Explicit SMS marketing permission + provider/route approved | One timely restock message | STOP, already purchased, still out of stock |

No "send three texts" default, no offer discounts without economics and no labeling ordinary gift buyers "churned."

## 5. Data and measurement

**Event plan:** `signup`, `view_item`, `begin_checkout`, `purchase`, `refund`, `email_delivered`, `email_clicked`, `sms_sent`, `sms_opted_out`, with real data source and per-channel consent, lawful ID joins and order dedupe. Not every event is necessarily available from Shopify/ESP without implementation.

**Primary KPI**: incremental **net contribution per eligible recipient**, when randomized holdout is feasible, including media/message/discount costs and returns. Diagnostics: delivered/clicks, STOP/unsubscribe/complaints, checkout and real qualified orders.

Do not rely on Apple MPP-inflated opens, aggregate ESP-attributed sales or Shopify pre/post-Sep-2026 session metrics to claim causal lift.

**Pilot:** Randomly assign consented eligible email recipients to baseline/no *marketing* vs helpful email when business value merits it, preserving transactional order communications; power and guardrails based on actual baseline. For SMS vs email, compare among customers with lawful opt-ins for both and separate exposure; otherwise selection bias is unavoidable.

**Handoff:** [Email brief](../templates/email-campaign-and-creative-brief.md), [SMS brief](../templates/sms-campaign-and-compliance-brief.md), [Journey Map](../templates/cross-channel-lifecycle-journey-map.md), [KPI dictionary](../templates/marketing-measurement-and-kpi-dictionary.md).

**Validation fixture:** [messaging-plan-draft.json](messaging-plan-draft.json) and [checker](../scripts/check_messaging_plan.py).
