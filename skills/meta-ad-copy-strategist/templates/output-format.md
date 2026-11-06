# Output format and machine-readable contract

For an in-depth task, default to a strategic memo followed by review-ready **drafts**. For small copy edits, give copy plus material claim/policy notes without a long report. Use JSON only if requested by the user or a downstream system expects it.

## Human-readable output

1. **Goal and marketing diagnosis** — activation vs brand vs hybrid; suspected communication vs product/offer/UX/availability issue; evidence level.
2. **Product facts and evidence** — verified specs, price/offer, policy, evidence IDs, significant unknowns.
3. **Buyer situation map** — trigger, desired progress, functional/emotional/social motives, push/pull/anxiety/habit, alternatives and reasons to decline.
4. **Market, brand and positioning map** — alternatives, parity/difference, buyer value, category, recognizable assets and purchase cues; keep it brief if the user only wants copy.
5. **Benefit and objection matrix** — feature → benefit → desired outcome; objection → real evidence → copy/visual/product-page response; drawbacks needing operational action.
6. **Angle shortlist** — distinct buyer motivation and experiment hypothesis for each candidate; reason to test; confidence separated from fact status.
7. **Copy units** — each `primary_text`, `headline`, `description` (if helpful), `cta`, `creative_brief`, `landing_page_check`, placement notes, evidence IDs.
8. **Claims/policy review** — risk and unresolved proof, including any blockers.
9. **Measurement plan** — primary commercial KPI, control, main change, validity caveats, next learning step.

## JSON schema example (informal)

```json
{
  "product": { "name": "Example vintage-inspired ring", "source_url": null },
  "objective": "purchases",
  "campaign_mode": "activation",
  "strategic_diagnosis": {"likely_constraint": "unverified", "other_possible_causes": ["sizing uncertainty", "product-page friction"], "status": "hypothesis"},
  "positioning": {"market_category": "vintage-inspired rings", "alternatives": ["plain band", "buying nothing"], "points_of_parity": ["size and product details"], "differentiated_value": "unverified", "status": "hypothesis"},
  "brand": {"name": null, "distinctive_assets": [], "category_entry_points": ["style refresh"], "association_status": "hypothesis"},
  "buyer_situations": [
    {
      "id": "buyer-1", "trigger": "Choosing an accessory",
      "job": "Find a ring that matches personal style",
      "motivations": ["aesthetics", "self-expression"],
      "push": "Wants a distinctive look", "pull": "Vintage-inspired detailing",
      "anxiety": "Uncertain about fit", "habit": "Keep current jewelry",
      "alternatives": ["Plain bands", "Buying nothing"],
      "status": "hypothesis", "evidence_ids": []
    }
  ],
  "evidence": [
    {"id": "E01", "claim": "Visible vintage-inspired detailing", "status": "verified", "source": "product photograph", "caveat": "Verify this SKU"}
  ],
  "angles": [
    {
      "angle_id": "A1", "name": "Personal style", "buyer_situation_id": "buyer-1",
      "motivation": "Aesthetic differentiation", "objection_addressed": null,
      "confidence": "low", "evidence_ids": ["E01"],
      "persuasion_mechanism": "aesthetic relevance", "brand_cue": null, "category_entry_point": "style refresh",
      "hypothesis": "Style-oriented copy may increase purchases versus feature-only copy when other variables are comparable."
    }
  ],
  "ads": [
    {
      "angle_id": "A1",
      "primary_text": "Vintage-inspired rings with character in every curve. Find a style that feels like yours.",
      "headline": "Explore Vintage-Style Rings",
      "description": "See all ring styles",
      "cta": "Shop Now", "creative_brief": "Photograph the ring's visible detail",
      "landing_page_check": "Verify design and inventory for the depicted SKU",
      "brand_cue": null, "category_entry_point": "style refresh",
      "evidence_ids": ["E01"], "risk_flags": [],
      "experiment_metric": "cost_per_purchase"
    }
  ]
}
```

### Data validation rules

- `evidence[].status`: `verified | buyer-reported | inferred | hypothesis | unknown`.
- `angle_id` and `evidence_ids` refer to identifiers in the same output.
- No unverified claim is promoted to `verified` merely because the model generated it.
- No numeric performance estimates are invented.
- `description` can be empty, because it is not reliably displayed across Meta placements.
- `cta` is a suggestion and must be checked against available Meta button labels in the target workflow.
- Any audience and motivation hypothesis remains labeled even when product features are verified.
- When producing multi-text variants, test all-pairs coherence or keep angle-specific combinations grouped as separate ad units.

For full research outputs, cross-check every angle against the strategic diagnosis, brand identifiers, category entry points and actual available proof. For a quick rewrite, omit the strategic sections not required by the brief.

Use `scripts/check_copy.py` for basic structural/length checks only. It cannot replace claim verification or a policy review.
