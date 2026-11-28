# Fine Print by Dhananjay Pandit (Telegram agent that watches services' terms and uses Jev to flag material changes)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Hacksgiving 2026 agent on a Fly.io Sprite that watches the terms pages of the services each member uses, diffs them daily, and has Jev judge each changed section: material or not, category, who it favours, opt-out available, severity. Members get a Telegram (or email) message only for material changes such as new arbitration clauses, AI training on your data or auto-renewal, and opt-out deadlines go into their calendar. An `/ask` mode answers questions about your watched terms with quotes checked against stored text.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/djpandit007/fly-io-hacksgiving) |
| Maintainer | [Dhananjay Pandit](https://github.com/djpandit007). Independently curated. |
| Format | Python (FastAPI) agent + Telegram bot on Fly.io Sprites |
| Requirements | Python with uv; for live use a Fly.io Sprite, a Telegram bot token and a provider serving Jev (OpenCode in the author's setup). |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/judge.py`](https://github.com/djpandit007/fly-io-hacksgiving/blob/ca3247168d44e8cd0202536e21a85d343410c65b/app/judge.py) at the pinned commit. |

## When to use

- People who want to know when terms they agreed to change in a way that matters.
- Mismatch: legal review; summaries are AI-generated.

## How it works

`app/judge.py` sends each changed clause with `noul`, `choice` and `score` questions to Jev (`jev-1.14`, served through OpenCode) and keeps only material changes for the writer agent. Integration evidence: [`app/judge.py`](https://github.com/djpandit007/fly-io-hacksgiving/blob/ca3247168d44e8cd0202536e21a85d343410c65b/app/judge.py).

## Get started

Run the tests and the app locally with your own provider settings.

```sh
git clone https://github.com/djpandit007/fly-io-hacksgiving && cd fly-io-hacksgiving
uv sync
cp .env.example .env   # provider URLs and keys
uv run pytest
uv run uvicorn app.main:app --reload --port 8080
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Privacy and limits: [github.com/djpandit007/fly-io-hacksgiving#privacy-and-limits](https://github.com/djpandit007/fly-io-hacksgiving#privacy-and-limits)

## Limits and data handling

Terms pages, documents members send and questions are read by the operator's AI providers; only deadlines, watchlists and verified emails are kept. Membership is invite-code only. No licence file, so no reuse rights are granted.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit ca3247168d44](https://github.com/djpandit007/fly-io-hacksgiving/tree/ca3247168d44e8cd0202536e21a85d343410c65b). Inspected the README (including privacy and limits) and `app/judge.py` at the pinned commit; no licence file present. Not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
