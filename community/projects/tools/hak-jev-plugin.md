# hak-jev-plugin

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hedera Agent Kit policy plugin: TypeSafe Jev gates sensitive tool calls (v0: SaucerSwap swaps) before sign; decisions notarized to HCS.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jmgomezl/hak-jev-plugin) |
| Maintainer | [jmgomezl](https://github.com/jmgomezl). Independently curated. |
| Format | npm package `hak-jev-plugin` — HAK v4 `AbstractPolicy` gate. |
| Requirements | Hedera Agent Kit context; optional `TYPESAFE_API_KEY` (else deterministic `RulesProvider`). |
| License | [MIT](https://github.com/jmgomezl/hak-jev-plugin/blob/70744ce5baa63034563f248329b4425908c927e2/LICENSE). TypeSafe and Hedera network usage may incur charges. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live swap/TypeSafe/HCS paths not run on the review host. |

## When to use

Use when HAK agents must pass typed execute/slippage/intent checks before signing swaps, with on-chain audit receipts. Prefer human Ledger approval plugins when you want a person in the loop instead.

## How it works

`JevGatePolicy` runs post-core-action: asks Jev (or rules) action/slippage_ok/intent_match; blocks below threshold; writes compact HCS receipts (no keys/raw user text).

## Get started

```sh
git clone https://github.com/jmgomezl/hak-jev-plugin.git
cd hak-jev-plugin
git checkout 70744ce5baa63034563f248329b4425908c927e2
# npm package: https://www.npmjs.com/package/hak-jev-plugin
```

## Examples and demos

- Upstream README policy flow and question table.
- npm: [hak-jev-plugin](https://www.npmjs.com/package/hak-jev-plugin).

## Limits and data handling

Live Jev receives swap params/quote/instruction text. HCS stores hashed receipts. Catalog checks did not execute live swaps.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 70744ce](https://github.com/jmgomezl/hak-jev-plugin/tree/70744ce5baa63034563f248329b4425908c927e2). AI-assisted README and license inspection; install/live paths not executed.
