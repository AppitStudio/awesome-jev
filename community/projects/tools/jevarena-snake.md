# JevArena (spectator arena where two Jev agents play Snake against each other via Vercel AI Gateway)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Public Next.js spectator app where two independent Jev agents duel at Snake; each spectator's page runs its own match, and without a key it shows a clearly labeled demo policy instead.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rolki-png/JevArena) |
| Maintainer | [rolki-png](https://github.com/rolki-png). Independently curated. |
| Format | Next.js web app (TypeScript, MIT) |
| Requirements | Node.js and a Vercel AI Gateway key (`AI_GATEWAY_API_KEY`) to drive the agents with Jev. |
| License | [MIT](https://github.com/rolki-png/JevArena/blob/925d6c294d91f686b97041c13ebef65ea4e08dcd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lib/agent/jev-adapter.ts`](https://github.com/rolki-png/JevArena/blob/925d6c294d91f686b97041c13ebef65ea4e08dcd/src/lib/agent/jev-adapter.ts) at the pinned commit. |

## When to use

- Watch Jev make fast game moves side by side.
- Mismatch: a playable game for humans; it is a spectator demo.

## How it works

`src/lib/agent/jev-adapter.ts` calls the AI SDK's `experimental_evaluate` through Vercel AI Gateway with model `typesafe-ai/jev`; if Jev fails that agent is marked BLOCKED rather than silently falling back. The key stays on the server. Integration evidence: [`src/lib/agent/jev-adapter.ts`](https://github.com/rolki-png/JevArena/blob/925d6c294d91f686b97041c13ebef65ea4e08dcd/src/lib/agent/jev-adapter.ts).

## Get started

Install, copy the env example (leave the key empty for the demo policy) and start the dev server on port 43123.

```sh
npm install
cp .env.example .env.local
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/rolki-png/JevArena/blob/925d6c294d91f686b97041c13ebef65ea4e08dcd/README.md](https://github.com/rolki-png/JevArena/blob/925d6c294d91f686b97041c13ebef65ea4e08dcd/README.md)
- Hosted demo: [jev-arena-ochre.vercel.app](https://jev-arena-ochre.vercel.app)

## Limits and data handling

Game state goes to Vercel AI Gateway and TypeSafe on the deployer's key.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 925d6c294d91](https://github.com/rolki-png/JevArena/tree/925d6c294d91f686b97041c13ebef65ea4e08dcd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
