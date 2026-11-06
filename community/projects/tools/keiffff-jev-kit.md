# jev-kit (TypeSafe SDK wrappers for versioned decision contracts, routers and evals)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeScript monorepo (`decision-contract`, `decision-router`, `decision-eval`) built on `@typesafe-ai/sdk` for fingerprinting decision contracts, routing, and evaluating TypeSafe Jev decision points such as permissions and semantic change checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/keiffff/jev-kit) |
| Maintainer | [keiffff](https://github.com/keiffff). Independently curated. |
| Format | TypeScript packages (MIT) |
| Requirements | Node/TypeScript toolchain and TypeSafe credentials for live calls. |
| License | [MIT](https://github.com/keiffff/jev-kit/blob/4d5b24dec8ba574c5d76dc9b0c3cc8ad1789f92e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/decision-contract/src/index.ts`](https://github.com/keiffff/jev-kit/blob/4d5b24dec8ba574c5d76dc9b0c3cc8ad1789f92e/packages/decision-contract/src/index.ts) at the pinned commit. |

## When to use

- Version and fingerprint decision question sets.
- Share contract helpers across agent permission and routing code.
- Mismatch: toolkit packages, not a full agent product.

## How it works

`packages/decision-contract/src/index.ts` re-exports `TypeSafeClient` and helpers from `@typesafe-ai/sdk` and adds fingerprintable `DecisionContract` types. Integration evidence: [`packages/decision-contract/src/index.ts`](https://github.com/keiffff/jev-kit/blob/4d5b24dec8ba574c5d76dc9b0c3cc8ad1789f92e/packages/decision-contract/src/index.ts).

## Get started

Install the packages from the monorepo and construct a contract with the TypeSafe client.

```sh
git clone https://github.com/keiffff/jev-kit.git && cd jev-kit
# install workspace per README
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/keiffff/jev-kit/blob/4d5b24dec8ba574c5d76dc9b0c3cc8ad1789f92e/README.md](https://github.com/keiffff/jev-kit/blob/4d5b24dec8ba574c5d76dc9b0c3cc8ad1789f92e/README.md)

## Limits and data handling

Contract state is sent to TypeSafe on your key when live.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 4d5b24dec8ba](https://github.com/keiffff/jev-kit/tree/4d5b24dec8ba574c5d76dc9b0c3cc8ad1789f92e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
