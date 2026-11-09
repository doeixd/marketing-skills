# Landing page brief and copy

Produced by [Workflow 4D](../workflows/04d-landing-page-build.md); guidance in the [landing page reference](../references/landing-page-design-and-copy.md); filled-in [example](../examples/landing-page-brief-example.md). Every claim carries an evidence ID from the [claim register](marketing-context.md); unknowns are `[NEEDS INPUT: …]`.

## 1. Rule of one
| Field | Value |
|---|---|
| One reader (buyer situation, awareness lens) | |
| One promise | |
| One offer (price, terms) | |
| One action (and one optional secondary action) | |
| Traffic source and the exact words/image that earned the click | |
| Page type and why | |
| Success metric, current baseline, and the downstream quality measure | |

## 2. First screen
| Element | Final wording / asset | Evidence IDs |
|---|---|---|
| Headline (chosen) | | |
| Headline alternatives considered | | |
| Subheadline | | |
| Visual (real product, in use) | | |
| Proof cue (source and count) | | |
| Button text | | |
| Reassurance line under the button | | |

Checks: continues the ad's promise ☐ · makes sense with no logo ☐ · a competitor couldn't say it ☐ · five-second test passed ☐

## 3. Section plan and copy
| # | Section | Buyer question answered | Copy (final wording) | Visual / proof asset | Evidence IDs |
|---|---|---|---|---|---|
| 2 | Proof strip | | | | |
| 3 | Problem / outcome | | | | |
| 4 | How it works / what you get | | | | |
| 5 | Evidence | | | | |
| 6 | Offer and price | | | | |
| 7 | Objections / FAQ | | | | |
| 8 | Risk reversal | | | | |
| 9 | Final call to action | | | | |

Sections deliberately left out and why:

## 4. Form
| Field | Required? | Why the next step needs it | Input type / autocomplete |
|---|---|---|---|

What the visitor is told happens after submitting:

## 5. Design direction
| Aspect | Decision |
|---|---|
| Reading order and most prominent element per screen | |
| Design match with the ad (image, colors, product shot) | |
| Palette and type (from the context file) | |
| First screen on a phone (sketch or description) | |
| Imagery list with alt text | |
| Motion (if any) and its purpose | |

## 6. Confirmation page
What was received · what happens next and when · one next step · conversion event:

## 7. Metadata
| Tag | Content |
|---|---|
| Title (aim ≤ 60 characters) | |
| Meta description (aim ≤ 155 characters) | |
| Canonical URL / index or noindex | |
| Open Graph title, description, image | |
| Structured data type | |
| "Advertisement" label (advertorial/listicle only) | |

## 8. Test plan
| Method | Who / how many | Finding | Change made |
|---|---|---|---|
| Five-second test | | | |
| Message test | | | |
| Phone usability run | | | |

## 9. Build and launch checklist
- [ ] First screen shows promise, visual and button on a phone without scrolling
- [ ] One `h1`; headings in order; alt text; contrast; labels above fields; keyboard works
- [ ] Core Web Vitals in the good range on mobile; hero image sized and not lazy-loaded
- [ ] Conversion events fire once; consent respected; UTMs preserved
- [ ] No fake urgency, hidden fees, pre-ticked boxes or navigation traps
- [ ] Footer: company identity, contact, privacy, terms, disclosures
- [ ] `python scripts/check_page_meta.py <page.html>` run and output reviewed
- [ ] [Review scorecard](landing-page-review-scorecard.md) completed
- [ ] Full path tested on real devices, including the confirmation page
- [ ] Owner approval to publish: ___
