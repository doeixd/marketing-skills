"""Ensure the modular marketing workflows and handoffs remain present."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class TestWorkflows(unittest.TestCase):
    def test_all_nine_workflows_present(self):
        files = sorted((ROOT / "workflows").glob("0[1-9]-*.md"))
        self.assertEqual(len(files), 9)
        for p in files:
            txt = p.read_text(encoding="utf-8")
            self.assertIn("Workflow ", txt)
            self.assertIn("Handoff", txt)

    def test_brand_discovery_subworkflow(self):
        paths = (
            'workflows/03a-brand-discovery-and-messaging.md',
            'references/brand-voice-and-copy-system.md',
            'templates/brand-discovery-intake.md',
            'templates/brand-messaging-library.md',
            'examples/brand-discovery-to-copy.md',
        )
        for name in paths:
            self.assertTrue((ROOT / name).is_file(), name)
        workflow = (ROOT / paths[0]).read_text(encoding='utf-8')
        for heading in ('brand reality', 'voice', 'selling points', 'headline', 'description', 'Handoff'):
            self.assertIn(heading.lower(), workflow.lower())

    def test_offering_discovery_subworkflow(self):
        paths = (
            'workflows/01a-offering-discovery-and-marketing-plan.md',
            'references/offering-research-and-marketing-planning.md',
            'templates/offering-discovery-intake.md',
            'templates/offering-dossier-and-marketing-plan.md',
            'examples/offering-discovery-to-marketing-plan.md',
        )
        for name in paths:
            self.assertTrue((ROOT / name).is_file(), name)
        workflow = (ROOT / paths[0]).read_text(encoding='utf-8').lower()
        for term in ('brand', 'buyer', 'alternatives', 'feature', 'benefit', 'drawback', 'objection', 'pricing', 'assurances', 'creative', 'headline', 'description', 'handoff'):
            self.assertIn(term, workflow)
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('(workflows/01a-offering-discovery-and-marketing-plan.md)', skill)
        plan = (ROOT / 'WORKFLOWS.md').read_text(encoding='utf-8')
        self.assertIn('Workflow 1A', plan)

    def test_seo_aeo_cro_specialist_workflows(self):
        paths = (
            'workflows/05a-seo-and-organic-search.md',
            'workflows/05b-aeo-ai-search-visibility.md',
            'workflows/04a-conversion-rate-optimization.md',
            'references/seo-fundamentals-and-ecommerce.md',
            'references/aeo-generative-search-and-citations.md',
            'references/cro-research-and-experimentation.md',
            'templates/search-and-conversion-audit.md',
            'templates/cro-experiment-brief.md',
            'examples/seo-aeo-cro-from-offering.md',
        )
        for name in paths:
            self.assertTrue((ROOT / name).is_file(), name)
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        operating = (ROOT / 'WORKFLOWS.md').read_text(encoding='utf-8')
        for name in ('04a-conversion-rate-optimization.md', '05a-seo-and-organic-search.md', '05b-aeo-ai-search-visibility.md'):
            self.assertIn(name, skill)
            self.assertIn(name, operating)
        aeo = (ROOT / 'references/aeo-generative-search-and-citations.md').read_text(encoding='utf-8').lower()
        self.assertIn('llms.txt', aeo)
        self.assertIn('citation', aeo)
        cro = (ROOT / 'references/cro-research-and-experimentation.md').read_text(encoding='utf-8').lower()
        self.assertIn('sample-ratio', cro)
        self.assertIn('guardrails', cro)

    def test_promotion_and_paid_search_specialists(self):
        paths = (
            'workflows/05c-promotion-strategy-and-distribution.md',
            'workflows/05d-social-content-hooks-and-community.md',
            'workflows/05e-creators-influencers-and-collaborations.md',
            'workflows/05f-pr-earned-media-and-press-releases.md',
            'workflows/05g-paid-search-google-ads.md',
            'references/promotion-fundamentals-and-integrated-distribution.md',
            'references/social-media-strategy-hooks-and-community.md',
            'references/influencers-collaborations-and-community-partnerships.md',
            'references/pr-press-releases-newswires-and-earned-media.md',
            'references/paid-social-amplification-and-promotion-measurement.md',
            'references/paid-search-google-ads-fundamentals.md',
            'templates/promotion-campaign-brief.md',
            'templates/social-content-and-hooks-calendar.md',
            'templates/creator-and-collaboration-brief.md',
            'templates/pr-newsroom-and-pitch.md',
            'templates/promotion-outcomes-review.md',
            'templates/google-ads-search-campaign-blueprint.md',
            'templates/google-search-rsa-and-assets.md',
            'templates/google-ads-optimization-and-experiments.md',
            'examples/promotion-from-research-to-distribution.md',
            'examples/google-ads-search-campaign-example.md',
            'examples/google-search-rsa-draft.json',
            'scripts/check_search_ads.py',
        )
        for name in paths:
            self.assertTrue((ROOT / name).is_file(), name)
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        system = (ROOT / 'WORKFLOWS.md').read_text(encoding='utf-8')
        for name in (
            '05c-promotion-strategy-and-distribution.md',
            '05d-social-content-hooks-and-community.md',
            '05e-creators-influencers-and-collaborations.md',
            '05f-pr-earned-media-and-press-releases.md',
            '05g-paid-search-google-ads.md',
        ):
            self.assertIn(name, skill)
            self.assertIn(name, system)
        paid = (ROOT / 'references/paid-search-google-ads-fundamentals.md').read_text(encoding='utf-8').lower()
        for phrase in ('keyword planner', 'negative keywords', 'ai max', 'conversion', 'rsa', 'smart bidding', 'quality score', 'experiment'):
            self.assertIn(phrase, paid)
        promo = (ROOT / 'references/pr-press-releases-newswires-and-earned-media.md').read_text(encoding='utf-8').lower()
        self.assertIn('syndication', promo)
        self.assertIn('newsworthiness', promo)

    def test_shopify_ecommerce_specialists(self):
        files = (
            "workflows/01b-shopify-ecommerce-diagnosis.md",
            "workflows/03b-shopify-catalog-and-merchandising.md",
            "workflows/04b-shopify-ecommerce-cro.md",
            "workflows/05h-shopify-ecommerce-seo.md",
            "workflows/05i-shopify-shopping-ads-and-tracking.md",
            "workflows/09a-shopify-lifecycle-retention.md",
            "workflows/05j-shopify-ecommerce-promotions.md",
            "references/shopify-ecommerce-strategy-and-economics.md",
            "references/shopify-catalog-merchandising-and-data.md",
            "references/shopify-ecommerce-cro-and-checkout.md",
            "references/shopify-ecommerce-seo-and-markets.md",
            "references/shopify-shopping-ads-feeds-and-attribution.md",
            "references/shopify-lifecycle-retention-and-automation.md",
            "references/shopify-theme-performance-and-measurement.md",
            "references/shopify-promotions-bundles-and-seasonal-campaigns.md",
            "references/shopify-ecommerce-skill-and-resource-library.md",
            "templates/shopify-store-audit-and-roadmap.md",
            "templates/shopify-product-collection-content-brief.md",
            "templates/shopify-pdp-cro-brief.md",
            "templates/shopify-search-merchandising-audit.md",
            "templates/shopify-merchant-feed-and-pixel-qa.md",
            "templates/shopify-lifecycle-and-retention-plan.md",
            "templates/shopify-ecommerce-promotion-brief.md",
            "examples/shopify-ecommerce-end-to-end.md",
        )
        for name in files:
            self.assertTrue((ROOT / name).is_file(), name)

        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        system = (ROOT / "WORKFLOWS.md").read_text(encoding="utf-8")
        for filename in (
            "01b-shopify-ecommerce-diagnosis.md",
            "03b-shopify-catalog-and-merchandising.md",
            "04b-shopify-ecommerce-cro.md",
            "05h-shopify-ecommerce-seo.md",
            "05i-shopify-shopping-ads-and-tracking.md",
            "09a-shopify-lifecycle-retention.md",
            "05j-shopify-ecommerce-promotions.md",
        ):
            self.assertIn(filename, skill)
            self.assertIn(filename, system)

        source = (ROOT / "references/shopify-ecommerce-skill-and-resource-library.md").read_text(encoding="utf-8")
        for name in ("Shopify/agent-skills", "Shopify/Shopify-AI-Toolkit", "proskillpacks", "nexscope-ai", "Baymard"):
            self.assertIn(name, source)
        self.assertIn("session", (ROOT / "references/shopify-ecommerce-cro-and-checkout.md").read_text(encoding="utf-8").lower())
        self.assertIn("Plus", (ROOT / "references/shopify-ecommerce-cro-and-checkout.md").read_text(encoding="utf-8"))
        self.assertIn("Web Pixels", (ROOT / "references/shopify-shopping-ads-feeds-and-attribution.md").read_text(encoding="utf-8"))

    def test_email_sms_analytics_specialists(self):
        paths = (
            "workflows/08a-marketing-analytics-and-measurement.md",
            "workflows/08b-attribution-incrementality-and-experiments.md",
            "workflows/08c-customer-segmentation-rfm-and-clv.md",
            "workflows/09b-email-marketing-campaigns-and-copy.md",
            "workflows/09c-sms-text-and-messaging-marketing.md",
            "workflows/09d-cross-channel-lifecycle-and-segmentation.md",
            "workflows/09e-email-deliverability-and-list-health.md",
            "references/email-marketing-strategy-copy-and-creative.md",
            "references/email-deliverability-consent-and-reputation.md",
            "references/sms-text-marketing-and-compliance.md",
            "references/lifecycle-orchestration-and-channel-governance.md",
            "references/marketing-analytics-data-model-and-reporting.md",
            "references/attribution-incrementality-experimentation-and-mmm.md",
            "references/customer-analytics-segmentation-rfm-and-clv.md",
            "references/email-sms-analytics-skills-and-resources.md",
            "templates/email-campaign-and-creative-brief.md",
            "templates/email-deliverability-and-consent-audit.md",
            "templates/sms-campaign-and-compliance-brief.md",
            "templates/cross-channel-lifecycle-journey-map.md",
            "templates/marketing-measurement-and-kpi-dictionary.md",
            "templates/marketing-attribution-and-incrementality-plan.md",
            "templates/customer-rfm-cohort-and-segment-plan.md",
            "templates/marketing-campaign-performance-review.md",
            "examples/email-sms-ecommerce-lifecycle-example.md",
            "examples/marketing-analytics-cohort-decision-example.md",
            "examples/messaging-plan-draft.json",
            "scripts/check_messaging_plan.py",
            "tests/test_messaging_plan.py",
        )
        for path in paths:
            self.assertTrue((ROOT / path).is_file(), path)
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        os = (ROOT / "WORKFLOWS.md").read_text(encoding="utf-8")
        for name in ("08a-marketing-analytics-and-measurement.md",
                     "08b-attribution-incrementality-and-experiments.md",
                     "08c-customer-segmentation-rfm-and-clv.md",
                     "09b-email-marketing-campaigns-and-copy.md",
                     "09c-sms-text-and-messaging-marketing.md",
                     "09d-cross-channel-lifecycle-and-segmentation.md",
                     "09e-email-deliverability-and-list-health.md"):
            self.assertIn(name, skill)
            self.assertIn(name, os)
        sms = (ROOT / "references/sms-text-marketing-and-compliance.md").read_text(encoding="utf-8")
        self.assertIn("Email opt-in", sms)
        self.assertIn("STOP", sms)
        deliverability = (ROOT / "references/email-deliverability-consent-and-reputation.md").read_text(encoding="utf-8")
        self.assertIn("DMARC", deliverability)
        self.assertIn("one-click", deliverability)
        analytics = (ROOT / "references/marketing-analytics-data-model-and-reporting.md").read_text(encoding="utf-8")
        self.assertIn("transaction_id", analytics)
        self.assertIn("contribution", analytics)

    def test_data_pipelines_implementation_extensions(self):
        files = (
            "workflows/08d-marketing-data-pipelines-and-measurement.md",
            "workflows/08e-event-instrumentation-and-conversion-qa.md",
            "workflows/08f-marketplace-etl-and-reconciliation.md",
            "workflows/08g-audience-activation-and-utm-governance.md",
            "references/2026-platform-data-api-updates.md",
            "references/campaign-utm-and-identity-governance.md",
            "templates/event-destination-and-consent-matrix.md",
            "templates/marketplace-extraction-and-reconciliation-contract.md",
            "templates/audience-activation-and-suppression-brief.md",
            "examples/marketing-data-pipeline-manifest.json",
            "scripts/check_marketing_data_plan.py",
            "tests/test_marketing_data_plan.py",
        )
        for path in files:
            self.assertTrue((ROOT / path).is_file(), path)
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        workflow = (ROOT / "WORKFLOWS.md").read_text(encoding="utf-8")
        for p in (
            "08e-event-instrumentation-and-conversion-qa.md",
            "08f-marketplace-etl-and-reconciliation.md",
            "08g-audience-activation-and-utm-governance.md",
        ):
            self.assertIn(p, skill)
            self.assertIn(p, workflow)
        refs = (ROOT / "references/2026-platform-data-api-updates.md").read_text(encoding="utf-8")
        for term in ("Shopify", "Etsy", "Amazon", "Meta", "Data Manager", "2026-01"):
            self.assertIn(term, refs)

    def test_meta_ads_setup_specialist(self):
        for name in ("workflows/05k-meta-ads-campaign-setup-and-optimization.md",
                     "references/meta-ads-campaign-setup-and-signal-quality.md",
                     "templates/meta-ads-campaign-blueprint.md"):
            self.assertTrue((ROOT / name).is_file(), name)
        for doc in ("SKILL.md", "WORKFLOWS.md"):
            self.assertIn("05k-meta-ads-campaign-setup-and-optimization.md", (ROOT / doc).read_text(encoding="utf-8"))
        ref = (ROOT / "references/meta-ads-campaign-setup-and-signal-quality.md").read_text(encoding="utf-8")
        for term in ("Conversions API", "event_id", "learning phase", "lookalike", "living in or recently in",
                     "back button", "comments", "ROAS", "CAC", "read-only"):
            self.assertIn(term, ref)
        self.assertIn("Comments", (ROOT / "workflows/07-launch-qa.md").read_text(encoding="utf-8"))

    def test_business_type_planning_and_advocacy_specialists(self):
        workflows = ("00-quickstart-first-30-days.md", "04c-pricing-research-and-tests.md", "04d-landing-page-build.md",
                     "05l-paid-social-and-video-platforms.md", "05m-marketplace-listings-and-ads.md",
                     "05n-local-marketing-and-reviews.md", "05o-b2b-saas-demand-generation.md",
                     "05p-media-plan-and-budget-allocation.md", "07a-launch-plan.md", "08h-marketing-review-cadence.md",
                     "09f-advocacy-reviews-referrals-and-reputation.md", "09g-subscription-retention-and-churn.md")
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        system = (ROOT / "WORKFLOWS.md").read_text(encoding="utf-8")
        for name in workflows:
            self.assertTrue((ROOT / "workflows" / name).is_file(), name)
            self.assertIn(name, skill)
            self.assertIn(name, system)
            self.assertIn("Stop conditions", (ROOT / "workflows" / name).read_text(encoding="utf-8"), name)
        for name in ("references/marketing-glossary.md", "references/privacy-consent-and-data-protection.md",
                     "references/reviews-referrals-loyalty-and-reputation.md",
                     "references/paid-platforms-tiktok-pinterest-youtube-linkedin-microsoft.md",
                     "templates/media-plan-and-budget.md", "templates/launch-plan.md", "templates/landing-page-brief.md",
                     "templates/advocacy-and-reputation-plan.md", "examples/brand-truth-example.md"):
            self.assertTrue((ROOT / name).is_file(), name)
        reviews = (ROOT / "references/reviews-referrals-loyalty-and-reputation.md").read_text(encoding="utf-8")
        for term in ("16 CFR Part 465", "gating", "suppression", "Holding statement"):
            self.assertIn(term, reviews)
        privacy = (ROOT / "references/privacy-consent-and-data-protection.md").read_text(encoding="utf-8")
        for term in ("GDPR", "Global Privacy Control", "Not legal advice"):
            self.assertIn(term, privacy)

    def test_landing_page_material(self):
        for name in ("references/landing-page-design-and-copy.md", "templates/landing-page-brief.md",
                     "templates/landing-page-review-scorecard.md", "examples/landing-page-brief-example.md",
                     "examples/landing-page-skeleton.html"):
            self.assertTrue((ROOT / name).is_file(), name)
        ref = (ROOT / "references/landing-page-design-and-copy.md").read_text(encoding="utf-8")
        for term in ("Rule of one", "message match", "Attention ratio", "MECLABS", "Advertisement",
                     "Labels above fields", "LCP", "WCAG", "Five-second test", "Message testing"):
            self.assertIn(term, ref)
        workflow = (ROOT / "workflows/04d-landing-page-build.md").read_text(encoding="utf-8")
        for link in ("landing-page-design-and-copy.md", "landing-page-review-scorecard.md", "check_page_meta.py"):
            self.assertIn(link, workflow)

    def test_core_handoffs_present(self):
        for name in ("WORKFLOWS.md", "templates/operating-brief.md", "templates/creative-production-brief.md", "templates/experiment-decision-log.md", "examples/workflow-from-research-to-sales.md"):
            self.assertTrue((ROOT / name).is_file(), name)

    def test_skill_links_to_orchestration(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("(WORKFLOWS.md)", skill)
        self.assertIn("decision packet", skill)

if __name__ == "__main__":
    unittest.main()
