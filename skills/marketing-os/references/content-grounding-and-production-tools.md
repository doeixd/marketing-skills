# Grounding, live data and production tools for marketing agents

Optional tools that put **real source material and live data** into a workflow, so strategy and copy are not generated from model priors alone. None of them are installed by or required for Marketing OS. Inspect each one's code, license, permissions and data handling before use. Checked November 2026; names and features change, so verify current repos.

## Permission boundary

| Class | Examples | Rule |
|---|---|---|
| **Read-only** | Search Console/GA4 queries, transcript extraction, reading highlights, crawling public pages, local rendering | Allowed inside a workflow when the user has granted access; record source and date as evidence |
| **External write** | Uploading audiences, editing campaigns, publishing posts, changing pixels, cloud-rendering into an account | Needs a named human confirmation for that specific action ([SKILL.md](../SKILL.md) principle 20) |

Prefer read-only connectors and scoped credentials. Never paste access tokens into chat or the [marketing context file](../templates/marketing-context.md).

## 1. Grounding in real customer and market language

Use these to collect verbatim phrases, objections, metaphors, hooks and pacing from real sources. Feed them into [buyer research](buyer-research.md) VOC extraction and the [master asset pipeline](social-media-strategy-hooks-and-community.md#master-asset--platform-transformation-pipeline).

- **Customer interview, sales-call and support transcripts:** the best grounding source. Use only with the participants' consent, and strip personal data before analysis.
- **Readwise highlights and Reader documents:** the official [Readwise CLI](https://docs.readwise.io/tools/cli) (`@readwise/cli`) and [readwiseio/readwise-skills](https://github.com/readwiseio/readwise-skills) let an agent query a team's saved research, articles and podcast highlights. Use the official package rather than third-party wrappers that ask for tokens.
- **Video and podcast transcripts** (industry talks, competitor webinars, top-performing category content): extract them to study structure, vocabulary and hook patterns. Respect platform terms of service and copyright. Analyze, don't republish; quotes need attribution and permission for commercial use.
- **Reviews, forums and social comments:** use them for VOC mining. Treat them as unrepresentative samples, and never present a scraped comment as a testimonial.

Tag all grounded material with `source | date | status` (usually `buyer-reported` or `inferred`) before it influences copy.

## 2. Live search and analytics data

Pull real impressions, CTR, queries, indexing and landing-page outcomes **before** issuing SEO or CRO recommendations ([5A](../workflows/05a-seo-and-organic-search.md), [4A](../workflows/04a-conversion-rate-optimization.md), [8A](../workflows/08a-marketing-analytics-and-measurement.md)).

- **Google Search Console MCP servers:** several community servers exist, among them [AKzar1el/mcp-gsc](https://glama.ai/mcp/servers/AKzar1el/mcp-gsc) (MIT, bundles weekly-review, indexing-triage and opportunity skills), [surendranb/google-search-console-mcp](https://github.com/surendranb/google-search-console-mcp) (note that its README says it collects diagnostic telemetry) and read-only servers. None is a Google product. Prefer read-only scopes and check maintenance and telemetry.
- **GA4:** the GA4 Data API, or a vetted MCP wrapper, for landing-page and conversion data. Reconcile against commerce orders as described in [measurement](measurement-pixels-ga4-and-attribution.md).
- **Third-party SEO suites** (Ahrefs, Semrush and similar) offer APIs or MCP servers on paid plans. Treat their traffic and keyword volumes as estimates, not first-party data.
- For data-engineering-grade connectors, see [marketing data tools](marketing-data-tools-skills-and-resources.md).

Never present an MCP or API response the agent didn't actually receive as observed data. If access is unavailable, write `[NEEDS INPUT: GSC export or access]`.

- **Meta Ads:** the [Meta Marketing API](https://developers.facebook.com/docs/marketing-apis/) directly, or connectors such as [Composio's Meta Ads toolkit](https://composio.dev/toolkits/metaads) (MCP/CLI, OAuth), let agents read insights and manage campaigns. Use read-only by default; creating, editing, pausing, budgets and audience uploads are external writes. Verify each connector tool's real behavior before use. See [Meta Ads setup §8](meta-ads-campaign-setup-and-signal-quality.md#8-agent-access-to-the-meta-marketing-api).

## 3. Pre-publication verification

Before publishing a page, email or campaign URL, verify mechanically:

- outbound and internal links resolve (this repo's [link checker](../scripts/check_links.py) shows the pattern for Markdown);
- title, meta description, canonical, Open Graph and Twitter-card tags are present and match the approved claims;
- structured data validates (Google's Rich Results Test or Schema Markup Validator) and matches visible content;
- campaign URLs follow the [UTM governance](campaign-utm-and-identity-governance.md) rules.

## 4. Programmatic creative

Code-rendered video and graphics (Remotion, HeyGen HyperFrames) are covered in [video storytelling](video-storytelling.md#programmatic-code-generated-video).

## 5. Other marketing-skill repositories (for comparison and borrowing patterns)

| Repository | Shape | Pattern worth noting | Tradeoff |
|---|---|---|---|
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | Library of many small single-purpose skills | Portable, no dependencies; cited across this repo's references | Brand context is re-entered per skill unless a shared context skill is used |
| [scayver/marketing-skills](https://www.skills.sh/scayver/marketing-skills) | Integrated "marketing OS" plus many skills | A root product-marketing context reused by downstream skills | More setup and folder coupling |
| [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) | Large domain library (160–240 entries, depending on snapshot), including page-type skills | Broad page-type and tactic coverage with a shared project-context file | Discovery metadata adds up when every skill is installed |

A multi-agent "orchestrator plus specialist subagents" design, as some repos use, trades latency and tokens for parallelism. Marketing OS deliberately uses one skill with on-demand workflows instead. Borrow patterns, not wording; verify licenses before reusing any text.
