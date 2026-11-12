# callscore (call-center quality scoring where Jev only picks closed options)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Demo pipeline that turns call-center recordings into a SQLite catalog of agent, team, quality score, critical failures and KPIs: local transcription and code handle measurement and scores, and Jev (via OpenRouter) only answers closed questions about each transcript, with unsure answers flagged for review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/epifaneia/callscore) |
| Maintainer | [epifaneia](https://github.com/epifaneia). Independently curated. |
| Format | Python pipeline (Apache-2.0; README in English and Spanish) |
| Requirements | Python, faster-whisper for local transcription, and an OpenRouter key; a simulated engine runs offline for free. |
| License | [Apache-2.0](https://github.com/epifaneia/callscore/blob/5b25454be2cff136c45338c4e1ccc7735ce847a2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`clients/jev.py`](https://github.com/epifaneia/callscore/blob/5b25454be2cff136c45338c4e1ccc7735ce847a2/clients/jev.py) at the pinned commit. |

## When to use

- Score call quality with a model that never writes free text.
- See a worked design of code guardrails around a decision model.
- Mismatch: demo with artificial calls only.

## How it works

`clients/jev.py` posts to OpenRouter's decisions endpoint with the pinned model `typesafe/jev-1.14`; the output guardrail checks Jev's decisions against what was measured from the audio and every coaching tip comes from the form, not the model. Integration evidence: [`clients/jev.py`](https://github.com/epifaneia/callscore/blob/5b25454be2cff136c45338c4e1ccc7735ce847a2/clients/jev.py).

## Get started

Install the requirements and run the offline demo on the sample transcripts.

```sh
pip install -r requirements.txt
cp .env.example .env
python run.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/epifaneia/callscore/blob/5b25454be2cff136c45338c4e1ccc7735ce847a2/README.md](https://github.com/epifaneia/callscore/blob/5b25454be2cff136c45338c4e1ccc7735ce847a2/README.md)

## Limits and data handling

Transcripts are sent to OpenRouter/TypeSafe on your key; audio is transcribed locally.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 5b25454be2cf](https://github.com/epifaneia/callscore/tree/5b25454be2cff136c45338c4e1ccc7735ce847a2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
