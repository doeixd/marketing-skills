# Privacy, consent and data protection for marketing (reviewed 2026-11-09)

A map of the privacy rules that most often affect pixels, audiences, email/SMS and analytics, so workflows ask the right questions. **Not legal advice.** Laws change quickly and apply by where the *customer* is, not where the business is; confirm with counsel and the regulators' own guidance. Channel-specific rules are in [email deliverability and consent](email-deliverability-consent-and-reputation.md), [SMS compliance](sms-text-marketing-and-compliance.md) and [audiences and identity](audiences-identity-and-reverse-etl.md).

## 1. Questions to answer before collecting or activating data

1. Where are the people whose data this is (countries, US states)?
2. What data, for which purpose, on what legal basis or consent, and is that recorded?
3. Which vendors receive it (ad platforms, analytics, ESP, session recording), under what contract?
4. Can a person see, delete and opt out of it, and does that propagate to audiences and vendors?
5. Is any of it sensitive (health, precise location, children's data, finances, biometrics, sexual orientation, religion, immigration status)?

Unknown answers are `[NEEDS INPUT]` and block customer-data activation ([8G](../workflows/08g-audience-activation-and-utm-governance.md)).

## 2. The main regimes

| Regime | Core idea for marketers | Practical effect |
|---|---|---|
| **EU/EEA GDPR + ePrivacy; UK GDPR + PECR** | Opt-in consent before non-essential cookies, pixels and similar tracking; a lawful basis for all processing; rights of access, erasure and objection to direct marketing | Consent banner with a real "reject" choice, tags blocked until consent, Google Consent Mode v2 signals, records of consent, processor agreements, transfer safeguards |
| **US state comprehensive privacy laws** (California CCPA/CPRA plus roughly twenty states by 2026) | Mostly opt-**out**: of sale, "sharing" for cross-context behavioral ads, targeted advertising and some profiling; opt-in for sensitive data; rights to know, delete, correct | "Do Not Sell or Share / Your Privacy Choices" link, honoring opt-out requests across pixels and audience uploads, privacy notice listing purposes and recipients, data-protection assessments in several states |
| **Global Privacy Control (GPC)** | A browser signal that counts as a valid opt-out | Legally required to honor in California and, per trackers, about a dozen states (among them CO, CT, MD, MN, MT, NE, NH, NJ, OR, TX, DE); regulators have run joint enforcement sweeps on it. Treat GPC as an opt-out of sale/sharing/targeted ads everywhere it's practical |
| **Health and sensitive data** | Stricter consent; some laws apply regardless of company size | Washington's My Health My Data Act and similar laws; FTC actions over sending health-related browsing or purchase events to ad platforms. Don't send sensitive categories or infer them for targeting |
| **Children** | US COPPA (under 13, amended rule 2025), state age-appropriate design laws, GDPR child consent ages | Don't target or knowingly collect from children without the required parental consent; platforms restrict ad targeting to minors |
| **Canada (PIPEDA, CASL), Brazil (LGPD), Australia, others** | Consent and transparency with local variations; CASL requires consent for commercial email/text | Check per market before expanding campaigns |

Counts and state lists come from compliance trackers that disagree in detail; use the [IAPP state tracker](https://iapp.org/resources/article/us-state-privacy-legislation-tracker/) for current status.

## 3. What this means for common marketing tasks

- **Pixels and Conversions APIs:** server-side sending does not remove the need for consent or opt-out handling; pass consent state with events; don't send data for users who declined or opted out. Hashing is pseudonymization, not anonymization.
- **Customer-list audiences and lookalikes:** only people whose data may be used for advertising under the applicable law and your notice; remove opted-out and deleted people on a schedule; follow each platform's customer-data terms.
- **Session recordings and heatmaps:** mask form fields and on-screen personal data; get consent where required; several US wiretap-law claims have targeted undisclosed session replay and chat tools.
- **Email and SMS:** separate consent per channel; US email is opt-out (CAN-SPAM) but SMS needs prior express written consent (TCPA); EU/UK/Canada generally need opt-in for both, with narrow existing-customer exceptions.
- **UTMs and URLs:** never put names, emails, phone numbers or other personal data in URLs ([UTM governance](campaign-utm-and-identity-governance.md)).
- **AI tools and agents:** don't paste customer personal data into tools without a data-processing agreement and a permitted purpose; keep it out of the [marketing context file](../templates/marketing-context.md).
- **Data minimization and retention:** collect what the purpose needs, keep it only as long as needed, and document both.

## 4. Minimum hygiene checklist

- [ ] Privacy notice names the purposes, categories and types of recipients actually in use, including advertising.
- [ ] Consent banner (where required) blocks tags until choice; rejecting is as easy as accepting.
- [ ] GPC and "Do Not Sell or Share" opt-outs are honored and flow to ad platforms.
- [ ] Deletion and opt-out requests propagate to ESP, CRM, ad audiences and warehouse.
- [ ] Vendor contracts (DPAs) in place for platforms receiving personal data.
- [ ] No sensitive-category data sent to ad platforms or used for targeting.
- [ ] A named person owns privacy decisions and incident response.

## Sources

- [GDPR text](https://gdpr-info.eu/), [UK ICO: direct marketing and PECR](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/), [EDPB guidelines](https://www.edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en).
- [California Privacy Protection Agency](https://cppa.ca.gov/), [California AG: CCPA](https://oag.ca.gov/privacy/ccpa), [Global Privacy Control](https://globalprivacycontrol.org/), [IAPP US state privacy legislation tracker](https://iapp.org/resources/article/us-state-privacy-legislation-tracker/).
- [COPPA Rule, 16 CFR 312](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312), [Google Consent Mode](https://support.google.com/google-ads/answer/10000067).
- 2026 state-law summaries: [BakerHostetler Q1 2026](https://www.bakerlaw.com/insights/state-privacy-in-brief-q1-2026/), [McGuireWoods](https://blogs.mcguirewoods.com/2026/01/28/data-privacy-day-2026-what-changed-on-jan-1-and-what-to-watch-next/).
