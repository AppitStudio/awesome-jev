# telegram-resender (Telegram client that forwards matching messages, with an optional Jev categories gate)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Telegram client that runs under your own user account (Telethon, not a Bot API bot), watches chats, channels and folders, and forwards matching messages to a target chat, forum topic or webhook with a link back to the source. Triggers include word lists, OpenAI prompt matches and reactions; an optional categories gate classifies each message with one Jev Choice question. Read-only: it never sends messages on your behalf.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/popstas/telegram-resender) |
| Maintainer | [popstas](https://github.com/popstas). Independently curated. |
| Format | Python service (Telethon) |
| Requirements | Python, Telegram API credentials for your account; a TypeSafe API key only for the categories gate. |
| License | [MIT](https://github.com/popstas/telegram-resender/blob/642d16540d6ec6f9f115db5366c6659b8c8e35d8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/categories.py`](https://github.com/popstas/telegram-resender/blob/642d16540d6ec6f9f115db5366c6659b8c8e35d8/src/categories.py) at the pinned commit. |

## When to use

- Collect relevant messages from many Telegram chats into one place.
- Mismatch: uses your personal account session; Jev is optional.

## How it works

`src/categories.py` uses the official `typesafe_sdk` (`AsyncTypeSafeClient`, `jev-latest` by default) to ask a single Choice question per message and forward only the configured categories. Integration evidence: [`src/categories.py`](https://github.com/popstas/telegram-resender/blob/642d16540d6ec6f9f115db5366c6659b8c8e35d8/src/categories.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/popstas/telegram-resender && cd telegram-resender
pip install -r requirements.txt
cp config-example.yml config.yml   # then edit and run per the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/popstas/telegram-resender#readme](https://github.com/popstas/telegram-resender#readme)

## Limits and data handling

Watched message text goes to TypeSafe only when the categories gate is configured (and to OpenAI for prompt triggers).

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 642d16540d6e](https://github.com/popstas/telegram-resender/tree/642d16540d6ec6f9f115db5366c6659b8c8e35d8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
