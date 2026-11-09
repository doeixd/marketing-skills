# Marketing context file — `.marketing-context/brand-truth.md`

A single, persistent, evidence-labeled record of brand and offering truth that every Marketing OS workflow reads **before** generating strategy or copy, and updates **after** a workflow produces approved facts. It removes re-entry of the same brand facts across tasks and keeps copy, SEO, ads, email and creative consistent.

## Rules

1. **Location:** `.marketing-context/brand-truth.md` at the root of the user's project (not inside this skill). One file per brand; for multi-brand projects use `.marketing-context/<brand-slug>.md`.
2. **Read first.** If the file exists, load it before any workflow step. Do not re-ask for facts it already records unless they are marked stale or the user signals a change.
3. **Create only with consent.** If it does not exist and the task needs brand facts, offer to create it from this template (brief intake, or [Workflow 3A](../workflows/03a-brand-discovery-and-messaging.md) / [1A](../workflows/01a-offering-discovery-and-marketing-plan.md) for depth). For a one-off quick rewrite, skip the file.
4. **Every row carries a status:** `verified`, `buyer-reported`, `inferred`, `hypothesis`, or `unknown`, plus a source and date. Only `verified` facts may appear as claims in publishable copy.
5. **Missing facts stay missing.** Write `[NEEDS INPUT: <what, why it matters>]` rather than a plausible guess. Never fill a gap with a fabricated price, statistic, testimonial, credential or policy.
6. **Freshness:** time-sensitive rows (price, offers, stock, shipping, policies, platform rules) need a `checked_at`; treat anything older than 90 days, or past an explicit expiry, as stale and re-verify before publishing.
7. **Approval:** record who approved voice rules and claim wording. Agent-drafted rows stay `hypothesis` until approved.
8. **No secrets or customer PII.** Never store credentials, API keys, customer lists or personal data here.

A filled-in [example](../examples/brand-truth-example.md) shows the expected level of detail. Check a file with `python scripts/check_context_file.py <path>` ([script](../scripts/check_context_file.py)): it flags invalid statuses, stale or expired rows, open `[NEEDS INPUT]` markers and stored secrets.

## Template

```markdown
# Brand truth — <Brand name>
Last reviewed: <YYYY-MM-DD> · Approved by: <name/role or [NEEDS INPUT]>

## 1. Identity
| Field | Value | Status | Source | Checked |
|---|---|---|---|---|
| Legal / trading name | | | | |
| Category the buyer would use | | | | |
| Markets / countries / languages | | | | |
| One-sentence positioning | | | | |
| Brand perspective / point of view | | | | |

## 2. Offerings (one row per product/service line)
| Offering | Verified facts (specs, materials, inclusions) | Price & offer | Shipping / returns / guarantee | Status | Checked |
|---|---|---|---|---|---|

## 3. Buyers and buying situations
| ID | Trigger / occasion | Buyer vs user/recipient | Job (When…, I want…, so I can…) | Alternatives incl. doing nothing | Status | Evidence |
|---|---|---|---|---|---|---|

## 4. Claim register (only `verified` rows may be published)
| Claim ID | Exact approved wording | Proof / source | Restrictions (markets, channels, qualifiers) | Status | Expires |
|---|---|---|---|---|---|

## 5. Competitive alternatives
| Alternative | Why a buyer might choose it | Our point of difference | Evidence | Status |
|---|---|---|---|---|

## 6. Objections and real limitations
| Objection | Real limitation? | Honest response / fix | Evidence |
|---|---|---|---|

## 7. Voice rules
- Sounds like: <3–5 traits, each with a "this, not that" example>
- Vocabulary to use (from real customer language):
- Words/claims never to use:
- Formality, person, humour, emoji, regional spelling:

## 8. Distinctive brand assets
Name treatment, logo, colours, typography, packaging, recurring visuals, sonic cues, taglines.

## 9. Compliance and channel constraints
Regulated claims, required disclosures, platforms/markets with restrictions, consent sources for email/SMS (describe, never list contacts).

## 10. Measurement anchors
Primary business KPI, source of truth for orders/leads, known tracking gaps, contribution margin or allowable CPA (or [NEEDS INPUT]).

## 11. Open questions
- [NEEDS INPUT: …]

## Change log
| Date | Change | By | Workflow |
|---|---|---|---|
```
