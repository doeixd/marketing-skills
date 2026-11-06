"""Ensure the modular marketing workflows and handoffs remain present."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class TestWorkflows(unittest.TestCase):
    def test_all_nine_workflows_present(self):
        files = sorted((ROOT / "workflows").glob("[0-9][0-9]-*.md"))
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

    def test_core_handoffs_present(self):
        for name in ("WORKFLOWS.md", "templates/operating-brief.md", "templates/creative-production-brief.md", "templates/experiment-decision-log.md", "examples/workflow-from-research-to-sales.md"):
            self.assertTrue((ROOT / name).is_file(), name)

    def test_skill_links_to_orchestration(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("(WORKFLOWS.md)", skill)
        self.assertIn("decision packet", skill)

if __name__ == "__main__":
    unittest.main()
