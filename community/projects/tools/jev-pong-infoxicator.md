# Jev vs Jev Pong by Ruben Casas (two browser agents play Pong in real time, with Jev or GPT Luna deciding each paddle move)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Recording-ready AI rivalry: two independent browser agents (VECTOR and CHAOS) each own one paddle in an authoritative Pong arena, with a spectator view and a separate 3D robot arena page. Each agent's decision model answers in real time; the author's matchups put Jev against GPT Luna. Runs locally with one command that opens three Chromium windows, or on Cloudflare Workers with an MCP app.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/infoxicator/jev-pong) |
| Maintainer | [infoxicator](https://github.com/infoxicator). Independently curated. |
| Format | TypeScript web app, Node server and Cloudflare Worker (no license file) |
| Requirements | Node.js 22+ and npm; `TYPESAFE_API_KEY` (or the mock mode) for Jev, an OpenAI key for Luna matchups; Cloudflare only for the hosted variant. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/Infoxicador/status/2123123981758968275)). |
| Jev evidence | [`worker/index.ts`](https://github.com/infoxicator/jev-pong/blob/9c65638ff0b1c966a1df2ac5eeffed5b21f547e6/worker/index.ts) at the pinned commit. |

## When to use

- Watch a decision model play a real-time game against another model, or record a demo of it.
- Mismatch: reusable code under an open license; no license file is present.

## How it works

`worker/index.ts` builds the players with `JEV_PROVIDER: 'typesafe'` and your `TYPESAFE_API_KEY`; `.env.local.example` shows `JEV_MODEL=jev-latest` and a `JEV_MOCK=1` mode for runs without a key. Integration evidence: [`worker/index.ts`](https://github.com/infoxicator/jev-pong/blob/9c65638ff0b1c966a1df2ac5eeffed5b21f547e6/worker/index.ts).

## Get started

Clone, install and start the demo; it opens Vector, Spectator and Chaos windows on localhost.

```sh
git clone https://github.com/infoxicator/jev-pong && cd jev-pong
npm ci
npm run demo   # http://127.0.0.1:5177
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/infoxicator/jev-pong/blob/9c65638ff0b1c966a1df2ac5eeffed5b21f547e6/README.md](https://github.com/infoxicator/jev-pong/blob/9c65638ff0b1c966a1df2ac5eeffed5b21f547e6/README.md)

## Limits and data handling

No license file on the reviewed commit, so reuse terms are not granted. Each paddle decision is a paid model call on your keys; game state goes to the configured providers. A demo project, not a benchmark.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 9c65638ff0b1](https://github.com/infoxicator/jev-pong/tree/9c65638ff0b1c966a1df2ac5eeffed5b21f547e6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
