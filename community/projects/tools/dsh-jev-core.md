# dsh-jev-core (strict TypeSafe Jev client for DeepSeek Harness plugins with argmax and key-set validation)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Shared npm client for DSH plugins that posts Noul/Choice/Score questions to TypeSafe Jev and refuses partial or non-argmax answers. Callers branch on `isConfigured()` for their own fallbacks; the core never silently degrades.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fan56/dsh-jev-core) |
| Maintainer | [fan56](https://github.com/fan56). Independently curated. |
| Format | TypeScript ESM package `@aiwayds/dsh-jev-core` (MIT; Node ≥22) |
| Requirements | Node.js ≥22 and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/fan56/dsh-jev-core/blob/24b34be2a86e0f7e5abdb6f064c324e954ff7c88/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/client.ts`](https://github.com/fan56/dsh-jev-core/blob/24b34be2a86e0f7e5abdb6f064c324e954ff7c88/src/client.ts) at the pinned commit. |

## When to use

- Share one strict Jev client across several DSH plugins.
- Fail closed when a response violates argmax or key-set rules.
- Mismatch: not a full agent; consumers must supply their own heuristics when unconfigured.

## How it works

`src/client.ts` posts to `https://api.typesafe.ai/v1/systemone` with a pinned `jev-1.13.0` model and validates every answer before return. Integration evidence: [`src/client.ts`](https://github.com/fan56/dsh-jev-core/blob/24b34be2a86e0f7e5abdb6f064c324e954ff7c88/src/client.ts).

## Get started

Install the package and call `classify` with a `TYPESAFE_API_KEY`.

```sh
npm install @aiwayds/dsh-jev-core
export TYPESAFE_API_KEY=...
# see README quick start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/fan56/dsh-jev-core/blob/24b34be2a86e0f7e5abdb6f064c324e954ff7c88/README.md](https://github.com/fan56/dsh-jev-core/blob/24b34be2a86e0f7e5abdb6f064c324e954ff7c88/README.md)

## Limits and data handling

Question state is sent to TypeSafe on your key. Strict validation means bad responses throw rather than soft-fail.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 24b34be2a86e](https://github.com/fan56/dsh-jev-core/tree/24b34be2a86e0f7e5abdb6f064c324e954ff7c88). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
