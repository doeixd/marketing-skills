# Meta Ads campaign blueprint

Produced by [Workflow 5K](../workflows/05k-meta-ads-campaign-setup-and-optimization.md). Unknowns are written `[NEEDS INPUT: …]`. This is a draft until an authorized person approves it in Ads Manager.

## 1. Goal and economics
| Field | Value | Status / source |
|---|---|---|
| Business outcome | | |
| Sellable markets (countries/regions) | | |
| Contribution margin per order | | |
| CLV (horizon, method) | | |
| Target CAC / break-even ROAS | | |

## 2. Signal readiness (hard stop if any critical row fails)
| Check | Pass/fail | Evidence |
|---|---|---|
| Pixel fires on key events | | |
| Conversions API live for key events | | |
| `event_id` deduplication verified in Events Manager | | |
| Customer-information parameters sent (consented) / match quality | | |
| Purchase value + currency accurate; no double-fires | | |
| Meta purchases vs store orders (last 7–28 days) | | |

## 3. Objective and optimization
| Field | Value | Rationale |
|---|---|---|
| Objective | | |
| Performance goal | | |
| Optimization event | | |
| Attribution setting | | |
| Expected cost per event | | |
| Events/week per ad set at planned budget (target ≈ 50) | | |
| Step-up-funnel compromise? Plan to return to purchase | | |

## 4. Controls and audiences
| Control | Setting |
|---|---|
| Locations included | |
| Locations excluded | |
| Exclusions (purchasers, customers, employees) | |
| Age / language (only if required) | |

| Audience test | Hypothesis | Seed / input | Scale | Budget share |
|---|---|---|---|---|
| Broad / Advantage+ audience | | | | |
| Lookalike A | | | 1% | |
| Lookalike B | | | 1–3% / 5–10% | |

Customer-list uploads: lawful basis, Custom Audience terms and suppression per [8G](../workflows/08g-audience-activation-and-utm-governance.md).

## 5. Structure and creative
| Campaign | Ad set | Budget | Ads (concept IDs) | Hypothesis | UTM |
|---|---|---|---|---|---|

Advantage+ creative enhancements allowed/denied: 

## 6. Monitoring plan
- Comment review cadence, owner and [moderation policy](../references/meta-ads-campaign-setup-and-signal-quality.md#7-feedback-loops-beyond-the-dashboard):
- Session recordings / exit survey tool (consent, masking):
- Spend limit (set in account) and stop conditions:
- Reporting: Meta-attributed vs store orders vs blended ROAS/CAC, weekly:

## 7. Approval
| Approver | Scope approved | Date |
|---|---|---|
