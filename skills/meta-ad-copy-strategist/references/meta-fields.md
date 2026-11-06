# Meta ad text fields, display, placements, copy structure

**Check current Meta Ads Manager previews and official placement specifications before publishing.** Field character counts frequently cited online are heuristic display targets, **not universal limits**. Objectives, placements, account features and creative formats change what is shown.

## Roles

| Field | Main purpose | Writing rule | Failure to avoid |
|---|---|---|---|
| Primary text | Set buyer relevance, core value, an angle or short argument | Put central value in opening sentence; can be longer if needed | Long prefatory fluff or hook with no product context |
| Headline | Express distinct product/benefit/offer/action | Make it legible alone and complementary | Repeating first sentence verbatim |
| Description | Optional supporting reassurance or detail | Treat as disposable; many placements suppress it | Carrying critical terms only here |
| CTA button | A supported Meta action for campaign type | Match objective and destination | Inventing unavailable button names |
| Image/video | Demonstrate what words claim | Ask what viewer can SEE vs what text must explain | Contradictory image and text |
| Destination | Complete the promise | Match product, pricing, availability, returns | Bait-and-switch or broken landing page |

## Practical display targets — advisory, not guarantees

| Field | Often-cited concise target | How to apply |
|---|---:|---|
| Primary text | ~125 characters to front-load message | Useful first-line target; long copy can be valid |
| Headline | ~27–40 characters | Prefer short enough to survive mobile/feed truncation |
| Description | ~25–30 characters | Optional support; do not rely on visibility |

The recommendations differ across sources and placements. Do not confuse "recommended length", "visible before truncation", and "Ads API field maximum". Do not hard-reject a draft based on this table. If the user provides an exact required character cap, enforce that cap in the final copy and count using the requested measurement (character/code point/grapheme as applicable). Emoji, Unicode and line breaks complicate counting and previews.

### Placement notes

- **Facebook and Instagram feeds**: primary text can sit above media; headline and supporting description may appear below media depending on ad type. Primary text is usually the reliable place to put central positioning.
- **Stories and Reels**: the experience is visual and full-screen; ad text and overlay are placement-specific. Shorten and ensure safe zones; consider spoken text/captions for video. Verify actual preview.
- **Right column / Audience Network / other placements**: different truncation or suppression patterns; never assume all text fields display.
- **Catalog/dynamic product ads**: ensure generated copy remains true for **every** product/variant in the set. Avoid a material or offer claim if only some SKUs qualify. Use product-specific data where supported.
- **Automated text variations / enhancements**: Meta may optimize which text appears or produce variants depending on enabled features. Review relevant settings, preview and brand/claim implications. Do not assume exact text is frozen without checking.

## Copy architecture: primary, headline, description should be additive

Example, hypothetical ring line:

> Primary: "Vintage-inspired rings with character in every curve. Find a style that feels like yours."
> Headline: "Explore Vintage-Style Rings"
> Description: "See all ring styles"

Three semantic jobs: create interest; identify selection; support browsing. No unverified assertions about metallurgy, handmade origin, discounts, shipping or bestseller status.

### Useful opening styles (choose based on evidence)

1. Direct benefit: product + concrete useful outcome.
2. Occasion: a realistic gifting or usage moment.
3. Product-specific feature: distinctive verified material, construction, size or functionality.
4. Buyer language: authentic expressed goal or problem (without implying sensitive personal attributes).
5. Contrast: fair difference from alternatives, supported.
6. Question: relevant and non-intrusive; avoid manipulative or personal-attribute questions.
7. Proof: verified review, quantitative specification or guarantee, with context and permissions.
8. Offer: actual deal/terms; no fictional countdowns.

Do not force PAS (Problem–Agitate–Solution), AIDA or WHY/WHAT/HOW on every product. Aspirational and decorative products may need no invented "pain". Match sophistication, awareness, and offer complexity.

## Combination safety

If Meta is to choose among multiple primary texts and headlines, perform **all-pairs coherence**: any primary text must make sense with any headline in the same group, and none may depend on an absent description. If variants need different offers, audiences, claims, or destination pages, separate them into distinct concepts/ad units.

## Example checks before handoff

- First sentence relevant and readable independently.
- Headline distinct but consistent with primary text.
- Description expendable.
- Actual CTA label supported by selected campaign, destination and Ads Manager.
- Creative displays the product/feature claimed.
- SKU/price/availability/policy true for each targeted variant.
- Product page directly verifies material claims and offer terms.
- Placement preview reviewed rather than guessed.
- Text enhancement settings reviewed if brand requires specific wording.

## Visual/communication adaptation required

The same wording is not the same ad across placements. For Feed, primary text and headline may carry more of the reasoning; for Stories/Reels the message should also be visible *in the creative*. Ensure overlays, spoken words, captions and fields **complement rather than repeat** one another. A `POV` or `GRWM` structure is not a replacement for an actual customer insight; see [platform idioms](platform-idioms-and-voice.md), [video storytelling](video-storytelling.md), and [placement playbook](meta-placement-playbook.md). Check music and creator rights, and review AI text/visual changes.

## Further reading

- [Meta Blueprint — Tips for Writing Effective Ad Copy](https://www.facebookblueprint.com/student/activity/293804-tips-for-writing-effective-ad-copy)
- [Meta Blueprint — Creative Diversification, May 2026](https://www.facebookblueprint.com/student/activity/707402)
- [Meta Ads Guide](https://www.facebook.com/business/ads-guide) — official specs; may require login; refer to current placement pages.
- [Rob Palmer — Meta ad-copy skill and reference](https://github.com/robpalmer99/claude-code-copywriting-skills/tree/main/ad-copy) — third-party examples; verify numbers against Meta.
