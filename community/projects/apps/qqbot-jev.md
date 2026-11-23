# qqbot by Mist-wu (QQ group chat bot where Jev decides whether to speak and DeepSeek decides what to say)

[All projects](../README.md) · [QQ bots](README.md#qq-bots)

A self-hosted QQ bot on NapCat. New group messages are batched and Jev gives the probability that the bot should join in; being @-mentioned or replied to lowers the bar but does not force a reply. DeepSeek writes the replies, describes images and stickers, and the bot keeps long-term memory of private chats. Chinese README.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Mist-wu/qqbot) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Mist-wu/qqbot#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-23. |
| Jev evidence | [`src/chat/gate.ts`](https://github.com/Mist-wu/qqbot/blob/5cfb31f7cf433d0cadd1126be689fa04d16980d2/src/chat/gate.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Mist-wu](https://github.com/Mist-wu). Independently curated. |
| Format | Node.js / TypeScript bot |
| Platform and availability | Self-hosted Node.js bot for QQ via NapCat (OneBot v11 WebSocket). |
| Jev's role | Jev returns Noul probabilities for whether to reply to the current batch of messages; code applies the thresholds. Without a TypeSafe key the bot only speaks in private chats, on @, replies or when named. |
| Requirements | Node.js 22+ and pnpm; a logged-in NapCat instance; DeepSeek and TypeSafe API keys. |
| License | [MIT](https://github.com/Mist-wu/qqbot/blob/5cfb31f7cf433d0cadd1126be689fa04d16980d2/LICENSE) |

## When to use

- See a "should I speak now?" Jev gate in front of an LLM chat bot.
- Mismatch: official QQ bot platforms; it relies on NapCat, an unofficial QQ client.

## How it works

`src/chat/gate.ts` uses the official `TypeSafeClient` from the TypeSafe JS SDK (`client.systemOne`) with the model from `JEV_MODEL` (default `jev-latest`) and one retry. Integration evidence: [`src/chat/gate.ts`](https://github.com/Mist-wu/qqbot/blob/5cfb31f7cf433d0cadd1126be689fa04d16980d2/src/chat/gate.ts).

## Get started

Enable a WebSocket server in NapCat, then install, configure the whitelists and keys, and run.

```sh
git clone https://github.com/Mist-wu/qqbot.git && cd qqbot
pnpm install
cp .env.example .env   # NAPCAT_TOKEN, DEEPSEEK_API_KEY, TYPESAFE_API_KEY, BOT_GROUPS ...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/Mist-wu/qqbot/blob/5cfb31f7cf433d0cadd1126be689fa04d16980d2/README.md](https://github.com/Mist-wu/qqbot/blob/5cfb31f7cf433d0cadd1126be689fa04d16980d2/README.md)

## Limits and data handling

Group and private messages are sent to TypeSafe (for the gate) and DeepSeek (for replies and image descriptions). Running a bot through an unofficial QQ client may break the platform's terms; check before use.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 5cfb31f7cf43](https://github.com/Mist-wu/qqbot/tree/5cfb31f7cf433d0cadd1126be689fa04d16980d2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
