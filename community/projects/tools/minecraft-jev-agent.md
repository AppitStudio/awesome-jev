# minecraft-jev-agent (embodied Minecraft Java agent where a typed decision plane picks grounded actions)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Embodied Minecraft Java agent: a sparse LLM planner decides what to do, a typed decision plane (TypeSafe Jev or Liquid d1, chosen by profile) decides which grounded transition to take, a kernel owns leases, effects and success, and stock Mineflayer moves the bot.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/souta-lab/minecraft-jev-agent) |
| Maintainer | [souta-lab](https://github.com/souta-lab). Independently curated. |
| Format | TypeScript monorepo (Node.js, Mineflayer) |
| Requirements | Node.js; a Minecraft Java server; a TypeSafe key for the Jev profile. |
| License | [MIT](https://github.com/souta-lab/minecraft-jev-agent/blob/e54bfbbeb1fa3abdc4d898cbe637af9ad2e26839/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/jev-harness/providers/systemone-direct.ts`](https://github.com/souta-lab/minecraft-jev-agent/blob/e54bfbbeb1fa3abdc4d898cbe637af9ad2e26839/packages/jev-harness/providers/systemone-direct.ts) at the pinned commit. |

## When to use

- Study a layered agent architecture with Jev choosing among grounded actions.
- Mismatch: research code with many moving parts.

## How it works

`packages/jev-harness/providers/systemone-direct.ts` calls TypeSafe `/v1/systemone`; `packages/jev-agent/src/jev.ts` turns kernel-proposed transitions into choice questions. Integration evidence: [`packages/jev-harness/providers/systemone-direct.ts`](https://github.com/souta-lab/minecraft-jev-agent/blob/e54bfbbeb1fa3abdc4d898cbe637af9ad2e26839/packages/jev-harness/providers/systemone-direct.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# see the README for setup; run the agent against a local Minecraft Java server
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/souta-lab/minecraft-jev-agent#readme](https://github.com/souta-lab/minecraft-jev-agent#readme)

## Limits and data handling

Game state is sent to the selected decision provider. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit e54bfbbeb1fa](https://github.com/souta-lab/minecraft-jev-agent/tree/e54bfbbeb1fa3abdc4d898cbe637af9ad2e26839). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
