# JEV Contact Center QA by M8 Apps (scores Spanish support-call transcripts against a QA rubric with Jev)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

A Python CLI that redacts identifiers from Spanish support-call transcripts, sends one Jev request per interaction against an eight-item weighted rubric, computes pass/fail with critical items, routes uncertain cases to a human review queue, and produces campaign HTML reports plus agreement statistics against human labels. Includes an offline fake client.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/m8appz-dotcom/jev-contact-center-qa) |
| Maintainer | [m8appz-dotcom](https://github.com/m8appz-dotcom). Independently curated. |
| Format | Python CLI (standard library) |
| Requirements | Python 3.12+; `TYPESAFE_API_KEY` for live evaluation (the offline walkthrough uses a fake client). |
| License | [Portfolio source review notice (no reuse license granted)](https://github.com/m8appz-dotcom/jev-contact-center-qa/blob/c1c09c022d0ea5abef24767e221e897351add752/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevqa/jev_client.py`](https://github.com/m8appz-dotcom/jev-contact-center-qa/blob/c1c09c022d0ea5abef24767e221e897351add752/jevqa/jev_client.py) at the pinned commit. |

## When to use

- See a complete contact-center QA pipeline with redaction, review routing and human-label comparison built on Jev.
- Mismatch: reuse in your own product; the license notice grants no reuse rights.

## How it works

`jevqa/jev_client.py` is a synchronous client for `POST /v1/systemone` at `https://api.typesafe.ai`; `jevqa/rubric.py` builds the typed questions and `jevqa/scoring.py` applies the weights and review routing. Integration evidence: [`jevqa/jev_client.py`](https://github.com/m8appz-dotcom/jev-contact-center-qa/blob/c1c09c022d0ea5abef24767e221e897351add752/jevqa/jev_client.py).

## Get started

Follow the offline quickstart in the README, then set your key for live runs.

```sh
git clone https://github.com/m8appz-dotcom/jev-contact-center-qa && cd jev-contact-center-qa
# offline walkthrough: see docs/DEMO.md
python scripts/eval_jev.py --fake
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Walkthrough: [github.com/m8appz-dotcom/jev-contact-center-qa/blob/c1c09c022d0ea5abef24767e221e897351add752/docs/DEMO.md](https://github.com/m8appz-dotcom/jev-contact-center-qa/blob/c1c09c022d0ea5abef24767e221e897351add752/docs/DEMO.md)
- Rubric: [github.com/m8appz-dotcom/jev-contact-center-qa/blob/c1c09c022d0ea5abef24767e221e897351add752/rubrics/soporte_es.json](https://github.com/m8appz-dotcom/jev-contact-center-qa/blob/c1c09c022d0ea5abef24767e221e897351add752/rubrics/soporte_es.json)

## Limits and data handling

Redacted transcript text is sent to TypeSafe. Portfolio project; the notice grants no additional reuse license, so do not treat it as open source.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit c1c09c022d0e](https://github.com/m8appz-dotcom/jev-contact-center-qa/tree/c1c09c022d0ea5abef24767e221e897351add752). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
