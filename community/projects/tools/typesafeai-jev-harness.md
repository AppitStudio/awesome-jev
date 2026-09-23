# jev-harness (TypeSafeAI)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Research-stage proposal-review contract from the TypeSafeAI community org: an LLM proposes one action, Jev answers four narrow questions, and code produces evidence for a host to consider—without applying patches or granting permission. Distinct from [AntonioCoppe/jev-harness](jev-harness.md) (policy/recipes/`jev-eval` library).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TypeSafeAI/jev-harness) |
| Maintainer | [TypeSafeAI](https://github.com/TypeSafeAI) community organization. Upstream states this org is independent of the official TypeSafe AI team; not an official SDK. Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Source-only TypeScript package **jev-harness 0.0.0** (Node 22+, pnpm) with Next.js demo/arena; not published to npm. |
| Requirements | Node 22+; `pnpm install --frozen-lockfile`. Offline `pnpm typecheck` / `pnpm test` / `pnpm bench:review` need no key. Live demo routing needs a configured TypeSafe key. |
| License | [MIT](https://github.com/TypeSafeAI/jev-harness/blob/82c083c556a6d30b86972dde7b1e4a6b2ae73928/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, contract/benchmark layout). Offline package install and live Jev were **not** executed on the review host. Upstream bench totals are scripted mock values, not re-measured here. |

## When to use

Use it when you want a pinned research harness that separates proposal validation, narrow Jev review questions, and host authorization—with offline fixtures and receipts. Prefer [jev-harness](jev-harness.md) for a published npm policy library; prefer [System One Harness](systemone-harness.md) for a Python agent loop over environment actions.

## How it works

The host validates a proposal, optionally obtains a Jev review over fixed question IDs, then `decide(validation, review, threshold)` yields evidence for the host. Live transport and execution remain host responsibilities. Offline `pnpm bench:review` runs synthetic fixtures through validation and a labeled mock transport.

## Get started

```sh
git clone https://github.com/TypeSafeAI/jev-harness.git
cd jev-harness
git checkout 82c083c556a6d30b86972dde7b1e4a6b2ae73928
pnpm install --frozen-lockfile
pnpm typecheck
pnpm test
pnpm bench:review
```

Pin for review: [commit 82c083c](https://github.com/TypeSafeAI/jev-harness/tree/82c083c556a6d30b86972dde7b1e4a6b2ae73928).

## Examples and demos

- Offline proposal-review fixtures and `pnpm bench:review`.
- Optional Next.js demo / `/arena` (loopback; live routing separate).

## Limits and data handling

Nothing in-package applies patches or grants permission. Live Jev sends proposal/review state to TypeSafe when configured. This listing did not install dependencies or call Jev.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 82c083c](https://github.com/TypeSafeAI/jev-harness/tree/82c083c556a6d30b86972dde7b1e4a6b2ae73928) (MIT). AI-assisted review of README and LICENSE. No live TypeSafe spend.

Related: [jev-harness](jev-harness.md), [System One Harness](systemone-harness.md), [jev-layer](jev-layer.md).
