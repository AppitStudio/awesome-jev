# Orbs

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted multi-bot chat: rooms hold people and bots, `@mentions` wake a bot, and with no mention TypeSafe Jev scores which bot should answer; a daemon on your machine runs each bot turn through your own Pi agent.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nikuscs/orbs) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/nikuscs/orbs#readme) (source-built app; no separate website verified). |
| Pricing and access | No app fee for the MIT source build; self-host locally (Bun + SQLite) or on your Cloudflare account. Bot turns run on whatever models your Pi reaches (billed by those providers); a TypeSafe key is needed only for Jev routing. Checked 2026-10-07. |
| Jev evidence | [`route-action.decide-jev.ts`](https://github.com/nikuscs/orbs/blob/eb400c1cdb9becc3b6f37a98539a773b1eb96408/apps/server/src/services/route/route-action.decide-jev.ts) sends one `systemOne` call with a per-bot fit Noul plus needs-reply/absent/group questions and turns the answers into responders; source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [nikuscs](https://github.com/nikuscs). Independently curated. |
| Format | Self-hosted web app (TanStack Start, Bun) + local daemon driving Pi |
| Platform and availability | Self-hosted: one local Bun process (SQLite + disk) or Cloudflare Workers/D1/R2/Durable Objects; source build only. |
| Jev's role | Jev decides who replies when no bot is mentioned (per-bot fit, whether the message needs a reply, group questions); mentions route directly. Pi and its configured models generate the actual replies. |
| Requirements | Bun 1.4.2, Pi 0.99.0+ on `PATH`, a `TYPESAFE_API_KEY` for Jev routing; optional Google OAuth; Cloudflare account for the hosted variant. |
| License | [MIT](https://github.com/nikuscs/orbs/blob/eb400c1cdb9becc3b6f37a98539a773b1eb96408/LICENSE). |

## When to use

- Run a group chat where several bots on different models share one room and the right one answers.
- Keep bot execution on your own machine while the chat runs locally or on Cloudflare.
- Mismatch: requires the separate Pi agent; Jev routing needs a TypeSafe key (the source also has roundtable and judge route drivers).

## How it works

Messages land in rooms on the server; the router in [`apps/server/src/services/route/`](https://github.com/nikuscs/orbs/tree/eb400c1cdb9becc3b6f37a98539a773b1eb96408/apps/server/src/services/route) honours `@handle`/`@everyone` and otherwise asks Jev. The daemon connects out with an organization API key and runs the selected bot's turn through `pi --mode rpc`, streaming the reply back.

## Get started

Run locally (from the README):

```sh
git clone https://github.com/nikuscs/orbs && cd orbs && bun install
cp apps/web/.env.example apps/web/.env   # add TYPESAFE_API_KEY for Jev routing
cd apps/web && bun run dev:cloudflare     # http://localhost:47101
# then start the daemon as described in README step 3
```

Jev routing calls are billed to your TypeSafe key; bot replies are billed by the providers Pi uses.

## Examples and demos

- README *Run it locally*, *Without Cloudflare* and *Cloudflare* deployment sections.
- README feature list (rooms, direct chats, routing, daemon keys).

## Limits and data handling

Message text and bot descriptions go to TypeSafe for routing; replies go to the models your Pi uses. Default mail driver prints verification links to the terminal. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit eb400c1cdb9b](https://github.com/nikuscs/orbs/tree/eb400c1cdb9becc3b6f37a98539a773b1eb96408). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
