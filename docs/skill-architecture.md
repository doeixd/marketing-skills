# Skill architecture and authoring guide

For maintainers of this repo. It explains how the skills are structured to follow the [Agent Skills specification](https://agentskills.io/specification), why, and the rules CI enforces. Runtime instructions for agents live in each skill's `SKILL.md`, not here.

## Progressive disclosure: three tiers

Runtimes load skills in tiers, so installed skills cost little until they are used.

| Tier | Content | When loaded | Budget in this repo |
|---|---|---|---|
| 1. Discovery | Frontmatter `name` + `description` | Always, for every installed skill | Description ≤ 1,024 chars; aim for what it does + when to use it |
| 2. Activation | `SKILL.md` body | When a task matches the description | ≤ 500 lines and ~5,000 tokens (enforced by `scripts/check_skill_spec.py`) |
| 3. Execution | `workflows/`, `references/`, `templates/`, `scripts/`, `examples/` | Only when `SKILL.md` or a workflow points to them | No hard limit; one topic per file |

The tradeoff is **context load** versus **cognitive load**. Every always-loaded token costs every session (context load); splitting into many user-invoked commands shifts the burden to people remembering which to call (cognitive load). Marketing OS uses one skill with a router table: one description in tier 1, a compact router in tier 2, and everything else in tier 3.

## Frontmatter

Spec fields: `name` (required; 1–64 chars, lowercase letters, digits and single hyphens, no leading/trailing hyphen; must equal the directory name), `description` (required; 1–1,024 chars), and the optional `license`, `compatibility`, `metadata` and `allowed-tools` (experimental).

Some clients add their own fields, such as Claude Code's `disable-model-invocation` (user-invoked only, which keeps the description out of standing context) or effort/model hints. They are **not** in the open spec, and other clients may ignore or reject unknown fields. Don't add them to the shared skill without checking each target client.

## Writing rules

1. **Prune no-op text.** A sentence that re-explains general marketing theory without changing what the agent does should go to `references/` or be deleted. Tier 2 holds routing, guardrails, contracts and done-criteria.
2. **Prefer checklists, schemas and completion criteria** over narrative. Every workflow step should name its output and its stop condition.
3. **One source of brand truth.** Workflows read `.marketing-context/brand-truth.md` ([template](../skills/marketing-os/templates/marketing-context.md)) instead of re-asking, and propose updates at handoff.
4. **Stop, don't invent.** Missing facts become `[NEEDS INPUT: …]`; undecidable self-review calls become `[NEEDS HUMAN REVIEW: …]`. Validators reject unresolved markers in publishable fields.
5. **Read-only by default.** Any write to an external system needs per-action human confirmation.
6. **Every workflow is routed** from `SKILL.md`, and every reference/template is linked from somewhere (CI warns on orphans).
7. **Validators are offline and structural.** Scripts in `scripts/` are standard-library Python 3.10+ with unit tests in `tests/`, so the skill runs with no install step. A passing validator is never evidence of compliance or performance.

## Evals

Offline validators check structure; [`evals/`](../evals/README.md) checks behavior with `claude plugin eval` (triggering, routing, no invented facts, guardrails). Evals cost usage, so they run by hand or through the manual `evals.yml` workflow. Re-run the routing and no-trigger cases after any change to the description, and add a case whenever a new workflow or guardrail is added.

## CI

`.github/workflows/validate-marketing-os.yml` runs the unit tests, `check_skill_spec.py`, each example validator and `check_links.py`.

## Roadmap

| Phase | Item | Status |
|---|---|---|
| 1. Spec alignment | Frontmatter limits, name = directory, tier-2 budget, split into references/scripts, CI check | Done (5.6.0) |
| 2. Context layer | Persistent brand-truth file, read-first directives, `[NEEDS INPUT]` handling | Done (5.6.0) |
| 3. Decision gates | Typed scoring of drafts (brand voice, unsubstantiated claims, tone) with confidence thresholds that route low-confidence or rejected drafts to `[NEEDS HUMAN REVIEW]` | Proposed. Today it is enforced through the review passes in the [core reasoning chain](../skills/marketing-os/references/core-reasoning-chain.md) and the copy linter's marker check. A model-backed gate (for example, a classifier returning `APPROVED` / `REJECT_TONE_VIOLATION` / `REJECT_UNSUBSTANTIATED_CLAIM` with a threshold of about 0.85) should be an **optional** script, so the skill keeps working with no dependencies. Confirm any library's actual API before adopting it. |
| 4. Live tooling | Search Console/GA4 MCP pointers, Readwise and transcript grounding, pre-publication link/meta/schema checks | Documented as optional, vetted pointers in [grounding and production tools](../skills/marketing-os/references/content-grounding-and-production-tools.md); nothing bundled |
| 5. Coverage | Business types beyond DTC ecommerce, planning (pricing, budget, launch, review cadence), advocacy and reputation, beginner path, glossary, privacy | Done (5.8.0) |
| 6. Evals | Routing, no-fabrication, guardrail, trigger and quality cases | Done (5.10.0): 41 cases in [`evals/`](../evals/README.md); run before each release |
| 7. Remaining channels | Affiliate programs, events and webinars, direct mail, podcast; campaign blueprint validator; reference freshness check | Planned: see the [improvement plan](improvement-plan.md) |

Not planned: splitting Marketing OS into dozens of top-level skills (it would raise tier-1 load and fragment the shared guardrails) or rewriting the validators in another language without a functional reason.
