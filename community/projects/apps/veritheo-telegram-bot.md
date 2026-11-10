# Veritheo (Spanish theology Telegram bot with Jev guards and routing)

[All projects](../README.md) · [Telegram bots](README.md#telegram-bots)

Spanish-language Telegram bot that answers theology questions, verifies claims and argues the opposing view, using Jev for reply routing, spam and prompt-injection guards and other typed checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alambertt/veritheo) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/alambertt/veritheo#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source; no license file on the reviewed commit. You host the bot and pay for Telegram-side hosting and model/TypeSafe usage. Checked 2026-11-10. |
| Jev evidence | [`services/typesafe.ts`](https://github.com/alambertt/veritheo/blob/3871ca5ec4915ff90aaba1d064c7225f871a27c0/services/typesafe.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [alambertt](https://github.com/alambertt). Independently curated. |
| Format | Telegram bot (TypeScript/Bun, source only) |
| Platform and availability | Telegram (self-hosted bot; source build) |
| Jev's role | Jev routes replies and runs typed guard checks (spam, prompt injection, claim verification) before the chat model answers. |
| Requirements | Bun, a Telegram bot token, the chat-model keys in `.env.example`, and `TYPESAFE_API_KEY` for the Jev features. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- See many small Jev gates wired into one chat bot, each behind its own flag.
- Run a Spanish theology Q&A bot in a group or private chat.
- Mismatch: no license file, so the code is source-available, not open source; you host it yourself.

## How it works

`services/typesafe.ts` uses `@typesafe-ai/sdk` with a 0.85 confidence floor and 3 s timeout; per-feature env flags switch on self-message, roast preflight, heresy selection, poll validation, claim verification, group-context ranking, spam and prompt-injection checks. Integration evidence: [`services/typesafe.ts`](https://github.com/alambertt/veritheo/blob/3871ca5ec4915ff90aaba1d064c7225f871a27c0/services/typesafe.ts).

## Get started

Copy `.env.example` to `.env`, add your bot token and keys, then run with Bun.

```sh
git clone https://github.com/alambertt/veritheo.git && cd veritheo
bun install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/alambertt/veritheo/blob/3871ca5ec4915ff90aaba1d064c7225f871a27c0/README.md](https://github.com/alambertt/veritheo/blob/3871ca5ec4915ff90aaba1d064c7225f871a27c0/README.md)

## Limits and data handling

Chat messages go to TypeSafe and the chat-model provider on your keys; the bot stores data in a local SQLite file.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 3871ca5ec491](https://github.com/alambertt/veritheo/tree/3871ca5ec4915ff90aaba1d064c7225f871a27c0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
