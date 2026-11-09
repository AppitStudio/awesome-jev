# pi continual-learning (Pi coding-agent package where TypeSafe Jev chooses learning directions and reviews memory)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Part of Frad's Pi packages: the continual-learning extension can use TypeSafe Jev to pick learning directions, review consolidated memory and parse free-form schedules.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/FradSer/pi-packages) |
| Maintainer | [FradSer](https://github.com/FradSer). Independently curated. |
| Format | Pi agent extension (TypeScript, MIT) |
| Requirements | The Pi coding agent, `pnpm install` in the checkout, and a `TYPESAFE_API_KEY` for the optional Jev decisions. |
| License | [MIT](https://github.com/FradSer/pi-packages/blob/1d3321e5a90527aed57059087564c4f84523ae96/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/continual-learning/extensions/jev-sdk.ts`](https://github.com/FradSer/pi-packages/blob/1d3321e5a90527aed57059087564c4f84523ae96/packages/continual-learning/extensions/jev-sdk.ts) at the pinned commit. |

## When to use

- Let a coding agent learn between sessions with typed Jev review.
- Schedule repeated work from plain-language requests.
- Mismatch: Jev is optional; without a key the features are refused.

## How it works

`jev-sdk.ts` lazily loads `@typesafe-ai/sdk`; `jev-learning.ts` and the `jev-memory-*` modules ask Jev typed questions, and explicit private-memory requests ask for consent before sending evidence to TypeSafe. Integration evidence: [`packages/continual-learning/extensions/jev-sdk.ts`](https://github.com/FradSer/pi-packages/blob/1d3321e5a90527aed57059087564c4f84523ae96/packages/continual-learning/extensions/jev-sdk.ts).

## Get started

Clone, run `pnpm install`, point Pi at `packages/continual-learning`, and add `jev` to `continual-learning.json` or set `TYPESAFE_API_KEY`.

```sh
git clone https://github.com/FradSer/pi-packages.git && cd pi-packages
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/FradSer/pi-packages/blob/1d3321e5a90527aed57059087564c4f84523ae96/README.md](https://github.com/FradSer/pi-packages/blob/1d3321e5a90527aed57059087564c4f84523ae96/README.md)

## Limits and data handling

Learning candidates and, with consent, memory evidence are sent to TypeSafe.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 1d3321e5a905](https://github.com/FradSer/pi-packages/tree/1d3321e5a90527aed57059087564c4f84523ae96). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
