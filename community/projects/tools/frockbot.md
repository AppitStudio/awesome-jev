# FrockBot (persistent Cloudflare AI bots with Jev turn supervision and browser-action choices)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Persistent conversational bots that run on Cloudflare with their own Computer; Jev decides which bot replies in group chats, supervises turns and picks browser actions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/timoconnellaus/frockbot) |
| Maintainer | [timoconnellaus](https://github.com/timoconnellaus). Independently curated. |
| Format | Cloudflare Workers app (MIT) |
| Requirements | A Cloudflare account (self-deploy) or frockbot.com, plus Jev access via Workers AI or TypeSafe. |
| License | [MIT](https://github.com/timoconnellaus/frockbot/blob/badad82a6e5387b80c868c5e22d5ed3d62f5d398/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/supervision/jev.ts`](https://github.com/timoconnellaus/frockbot/blob/badad82a6e5387b80c868c5e22d5ed3d62f5d398/app/supervision/jev.ts) at the pinned commit. |

## When to use

- Run always-on bots that extend themselves.
- Use Jev for group-chat turn-taking and browser choices.
- Mismatch: needs Cloudflare; hosted frockbot.com has its own billing.

## How it works

`app/supervision/jev.ts` implements the TurnSupervisor with `@typesafe-ai/sdk`; `computer/agent.ts` drives pages by Jev's choices and `app/billing/jev.ts` meters Jev on Workers AI by input tokens. Integration evidence: [`app/supervision/jev.ts`](https://github.com/timoconnellaus/frockbot/blob/badad82a6e5387b80c868c5e22d5ed3d62f5d398/app/supervision/jev.ts).

## Get started

Deploy the simple profile from frockbot.com/deploy or `scripts/deploy-bundle.ts` into your Cloudflare account per the README.

```sh
git clone https://github.com/timoconnellaus/frockbot.git && cd frockbot
bun install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/timoconnellaus/frockbot/blob/badad82a6e5387b80c868c5e22d5ed3d62f5d398/README.md](https://github.com/timoconnellaus/frockbot/blob/badad82a6e5387b80c868c5e22d5ed3d62f5d398/README.md)

## Limits and data handling

Conversation and page context go to Jev (Workers AI or TypeSafe) on your account.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit badad82a6e53](https://github.com/timoconnellaus/frockbot/tree/badad82a6e5387b80c868c5e22d5ed3d62f5d398). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
