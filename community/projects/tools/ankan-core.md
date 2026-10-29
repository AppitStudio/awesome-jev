# Ankan Core (self-hosted anything tracker with an MCP proxy and optional Jev routing for Telegram messages)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted tracker for anything you want to log, with a Vue frontend, a local Convex backend and an MCP proxy, started with Docker Compose. A Telegram bot can add entries from chat; with a Jev key set, incoming Telegram text is classified by Jev before falling back to Google AI. Email one-time-code sign-in through ZeptoMail.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bharatkashyap/ankan-core) |
| Maintainer | [bharatkashyap](https://github.com/bharatkashyap). Independently curated. |
| Format | Docker Compose app (Vue, Convex, TypeScript) |
| Requirements | Docker Compose v2, a ZeptoMail key and sender; optionally a TypeSafe key, Google AI key and Telegram bot. |
| License | [MIT](https://github.com/bharatkashyap/ankan-core/blob/9917880e3b6940eb2cd06e3948a289c1639b8abe/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`convex/lib/jevRouter.ts`](https://github.com/bharatkashyap/ankan-core/blob/9917880e3b6940eb2cd06e3948a289c1639b8abe/convex/lib/jevRouter.ts) at the pinned commit. |

## When to use

- Run your own tracker that agents (via MCP) and a Telegram bot can write to.
- Mismatch: Jev is optional and only routes Telegram text.

## How it works

`convex/lib/jevRouter.ts` posts Telegram text to `https://api.typesafe.ai/v1/systemone` with a pinned `jev-1.13.0` to decide how to handle it. Integration evidence: [`convex/lib/jevRouter.ts`](https://github.com/bharatkashyap/ankan-core/blob/9917880e3b6940eb2cd06e3948a289c1639b8abe/convex/lib/jevRouter.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/bharatkashyap/ankan-core.git && cd ankan-core
cp .env.example .env   # set ZeptoMail keys (and JEV_API_KEY to enable routing)
docker compose up
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/bharatkashyap/ankan-core#readme](https://github.com/bharatkashyap/ankan-core#readme)

## Limits and data handling

With `JEV_API_KEY` set, Telegram message text goes to TypeSafe; data otherwise stays in your Convex volume.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 9917880e3b69](https://github.com/bharatkashyap/ankan-core/tree/9917880e3b6940eb2cd06e3948a289c1639b8abe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
