# Meta Ads campaign setup: objective, signal quality, audiences and feedback loops (reviewed 2026-11-09)

Meta delivery is largely automated: the system finds people likely to take **the action you tell it to optimize for**. Your main levers are therefore the optimization event, the quality and volume of the conversion signal you send back, hard constraints (geography, exclusions, budget), the creative, and the landing page. Settings and names change often; confirm in Ads Manager and [Meta Business Help](https://www.facebook.com/business/help) before launch. Third-party figures below are labeled as such.

## 1. Optimize for the outcome you actually want

- Pick the objective and performance goal **closest to the real business outcome**: Sales → purchase (or purchase value) for ecommerce; Leads → a *qualified* lead event (ideally a CRM-qualified or offline conversion) rather than a raw form submit; app promotion → a meaningful in-app event.
- **You get what you optimize for.** Optimizing for link clicks, landing-page views or engagement buys clicks, views or engagement, often from people unlikely to buy. Use upper-funnel goals only for deliberate brand/reach work with appropriate [brand metrics](marketing-effectiveness.md).
- **Value optimization** (maximize purchase value, or a ROAS goal) needs accurate `value` and `currency` on every purchase, ideally contribution-aware.
- Write the chosen objective, performance goal, conversion event, attribution setting and the rationale into the [campaign blueprint](../templates/meta-ads-campaign-blueprint.md).

## 2. Signal volume: give the system enough events to learn

- An ad set exits Meta's **learning phase** after roughly **50 optimization events within 7 days** of its last significant edit; below that it shows "Learning limited". Third-party reports of lower thresholds exist but are anecdotal, so check the ad set's delivery status rather than assuming. A significant edit (budget jump, targeting, creative, bid or event change) can restart learning.
- If the deepest event (purchase) is too rare for the budget, choose deliberately among: **consolidating** ad sets/campaigns so events pool; raising budget if the economics allow; optimizing one step up the funnel (e.g. add-to-cart or initiate checkout) **as a documented, temporary compromise** whose purchase rate you monitor; or not running conversion campaigns yet.
- Rough feasibility check: `weekly budget ÷ expected cost per optimization event ≥ ~50` per ad set. If it fails, don't split budget across many ad sets.

## 3. Conversion signal quality: send accurate, deduplicated, rich events

Detail lives in [measurement](measurement-pixels-ga4-and-attribution.md), [8E instrumentation](../workflows/08e-event-instrumentation-and-conversion-qa.md) and the [2026 API notes](2026-platform-data-api-updates.md). Minimum before scaling:

- **Pixel + Conversions API** for key events, with a shared `event_id` per event so browser and server copies **deduplicate**; verify in Events Manager (deduplication and event match quality).
- **Customer information parameters** sent where consent and law allow (hashed email/phone, external ID, `fbp`/`fbc`, IP/user agent from the server). More matched parameters generally improve match quality; never send data the customer hasn't consented to share.
- **Accurate values:** purchase value/currency matches the order; no double-firing on thank-you page reloads; test orders and refunds excluded or adjusted.
- **Reconcile** Meta-reported purchases against store orders weekly. A persistent gap is a tracking problem to fix before judging creative.

## 4. Hard constraints first, then audience inputs

- **Geography is a hard control.** Include only countries/regions you actually sell and ship to, at prices and in languages you support. Leaving "worldwide" or broad regions on can spend budget in low-cost markets that never buy. Meta location targeting reaches people *living in or recently in* a location; check whether that matches the offer (local services, regional shipping).
- Other hard controls: minimum age, language where it matters, **exclusions** (recent purchasers, existing customers for acquisition campaigns, employees), and placements only when there is a creative or brand-safety reason.
- **Advantage+ audience** treats many inputs (age ranges, detailed targeting, custom and lookalike audiences) as **suggestions**, not fences, depending on the performance goal (practitioner reports; verify for the goal you use). Put what *must* be true in controls; treat the rest as hints.

## 5. First-party audiences: custom and lookalike

- Upload **consented** customer lists (purchasers, high-value or repeat customers, subscribers) as custom audiences for exclusion, retention or as lookalike seeds. Follow [8G audience activation](../workflows/08g-audience-activation-and-utm-governance.md): lawful basis, Meta's Custom Audience terms, hashing, suppression and deletion propagation. Marketplace buyer data (e.g. Amazon/Etsy) usually may not be uploaded.
- **Seed quality beats size:** a seed of best customers (high CLV, low returns) usually beats "all emails". Meta's guidance has historically suggested at least a few hundred to a thousand people; check current minimums.
- **Test lookalike scales** (e.g. 1%, 1–3%, 5–10%) and broad/Advantage+ audience against each other as distinct hypotheses with enough budget for each. Expect broad delivery to compete well when the conversion signal is strong.

## 6. KPIs: decide what matters, and don't trust platform numbers alone

- Ecommerce defaults: **ROAS** (on revenue *and* on contribution margin), **CAC / cost per new customer**, and **customer lifetime value**, so you know the CAC you can afford and how fast it pays back. Define each in the [KPI dictionary](../templates/marketing-measurement-and-kpi-dictionary.md).
- Meta's figures are **platform-attributed**: they use Meta's attribution window and modeling, overlap with other channels' credit, and can be off by enough to change decisions. Compare against store orders, new-vs-returning customer counts, and blended metrics (total revenue ÷ total ad spend; total new customers ÷ total spend). Use [incrementality tests](attribution-incrementality-experimentation-and-mmm.md) when budget decisions are large.

## 7. Feedback loops beyond the dashboard

- **Session recordings and heatmaps** (e.g. PostHog, Microsoft Clarity, Hotjar) on ad landing pages show what visitors look at, where they hesitate and where they leave. Mask inputs and personal data, honor consent, and treat recordings as clues for [CRO](cro-research-and-experimentation.md) hypotheses, not proof.
- **Ask non-buyers why**, respectfully: an exit-intent or scroll-depth survey, an on-page one-question poll, or a post-purchase "what almost stopped you?" question. **Never hijack the back button** or trap navigation. It angers visitors, is fragile, and since June 15, 2026 is a [Google Search spam-policy violation](https://developers.google.com/search/blog/2026/04/back-button-hijacking) that can trigger demotion or manual action.
- **Monitor ad comments** daily during launch and after scaling. A single repellent, false or unanswered comment ("scam", "never arrived") pinned near the top can sink an ad's performance. Answer genuine questions, fix real service problems, and hide or delete only spam, abuse or policy-violating comments per a written moderation policy. Never delete legitimate criticism to fake sentiment, and never seed fake positive comments. Note comment themes in the evidence ledger as `buyer-reported`.

## 8. Agent access to the Meta Marketing API

Agents can read insights and manage campaigns through the [Meta Marketing API](https://developers.facebook.com/docs/marketing-apis/) directly or via connectors such as [Composio's Meta Ads toolkit](https://composio.dev/toolkits/metaads) (MCP/CLI; OAuth). Rules:

- Start **read-only** (insights, configuration audits, comment review). Create, edit, pause, budget or audience-upload actions are external writes needing per-action human confirmation ([SKILL.md](../SKILL.md) principle 20), with spend limits set in the account itself.
- Verify each tool's actual behavior (`composio tools info <tool>` or the API reference) before use, since connector tool descriptions can be wrong. Use a dedicated system user/app with least-privilege permissions; never paste tokens into chat or the context file.
- Log every change (who approved, before/after, time) in the [experiment decision log](../templates/experiment-decision-log.md).

## Sources

- Meta: [Business Help Center](https://www.facebook.com/business/help), [Marketing API](https://developers.facebook.com/docs/marketing-apis/), [Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api/), [Meta Blueprint](https://www.facebookblueprint.com/).
- Learning phase (third-party summaries of Meta guidance): [PPC Land: Meta on ad sets under 50 weekly conversions](https://ppc.land/meta-says-ad-sets-under-50-weekly-conversions-cost-28-more-per-purchase/), [Jetfuel: learning phase 2026](https://jetfuel.agency/what-is-the-meta-ads-learning-phase-how-to-exit-it-faster-in-2026/).
- Audience controls vs suggestions (practitioner): [Jon Loomer: targeting suggestions](https://www.jonloomer.com/targeting-suggestions/), [Jon Loomer: Advantage+ audience best practices](https://www.jonloomer.com/advantage-plus-audience-best-practices-guide/).
- [Google: back button hijacking spam policy (April 2026)](https://developers.google.com/search/blog/2026/04/back-button-hijacking).
- Practitioner input: tips from an ecommerce operator (November 2026) informed sections 1–8; each was checked against the sources above.
