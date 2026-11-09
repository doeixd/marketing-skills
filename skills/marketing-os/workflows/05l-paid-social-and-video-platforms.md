# Workflow 5L — Paid platforms beyond Meta and Google Search: TikTok, Pinterest, YouTube/Demand Gen, LinkedIn, Microsoft

**Trigger:** TikTok Ads, Spark Ads, TikTok Shop/GMV Max, Pinterest Ads, YouTube or Demand Gen campaigns, LinkedIn Ads, Microsoft/Bing Ads, "which other ad platform should we try?", or expanding beyond Meta and Google Search.

**Place:** Optional specialist in [Stage 5](05-channel-and-campaign.md). The setup logic is the same as [5K Meta Ads](05k-meta-ads-campaign-setup-and-optimization.md): real outcome → clean signal → highest-intent event with enough volume → hard controls → authorized launch → judge against business truth. This workflow covers what differs per platform. Load the [platform reference](../references/paid-platforms-tiktok-pinterest-youtube-linkedin-microsoft.md); budget comes from the [media plan](05p-media-plan-and-budget-allocation.md).

## 1. Decide whether to add a platform at all

Add one only when (a) an existing channel is measured and near diminishing returns, or (b) the buyer clearly spends attention there and not on current channels, and (c) the budget covers the platform's minimum viable spend **and** the native creative it needs. A platform funded with leftovers and recycled creative usually fails for that reason, not because the platform is wrong.

| Buyer and offer | Usually worth testing |
|---|---|
| Visual, impulse-friendly consumer products; creator-led demand | TikTok |
| Planned, visual purchases (home, fashion, weddings, gifts, recipes, DIY) | Pinterest |
| Products needing demonstration or explanation; broad reach | YouTube / Demand Gen |
| B2B with a definable job title, seniority or company list | LinkedIn |
| Search demand already working on Google; older or desktop-heavy buyers | Microsoft Ads |

## 2. Signal first

Install the platform's browser tag **and** server-side API (TikTok Pixel + Events API; Pinterest Tag + Conversions API; Google tag + enhanced conversions; LinkedIn Insight Tag + Conversions API; Microsoft UET with consent mode), deduplicated with a shared event ID, with consent respected. Implementation: [8E](08e-event-instrumentation-and-conversion-qa.md). Catalog platforms need product IDs in events that match the feed.

## 3. Configure for the real outcome

Choose the objective and optimization event closest to the purchase or qualified lead, run the volume check (~50 events per ad set per week is the commonly cited threshold on TikTok and Pinterest as well; verify per platform), set locations and exclusions as hard controls, and keep the structure consolidated. Record the same fields as the [Meta campaign blueprint](../templates/meta-ads-campaign-blueprint.md), noting platform-specific settings from the reference.

## 4. Make native creative

Each platform has its own viewing behavior; resized Meta ads underperform. Use the [master asset pipeline](../references/social-media-strategy-hooks-and-community.md#master-asset--platform-transformation-pipeline) and the per-platform notes in the reference. Creator content needs written paid-usage rights and platform authorization (e.g. TikTok Spark Ads codes); AI-generated or significantly edited realistic content must be labeled where the platform requires it.

## 5. Launch, monitor, evaluate

[Launch QA](07-launch-qa.md) and explicit authorization apply. Compare platform-reported results with store orders or CRM-qualified leads and with blended CAC; view-through-heavy platforms (video, Pinterest) over- or under-credit depending on the window, so use the [incrementality methods](08b-attribution-incrementality-and-experiments.md) before large budget shifts. Decide scale / hold / cut by the rules set in the media plan.

**Stop conditions:** no verified conversion signal; budget below the platform's minimum viable spend; no capacity for native creative; product or claims restricted by the platform's ad policies.
