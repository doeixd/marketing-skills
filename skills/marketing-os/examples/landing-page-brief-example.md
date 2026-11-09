# Worked example: landing page brief for the Marguerite ring (hypothetical)

**Demonstration only.** Uses the hypothetical brand in the [context file example](brand-truth-example.md); no real data. It shows a filled-in [landing page brief](../templates/landing-page-brief.md) from [Workflow 4D](../workflows/04d-landing-page-build.md), including what stays blocked. The matching HTML is the [skeleton](landing-page-skeleton.html).

## 1. Rule of one
| Field | Value |
|---|---|
| One reader | B2: someone choosing a birthday or anniversary gift for a partner; solution-aware (wants jewelry, hasn't heard of this brand) |
| One promise | A ring that looks personally chosen, in a size you can get right and return if you don't |
| One offer | Marguerite ring, $68, gift box included, 30-day returns (C3) |
| One action | Choose a size and add to cart. Secondary: open the printable sizer |
| Traffic source | Instagram Reels ad: close-up of the engraving turning in daylight, overlay "The ring she hasn't seen everywhere" |
| Page type | Click-through page. The product page lacks the sizing help and gift framing this visitor needs |
| Success metric | Add-to-cart rate from ad traffic; baseline `[NEEDS INPUT: current product page rate]`. Quality measure: orders and return rate |

## 2. First screen
| Element | Final wording / asset | Evidence IDs |
|---|---|---|
| Headline (chosen) | A vintage-style silver ring she hasn't seen everywhere | C1 (silver); "vintage-style" per voice rules |
| Alternatives considered | "An ornate, vintage-style ring in new sterling silver" (clear but not gift-led); "The gift that looks like you searched for it" (could be any gift brand: failed the competitor test) | |
| Subheadline | New sterling silver with period engraving. Pick her size, or use our printable sizer. Ships in 2 business days. | C1, C2 |
| Visual | The same daylight close-up as the ad, then the ring on a hand | `[NEEDS INPUT: unedited on-hand photo]` |
| Proof cue | "Rated 4.7 by 41 customers" | `[NEEDS INPUT: confirm rating; 41 reviews verified]` |
| Button text | Choose her size | |
| Reassurance line | Free gift box. Returns within 30 days. | C3 |

Checks: continues the ad's promise ☑ · makes sense with no logo ☑ · a competitor couldn't say it ☐ (partly: "vintage-style silver" is specific, "hasn't seen everywhere" is not provable; keep as tone, don't present as fact) · five-second test ☐ (planned)

## 3. Section plan and copy
| # | Section | Buyer question | Copy | Asset | Evidence |
|---|---|---|---|---|---|
| 2 | Proof strip | Can I trust this? | Left out until the rating is confirmed | | |
| 4 | What you get | What exactly is it? | "Sterling silver, stamped 925. Whole sizes 5 to 10. Arrives in a green gift box, ready to give." | Stamp close-up; gift box photo | C1 |
| 5 | Evidence | Will she like it? | Two gifting reviews, quoted in full with first name and month | `[NEEDS INPUT: reviewer permission]` | B2 evidence |
| 6 | Offer and price | What does it cost in total? | "$68. US shipping calculated at checkout. Ships in 2 business days." | | C2 |
| 7 | FAQ | What might stop me? | "What if I don't know her size?" → sizer + exchange. "Is it an antique?" → "No. It's a new ring made in a vintage style." "Half sizes?" → "Whole sizes only; if she's between sizes, choose the larger." | Printable sizer | Objections table |
| 8 | Risk reversal | What if it's wrong? | "Return or exchange within 30 days. You pay return postage." | | C3 |
| 9 | Final call to action | What now? | "Give her a ring with some history in its design." Button: "Choose her size" | | |

Left out: problem section (the visitor already wants a gift), founder's note (no verified story yet: `[NEEDS INPUT]`), "handmade" (claim C4 unresolved).

## 4. Form
Size selector only (required to add to cart). No email capture before the cart.

## 5. Design direction
| Aspect | Decision |
|---|---|
| Reading order | Product image → headline → button. Button is the only solid-color element on the first screen |
| Design match | Same daylight macro shot and deep green as the ad's end card |
| Palette and type | Deep green, cream, silver-grey; serif wordmark and headings, plain sans body at 17px `[NEEDS INPUT: brand files]` |
| First screen on a phone | Image top half; headline two lines; button full width; reassurance under it |
| Imagery | Engraving macro; ring on hand in daylight; 925 stamp; gift box. Alt text describes each plainly |
| Motion | None |

## 6. Confirmation page
Standard order confirmation: item and size, delivery estimate, "Need to change the size? Reply to this email before it ships."

## 7. Metadata
Title: "Marguerite Vintage-Style Silver Ring | Example Ring Co." · Description: "A new sterling silver ring in an ornate period style. Whole sizes 5 to 10, ships in 2 business days, 30-day returns." · Canonical: the product URL; this page `noindex` (paid traffic only) · Structured data: Product with Offer.

## 8. Test plan
Five-second test with five people outside the business; phone run-through of size selection and checkout; proofread claims against C1–C3.

## Open items blocking launch
- `[NEEDS INPUT: unedited on-hand photo]`
- `[NEEDS INPUT: confirmed rating and reviewer permission]`
- Purchase event deduplication not verified (from the context file)
- Owner approval
