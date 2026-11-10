# Brigade (consumer-app business primitives for agents with a TypeSafe semantic adapter)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

CLI, MCP server and skill giving AI agents shared capabilities, providers and recipes for running a consumer-app business, with a TypeSafe System One adapter for semantic judgments and Jev-directed build-loop recipes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Clueless-Creations/Brigade) |
| Maintainer | [Clueless-Creations](https://github.com/Clueless-Creations). Independently curated. |
| Format | CLI, MCP server and agent skill (TypeScript, MIT) |
| Requirements | Node.js toolchain per the README; a TypeSafe key only if you enable the live TypeSafe transport. |
| License | [MIT](https://github.com/Clueless-Creations/Brigade/blob/a0b55e91dec9c7f76e5b2c920899da193f8d2fa8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`adapters/providers/typesafe/transport.ts`](https://github.com/Clueless-Creations/Brigade/blob/a0b55e91dec9c7f76e5b2c920899da193f8d2fa8/adapters/providers/typesafe/transport.ts) at the pinned commit. |

## When to use

- Give agents a structured operating layer for product, funnel and monetization work.
- Route semantic yes/no or ranking judgments to Jev behind a provider contract.
- Mismatch: early-stage; live TypeSafe HTTP is opt-in and the fake transport is not evidence of live support.

## How it works

`adapters/providers/typesafe/` implements support/encode/transport/decode for System One; the transport has `fake` (wiring tests only) and `live-http` kinds, and `catalog/workflows/jev-active-*.ts` recipes use Jev as a swappable judge, never the policy owner. Integration evidence: [`adapters/providers/typesafe/transport.ts`](https://github.com/Clueless-Creations/Brigade/blob/a0b55e91dec9c7f76e5b2c920899da193f8d2fa8/adapters/providers/typesafe/transport.ts).

## Get started

Follow the README's Get started section; Jev is optional and not required for basic setup.

```sh
git clone https://github.com/Clueless-Creations/Brigade.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Clueless-Creations/Brigade/blob/a0b55e91dec9c7f76e5b2c920899da193f8d2fa8/README.md](https://github.com/Clueless-Creations/Brigade/blob/a0b55e91dec9c7f76e5b2c920899da193f8d2fa8/README.md)

## Limits and data handling

With the live transport on, the judged business context goes to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit a0b55e91dec9](https://github.com/Clueless-Creations/Brigade/tree/a0b55e91dec9c7f76e5b2c920899da193f8d2fa8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
