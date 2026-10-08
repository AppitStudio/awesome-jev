# omp-jev-tier

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Extension for the omp coding agent that uses omp's native judge role (normally `typesafe/jev-latest`) for subagent model tiering and automatic plan mode, without patching omp or changing configured model roles, fallbacks or usage reserve; it refuses judgments from non-Jev judge models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/charliemartin0/omp-jev-tier) |
| Maintainer | [charliemartin0](https://github.com/charliemartin0). Independently curated. |
| Format | omp plugin (`omp plugin install github:charliemartin0/omp-jev-tier`) |
| Requirements | omp 18.8.4 (target), Bun 1.3.14+; omp `judge` role set to a native Jev model with `TYPESAFE_API_KEY` or `/login typesafe`. |
| License | [MIT](https://github.com/charliemartin0/omp-jev-tier/blob/00719e0e101ab5ecc1b0b144ee144a7e08f95605/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Send simple subagent work to cheaper tiers automatically in omp.
- Mismatch: only verified against omp 18.8.4.

## How it works

[`judge.ts`](https://github.com/charliemartin0/omp-jev-tier/blob/00719e0e101ab5ecc1b0b144ee144a7e08f95605/judge.ts) calls omp's judge; [`core.ts`](https://github.com/charliemartin0/omp-jev-tier/blob/00719e0e101ab5ecc1b0b144ee144a7e08f95605/core.ts) and [`plan.ts`](https://github.com/charliemartin0/omp-jev-tier/blob/00719e0e101ab5ecc1b0b144ee144a7e08f95605/plan.ts) apply tiering and plan-mode policy.

## Get started

Install through omp (README):

```sh
omp plugin install github:charliemartin0/omp-jev-tier
```

Judge calls bill your TypeSafe account.

## Examples and demos

- Config example: [`config.example.json`](https://github.com/charliemartin0/omp-jev-tier/blob/00719e0e101ab5ecc1b0b144ee144a7e08f95605/config.example.json).

## Limits and data handling

Task context goes to TypeSafe via omp. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 00719e0e101a](https://github.com/charliemartin0/omp-jev-tier/tree/00719e0e101ab5ecc1b0b144ee144a7e08f95605). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
