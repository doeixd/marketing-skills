# Marketing data tools, agent skills and learning resources

**Research date: 2026-11-06.** A curated decision map for Marketing OS. These are **links to existing skills/documentation, not installed dependencies**; availability, API versions, costs and licenses need review. Learn from upstream structure and adapt original guidance; do not copy third-party skills verbatim. Official technical documentation outranks workflow prose.

## Agent skills: inspect before use

| Maintainer / collection | Relevant skills or patterns | Best use and limitations |
|---|---|---|
| [dbt-labs/dbt-agent-skills](https://github.com/dbt-labs/dbt-agent-skills) | `using-dbt-for-analytics-engineering`, unit tests, docs, semantic layer, Mesh, job troubleshooting | **Vendor-maintained** for dbt modeling/testing; verify the project's own versions and downstream compatibility; does not extract marketplace data |
| [rudderlabs/rudder-agent-skills](https://github.com/rudderlabs/rudder-agent-skills) | `rudder-setup`, `rudder-tracking-plans`, `rudder-instrumentation-planning`, `rudder-instrumentation-debugging`, data catalog/graphs, CLI/transformations/Profiles | **Vendor-maintained** for RudderStack collection/contracts, transformations and reverse ETL; requires suitable account/tools; not neutral evidence of effectiveness |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | `analytics-tracking` (or current named equivalent), event/UTM plan, GA4 setup/audit, measurement strategy, CRO, experimentation | Independent modular marketing implementation workflow; inspect current skill name/path and actual claims before relying on code |
| [Shopify/agent-skills](https://github.com/Shopify/agent-skills) and [Shopify/Shopify-AI-Toolkit](https://github.com/Shopify/Shopify-AI-Toolkit) | Shopify Admin GraphQL, custom data, Liquid, integrations and schema lookup | **Shopify-authored** API/code tasks; verify app scopes, platform behavior, privacy and current API schema |
| [Dataslayer-AI/Marketing-skills](https://github.com/Dataslayer-AI/Marketing-skills) | Cross-channel GA4/Google/Meta reports, paid media audits and aggregate reporting via Dataslayer MCP | Useful reporting workflow and QA inspiration; vendor/integration dependence, needs authorized live access, may have commercial costs |
| [Etsy Open API v3](https://developer.etsy.com/) | API reference plus **official OpenAPI developer MCP server** | Not an Agent Skill, but a live API-spec aid for authorized seller receipts/orders and inventory. Check access, terms and endpoints |
| [Google Analytics developer docs](https://developers.google.com/analytics) and [Google Tag Platform docs](https://developers.google.com/tag-platform) | Developer guides, Event Builder, DebugView/Tag Assistant and consent testing | Official implementation references rather than installable agent skills |
| [Meta Blueprint](https://bep.facebookblueprint.com/student/path/253116-optimize-conversions-api-course) | CAPI coverage, quality, deduplication, event match and freshness | Official education; cross-check live Events Manager diagnostics and exact Graph API version |

**How to use a third-party skill:** inspect license, current SKILL.md, prerequisites, permissions and last update; borrow the workflow insight, then validate code against the platform's *official current docs*. Never execute unaudited repository commands, automatically install tools or grant account permissions without approval.

## Connectors / ingestion

- **[Airbyte connectors](https://docs.airbyte.com/integrations)** — managed/self-hosted extraction options including Shopify, Amazon Seller Partner, Amazon Ads and numerous analytics/ad sources. Check actual streams, incremental capability, cost, auth requirements, connector freshness and self-hosted restrictions; a connector listing is not evidence every field/region is supported.
- **[dlt verified sources](https://dlthub.com/docs/dlt-ecosystem/verified-sources)** — programmable Python ELT for Shopify, Facebook Ads, Google Ads, Google Analytics and more; easy to extend for REST/GraphQL, but requires operational ownership and authorization.
- **[Meltano](https://docs.meltano.com/)** / [Singer taps and targets](https://hub.meltano.com/) — modular extractor/loader workflows; inspect individual plugin maintenance and stream coverage.
- **Custom TypeScript/Node pipelines** — apt when merchant integrations are niche or strongly typed, but build rate limit, idempotence, cursor state, schema versioning, replay, secret management, monitoring and integration tests before relying on production revenue. A homegrown connector has continuing maintenance costs.
- **Native Shopify Google/Meta channels, platform CSV exports and official marketplace reports** — often simplest valid solution for a single store; audit duplicates/coverage before layering a CDP.

## Warehouse / transformation / validation

- **[dbt](https://docs.getdbt.com/)** — modular SQL models, source freshness, contracts, assertions, snapshots, semantic layer and CI; best for analytic transformations, not API ingestion.
- **[DuckDB](https://duckdb.org/docs/stable/)** — local analysis of CSV/Parquet/JSON; efficient for one-off audits and early prototypes.
- **[BigQuery](https://cloud.google.com/bigquery/docs)** — integrates GA4 event exports and warehouse marts; use partition filtering/cost controls, region/privacy governance and documented export/UI differences.
- **[PostgreSQL](https://www.postgresql.org/docs/)** / SQLite — pragmatic small-to-mid-size canonical data marts and reliable idempotent upserts.
- **[Great Expectations](https://docs.greatexpectations.io/docs/core/introduction/)** — business-readable data quality expectations; [dbt tests](https://docs.getdbt.com/docs/build/data-tests) can be a simpler starting point.
- **[Dagster](https://docs.dagster.io/)** / [Prefect](https://docs.prefect.io/) — orchestration/monitoring for enough pipelines to warrant it; scheduling infrastructure does not fix bad accounting definitions.

## Event/CDP and activation infrastructure

- **[Google Tag Manager server-side](https://developers.google.com/tag-platform/tag-manager/server-side/intro)** — intermediary event collection and transformation with configurable first-party endpoint; do not bypass consent.
- **[RudderStack](https://www.rudderstack.com/docs/)** — event collection, tracking plans, identity/warehouse audiences and activation; audit data residency, price, features and sync governance.
- **[Twilio Segment](https://segment.com/docs/connections/spec/)** — event specification and source-to-destination design patterns; vendor product, not a mandatory dependency.
- **[Google Analytics](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce), [Meta Events Manager](https://www.facebook.com/business/tools/meta-pixel), [Shopify Web Pixels](https://shopify.dev/docs/api/web-pixels-api)** — primary collection quality and destination semantics.

## Official primary-source reading path by task

| Problem | Source of technical truth | Practical check |
|---|---|---|
| Meta Pixel/CAPI missing or double counting | [Meta CAPI docs](https://developers.facebook.com/docs/marketing-api/conversions-api/) and [Blueprint](https://bep.facebookblueprint.com/student/path/253116-optimize-conversions-api-course) | Browser/server event IDs, event name, test events, consent and diagnostics |
| GA4 ecommerce mismatch | [GA4 recommended events](https://developers.google.com/analytics/devguides/collection/ga4/reference/events) and [BigQuery schema](https://support.google.com/analytics/answer/7029846) | Transaction dedupe, value/variant IDs, session vs first-touch attribution |
| Shopify checkout/event collection | [Shopify pixel sandbox](https://shopify.dev/docs/api/web-pixels-api) and [privacy](https://shopify.dev/docs/api/customer-privacy) | Live integration inventory, consent and checkout_completed |
| Etsy orders/API | [Etsy Open API v3](https://developer.etsy.com/documentation/reference) | OAuth scope, pagination, receipt+transaction key, refunds and rate headers |
| Amazon orders/reports | [Amazon SP-API Reports](https://developer-docs.amazon/sp-api/docs/reports-api) and [Data Kiosk](https://developer-docs.amazon/sp-api/lang-en_US/docs/data-kiosk-api) | Seller+marketplace keys, async report status, fee and money-flow grain |
| UTMs and click IDs | [Google URL builders](https://support.google.com/analytics/answer/10917952) and [tagging rules](https://support.google.com/analytics/answer/11242870) | Landing URL retains parameters, lowercased taxonomy, auto-tag handling |
| Data modeling and freshness | [dbt CDC guidance](https://docs.getdbt.com/best-practices/how-we-handle-cdc/2-choosing-incremental-or-snapshots) | Stable grain, backfill, late edits, freshness, uniqueness, source reconciliation |
| First-party audience activation | [Google customer-data policy](https://business.google.com/us/accelerate/resources/articles/customer-data-policies/), platform rules and [Shopify customer segments](https://help.shopify.com/en/manual/customers/customer-segmentation) | Consent purpose, removals, exclusions, match diagnostics and owner approval |

## Select an approach without tool cargo cult

- **One Shopify store + low volume + basic campaigns:** native integrations + QA spreadsheet + scheduled CSV recon + GA4/Shopify reports; do not introduce an expensive CDP/warehouse by default.
- **Multi-store Shopify with Etsy/Amazon:** incremental seller API/report ELT + SKU bridge + canonical order/fees marts + distinct ads/GA4 marts, with daily reconciliation.
- **Many ad platforms / heavy audience work:** governed warehouse + collection specification + documented consent + dbt/dlt/Airbyte + tested reverse ETL, after verifying ROI and account permissions.

Revisit official schemas, service costs, SDK behavior and restrictive ads/marketplace data-sharing policies each time an implementation is designed.
