# CRO experiment / conversion diagnosis brief

Use for tests where a meaningful uncertainty warrants experimentation. Do **not** require a test before repairing a broken checkout, false policy or objectively incorrect product page.

## 1. Decision
- Page/product/service and affected stage:
- Buyer situation, traffic mix and business bottleneck:
- Observed evidence (quant + qualitative), date and confidence:
- Competing explanation:
- Goal and what will change if the hypothesis is supported or refuted:
- Should this be a straightforward defect fix instead?

## 2. Hypothesis and treatments
- **Hypothesis:** If [change] because [mechanism], then [qualified buyer] will be better able to [decision/action] and [metric] may improve.
- **Control:** exact current version and URL:
- **Treatment:** exact changes to copy, imagery, layout, features or policy and URL:
- **What stays constant:** price, inventory, traffic allocation, promotions, other tests (or tracked caveats):
- Claim/policy/brand approvals and accessibility considerations:

## 3. Instrumentation, outcomes and guardrails
- Randomization unit and stable assignment:
- Eligibility and exposure definition:
- Primary commercial metric **and denominator**:
- Secondary diagnostic metrics:
- Guardrails (net contribution, refunds, returns, support burden, load performance, activation, accessibility, complaints):
- Event instrumentation reconciliation (store/CRM vs analytics):
- Predeclared exclusion and data-quality rules:
- Sample ratio mismatch check, crossover, bot/test contamination:

## 4. Statistical plan
- Baseline conversion rate / sample and time window:
- Minimum detectable change worth acting on:
- Significance/confidence or Bayesian criterion (choose in advance):
- Desired power, realistic sample estimate, expected runtime from observed traffic:
- Multiple-testing, repeated-look/peeking and stopping plan:
- Device/market splits predeclared vs post-hoc:
- When results will be inconclusive and what to do next:

## 5. Results and decision
| Metric | Control | Treatment | Estimated difference and uncertainty | Guardrail impact | Notes |
|---|---|---|---|---|---|

- Validity checks passed? SRM / instrumentation / sample size / uptime:
- Plausible mechanism and alternative explanations:
- **Decision:** ship / iterate / stop / inconclusive:
- Implementation, monitoring and rollback owner:
- What the test *does not* establish:
- Follow-on learning:
