# DurableMMO (cozy multiplayer farming game on Cloudflare where villagers can make decisions with Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Multiplayer farming game in the valley of Mossbrook: farm, mine, fight light monsters and chat with ten villagers. Villager decisions come from rules, optionally TypeSafe Jev, while Workers AI writes their lines. Runs on Cloudflare Workers and Durable Objects with a PixiJS client.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/elsodev/durable-objects-mmorpg) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/elsodev/durable-objects-mmorpg#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-01. |
| Jev evidence | [`src/worker/npc/brain.ts`](https://github.com/elsodev/durable-objects-mmorpg/blob/faec027b8a0754a13ae289a95fbd80d100295e83/src/worker/npc/brain.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [elsodev](https://github.com/elsodev). Independently curated. |
| Format | Web game (TypeScript, Cloudflare Workers + Durable Objects, PixiJS) |
| Platform and availability | Self-hosted web game (browser client). |
| Jev's role | Typed NPC decisions such as how to respond to a player. |
| Requirements | Node.js 22+; Cloudflare account to deploy; optional TypeSafe key. |
| License | [Apache-2.0](https://github.com/elsodev/durable-objects-mmorpg/blob/faec027b8a0754a13ae289a95fbd80d100295e83/LICENSE) |

## When to use

- Self-host a small multiplayer game with typed NPC decisions.
- Mismatch: Jev is optional; NPCs fall back to rules.

## How it works

`src/worker/npc/brain.ts` classifies player intent with rules, then asks Jev (`src/worker/npc/jev.ts`) for a typed decision, and finally has Workers AI write the line; `budget.ts` caps calls. Integration evidence: [`src/worker/npc/brain.ts`](https://github.com/elsodev/durable-objects-mmorpg/blob/faec027b8a0754a13ae289a95fbd80d100295e83/src/worker/npc/brain.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm run dev:local
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/elsodev/durable-objects-mmorpg#readme](https://github.com/elsodev/durable-objects-mmorpg#readme)

## Limits and data handling

Player chat with villagers is sent to TypeSafe when the key is set. No hosted instance verified. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit faec027b8a07](https://github.com/elsodev/durable-objects-mmorpg/tree/faec027b8a0754a13ae289a95fbd80d100295e83). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
