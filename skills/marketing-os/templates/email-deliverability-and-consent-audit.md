# Email domain, list permission, unsubscribe and deliverability audit

Use [Deliverability 9E](../workflows/09e-email-deliverability-and-list-health.md) and [email sender reference](../references/email-deliverability-consent-and-reputation.md). **Only call an item "verified" after inspecting live evidence.**

## Sender and provider
- Brand / actual sending domain and From / ESP and account:
- Personal Gmail daily send volume and bulk sender history (same organizational domain):
- Domains/IPs for marketing vs transaction; country/recipient mix:
- Reports accessible (Postmaster, ESP, actual headers/DNS, Yahoo etc):
- Date/observer/approval owner:

## Technical verification
| Check | Required by whom and when | Evidence (DNS/header/provider) | Verified/failed/unknown | Owner and exact fix |
|---|---|---|---|---|
| SPF | | | | |
| DKIM | | | | |
| DMARC, policy and visible-From alignment | | | | |
| PTR/reverse DNS, TLS, RFC 5322 headers | | | | |
| One-click unsubscribe, RFC 8058 where required | | | | |
| Visible unsubscribe/body footer and physical address | | | | |
| Google Postmaster spam complaint/domain reputation | | | | |
| Yahoo/other mailbox rules | | | | |
| ESP suppression across all integrations | | | | |

## Consent/source and list health
| Source/segment | Relationship and channel | Consent/legal basis and proof | Jurisdiction | Last useful engagement (click/order) | Bounces/complaints/opt-outs | Action |
|---|---|---|---|---|---|---|

- US CAN-SPAM business-to-business coverage and transactional primary-purpose assessment:
- UK/other local opt-in/soft-opt-in basis and separate SMS permissions:
- List acquisition/import policy and proof of subscriber expectations:
- Unsubscribe processing/propagation verified across Shopify/Klaviyo/other ESP:
- Stale/dormant/sunset or repermission strategy without unauthorized sends:
- Apple MPP open-rate distortion explicitly noted:
- Provider suppression, complained/hard bounced addresses and response owner:

## Diagnostic decision
| Incident | Actual evidence, period | Technical vs audience vs creative vs reporting hypothesis | P0/P1/P2 corrective action | Verify after |
|---|---|---|---|---|

- Stop/pause impacted promotion? why:
- Changes requiring DNS/ESP owner or legal review:
- Render/links/identity test addresses (internal authorized only):
- Send approval and monitoring:
