# Workflow 7 — Preflight, approval and launch QA

**Trigger:** Campaign creative and product destination have been drafted; before publishing, spending, or changing a live campaign.

For a dated product or campaign launch across channels, plan it with [7A launch plan](07a-launch-plan.md); this workflow is the final pre-flight check.

## A. Hard-stop checks (must pass)

- **Authority:** User/business owner explicitly authorizes account changes, spend, schedule and final publication. A copywriting request is not permission to publish.
- **Product/offer:** Real product available, correct price/discount/terms, right SKU/variant, accurate stock and expected delivery.
- **Claims/policy:** Every material, guarantee, scarcity, health/financial, endorsement and performance claim verified. Check current Meta Advertising Standards and applicable laws. No sensitive personal-attribute assertions.
- **Destination:** Working URL, correct item/category, mobile use, clear price/returns/shipping, usable checkout.
- **Creative:** Final image/video rights and accurate product depiction; no invented testimonials; creator/music permissions and paid-relationship disclosures as applicable; legible overlays/captions, appropriate muted-viewing path, consistent brand cues; preview **every selected placement** with real account renderings. See [creative QC](../references/creative-quality-control.md) and [Meta placement playbook](../references/meta-placement-playbook.md).
- **Measurement:** Correct outcome event and domain, pixel/API configuration where applicable, event duplication diagnostics, order-source consistency, purchase value/currency and attribution assumptions; do a permitted test transaction where feasible.
- **Economics:** Budget, goal, economic guardrails, inventory capacity and who can pause spend are known.
- **Automated enhancements:** Review enabled Advantage+ transformations in each placement (SAY = text/offers/claims; SHOW = generated/expanded media, music or overlays; SEND = CTA/destination). Reject unapproved changed promises or misleading product depictions.
- **Creative manifest QA:** Run [creative manifest linter](../scripts/check_creative.py) when structured specs exist; **a passing script does not replace visual or rights review**. Record source/master/placement export versions.

## B. Pre-launch configuration record

| Field | Record |
|---|---|
| Campaign objective | Matches the actual business outcome; verify available settings |
| Campaign/ad set/ad IDs | Capture actual IDs once created |
| Audience/reach | Actual settings, targeting restrictions and exclusions as applicable |
| Placements | Selected surfaces and previews |
| Optimized conversion | Correct event and value source |
| Budget/schedule | Exact user-approved values |
| Creatives | Version IDs, concepts, final copy, visuals, destination |
| Disclosure/policy | Relevant category and claims review notes |
| Primary KPI & guardrails | Contribution, purchase, quality, delivery and budget risks |
| Test plan | What changes, control, duration, sampling caveats |
| Approval | Who approved what and when |

## C. During initial delivery

Monitor delivery and tracking sanity, spend versus authorized limits, site uptime, customer complaints and early order quality. Don't 'optimize' the campaign based solely on noisy first-day CTR or interrupt learning with constant changes. Follow current platform recommendations, actual scale and business urgency. Only take authorized actions.

**Comments:** review ad comments at least daily during launch and after budget increases. A single repellent, false or unanswered comment can sink an ad. Answer real questions, escalate service problems, and hide only spam, abuse or policy violations per a written policy; never delete legitimate criticism or seed fake praise. **Visitor behavior:** review consented session recordings and exit/intercept survey answers on the landing page; never hijack the back button ([why](../references/meta-ads-campaign-setup-and-signal-quality.md#7-feedback-loops-beyond-the-dashboard)).

## D. Stop/pause conditions

Explicitly define in advance, for example: broken checkout, expired offer, invalid tracking after inspection, deceptive claims discovered, overspending versus authorization, stockout, severe shipping issue or a sustained economic shortfall with adequate data. Avoid arbitrary universal dollar thresholds; use owner-approved limits.

**Handoff:** final configuration, source creative, approval, measurement baseline → [diagnosis and experiment](08-measure-diagnose-experiment.md). Consult [Meta Ads Manager learning](https://www.facebookblueprint.com/student/collection/507792-meta-ads-manager-learning) and [compliance reference](../references/compliance.md).
