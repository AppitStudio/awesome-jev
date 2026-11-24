# MCP Grand Prix by Ruben Casas (two-team F1 racing demo where Jev is the race engineer and driver, with MCP Apps pit-wall views)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Local racing game for two players at Monza and Las Vegas: each team has a race engineer that picks strategy and a driver that picks intent, run by Jev versus Jev or Jev versus GPT-6 Luna, while local code handles the physics. The server exposes an MCP endpoint and an MCP Apps pit-wall view.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/infoxicator/mcp-events-grand-prix) |
| Maintainer | [infoxicator](https://github.com/infoxicator). Independently curated. |
| Format | TypeScript / Vite web game with a local Node server and MCP endpoint |
| Requirements | Node.js 22+; mocks by default. For live play a TypeSafe key (or Jev through OpenRouter or Vercel AI Gateway) and an OpenAI key for Luna. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/race-brains.ts`](https://github.com/infoxicator/mcp-events-grand-prix/blob/a7c226d0228fc2547e6812daa4cf340b942e1ffc/server/race-brains.ts) at the pinned commit. |

## When to use

- Show Jev's speed in a live, watchable demo, or try MCP Apps with a game.
- Mismatch: a polished game release; this is an event demo.

## How it works

`server/race-brains.ts` calls `TypeSafeClient.systemOne({state, questions})` from `@typesafe-ai/sdk` for engineer and driver decisions, with OpenRouter and Vercel AI Gateway as alternative Jev providers. Integration evidence: [`server/race-brains.ts`](https://github.com/infoxicator/mcp-events-grand-prix/blob/a7c226d0228fc2547e6812daa4cf340b942e1ffc/server/race-brains.ts).

## Get started

Install and launch the three-window demo; it runs on mocks until you add keys in `.env.local`.

```sh
git clone https://github.com/infoxicator/mcp-events-grand-prix.git && cd mcp-events-grand-prix
npm ci
npm run demo   # http://127.0.0.1:5277
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/infoxicator/mcp-events-grand-prix/blob/a7c226d0228fc2547e6812daa4cf340b942e1ffc/README.md](https://github.com/infoxicator/mcp-events-grand-prix/blob/a7c226d0228fc2547e6812daa4cf340b942e1ffc/README.md)
- Related listing by the same maker: [jevlist.ai/projects/jev-pong-infoxicator](https://jevlist.ai/projects/jev-pong-infoxicator)

## Limits and data handling

With live providers, race state is sent to TypeSafe (or OpenRouter/Vercel) and OpenAI. No license file, so no reuse terms are granted.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit a7c226d0228f](https://github.com/infoxicator/mcp-events-grand-prix/tree/a7c226d0228fc2547e6812daa4cf340b942e1ffc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
