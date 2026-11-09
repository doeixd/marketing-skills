# Workflow 5M — Marketplace marketing: Amazon and Etsy listings, search and ads

**Trigger:** Amazon or Etsy listing optimization, titles/bullets/tags, A+ content, marketplace SEO, Sponsored Products/Brands, Etsy Ads or Offsite Ads, low marketplace conversion, ACOS/TACOS questions, or launching a product on a marketplace.

**Place:** Optional specialist in [Stage 5](05-channel-and-campaign.md). Data extraction and finance reconciliation are in [8F](08f-marketplace-etl-and-reconciliation.md); this workflow is about selling *on* the marketplace. Marketplace rules change frequently: items marked *(reported)* are from third-party sources as of November 2026 and must be confirmed in Seller Central or Etsy's seller handbook.

## 1. Establish economics and eligibility

Per SKU: price, landed cost, marketplace fees (referral/transaction, fulfilment, payment, ads), returns, and contribution margin. Confirm category approval, restricted-product rules, and (Amazon) Brand Registry status, which gates A+ content, Sponsored Brands, Brand Analytics and Vine.

**Deliverable:** per-SKU contribution table and the break-even ad cost of sale.

## 2. Research how buyers search and choose

Use the marketplace's own data first: Amazon Brand Analytics (Search Query Performance, top search terms), search-term reports from ads, Etsy Stats and search analytics, the autocomplete suggestions, and competitor listings' questions and reviews. Extract buyer vocabulary, the attributes buyers filter on, and the objections in 1–3 star reviews of the category ([buyer research](../references/buyer-research.md)).

## 3. Build the listing

| Element | Amazon | Etsy |
|---|---|---|
| Title | *(Reported, from a June 10, 2026 Seller Central notice)* since July 27, 2026 titles outside media categories are limited to 75 characters including spaces, with further detail in a separate Item Highlights field; Amazon may propose or apply replacement titles, and limits can differ by marketplace and category style guide, so follow the style guide shown in Seller Central. Lead with brand, product type and the deciding attribute. | Clear, readable description of the item first; Etsy has moved away from keyword-stuffed titles. |
| Structured data | Complete every relevant attribute and backend search term; variations set up correctly. Attributes increasingly feed AI shopping assistants (Rufus), so specific, factual, question-answering content matters. | All 13 tags, attributes, categories, materials, personalization options. |
| Body | Five bullets: one buyer benefit each, grounded in a verified fact. A+ content for comparison, use and proof. | Description that answers size, materials, process, shipping and care in the first lines. |
| Images/video | Main image compliant (product on white); then scale, use, detail, what's included, comparison; video where available. | First photo decides the click; show scale, variants, process; video. |
| Trust | Accurate delivery, returns; reviews only through permitted means (Amazon Vine, the "Request a Review" button). | Shop policies, about section, processing times, Star Seller criteria. |

Claims must match the product exactly and comply with category rules (health, safety, environmental and comparative claims are heavily restricted). Use the [claim register](../templates/marketing-context.md).

## 4. Advertise where it pays

- **Amazon:** start with Sponsored Products on the best-converting listings; harvest converting search terms from automatic into manual campaigns and add negatives; add Sponsored Brands and Sponsored Display once Sponsored Products is profitable. Judge by **TACOS** (ad spend ÷ total sales) and contribution, not ACOS alone, because ads also lift organic rank. Don't advertise listings that are out of stock, lack reviews or lose the featured offer.
- **Etsy:** Etsy Ads promote listings inside Etsy at a daily budget; advertise proven listings. **Offsite Ads** are run by Etsy on external sites: the fee is charged only on attributed orders, *(reported)* 15% for shops under US$10,000 trailing-12-month sales (opt-out allowed) and 12% above (mandatory), capped per order. Build that fee into pricing.
- **External traffic:** use Amazon Attribution links or Etsy's Share & Save links to measure it. See [media plan](05p-media-plan-and-budget-allocation.md).

## 5. Stay inside the rules

Never buy, trade, gate or selectively solicit reviews; never ask for positive reviews in inserts or messages; never divert marketplace buyers to your own site using their marketplace contact data. These breach marketplace policy and the [FTC reviews rule](../references/reviews-referrals-loyalty-and-reputation.md), and risk account suspension. Marketplace buyer data generally may not be exported for ad audiences ([8G](08g-audience-activation-and-utm-governance.md)).

## 6. Measure and iterate

Track sessions, conversion rate (unit session percentage), search rank for priority terms, return reasons, review themes, ad cost of sale, TACOS and contribution per SKU. Change one major listing element at a time (Amazon's Manage Your Experiments supports split tests for eligible brands). Reviews and returns that reveal a product problem go to [commercial diagnosis](01-commercial-diagnosis.md), not into copy.

**Stop conditions:** negative contribution after fees at any plausible ad cost; unverifiable claims the category requires proof for; listing suppressed or policy-flagged.

**Sources:** [Amazon Seller Central Help](https://sellercentral.amazon.com/help/hub/reference/external/G10471), [Amazon Ads learning](https://advertising.amazon.com/library/guides), [Etsy Seller Handbook](https://www.etsy.com/seller-handbook), [Etsy fees policy](https://www.etsy.com/legal/fees/); Amazon 2026 title change as reported by [Zentail](https://www.zentail.com/blog/amazon-is-cutting-product-titles-to-75-characters-heres-what-sellers-need-to-know) and [Linnworks](https://help.linnworks.com/support/solutions/articles/7000100095-amazon-listing-title-character-limit-changes).
