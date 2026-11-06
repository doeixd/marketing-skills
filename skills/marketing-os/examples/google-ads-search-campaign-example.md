# Worked Google Ads Search campaign — factual inputs → intent → RSA → measurement

**Fictional illustration, not an actual advertiser or live Google Ads account.** No actual Keyword Planner volume/CPC, ad spend, CPA, ROAS, sales, customer studies or verified product facts are available. This is a *planning and copy construction* example. Use [Paid Search 5G](../workflows/05g-paid-search-google-ads.md).

## Example 1: Vintage-inspired ornamental ring (fictional brand: Example Atelier)

**Verified only within this invented exercise:** the business sells a ring; site title says "vintage-inspired patterned ring"; product photograph shows detail. Prices, materials, shipping, returns, size, delivery, manufacturer and reviews are **unknown**. The brand name is a placeholder, not a real business.

### Buyer search demand hypotheses

| Candidate query | Job/intent | Match test | Landing | Reason / risk |
|---|---|---|---|---|
| vintage inspired ring | Browse/buy design | Phrase or exact *candidate*, semantic variants still apply | Specific ring PDP | Real style is relevant |
| ornate ring | Broad style consideration | Phrase candidate, monitor terms | Collection (only if real) or PDP | "Ornate" is a subjective fit, confirm photo |
| patterned ring | Design consideration | Broad *only with quality goal + review*, else phrase | Actual PDP | Might include unrelated materials/ceremony |
| example atelier ring | Brand navigation (fictional) | Exact/phrase candidate | Real brand collection | Monitor organic cannibalization and incrementality |
| ring resizing near me | Local service | **Do not target** unless resizing is actually offered | — | Customer wants a service not demonstrated here |

**Potential negative themes to investigate**, not automatic blanket exclusions: jewelry repair, free clipart, ring tattoo, career/jobs. Review real search terms and possible valuable overlaps before adding. Do not invent keyword-planner numbers.

### Draft campaign architecture
- **Goal:** product purchase, but must first validate proper purchase conversion and values.
- **Structure:** Search / product-style intent / one tightly relevant ad group → ring page. A separate brand campaign only if there's actual branded search and an incrementality rationale.
- **Bidding:** select after actual reliable purchase tracking, margins and spend risk are known; do not assert a target CPA/ROAS.
- **Geo:** only places business actually ships; verify presence vs interest defaults and target market.
- **Network and AI Max:** record Google Search / partners and AI Max matching, text customization, Final URL expansion individually. Since product attributes/policies aren't yet verified, do not enable broad URL/text expansion unreviewed.
- **Status:** drafts/PAUSED, no spend authorized.

### RSA candidate assets (all 30-character headlines, 90-character descriptions or fewer, verify in live editor)

Headlines:
1. "Vintage-Inspired Ring"
2. "Explore Patterned Details"
3. "Example Atelier" *(fictional brand placeholder)*
4. "An Ornamental Ring Design"
5. "Look Closer at the Pattern"
6. "See the Ring Up Close"
7. "Explore the Ring"
8. "Inspired by Vintage Style"
9. "Consider a More Detailed Look"

Descriptions:
1. "Explore this vintage-inspired patterned ring and view its design details."
2. "A closer look at an ornamental ring style. See the product before you choose."
3. "Prefer something with more visual detail? Explore the ring and its design."

The RSA does **not** claim sterling silver, bespoke craft, exclusive price, free delivery or warranty. Combinations should be reviewed for redundant/awkward meaning, not simply character count. A few phrases express possible aesthetic preference, not proven survey results.

**Sitelinks:** Use only **real** URLs, such as product details, an actual size guide or genuine returns page. Until those pages/terms are verified, supply a shot/info request instead of invented sitelinks. No fake "limited-time 25% off" assets.

### Launch blockers
1. Actual brand and voice, final URL, product materials/scale/sizes, price, stock, shipping, taxes and return policy.
2. Conversion action test purchase, transaction ID and net value; account primary/secondary goals.
3. Keyword Planner estimates and actual buyer query/competitor research.
4. Profitability limits, geography and budgets.
5. Human approval of all ad/AI-generated variations and URL expansion.

### Evaluation
Qualified purchases and net contribution are primary. Compare searches, query relevance, cost, mobile PDP/checkout, returns and actual demand. A high CTR or "Excellent" Ad Strength alone isn't a success. Test only after valid baseline.

## Example 2: B2B AI operations review service (hypothetical)

**Proposed, unverified service:** scoped workflow mapping and recommendation report. Do not claim the scope, fee, team credentials, savings, timeline or privacy terms are real until confirmed.

- **Who searches:** operations leader exploring "workflow automation consulting", potentially a distinct approval path from IT/security.
- **Competing choices:** build internally, software vendor, general consultant, postpone.
- **Query clusters:** "workflow process assessment consultant" (service intent); "AI automation for office tasks" (ambiguous research, assess); "free workflow template" (educational and likely less purchase-ready); real brand navigation if demand exists.
- **Positioning hypothesis:** diagnostic clarity before paying for implementation. Verify real scope.
- **Potential headline:** "Map Workflows Before Building"; no fabricated ROI.
- **Potential description:** "Explore an assessment approach to workflows, constraints and automation candidates." Only if an actual service page explains that approach.
- **Conversion goal:** qualified accepted lead or booked held consultation with CRM and actual economic value rather than raw form count. Review 2026 Google Data Manager offline conversion process and consent.
- **Landing:** explain scope, deliverables, exclusions, process, real credentials, case studies only with permission, pricing or discovery terms if real, contact form and data handling.

**What not to do:** target all terms containing "AI" with broad matching and no negatives; declare 10X savings; force the algorithm to optimize a form-submit that attracts unqualified leads; accept Google AI-generated ads without reviewing actual claims.

## Strategic comparisons

- **Google Ads Search** meets active search intent; hook is often specific relevance and evidence, not a sensational curiosity gap.
- **Meta/Instagram** may help buyers become aware of a style/brand before search; creative often demonstrates the product visually.
- **SEO/AEO** builds discoverable, truthful resource pages supporting both organic research and landing quality.
- **CRO** helps relevant visitors make the decision and complete it. All four benefit from a shared offering fact/claim ledger.

**Sample JSON for automated length validation:** [google-search-rsa-draft.json](google-search-rsa-draft.json). Run `python scripts/check_search_ads.py examples/google-search-rsa-draft.json`. Passing a structural linter does **not** mean Google Ads approval, campaign setup, tracked sales, or confirmed product claims.
