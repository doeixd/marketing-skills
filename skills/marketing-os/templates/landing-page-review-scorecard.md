# Landing page review scorecard

For reviewing a draft or a live page ([Workflow 4D](../workflows/04d-landing-page-build.md), [4A](../workflows/04a-conversion-rate-optimization.md)). Criteria come from the [landing page reference](../references/landing-page-design-and-copy.md). Score what you can observe; mark anything that needs data or access as `[NEEDS INPUT]`. The score is a way to find and rank problems, not a prediction of conversion.

**Page:** ___ · **Traffic source reviewed with it (ad, email, keyword):** ___ · **Device checked:** phone ☐ desktop ☐ · **Date:** ___

Score each line 0 (absent or wrong), 1 (partly), 2 (clearly yes). Note the evidence.

## A. Match and focus
| # | Question | 0–2 | Evidence / note |
|---|---|---|---|
| A1 | Headline continues the promise and words of the ad, email or search that led here | | |
| A2 | The page's look matches what was clicked (product, image, colors) | | |
| A3 | One reader, one promise, one offer, one primary action | | |
| A4 | Few ways to leave: no unrelated navigation or competing buttons | | |

## B. First screen
| # | Question | 0–2 | Evidence / note |
|---|---|---|---|
| B1 | A stranger could say what is offered and for whom after five seconds | | |
| B2 | Headline is specific: makes sense without the logo; a competitor couldn't say it | | |
| B3 | Real product shown, ideally in use | | |
| B4 | One checkable proof cue near the claim | | |
| B5 | Button names the outcome; reassurance under it; visible on a phone without scrolling | | |

## C. Persuasion and proof
| # | Question | 0–2 | Evidence / note |
|---|---|---|---|
| C1 | Features are stated as fact → benefit and shown, not listed | | |
| C2 | The buyer's real objections are answered, in plain words, including limits | | |
| C3 | Proof is specific, attributed, and matches the promise | | |
| C4 | Price, total cost, what's included and terms are clear before the click | | |
| C5 | Risk reversal (returns, trial, cancellation) is stated accurately | | |
| C6 | Copy is plain: short sentences, common words, specifics over adjectives | | |

## D. Friction
| # | Question | 0–2 | Evidence / note |
|---|---|---|---|
| D1 | Form asks only for what the next step needs; labels above fields; clear errors | | |
| D2 | The page says what happens after the action | | |
| D3 | Loads fast on a phone; nothing shifts while loading | | |
| D4 | No pop-up on arrival; nothing blocks the content | | |
| D5 | Confirmation page confirms, sets expectations and offers one next step | | |

## E. Trust, access and honesty
| # | Question | 0–2 | Evidence / note |
|---|---|---|---|
| E1 | Every claim is supported; no invented reviews, numbers or urgency | | |
| E2 | Company identity, contact, privacy and terms are present | | |
| E3 | Accessible basics: one `h1`, heading order, alt text, contrast, keyboard, labels | | |
| E4 | Advertorial or listicle is labeled "Advertisement" above the headline (n/a otherwise) | | |
| E5 | No dark patterns | | |

## Result
| Section | Score | Max |
|---|---|---|
| A. Match and focus | | 8 |
| B. First screen | | 10 |
| C. Persuasion and proof | | 12 |
| D. Friction | | 10 |
| E. Trust, access and honesty | | 10 |

**Any 0 in A1, B1, C4, E1 or E5 is a blocker regardless of total.**

## Prioritized fixes
| # | Problem (with evidence) | Likely cause (motivation mismatch / unclear value / friction / anxiety / distraction) | Fix | Effort | Fix now or test? |
|---|---|---|---|---|---|

Checker output (`python scripts/check_page_meta.py`):

What could not be assessed without data or access:
