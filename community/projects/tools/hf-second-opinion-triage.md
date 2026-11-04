# HF Second Opinion Triage (Splunk Enterprise Security app that shows a Jev-suggested disposition and urgency next to the ES AI SOC Analyst; Japanese and English docs)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Splunk app, in public beta, that sends each Enterprise Security finding to a decision model (TypeSafe Jev by default, or a compatible model) and shows a suggested disposition (true positive, false positive, benign, undetermined) and urgency, with a one-click action on a finding. An LLM you choose can explain a suggestion, and it can be written back as a Note; ES fields are never changed and analysts decide. The README reports 32 of 33 dispositions right on its own labelled set of BOTS v3 findings.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hidefujimori/hf-second-opinion-triage) |
| Maintainer | [hidefujimori](https://github.com/hidefujimori). Independently curated. |
| Format | Splunk app (`.spl` package, Python and React), English and Japanese UI and docs |
| Requirements | Splunk Enterprise 10.x or Splunk Cloud with Enterprise Security 8.x, and your own TypeSafe key; an LLM key only if you want explanations. |
| License | [Apache-2.0](https://github.com/hidefujimori/hf-second-opinion-triage/blob/5b1ccdfe9f6d82f09c9abeb39efb65a5fc069f0f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/second_opinion_triage/bin/jev_triage/jev_client.py`](https://github.com/hidefujimori/hf-second-opinion-triage/blob/5b1ccdfe9f6d82f09c9abeb39efb65a5fc069f0f/app/second_opinion_triage/bin/jev_triage/jev_client.py) at the pinned commit. |

## When to use

- Add an independent, structured second opinion on SOC findings and compare it with the ES AI SOC Analyst result.
- Mismatch: it is a beta tested on Splunk 10.4.x with ES 8.7.x, and the accuracy figure comes from a 33-finding set the author labelled.

## How it works

`jev_client.py` posts each finding's facts and typed questions to `https://api.typesafe.ai/v1/systemone` (or another System One endpoint you configure), and the app turns the probabilities into a suggested disposition and urgency with daily limits on automatic calls. Integration evidence: [`app/second_opinion_triage/bin/jev_triage/jev_client.py`](https://github.com/hidefujimori/hf-second-opinion-triage/blob/5b1ccdfe9f6d82f09c9abeb39efb65a5fc069f0f/app/second_opinion_triage/bin/jev_triage/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
# Splunk: Apps > Manage Apps > Install app from file > second_opinion_triage-<version>.spl
# then open the app's Setup page and add your Jev key (see docs/en/quickstart.md)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- English quick start: [github.com/hidefujimori/hf-second-opinion-triage/blob/5b1ccdfe9f6d82f09c9abeb39efb65a5fc069f0f/docs/en/quickstart.md](https://github.com/hidefujimori/hf-second-opinion-triage/blob/5b1ccdfe9f6d82f09c9abeb39efb65a5fc069f0f/docs/en/quickstart.md)
- Data sent outside Splunk: [github.com/hidefujimori/hf-second-opinion-triage/blob/5b1ccdfe9f6d82f09c9abeb39efb65a5fc069f0f/docs/en/reference.md](https://github.com/hidefujimori/hf-second-opinion-triage/blob/5b1ccdfe9f6d82f09c9abeb39efb65a5fc069f0f/docs/en/reference.md)

## Limits and data handling

Finding facts go from the Splunk search head to TypeSafe (and finding text to your LLM when you ask for an explanation) on your keys, so review the README's data-sent section before enabling it on production data. It is a beta that only suggests; it never changes ES fields. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 5b1ccdfe9f6d](https://github.com/hidefujimori/hf-second-opinion-triage/tree/5b1ccdfe9f6d82f09c9abeb39efb65a5fc069f0f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
