# Shopify Google/Meta product feeds, conversion pixels and ads QA

Use [Ads 5I](../workflows/05i-shopify-shopping-ads-and-tracking.md), [Google Search 5G](../workflows/05g-paid-search-google-ads.md) and [Shopify feed/measurement guide](../references/shopify-shopping-ads-feeds-and-attribution.md).

## Integration status
- Shopify domain/store/theme/plan and market:
- Installed Google & YouTube, Facebook & Instagram by Meta, other apps (verify):
- Google Merchant Center/Google Ads/Meta Business Manager/catalog IDs where permitted:
- Real ad objective: new/returning qualified purchases, stock and margin constraints:
- Consent/privacy and platform account permissions:
- Source export and verification date:

## SKU / variant feed matrix
| Shopify product/variant/SKU | Actual title/attributes | GTIN/MPN/brand | Shopify price/stock/currency by market | Google feed status/error | Meta feed status/error | Product landing/SEO | Resolution owner |
|---|---|---|---|---|---|---|---|

**No fabricated GTIN, sale price, inventory, review score or category.** Check product/variant identities and marketplace policy.

## Event and conversion integrity
| Customer event | Shopify pixel source/consent state | GA4 | Google Ads primary/secondary | Meta browser/server | ID/value/currency dedupe | Expected vs observed test | Issue |
|---|---|---|---|---|---|---|---|
| product viewed | | | | | | | |
| add to cart | | | | | | | |
| checkout started | | | | | | | |
| purchase/checkout completed | | | | | | | |
| returns/cancellations/quality | | | | | | | |

- Shopify September 2026 session definition and marketing report consolidation noted:
- Cross-domain, redirects, auto-tagging and UTM:
- Transaction IDs and duplicate server/browser purchases:
- Customer privacy/consent and app vs custom pixel sandbox:
- Store orders/refunds vs attributed channel reporting:
- Events used for automated bidding and false proxy risks:

## Campaign and economics
| Channel/campaign/product set | Search/buyer job | Verified angle/creative | Landing | Margin/acceptable acquisition cost | Budget permission | Outcome + guardrail |
|---|---|---|---|---|---|---|

- Google Shopping/PMax / brand/nonbrand safeguards and feed eligibility:
- Meta catalog/product set + matching IDs, dynamic creative/copy and placement:
- Paid Search keywords/negatives/RSAs when applicable:
- Actual ads/merchant/Meta policy and restricted category requirements:
- Launch authorization, spend ceiling, rollback and monitoring owner:
