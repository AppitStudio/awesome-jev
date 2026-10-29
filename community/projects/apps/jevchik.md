# Jevchik (Telegram group bot: karma for useful messages, anti-spam for newcomers, judged by Jev)

[All projects](../README.md) · [Telegram bots](README.md#telegram-bots)

Self-hosted Telegram bot for group chats: members earn karma from reactions, replies, thanks and from messages Jev judges useful, a karma number appears next to their names, newcomers get spam screening, and a Mini App shows weekly, monthly and all-time leaderboards. Bot texts are in Russian; docs in Russian and English.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/smixs/jevchik) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/smixs/jevchik#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free to self-host. TypeSafe usage is billed to your key. Checked 2026-10-29. |
| Jev evidence | [`src/adapters/jev.ts`](https://github.com/smixs/jevchik/blob/05ebde5215076a10801079ffd59d383cd7e8abcf/src/adapters/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [smixs](https://github.com/smixs). Independently curated. |
| Format | Node.js bot and Telegram Mini App (TypeScript, Docker) |
| Platform and availability | Self-hosted with Docker Compose; no public instance verified. |
| Jev's role | Scores messages for usefulness and screens newcomers' messages for spam. |
| Requirements | Docker, a Telegram bot token and a TypeSafe API key. |
| License | [MIT](https://github.com/smixs/jevchik/blob/05ebde5215076a10801079ffd59d383cd7e8abcf/LICENSE) |

## When to use

- Reward helpful members and filter spam in a busy group chat.
- Mismatch: Russian bot texts.

## How it works

`src/adapters/jev.ts` posts messages to `https://api.typesafe.ai/v1/systemone` with a pinned `jev-1.13.0`. Integration evidence: [`src/adapters/jev.ts`](https://github.com/smixs/jevchik/blob/05ebde5215076a10801079ffd59d383cd7e8abcf/src/adapters/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/smixs/jevchik && cd jevchik
cp .env.example .env   # bot token and TYPESAFE_API_KEY
docker compose up -d
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Russian and English): [github.com/smixs/jevchik#readme](https://github.com/smixs/jevchik#readme)

## Limits and data handling

Group messages go to TypeSafe for judging; admins should tell members.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 05ebde521507](https://github.com/smixs/jevchik/tree/05ebde5215076a10801079ffd59d383cd7e8abcf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
