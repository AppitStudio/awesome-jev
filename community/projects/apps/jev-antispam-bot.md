# Jev Anti-Spam Bot

[All projects](../README.md) · [Telegram bots](README.md#telegram-bots)

Minimal grammY Telegram bot that asks TypeSafe Jev whether group messages are spam and deletes only high-confidence linked matches.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/backmeupplz/jev_antispam_bot) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/backmeupplz/jev_antispam_bot#readme) — self-hosted bot; no separate managed product page. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-20**. Requires a Telegram bot token and `TYPESAFE_API_KEY`. Optional `DATABASE_URL` for chat/deletion statistics. Provider, Telegram, and optional Postgres hosting costs are separate. |
| Jev evidence | Inspected [src/spam.ts](https://github.com/backmeupplz/jev_antispam_bot/blob/b6476303472b824e3d4c4e07a8b9f97b09ac7dec/src/spam.ts): posts to `https://api.typesafe.ai/v1/systemone` with pinned model `jev-1.13.0` and a suite of Noul spam questions plus linkage. Offline `bun run check` mocks Telegram/classifier. Live Telegram moderation was not run. |
| Disclosure | Free source access does not include inference or hosting. Connecting the bot as a group admin with delete permission enables automatic deletions. AI-assisted, independently curated listing; no commercial relationship was declared. Inclusion is not endorsement. |
| Maintainer | [backmeupplz](https://github.com/backmeupplz). |
| Format | TypeScript / Bun grammY bot with optional PostgreSQL stats. |
| Platform and availability | Self-hosted process (Bun or Docker). Requires BotFather privacy mode disabled and **Delete messages** admin permission in each group. |
| Jev's role | Scores multiple spam Noul signals per message (and linkage across a short in-memory history); application code deletes only when the strongest signal meets `SPAM_THRESHOLD` (default 0.90) and fail-opens on classifier/Telegram errors. |
| Requirements | Bun (or Docker), Telegram bot token, TypeSafe API key. Optional private Postgres for stats only. |
| License | [MIT](https://github.com/backmeupplz/jev_antispam_bot/blob/b6476303472b824e3d4c4e07a8b9f97b09ac7dec/LICENSE). |

## When to use

Use it to moderate Telegram groups against common promo/scam patterns with calibrated Jev probabilities and explicit fail-open behavior. Prefer simpler keyword bots when you do not want provider calls. Distinct from the catalogued Discord [Jev Moderation Bot](jev-moderation-bot.md).

## How it works

Non-exempt group text/captions are evaluated in one Jev request. Admins, bot senders, and proven linked official channels are skipped. After a spam signal clears the threshold, a second linkage pass selects a contiguous recent suffix to delete with the current message. History is process-local (~10 messages / ~10 minutes) and is not persisted. Structured logs omit message text and sender identity. Optional Postgres records chat sightings and successful deletion counts only.

## Get started

```sh
git clone https://github.com/backmeupplz/jev_antispam_bot.git
cd jev_antispam_bot
git checkout b6476303472b824e3d4c4e07a8b9f97b09ac7dec
cp .env.example .env   # TELEGRAM_BOT_TOKEN, TYPESAFE_API_KEY
bun install
bun run check
# Live (deletes in groups where the bot is admin): bun start
```

Set BotFather privacy to **Disable**, then add the bot as a group admin with delete permission. Live `bun start` and `RUN_LIVE_JEV=1` tests are billable and were not run here.

## Examples and demos

- [src/*.test.ts](https://github.com/backmeupplz/jev_antispam_bot/tree/b6476303472b824e3d4c4e07a8b9f97b09ac7dec/src): deterministic handler/history/deletion tests with mocks.
- `src/spam.live.test.ts` is opt-in live regression (not executed).
- Docker build instructions are in the upstream README.

## Limits and data handling

Message text/captions and recent in-memory history projections go to TypeSafe when classified. Fail-open keeps messages on errors. Thresholds are operational policy, not measured spam accuracy. Media without captions is not classified. Optional stats DB never stores message text. Abrupt crashes can lose unflushed stats; moderation continues.

## Review and maintenance

Reviewed on **2026-09-20** at [commit b647630](https://github.com/backmeupplz/jev_antispam_bot/tree/b6476303472b824e3d4c4e07a8b9f97b09ac7dec): MIT. AI-assisted source review of `spam.ts`, bot handlers, README, and license. On Bun 1.4.2, **`bun run check`: 43 passed, 16 skipped** (live Jev and Postgres integration skips). No live Telegram or TypeSafe calls were performed.

Related: [Jev Moderation Bot](jev-moderation-bot.md) (Discord).
