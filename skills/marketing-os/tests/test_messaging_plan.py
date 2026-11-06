"""Structural tests for email/SMS creative and publication readiness."""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_messaging_plan", ROOT / "scripts" / "check_messaging_plan.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def email():
    return {"id": "email-01", "channel": "email", "status": "draft",
            "audience": "Eligible opted-in sample", "subject": "A message",
            "preheader": "Useful context", "body": "Useful, real, truthful content",
            "landing_url_or_action": "https://example.org/"}


def sms():
    return {"id": "sms-01", "channel": "sms", "status": "draft",
            "audience": "Eligible separate SMS permission sample",
            "body": "Brand: Helpful information. Reply STOP to opt out.",
            "landing_url_or_action": "https://example.org/"}


class MessagingPreflightTest(unittest.TestCase):
    def test_sample_drafts(self):
        data = json.loads((ROOT / "examples" / "messaging-plan-draft.json").read_text(encoding="utf-8"))
        self.assertEqual(validator.validate(data), [])

    def test_missing_email_subject_and_preheader(self):
        msg = email()
        msg.pop("subject")
        msg.pop("preheader")
        errors = validator.validate({"messages": [msg]})
        self.assertTrue(any("email subject" in e for e in errors))
        self.assertTrue(any("email preheader" in e for e in errors))

    def test_duplicate_ids(self):
        errors = validator.validate({"messages": [email(), email()]})
        self.assertTrue(any("duplicate message id" in e for e in errors))

    def test_unverified_sms_cannot_be_publish_ready(self):
        msg = sms()
        msg["status"] = "publish_ready"
        errors = validator.validate({"messages": [msg]})
        self.assertTrue(any("sms_specific_opt_in_verified" in e for e in errors))
        self.assertTrue(any("stop_help_tested" in e for e in errors))
        self.assertTrue(any("quiet_hours_checked" in e for e in errors))
        self.assertTrue(any("activated_by_authorized_human" in e for e in errors))

    def test_gmail_bulk_one_click(self):
        msg = email()
        msg["status"] = "publish_ready"
        msg["gmail_bulk_sender"] = True
        errors = validator.validate({"messages": [msg]})
        self.assertTrue(any("one-click unsubscribe" in e for e in errors))
        self.assertTrue(any("recipient_eligibility_verified" in e for e in errors))

    def test_email_sms_consent_separate(self):
        msg = sms()
        msg["status"] = "publish_ready"
        msg["recipient_eligibility_verified"] = True
        errors = validator.validate({"messages": [msg]})
        self.assertTrue(any("sms_specific_opt_in_verified" in e for e in errors))

    def test_ready_case_has_real_review_gates(self):
        msg = sms()
        msg.update({
            "status": "publish_ready",
            "recipient_eligibility_verified": True,
            "suppression_verified": True,
            "claims_verified": True,
            "destination_verified": True,
            "channel_policy_reviewed": True,
            "activated_by_authorized_human": True,
            "sms_specific_opt_in_verified": True,
            "sender_route_verified": True,
            "stop_help_tested": True,
            "quiet_hours_checked": True,
            "provider_segment_cost_checked": True,
            "approved_by": "Owner (example)",
        })
        self.assertEqual(validator.validate({"messages": [msg]}), [])


if __name__ == "__main__":
    unittest.main()
