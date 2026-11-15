# BanHammerBot (Telegram group moderation bot where Jev scores each message, avatar and recent history for ads and spam before any ban)

[All projects](../README.md) · [Telegram bots](README.md#telegram-bots)

Self-hosted Telegram bot that sends Jev the sender's display name, username, visible avatar, current message (with hidden link targets and images) and up to five recent messages, and asks three yes/no questions: unsolicited ad, spam and profile promotion. Scores from 0.70 go to review; only 0.98 or higher bans and deletes, and dry run is available per group. Adds a private admin menu, new-member mutes and an audit log in SQLite.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/crzidea/BanHammerBot) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/crzidea/BanHammerBot#readme) (source-built; no separate product site verified). |
| Pricing and access | Public source with no license file (all rights reserved by default); no purchase fee; you host it and pay TypeSafe usage on your key. Checked 2026-11-15. |
| Jev evidence | [`banhammerbot/decision.py`](https://github.com/crzidea/BanHammerBot/blob/12e0fc0dbccf40f7ac2bec8b609df099e234544c/banhammerbot/decision.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [crzidea](https://github.com/crzidea). Independently curated. |
| Format | Python bot (uv, Docker Compose) |
| Platform and availability | Telegram (self-hosted bot, long polling; no public server needed) |
| Jev's role | Jev scores each group message and its sender's profile for unsolicited ads, spam and profile promotion; the bot's thresholds decide review or ban. |
| Requirements | Python 3.11+ and uv (or Docker), a Telegram bot token with Ban users and Delete messages rights, and a `TYPESAFE_API_KEY`. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Remove ad and spam accounts from Telegram groups with confidence thresholds and dry run.
- Mismatch: audio or video spam; other media is described by type and caption only.

## How it works

`banhammerbot/config.py` pins `jev-1.14.0` at `https://api.typesafe.ai/v1/systemone`; `banhammerbot/decision.py` builds the request (text plus images) and validates the three Noul answers; API failures or bad probabilities never ban. Integration evidence: [`banhammerbot/decision.py`](https://github.com/crzidea/BanHammerBot/blob/12e0fc0dbccf40f7ac2bec8b609df099e234544c/banhammerbot/decision.py).

## Get started

Create the bot, fill in the two credentials, check, then run (start in dry run).

```sh
git clone https://github.com/crzidea/BanHammerBot && cd BanHammerBot
cp .env.example .env && chmod 600 .env   # TELEGRAM_BOT_TOKEN, TYPESAFE_API_KEY
uv sync --frozen
uv run banhammerbot --check
uv run banhammerbot
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/crzidea/BanHammerBot/blob/12e0fc0dbccf40f7ac2bec8b609df099e234544c/README.md](https://github.com/crzidea/BanHammerBot/blob/12e0fc0dbccf40f7ac2bec8b609df099e234544c/README.md)

## Limits and data handling

Group messages, profile names and avatars are sent to TypeSafe on your key. Jev image input is experimental per TypeSafe; the default thresholds are starting points, not measured accuracy. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 12e0fc0dbccf](https://github.com/crzidea/BanHammerBot/tree/12e0fc0dbccf40f7ac2bec8b609df099e234544c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
