# First-party audiences, datasets, reverse ETL, suppression and UTM brief

Use [Audience/UTM Workflow 8G](../workflows/08g-audience-activation-and-utm-governance.md), [identity guidance](../references/campaign-utm-and-identity-governance.md) and [Data Manager/Meta sources](../references/2026-platform-data-api-updates.md).

## Purpose and scope
- Real marketing question, buyer/offer and intended outcome (qualification, exclusion, retention, measurement):
- Audience type: Meta Website Custom Audience / Customer List / Lookalike / Google Customer Match / CRM segment / offline conversion:
- Dataset/pixel vs ad account vs audience object IDs (verified live):
- Account permissions; user/owner, legal/data-protection approvals:
- Source, lawful collection purpose, country, marketplace restrictions and consent:
- Why this membership set may be used for **this** ad destination (not simply email opt-in):
- Restricted or sensitive category/age policies and anti-discrimination review:

## Exact membership logic
| Step | Source/system and grain | Predicate and source date | Purpose/consent rule | Suppression/erasure | Expected count (observed only) | Error condition |
|---|---|---|---|---|---|---|
| Seed/include | | | | | | |
| Remove recent purchasers | | | | | | |
| Remove opt-outs/legal restrictions | | | | | | |
| Product or market eligibility | | | | | | |

- Audience version/name, expiry/membership window, refresh and deletion SLA:
- Destination supported identifiers, normalizing/hash policy, secure transport:
- Media spend owner; platform terms and eligible audience minimum checked:
- Test/sandbox-only dry-run and destination diagnostics:
- No direct Etsy/Amazon buyer audience import unless platform explicitly permits and legal basis established.

## URL/campaign mapping
| Channel/publisher | Final URL | utm_source | utm_medium | utm_campaign | utm_id | utm_content | utm_term | Platform click tag/redirect QA |
|---|---|---|---|---|---|---|---|---|

- Case/GA4 cost-data import mapping, Google auto-tag and platform macro check:
- No PII/contact identifiers, invalid credentials or secret tokens in URLs:
- Amazon Attribution tagging if landing on Amazon (UTMs aren't equivalent):
- Internal links must not override external acquisition attribution:

## Activation QA and outcomes
- Eligible count matches source; privacy deletion/opt-out propagates:
- False inclusions sample checked by authorized owner without exposing customer identities:
- Uploaded / matched / reachable counts **observed**, not assumed:
- Ad-platform results kept separate from commerce-ledger orders and incremental lift:
- Internal approval of audience scope, live upload, ad delivery and spending: **pending until explicit**:
