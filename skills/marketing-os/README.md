# Marketing OS

**Version 5.0 — an evidence-grounded marketing operating system, creative director and Meta ad-writing Agent Skill.**

A reusable [Agent Skills](https://agentskills.io/specification) package for understanding brands, offerings, markets, and buyers, then planning discovery, conversion and growth across organic search, AI answer engines, paid advertising, and customer experiences. It combines marketing fundamentals, JTBD research, competitive positioning, brand memory, perceived value and pricing, ethical persuasion and signaling, genuine objections, creative concepts, and experiments.

> **Core philosophy:** Think about **why customers would choose the offering**, **what else they could choose**, **what makes the promise believable**, **what prevents purchase**, and **whether copy is even the best intervention**. Then write selective, compelling ads.

## New in v5.0: Marketing OS identity

Renamed from **Meta Ad Copy Strategist** to **Marketing OS** (`marketing-os`) to reflect the full marketing operating system: brand and offering research, positioning, messaging, SEO/AEO/CRO, Meta creative and advertising, measurement, and growth. Installation paths and validation configuration have been updated; all existing workflows remain.

## New in v4.3: SEO, AEO and CRO foundations + workflows

The skill now covers **the full discovery-to-conversion path**, connecting brand and offering knowledge with organic search, AI answers and purchase experience:

- [SEO Workflow 5A](workflows/05a-seo-and-organic-search.md) and [SEO reference](references/seo-fundamentals-and-ecommerce.md): buyer search intent, index/crawl/JS rendering, site architecture, page copy, merchant product/offer schema and feeds, technical/mobile UX, Search Console and results.
- [AEO Workflow 5B](workflows/05b-aeo-ai-search-visibility.md) and [AI answer reference](references/aeo-generative-search-and-citations.md): reliable first-party answers, entity/product correctness, Google AI Search requirements, Bing Copilot citations and honest reporting limitations. No guaranteed inclusion or special llms.txt requirement.
- [CRO Workflow 4A](workflows/04a-conversion-rate-optimization.md) and [CRO reference](references/cro-research-and-experimentation.md): mobile product-page usability, price/trust/shipping/returns, checkout/form funnel issues, business outcome quality, statistically responsible experiments and guardrails.
- [Search and conversion audit](templates/search-and-conversion-audit.md), [CRO experiment brief](templates/cro-experiment-brief.md), [worked research-to-sale example](examples/seo-aeo-cro-from-offering.md), and an updated [annotated source library](references/sources.md).

**Core distinction:** SEO helps potential buyers find appropriate pages; AEO concerns useful, accurate answers and measurable citation surfaces; CRO reduces obstacles to making an informed, commercially valuable decision. They share the same verified product/brand evidence. These are optional specialist workflows within the original nine-stage system.

## New in v4.2: Offering discovery → buyer value → full marketing plan

The [Offering Discovery Workflow 1A](workflows/01a-offering-discovery-and-marketing-plan.md) investigates a **specific product, service, software tool, subscription or bundle** holistically: what is delivered, who buys or uses it, buying occasions, desired outcomes (including aesthetic or emotional desires), alternatives/status quo, features and buyer benefits, actual limitations, objections, assurances, pricing and economics, credible proof, brand fit and voice. It turns that research into a product-specific positioning proposal, evidence-backed selling-point bullets, short/long descriptions, headline and support-line banks, Meta ad concepts/visuals, product-page fixes, channel recommendations and testable go-to-market priorities.

- [Workflow 1A](workflows/01a-offering-discovery-and-marketing-plan.md) — questions → evidence → diagnosis → decisions → marketing outputs.
- [Research and planning framework](references/offering-research-and-marketing-planning.md) — JTBD, Strategyzer, alternatives-first positioning, service 7Ps, truthful assurances and offer economics.
- [Offering intake](templates/offering-discovery-intake.md) · [Dossier/marketing plan template](templates/offering-dossier-and-marketing-plan.md) · [Worked physical-product and service examples](examples/offering-discovery-to-marketing-plan.md).

Brand discovery is **optional when sufficient approved brand context exists**; otherwise gather a light brand scan or run 3A. The offering workflow is an optional sub-workflow of Stage 1, not an additional mandatory stage.

## New in v4.1: brand discovery → voice → reusable copy

The new [Brand Discovery Workflow 3A](workflows/03a-brand-discovery-and-messaging.md) investigates what a brand **claims**, **demonstrates**, and what buyers **perceive**. It analyzes brand perspective, personality, customer desires, selling points, verified advantages, tone, phrase patterns and limitations, then turns the findings into a coherent [message and copy library](templates/brand-messaging-library.md): benefit bullets, product descriptions, headlines, Meta primary texts and supporting descriptions, hooks, CTAs and channel-specific variants. The process includes a [discovery interview template](templates/brand-discovery-intake.md), a [voice/copywriting research guide](references/brand-voice-and-copy-system.md), and a [worked example](examples/brand-discovery-to-copy.md). No invented founder story, customer quotes, exclusive benefits, or fake scarcity.

## New in v4: creative direction, Instagram/Reels native formats and QA

The workflow now travels **from customer reason → creative concept → visual communication → platform-native production → validated ad draft**. The system knows how to ask for missing real footage instead of inventing product details, creator praise or offers.

- **Visual creative direction:** exact hero subject, framing, lighting, color fidelity, scale, layout, text hierarchy and recognizable brand cues. [Visual guide](references/visual-direction.md).
- **Platform-specific playbooks:** Feed 4:5, Stories/Reels 9:16, carousel 1:1, safe-zone templates, field visibility, and Meta's automated creative variations. [Placement playbook](references/meta-placement-playbook.md).
- **Reels scripts/communication:** native-feeling hooks, demos, unboxing, try-ons, `POV`, `GRWM`, voiceovers, audio, captions and sequential storytelling without forced slang or fabricated experiences. [Video](references/video-storytelling.md) · [Language/idioms](references/platform-idioms-and-voice.md).
- **Creator UGC/partnership rights:** authorized creator use, real testimonials, paid-audio licensing, clear paid endorsements and honest script direction. [Creator guide](references/creator-partnerships-and-rights.md).
- **Reviews and safeguards:** human QA, eight-dimension creative rubric, launch hard stops, product/visual integrity and additional creative-manifest linter. [Scorecard](templates/creative-review-scorecard.md) · [Linter](scripts/check_creative.py).
- **Production outputs:** [Creative director's brief](templates/creative-direction-brief.md), [storyboard/shot list](templates/shot-list-and-storyboard.md), [Reels example](examples/reels-creative-direction.md), and [example manifest](examples/creative-manifest.json).

These guidelines are current as of **November 6, 2026** and are not immutable Meta specifications. Live Ads Manager previews, rights and approval always win over a generalized reference.

## What is new in v3: executable marketing workflows

The package now answers **"what do we need to understand, what do we do with the answer, and what comes next?"** across product selection, research, positioning, offer, advertising, launch, measurement and growth.

- Start with the [**Marketing Operating System**](WORKFLOWS.md): a nine-workflow route map, inputs/outputs, readiness gates, decision tables and recurring operating rhythm.
- Use nine focused [**workflow runbooks**](workflows/01-commercial-diagnosis.md) for commercial diagnosis, buyer research, positioning/brand, offer/store readiness, channel strategy, creative production, launch QA, measurement/experimentation and retention/scaling.
- Use [**operating brief**](templates/operating-brief.md), [**creative brief**](templates/creative-production-brief.md) and [**experiment decision log**](templates/experiment-decision-log.md) to pass findings from one workflow into the next.
- Read a [**worked research-to-sales example**](examples/workflow-from-research-to-sales.md) with concrete buyer hypotheses, creative angles, economic boundaries, and reasons to fix a product page instead of rewriting copy.

The system is modular: a quick ad-copy request still takes a short route. A diagnosis can recommend **not spending on ads** until a product, price, checkout, inventory or tracking problem is addressed.

## What's improved in v2

- **Marketing diagnosis before copy:** separates message issues from product, pricing, distribution, landing-page, brand, demand and measurement problems.
- **A real positioning process:** alternatives → differentiated capabilities → value → best-fit customer circumstances → category; includes category expectations and trade-offs.
- **Brand strategy:** Keller's brand associations and Ehrenberg-Bass's mental/physical availability, category entry points and distinctive assets. Ads can vary by angle without abandoning brand recognition.
- **Customer psychology:** buyer versus user/recipient, JTBD, four switching forces, buying occasions, non-linear exploration/evaluation and decision friction.
- **Persuasion and credibility:** ELM, persuasion knowledge, ethical Cialdini, quality/trust/identity signaling and Fogg's motivation–ability–prompt model.
- **Product value and price:** benefit ladders, total perceived sacrifice, risk reduction and truthful handling of real drawbacks.
- **Better measurement:** brand-building versus short-term activation, ad-concept testing, commercial outcomes, brand measures and causal cautions.
- **Practical references:** linked research notes, an expanded source index, a strategic brief template and a full end-to-end diagnosis example.

## How it works

```text
Actual product & campaign facts
            ↓
Buyer situation, desired progress and alternatives
            ↓
Product benefit, perceived value, objections and weaknesses
            ↓
Competitive positioning + brand identity / buying cues
            ↓
Trust and persuasion mechanism + claim proof
            ↓
Creative concepts → shot/storyboard → brand cues → formats
            ↓
Distinct Meta ad fields and placement-specific assets
            ↓
Policy review, skeptical-buyer audit, landing-page match
            ↓
Controlled learning and strategic revision
```

A quick copy-edit request takes a shorter route; the skill does **not** require a full strategy report every time.

## Install

Install from the published `doeixd/marketing-skills` repository with a compatible Agent Skills installer:

```bash
npx skills add doeixd/marketing-skills --skill marketing-os
```

Or download the ZIP, unpack it and copy the full directory to your tool's agent skills folder, for example:

```bash
mkdir -p .agents/skills
cp -R marketing-os .agents/skills/marketing-os
```

For Claude Code, the local folder can be `.claude/skills/marketing-os/`. See your tool's specific installation instructions. The skill lives at `skills/marketing-os/` inside [doeixd/marketing-skills](https://github.com/doeixd/marketing-skills).

## Example prompts

> Diagnose whether my product-page and Meta ad conversion problem comes from weak copy, a confusing offer, buyer uncertainty or product-market mismatch. Give me evidence gaps and a test plan.

> Research how buyers choose this product, including buying occasions, actual alternatives, feature-to-benefit ladders, brand cues, emotional motives and real drawbacks; then write three distinct ad concepts.

> Investigate this product or service end-to-end. Discover exactly what is sold, the customers and situations it serves, motivations and drawbacks, alternatives, positioning, feature-benefit proof, pricing, assurances and the best plan to market it. Generate a reusable copy bank with bullets, descriptions, headlines, Meta ad concepts and what should be fixed before launching.

> Discover this brand from its website, products, reviews and existing marketing. Explain what makes it special, its actual voice and perspective, the claims it can support and customer reservations; create a reusable copy bank with benefit bullets, headlines, descriptions and Meta ad units.

> Develop a positioning strategy for my brand: category expectations, points of parity/difference, best-fit customers, distinctive assets, category entry points and value to communicate in ads.

> Write Facebook Feed and Instagram Feed primary text/headline/description combinations that preserve our brand identity while testing gifting, aesthetic and product-led angles.

> These are my campaign results. Separate what is actually known from causal guesses; tell me whether to fix landing-page UX, change positioning or test new creative.

> Give me a 9:16 Instagram Reels storyboard for this SKU, with exact shots, overlay text, voiceover, brand cue, muted-viewing check, rights constraints, and a 4:5 Feed cut. Distinguish facts from buyer hypotheses.

> I want to sell this new product. Run the marketing workflow from commercial viability through customer research, positioning, offer, channel selection, ad concepts, launch QA and measurement. Label unknowns and tell me when ads are not the next move.

## Reference library

| Document | When to read |
|---|---|
| [SEO fundamentals and ecommerce](references/seo-fundamentals-and-ecommerce.md) | Technical eligibility, buyer intent, architecture, on-page copy and product search features |
| [AEO / AI search citations](references/aeo-generative-search-and-citations.md) | Google AI Search requirements, question-first information and citation measurement limits |
| [CRO and experimentation](references/cro-research-and-experimentation.md) | Buyer friction, store funnels, data integrity and trustworthy A/B testing |
| [Marketing fundamentals](references/marketing-fundamentals.md) | Diagnose the broader business and marketing system |
| [Buyer research](references/buyer-research.md) | JTBD, buyer situations, customer language and evidence |
| [Market positioning](references/market-positioning.md) | Alternatives, capabilities, value, best-fit customers, category |
| [Brand strategy](references/brand-strategy.md) | Brand equity, distinctiveness, category entry points and memory |
| [Brand voice and copy system](references/brand-voice-and-copy-system.md) | Discover the real voice, differentiate identity from perception, distill into reusable phrasing |
| [Product value and pricing](references/product-value-and-pricing.md) | Feature–benefit ladders, total sacrifice and price concerns |
| [Persuasion and signaling](references/persuasion-and-signaling.md) | ELM, Cialdini, PKM, quality signals and buyer decision barriers |
| [Positioning and objections](references/positioning-and-objections.md) | Objection matrices, benefits and drawbacks |
| [Creative strategy](references/creative-strategy.md) | Translate buyer motives into distinct visual promises and creative territories |
| [Visual direction](references/visual-direction.md) | Frame, camera, typography, product fidelity, brand cues and review language |
| [Meta placement playbook](references/meta-placement-playbook.md) | 4:5 / 9:16 / carousel, safe zones, Reels/Stories/Feed, automated enhancements |
| [Video storytelling](references/video-storytelling.md) | Reels story types, hooks, short-video scripts, audio and captions |
| [Instagram/platform idioms](references/platform-idioms-and-voice.md) | POV, GRWM, unboxing, natural diction and multi-channel communication |
| [Creator partnerships & rights](references/creator-partnerships-and-rights.md) | FTC disclosures, permissions, licenses and authentic creator direction |
| [Creative quality control](references/creative-quality-control.md) | QA gates, eight-item scorecard, systematic revision |
| [Meta fields](references/meta-fields.md) | Primary text, headlines, description, CTA and placement logic |
| [Compliance](references/compliance.md) | Policy risks and claim verification |
| [Marketing effectiveness](references/marketing-effectiveness.md) | Brand vs activation and measurement horizons |
| [Testing and learning](references/testing-and-learning.md) | Creative experiments, campaign metrics and learning records |
| [Quality rubric](references/quality-rubric.md) | Skeptical buyer and editorial review |
| [Annotated sources](references/sources.md) | Primary research, Meta and open-source skill links |

## Operational workflows

See [the complete workflow guide](WORKFLOWS.md), which links to nine core stage runbooks **plus optional offering discovery (1A), brand discovery (3A), CRO (4A), SEO (5A), and AEO (5B)**, decision gates, and the source-backed operating loop.

## Templates and examples

- [Search and conversion audit](templates/search-and-conversion-audit.md), [CRO experiment brief](templates/cro-experiment-brief.md), [SEO/AEO/CRO worked example](examples/seo-aeo-cro-from-offering.md)

- [Brand discovery intake](templates/brand-discovery-intake.md), [messaging library template](templates/brand-messaging-library.md), and [worked example](examples/brand-discovery-to-copy.md)
- [Product and campaign intake](templates/intake.md)
- [Strategic marketing brief](templates/strategy-brief.md)
- [Output and example JSON contract](templates/output-format.md)
- [Simple vintage ring copy example](examples/vintage-ring.md)
- [End-to-end marketing diagnosis](examples/strategic-diagnosis.md)
- [Machine-readable example ad variants](examples/ad-variants.json)
- [Commercial operating brief](templates/operating-brief.md)
- [Ad concept and production brief](templates/creative-production-brief.md)
- [Experiment/decision log](templates/experiment-decision-log.md)
- [Research-to-sales workflow example](examples/workflow-from-research-to-sales.md)
- [Creative direction brief](templates/creative-direction-brief.md), [shot list](templates/shot-list-and-storyboard.md), and [creative review scorecard](templates/creative-review-scorecard.md)
- [Reels direction example](examples/reels-creative-direction.md) and [planned creative manifest](examples/creative-manifest.json)

All example products, buyer motives and ads are **illustrative**; do not treat them as real customer interviews, verified product claims or proven winners.

## Validation

```bash
python3 scripts/check_copy.py examples/ad-variants.json
python3 scripts/check_creative.py examples/creative-manifest.json
python3 scripts/check_links.py
python3 -m unittest discover -s tests -v
```

The copy and creative linters check structural issues, advisory lengths, planned dimensions/safe-zone overlaps and release metadata. It **does not** verify factual claims, brand effectiveness, buyer motives, Meta policy approval or advertising performance. Meta placement guides and current account previews take precedence over stale character-length rules.

## Boundaries

Read-only analysis and draft generation are the default. This skill does **not** authorize campaign publishing, changes to spend or ad account modifications. Sensitive-attribute targeting assumptions, fabricated scarcity, endorsements or claims, and misleading comparisons are prohibited by the skill. It is independent of, and not endorsed by, Meta.

License: [MIT](LICENSE).
