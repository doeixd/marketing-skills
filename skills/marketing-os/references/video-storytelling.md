# Reels, Stories and short-video production: hooks, scripts, direction

**Principle:** Stop *qualified* viewers, show the product and benefit early, and leave viewers with a truthful reason to act or remember the brand. There is no universal 'ideal 3-second hook' or compulsory video length. Use duration appropriate to the message, footage and placement.

## Story structures to choose from

| Format | First image / hook | Middle | End | Suitable for |
|---|---|---|---|---|
| Product reveal | Detail that shows what makes item distinctive | Wider context and scale | Full product + brand / next step | Design-led products |
| Demonstration | Show the task/result first | Show 1–2 steps or features | Real product + proof/CTA | Functional products |
| Question→answer | Ask an actual buying question | Show answer with evidence | Clarify trade-off and next step | Consideration/objections |
| Unboxing | Real sealed-to-open presentation | Item + actual contents | Brand/product | Gifting & fulfillment trust |
| Try-on/styling | Product in a genuine use context | Two complementary views | Size/materials/CTA | Apparel/accessories |
| Compare | State fair criteria | Demonstrate actual differences | Who each option suits | High-consideration shopping |
| Creator perspective | Real personal use case disclosed accurately | Honest experience/demonstration | Product and clear affiliation | Creator content with permissions |
| Sequenced Story | One idea per frame | Proof/variety/objection | CTA | 2–3-frame Story plan |

## Script template (illustrative 15-second treatment; timing is not a performance guarantee)

| Time | Visual | Spoken/audio | On-screen text | Brand/evidence |
|---|---|---|---|---|
| 0–2s | Real product/action or buying moment | Product-specific line/question | 3–6 readable words | Brand cue in context |
| 2–6s | Product detail/use | Explain observable benefit | Minimal reinforcement | Verified feature |
| 6–11s | Show scale, option, objection answer | Honest proof or comparison | One evidence cue | Actual materials/policy if present |
| 11–15s | Full product and handoff to website | Concrete next step | Short CTA consistent with app | Name, exact destination |

**Hook → setup → payoff → CTA** is a common practitioner beat structure for educational short video. Illustrative timing is roughly hook 0–3s (specific claim, question or visible result), setup to ~15s (context or problem), payoff to ~45s (the actual tip, demo or breakdown) and CTA in the final seconds (one low-friction action). Treat it as a starting storyboard, not a rule. Product-first openings and shorter cuts often fit commerce better.

15 seconds is *one storyboard option*; a 6-, 10-, 20- or 30-second execution may better serve another message. Don't pad duration with transitions or rush accessibility/disclosure text.

## Production direction

- **Opening:** Make opening *specific* ("Here's how the actual clasp works" vs "You won't believe this"). Product-first can be superior to a generic curiosity hook.
- **Shooting:** Request wide master footage plus close-ups, static product frames for thumbnails, clean backgrounds, a steady shot, product handling/scale, and adequate room for crop/safe zones. Keep unaltered masters.
- **Edit:** Cuts follow meaningful changes in angle/action/proof, not a mandatory beat interval. Remove pauses that add nothing; avoid jump-cut incoherence. Subtitles should be synchronized, readable and never claim things voiceover doesn't.
- **Sound:** Voiceover for explanation, genuine product sound for tactile evidence, approved music where suitable. Make silent viewing understandable. Do not assume trending platform music is licensed for ads.
- **Typography:** Use short readable overlays, clear high-contrast type, hold long enough for reading; don't place key text under UI rails/CTA. Test at actual phone size.
- **Closing:** Show a brand-linked product frame, truthful CTA, actual destination/offer. Don't defer *all* branding until the final moment.
- **Audio/visual accessibility:** Meaning should be available without sound when practical; captions for speech, don't hide essential information only in tiny lower-third overlays, avoid flashes/overly rapid edits.

## Programmatic (code-generated) video

Agents can now produce motion graphics, text overlays, captions, data visualizations and preview cuts from code, rendered locally. Examples are [Remotion](https://www.remotion.dev/) (React; check its license, since companies above a small size need a paid company license) and HeyGen's [HyperFrames](https://github.com/heygen-com/hyperframes) (HTML/CSS → MP4 with headless Chrome and FFmpeg; Apache-2.0, released April 2026, with installable agent skills).

- Use them for **overlays, typography, product-spec cards, captions, data stories and storyboard previews** built from real footage and approved claims.
- **Never render fabricated product features, fake UI, invented reviews or synthetic "customer" footage.** The rights and authenticity rules in [creative QC](creative-quality-control.md) apply to every rendered frame.
- Keep the composition source (code plus asset manifest) under version control with claim IDs, so a corrected fact can be re-rendered everywhere.
- Rendering locally is a read-only action. Cloud rendering or uploading to an account or ad platform is an external write and needs human confirmation.

## What 'native' means—and does not mean

Native-feeling means understandable within the platform's viewing rhythm and UI. It may involve handheld footage, product demos, direct address, on-screen captions or genuine creator perspective. It does **not** require low production quality, intrusive slang, staged reviews, artificial reaction shots, fake phone interfaces or unlicensed trending audio.

### Shot request structure

`shot_id | time | framing/camera | action | specific product fact shown | VO | overlay | brand cue | rights/source | crop/safe-zone notes`.

Ensure the first 1–2 frames already communicate category/use where possible. Film both a clean/no-text master and an approved-caption version for easier placement adaptation.

Sources: [Meta Blueprint Reels creation 2026](https://www.facebookblueprint.com/student/activity/694002); [Meta Blueprint Reels best practices](https://www.facebookblueprint.com/student/activity/289630-instagram-messaging); [Meta Blueprint Reels training 2025](https://www.facebookblueprint.com/student/page/641202); [Adobe/Meta Reels creative essentials](https://blog.adobe.com/en/publish/2024/11/04/unlock-potential-reels-best-practices-for-creative-success-using-adobe-creative-cloud).
