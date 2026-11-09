# Workflow 4D — Landing pages: type → message match → first screen → sections and copy → design → build → test

**Trigger:** "Write/build/design a landing page", a campaign needs a destination, a new product, lead-magnet, waitlist, comparison, pricing or advertorial page, "review/tear down this landing page", or CRO found the existing page can't be fixed by small changes.

**Place:** Optional specialist in [Stage 4](04-offer-and-conversion.md). [4A CRO](04a-conversion-rate-optimization.md) diagnoses funnels; this builds or reviews one page. Load the [landing page reference](../references/landing-page-design-and-copy.md) and the [marketing context file](../templates/marketing-context.md). Outputs: a [landing page brief with full copy](../templates/landing-page-brief.md) ([worked example](../examples/landing-page-brief-example.md)); for a review, a [scorecard](../templates/landing-page-review-scorecard.md). Built HTML is checked with the [page checker](../scripts/check_page_meta.py) ([skeleton](../examples/landing-page-skeleton.html)).

**Reviewing an existing page?** Do step 1, then score it with the scorecard and return prioritized fixes. Rebuild only if the page type, promise or offer is wrong.

## 1. Fix the rule of one

Write one line each: the **one reader** (buyer situation and awareness lens), the **one promise**, the **one offer** (with price and terms), the **one action**, and the traffic source with the exact words and image that earned the click. Unknown offer, price or terms → `[NEEDS INPUT]` (blocking). Different audiences or promises get separate pages or variants.

## 2. Choose the page type and length

Pick from the [page-type table](../references/landing-page-design-and-copy.md#2-choose-the-page-type): click-through, lead capture, long-form, the product page itself, advertorial/listicle, comparison, pricing or waitlist. For warm, product-aware traffic, first ask whether the existing product page is the right destination. Length follows the number of real questions the buyer still has. Advertorials and listicles must carry an "Advertisement" label above the headline.

## 3. Gather the raw material

Verbatim customer language for the problem, outcome and objections; verified claims and proof assets with permission; real product visuals; the competing alternatives. If there is no customer language yet, mark headline and objection copy `hypothesis` and plan a message test (step 8).

## 4. Design the first screen

Draft three to five headline options from customer language, then choose with the tests in the [reference](../references/landing-page-design-and-copy.md#4-above-the-fold): does it continue the ad's promise, make sense with no logo, and say something a competitor couldn't? Then write the subheadline (how, for whom), choose the product visual, one checkable proof cue, and a call to action that names the outcome with a reassurance line under it. A stranger should be able to say what is offered, for whom, and what to do after five seconds.

## 5. Plan the sections and write the copy

Order sections by the buyer's next questions and drop any this buyer doesn't need:

| # | Section | Answers |
|---|---|---|
| 1 | Hero | What is it, for whom, why care, what do I do? |
| 2 | Proof strip | Can I trust this? |
| 3 | Problem / desired outcome | Is this for my situation? (buyer's words; no manufactured pain) |
| 4 | How it works / what you get | What exactly happens? (fact → benefit, each shown) |
| 5 | Evidence | Does it work for people like me? (proof matched to the promise) |
| 6 | Offer and price | What does it cost and include, in total? |
| 7 | Objections / FAQ | What might stop me? (honest about limits) |
| 8 | Risk reversal | What if it's wrong for me? |
| 9 | Final call to action | What now? |
| — | Footer | Who is behind this? (identity, contact, privacy, terms, disclosures) |

Write every block in final wording, each claim tagged with its evidence ID. Plain words, short sentences, specifics over adjectives. Forms ask only for what the next step needs and say what happens after submitting.

## 6. Set the design direction

Specify, don't decorate: the reading order and what is most prominent on each screen; the ad-to-page design match (image, colors, product shot); brand palette and type from the context file; the phone layout of the first screen; the form layout (labels above fields); imagery list with alt text; motion, if any, and why. Avoid the generic template look described in the [design notes](../references/landing-page-design-and-copy.md#8-design). If a design or frontend skill is available, hand it this section plus the copy; it must not change claims or wording.

## 7. Build requirements

- **Phone first:** promise, visual and button visible without scrolling; no pop-up on arrival.
- **Speed:** good Core Web Vitals (LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1); sized and compressed hero image that is not lazy-loaded; scripts deferred.
- **Accessibility:** WCAG 2.2 AA basics: one `h1`, ordered headings, alt text, contrast, labelled fields, keyboard and focus.
- **Metadata:** title, description, canonical, Open Graph and Twitter tags, structured data matching visible content; `noindex` for paid-only duplicates.
- **Tracking and consent:** primary and secondary events fire once; consent respected; UTMs kept ([8E](08e-event-instrumentation-and-conversion-qa.md)).
- **Confirmation page:** what was received, what happens next and when, one useful next step.
- **No dark patterns** (fake urgency, hidden fees, pre-ticked boxes, navigation traps).

Run `python scripts/check_page_meta.py <page.html>` and report its output.

## 8. Test before launch

Score the draft with the [scorecard](../templates/landing-page-review-scorecard.md). Then use what the situation allows: a five-second test with outsiders; a message test with 12–20 people who match the buyer; a usability run on phones; a proofread of every claim against its source; a real-device test of the whole path including the confirmation page. Publishing needs owner approval.

## 9. Launch and learn

Watch conversion by source and device, recordings, form drop-off, and the quality of what converts (qualified leads, orders, refunds). A/B test only where conversions are plentiful, and test big differences first (offer, promise, page type, proof). Feed findings to [4A](04a-conversion-rate-optimization.md) and the context file.

**Stop conditions:** no verified offer, price or terms; claims without proof; an advertorial the owner won't label as advertising; no way to record the conversion.
