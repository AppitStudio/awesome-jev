# tg-bot-template (Telegram support-bot template that answers from your docs, with Jev for intent and bad-answer checks)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python template for a Telegram bot that answers questions about a product from its docs and code, extracted from a production bot: OpenRouter model fallback ladder, message batching, screenshot-to-text, feedback, access control and admin commands, with 878 tests. With a TypeSafe key, Jev classifies message intent (small talk gets a short answer) and judges borderline degenerate model replies; without it those checks fall back to regexes. Code comments in Russian.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/octrow/tg-bot-template) |
| Maintainer | [octrow](https://github.com/octrow). Independently curated. |
| Format | Python template (python-telegram-bot 22, SQLite, uv) |
| Requirements | Python via uv; a Telegram bot token; an OpenRouter key; optionally `TYPESAFE_API_KEY` for the Jev checks. |
| License | [MIT](https://github.com/octrow/tg-bot-template/blob/5eaabb5871ca10463ab0f3668c1f650955008097/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/tgbot/jev.py`](https://github.com/octrow/tg-bot-template/blob/5eaabb5871ca10463ab0f3668c1f650955008097/src/tgbot/jev.py) at the pinned commit. |

## When to use

- Start a docs-grounded support bot with a cheap typed classifier guarding intent and reply quality.
- Mismatch: Jev is optional; without the key, intent classification is off.

## How it works

`jev.py` sends the text with one or more choice questions to `api.typesafe.ai/v1/systemone` (`jev-latest`) in a single request and fails open, returning no probabilities and a logged reason on any error. Integration evidence: [`src/tgbot/jev.py`](https://github.com/octrow/tg-bot-template/blob/5eaabb5871ca10463ab0f3668c1f650955008097/src/tgbot/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync --extra dev
cp deploy/env.example .env   # bot token, keys (TYPESAFE_API_KEY optional)
uv run python -m tgbot
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Template-copy decision record: [github.com/octrow/tg-bot-template/blob/5eaabb5871ca10463ab0f3668c1f650955008097/docs/adr/0006-template-is-a-copy.md](https://github.com/octrow/tg-bot-template/blob/5eaabb5871ca10463ab0f3668c1f650955008097/docs/adr/0006-template-is-a-copy.md)

## Limits and data handling

With the key set, user messages and candidate bot replies are sent to TypeSafe. Copies of the template do not receive upstream updates. Not affiliated with Telegram or TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 5eaabb5871ca](https://github.com/octrow/tg-bot-template/tree/5eaabb5871ca10463ab0f3668c1f650955008097). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
