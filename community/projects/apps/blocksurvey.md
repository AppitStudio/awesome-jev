# BlockSurvey (privacy-first survey platform that uses Jev to judge answers before its AI follow-ups and to check surveys)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hosted survey and form platform with end-to-end encryption, AI survey creation, AI follow-up questions and AI analysis. BlockSurvey's engineering blog describes four places it uses Jev: judging each open answer (genuine attempt, wants to stop, matching sentiment) before the language model writes a follow-up; checking whether open-ended questions could identify a person before a survey is marked anonymous; choosing the question type when a survey is built with AI; and scoring a draft survey on rubric items in parallel batches.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://blocksurvey.io) |
| Tags | `Closed source` · `Freemium` · `Commercial` |
| Product homepage | [blocksurvey.io](https://blocksurvey.io) |
| Pricing and access | [Pricing](https://blocksurvey.io/pricing): Free plan ($0, 10 responses, 3 AI survey creations), Standard $49/month, Premium $99/month, Team $149/month (lower prices billed yearly) and Enterprise on request; paid plans have a 14-day free trial. Checked **2026-11-19**; checkout and trial terms were not tested. AI follow-up questions are listed from the Premium plan. |
| Jev evidence | Vendor documentation: the engineering post [How BlockSurvey uses JEV](https://blocksurvey.io/engineering/how-blocksurvey-uses-jev) (Hari S K, 2026-11-01) describes each Jev use and the fallbacks, and the company [X post](https://x.com/blocksurvey/status/2123409857227235550) (2026-11-19) points to it. The implementation was not inspected. |
| Disclosure | Closed source, commercial product. Source was not inspected; Jev use is documented by the vendor, not independently observed API traffic. Independently curated for Awesome Jev; no affiliation or commercial relationship with the vendor. Inclusion is not an endorsement. Discovered via X ([post](https://x.com/blocksurvey/status/2123409857227235550)). |
| Maintainer | [BlockSurvey](https://blocksurvey.io) ([@blocksurvey](https://x.com/blocksurvey)). |
| Format | Hosted web application for surveys and forms. |
| Platform and availability | Web (hosted). |
| Jev's role | Per the vendor: decides whether an answer deserves an AI follow-up, whether a question asks for identifying information, which question type a label needs, and how a draft survey scores on rubric items. A language model still writes the follow-ups and summaries. |
| Requirements | A BlockSurvey account; a paid plan for higher response limits and AI follow-ups. |
| License | Proprietary hosted service. No public repository found. |

## When to use

Use BlockSurvey if you want hosted, encrypted surveys with AI follow-ups that skip junk or finished respondents, and a check before marking a survey anonymous. It is a commercial product, not a library. Mismatch: if you need to inspect or self-host the decision logic.

## How it works

Per the vendor's post, a decision comes before any writing. For follow-ups, Jev judges the answer first and the language model is called only when needed; if Jev is slow or unavailable the check is skipped and the language model is called anyway. For anonymity, a survey is not marked anonymous unless Jev can answer. Question-type choice uses rules first, then a Jev Choice, with the earlier model as fallback. Survey scoring sends rubric items to Jev in parallel and weights uncertain answers less in code. No API calls were observed for this listing.

## Get started

This path follows the public site; it was not executed (no sign-up).

1. Open [blocksurvey.io](https://blocksurvey.io) and start on the free plan or a 14-day trial.
2. Create a survey (with or without AI) and turn on AI follow-up questions on a plan that includes them.
3. Review responses and follow-ups before relying on the automation.

## Examples and demos

- [How BlockSurvey uses JEV](https://blocksurvey.io/engineering/how-blocksurvey-uses-jev) (vendor engineering post).
- [Company X post with a demo video](https://x.com/blocksurvey/status/2123409857227235550) (vendor material; video not reproduced).

## Limits and data handling

Closed source: the Jev questions, thresholds and fallbacks were described by the vendor but not inspected. Survey answers are processed by BlockSurvey and, per the vendor, by TypeSafe and a language model provider for the AI features; check BlockSurvey's privacy and data-processing terms. Response limits and AI quotas depend on the plan.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) with AI assistance. Primary sources: [blocksurvey.io/engineering/how-blocksurvey-uses-jev](https://blocksurvey.io/engineering/how-blocksurvey-uses-jev) and [blocksurvey.io/pricing](https://blocksurvey.io/pricing) (both fetched 2026-11-19) and the company's [X post](https://x.com/blocksurvey/status/2123409857227235550) (2026-11-19). No sign-up, payment or live use. Catalog de-dupe found no existing BlockSurvey listing.
