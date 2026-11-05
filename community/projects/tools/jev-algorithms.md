# jev-algorithms (TypeScript library of batched sort, top-k, threshold search, clustering and matching algorithms that run on Jev answers)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Runtime-agnostic TypeScript algorithms built on typed Jev questions: pairwise `sort`, `selectTopK`, threshold and first-true search, `clusterByRelation` and more, each documented with its request cost in terms of `n` items and batched up to 40 questions per request. Adapters cover the TypeSafe API, Cloudflare Workers AI and an in-memory test double.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HikaruEgashira/jev-algorithms) |
| Maintainer | [HikaruEgashira](https://github.com/HikaruEgashira). Independently curated. |
| Format | npm package `@hikae/jev-algorithms` (TypeScript) |
| Requirements | Node.js and a `TYPESAFE_API_KEY` for the TypeSafe adapter (or a Workers AI binding). |
| License | [MIT](https://github.com/HikaruEgashira/jev-algorithms/blob/fe2441f824bc0fd54fa7ad5ead3fbad4cc5aced1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/adapters/typesafe.ts`](https://github.com/HikaruEgashira/jev-algorithms/blob/fe2441f824bc0fd54fa7ad5ead3fbad4cc5aced1/src/adapters/typesafe.ts) at the pinned commit. |

## When to use

- Rank, select or group items by a natural-language criterion without writing the comparison loop yourself.
- Keep Jev request counts low with batched comparisons.
- Mismatch: an early 0.1.0 library; check the README for algorithm costs before large inputs.

## How it works

`createTypeSafeClient` posts typed `noul`, `choice` and `score` questions to TypeSafe System One; the algorithms in `src/algorithms/` batch comparisons level by level (randomized quicksort, quickselect, clustering) over the same client contract. Integration evidence: [`src/adapters/typesafe.ts`](https://github.com/HikaruEgashira/jev-algorithms/blob/fe2441f824bc0fd54fa7ad5ead3fbad4cc5aced1/src/adapters/typesafe.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install @hikae/jev-algorithms
# then: const jev = createTypeSafeClient({ apiKey: process.env.TYPESAFE_API_KEY! });
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with quick start and algorithm table: [github.com/HikaruEgashira/jev-algorithms/blob/fe2441f824bc0fd54fa7ad5ead3fbad4cc5aced1/README.md](https://github.com/HikaruEgashira/jev-algorithms/blob/fe2441f824bc0fd54fa7ad5ead3fbad4cc5aced1/README.md)

## Limits and data handling

Item states you pass are sent to TypeSafe on your key; keep the key on a server. Request-count figures are the README's own analysis and were not independently measured.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit fe2441f824bc](https://github.com/HikaruEgashira/jev-algorithms/tree/fe2441f824bc0fd54fa7ad5ead3fbad4cc5aced1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
