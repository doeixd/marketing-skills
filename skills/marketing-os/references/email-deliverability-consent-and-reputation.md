# Email deliverability, sender authentication, consent and list quality

Reviewed 2026-11-06. Use [Deliverability Workflow 9E](../workflows/09e-email-deliverability-and-list-health.md), [Sender/Consent Audit](../templates/email-deliverability-and-consent-audit.md), [Email Strategy](email-marketing-strategy-copy-and-creative.md) and [SMS Legal Reference](sms-text-marketing-and-compliance.md).

## 1. Sender legitimacy and deliverability are distinct

**Delivery** means the receiving service accepted a message; **inbox placement** means it reached an inbox instead of spam/promotions or being blocked. No ESP can guarantee inbox placement. Segmentation and great copy cannot compensate for broken DNS, poor authentication, complaints, unwanted messages or bad lists.

For marketing emails check the **actual sending domain and provider** and who owns DNS/verification. Distinguish SPF authorization, DKIM cryptographic signature, DMARC authentication/alignment/policy, reverse DNS and TLS, from optional BIMI logos. Never falsely label a domain "authenticated" because someone supplied DNS setup instructions; verify live provider reports or DNS. DMARC `p=none` can meet Gmail bulk-sender policy but is monitoring, not active spoof-rejection enforcement.

## 2. Gmail requirements (as of Nov 2026; verify before launch)

Google [Gmail Sender Guidelines](https://support.google.com/mail/answer/81126):
- All senders to personal Gmail: at least **SPF or DKIM**, valid forward/reverse DNS (PTR), TLS, RFC 5322-compliant headers and spam rate below 0.3% in Postmaster Tools; Google advises aiming below 0.1%.
- Bulk senders (approximately **5,000 or more messages/day to personal Gmail** from the same primary domain): **SPF and DKIM**, **DMARC** (policy can be `p=none`), alignment of visible From domain with SPF or DKIM, plus compliant list-unsubscribe for marketing/subscribed messages.
- Bulk commercial/subscribed messages need **RFC 8058 one-click unsubscribe** with appropriate `List-Unsubscribe` and `List-Unsubscribe-Post` headers **and** a visible body unsubscribe link. A body-only link or `mailto:` header does not fulfill Google's one-click requirement for eligible bulk promotional sends.
- Google bulk sender classification persists after meeting threshold; consult [Sender Guidelines FAQ](https://support.google.com/mail/answer/14229414). Gmail began ramping enforcement November 2025. Don't assume 4,999 always avoids rules or requirements of other inbox providers.
- Gmail "Promotions" tab classification is not necessarily spam, and third-party claims about defeating it aren't reliable.

Also inspect [Yahoo Sender Best Practices](https://senders.yahooinc.com/best-practices/) and any Microsoft/ESP policy applicable to recipient mix. Provider requirements evolve. Monitor Google Postmaster Tools compliance, spam complaint rate, domain reputation, DKIM/authentication and delivery deferrals; not all small senders have enough volume for meaningful Postmaster data.

## 3. CAN-SPAM: correct US distinctions

The [FTC CAN-SPAM guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) governs *commercial* email, including B2B. It generally does **not** require advance opt-in consent for all US commercial email, but it does require truthful headers/subject, correct advertiser identity, required postal address, clear opt-out, honoring requests within **10 business days**, functional opt-out for **at least 30 days** after sending, and no deceptive content. Consent and platform policies may be stricter, as can rules in other countries. **Best marketing practice is affirmative, recorded opt-in**; don't represent that as exactly the same thing as US CAN-SPAM law.

A bona fide transactional/relationship message is treated differently under CAN-SPAM. **Adding promotional content can affect its primary purpose**, so do not label cart abandonment, product recommendations or marketing offers "transactional" merely because a customer has an order history.

## 4. International and state/sector caveats

UK [ICO PECR electronic marketing guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/) was updated April 2026 and distinguishes individuals vs corporate subscribers, specific consent vs narrowly defined existing-customer "soft opt-in"; email and SMS consent may need to be separate. EU GDPR/ePrivacy rules, Canada's CASL and US state/privacy laws require jurisdiction-specific review. Do not infer one global legal policy. Legal counsel or compliance owner should review large-scale/multi-country sends and regulated categories.

**Consent register**: contact identifier, communication **channel**, brand/sender, country/state, source/form wording, timestamp/time zone, proof (IP/form version only if lawfully collected), permitted purposes, opt-in/soft-opt-in basis, withdrawal/suppression, third-party consent restrictions, age/sector limits where relevant, audit owner and deletion policy. Reconsent requires genuine affirmative action; don't silently override an opt-out during data migration.

## 5. List health and reputation

Prioritize real explicit subscribers, not purchased/scraped/generic cold lists or unsolicited imports. For a new domain/large list, **gradual volume ramp** and engagement from genuine recipients matters more than magic "warm-up" software; never fabricate opens/clicks or use bots to inflate engagement. Monitor complaints, bounced/invalid addresses, suppression lists, opt-outs, old audiences, and permission/source quality.

List hygiene workflow:
1. Reconcile actual ESP suppression and source.
2. Segment by permission, activity and useful preference signals, acknowledging that open-based inactivity is unreliable due to Apple MPP.
3. Stop sending marketing to hard bounces/complainers and unsubscribed addresses; handle uncertain addresses thoughtfully (do not automatically delete transactional account contact).
4. Reduce frequency/ask preferences for dormant recipients where permitted; avoid repeatedly emailing uninterested recipients "for reactivation".
5. Validate real unsubscribe route, processing time, suppression propagation to all sending systems and backup.
6. Separate lifecycle/campaign/transactional streams when technically warranted, but do not assume domain separation fixes poor reputation.

**Complaint thresholds** are guidance/requirements of inbox provider and can vary. Do not claim a "good open rate" guarantees deliverability.

## 6. Diagnostic decision tree

| Signal | Investigate | Correct action |
|---|---|---|
| Gmail block/defer or auth failures | SPF/DKIM/DMARC alignment, PTR, TLS, provider config | Actual DNS/provider remediation with owner approval |
| Sudden spam complaint spike | Audience origin, frequency, promises, opt-out, campaign topic | Pause affected marketing, correct consent/list/message |
| Low clicks but apparent high opens | Apple MPP, irrelevant promise, broken links, scanners | Check actual verified site visits and intended recipient value |
| High unsubscribe rate | Wrong audience, unmet frequency expectations, poor targeting | Relevance/frequency/preference controls |
| Bounces | Bad import/stale data, signup typos, provider issue | Real hygiene, confirmed opt-in, suppression |
| Provider complaint but "all sent" | Accepted != inbox placed, domain reputation | Sender diagnostics/postmaster and complaint behavior |
| Marketing emails to unsubscribed contacts | Duplicated ESP/automation, sync lag or missing exclusion | Stop, audit sync, reconcile suppression, remediate before further sends |

## 7. Sources

- [Google Gmail Sender Guidelines](https://support.google.com/mail/answer/81126), [Sender FAQ](https://support.google.com/mail/answer/14229414)
- [Google Postmaster Tools](https://postmaster.google.com/)
- [Yahoo Sender Best Practices](https://senders.yahooinc.com/best-practices/)
- [FTC CAN-SPAM Guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)
- [UK ICO PECR electronic marketing 2026](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/)
- [Klaviyo Deliverability Metrics](https://help.klaviyo.com/hc/en-us/articles/115000201131)
- [Klaviyo Apple MPP](https://help.klaviyo.com/hc/en-us/articles/4416803987739)
