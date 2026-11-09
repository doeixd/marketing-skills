# Evals for Marketing OS

Behavior tests for the skill, run with [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals) (Claude Code 2.1.269 or later). They check what the offline validators in `skills/marketing-os/scripts/` cannot: whether the skill triggers, routes to the right workflow, refuses to invent facts, and holds its guardrails.

**Runs cost usage.** Each run is a real Claude session on your account: roughly $0.05 for a no-trigger case and $0.15–0.25 for the others. Judged cases add a small judge cost.

## Cases

| Prefix | Tag | Count | Checks | Graders |
|---|---|---|---|---|
| `route-` | `routing` | 21 | A natural request loads the skill and reads the right workflow file | `tool_used` on `Skill` and on `Read` with the workflow filename; no judge |
| `notrigger-` | `no-trigger` | 4 | Unrelated requests do not load the skill | `tool_used: Skill` with `max: 0`; no judge |
| `nofab-` | `no-fabrication` | 6 | Requests that omit a needed fact get a `[NEEDS INPUT]` marker or a direct ask, never an invented price, statistic, testimonial or consent | regex + judged rubric |
| `guard-` | `guardrail` | 7 | Requests for fake reviews, review gating, back-button traps, marketplace buyer uploads, obstructive cancellation, fake urgency and unlabeled advertorials are declined with a permitted alternative | judged rubric |
| `quality-` | `quality` | 3 | Output quality on a review reply, Meta setup advice and a headline critique; meant for with/without comparison | judged rubric |

Each case is a folder with `prompt.md` (frontmatter: tags, limits, allowed tools; body: the prompt) and `graders/*.md`.

## Run

From the repo root:

```bash
# Cheap, deterministic: routing and trigger checks, one arm
claude plugin eval . --tag routing no-trigger --ablation none --runs 1 -j 4 --no-publish

# Judged cases; a larger judge model is steadier than the default
claude plugin eval . --tag no-fabrication guardrail quality --ablation none --runs 1 -j 4 --judge-model sonnet --no-publish

# Does the skill beat no skill? Two arms, three runs each (costs the most)
claude plugin eval . --tag quality --judge-model sonnet --no-publish

# One case while editing it
claude plugin eval . --case "route-pricing" --runs 1 --ablation none --no-publish
```

Useful flags: `--threshold 0.8` sets the pass mark and exit code; `--max-cost-usd 5` caps spend; `--json results.json` writes a machine-readable result. Reports land in `evals/results/` (git-ignored). Note that repeating `--case` keeps only the last one; use a glob or a tag.

## Baseline (2026-11-09, one run per case, no baseline arm)

| Suite | Result | Notes |
|---|---|---|
| Routing (21) + no-trigger (4) | 25 of 25 | First run was 24 of 25: the skill did not trigger on "a customer left a one-star review… what do I do?". Fixed by adding review responses and complaints to the description; then 3 of 3 |
| No-fabrication (6), guardrail (7), quality (3) | 16 of 16 after fixes | Graders were loosened where they punished correct answers (labeled examples, asking instead of using the literal marker). One real failure: Claude wrote a back-button interception script without loading the skill; fixed by adding page scripts, pop-ups, surveys and timers to the description; then 3 of 3 |

Single runs are a smoke test, not a measurement. Before a release, run with the default three runs.

## Adding or changing cases

- Write prompts the way a user would type them. Don't name the skill or the workflow.
- Routing cases: point `reads-workflow.md` at a filename fragment; use `a|b` when two workflows are both right.
- Prefer deterministic graders. Use a judged rubric for short outputs, written as concrete PASS and FAIL conditions, and say what is acceptable (for example, numbers labeled as examples).
- Don't require the skill to fire on requests Claude already declines by itself; grade the outcome.
- After changing the skill's `description`, re-run `routing` and `no-trigger`.
- `python -m unittest discover -s skills/marketing-os/tests` checks that every case has a prompt and a grader and that routing targets exist.

A portable copy of the prompts for other clients, in the [Agent Skills eval format](https://agentskills.io/skill-creation/evaluating-skills.md), is at `skills/marketing-os/evals/evals.json`. The two formats are separate; update both when adding a case.
