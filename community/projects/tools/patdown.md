# patdown

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Fuzzy markdown-rule linter CLI: walk a tree against rules in markdown, with a swappable judge whose default backend is TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tyler-dot-earth/patdown) |
| Maintainer | [tyler-dot-earth](https://github.com/tyler-dot-earth). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript monorepo; npm CLI **patdown 0.5.0** plus `@patdown/jev` / `@patdown/rules` (0BSD). |
| Requirements | Node.js ≥ 22.22.2; `TYPESAFE_API_KEY` for the default Jev judge; optional adapters for other rule sources/judges. |
| License | [0BSD](https://github.com/tyler-dot-earth/patdown/blob/fe95dc727e0610d3d2c165ccbeeba844489dcb77/LICENSE) (GitHub license API may show `NOASSERTION`; LICENSE and package.json declare 0BSD). |

## When to use

Use it to lint files against plain-English or markdown-encoded fuzzy rules, or to ask yes/no questions via `patdown ask`. Prefer [toolgate](toolgate.md) or [pi-jev-sentinel](pi-jev-sentinel.md) for agent tool-call gates rather than tree linting.

## How it works

[`packages/patdown-jev/src/jev-system-one.ts`](https://github.com/tyler-dot-earth/patdown/blob/fe95dc727e0610d3d2c165ccbeeba844489dcb77/packages/patdown-jev/src/jev-system-one.ts) posts to `https://api.typesafe.ai/v1/systemone` with `TYPESAFE_API_KEY`. Rules load from `AGENTS.PATDOWN.md` or `--rules`; adapters can replace the markdown rule source. The judge interface is provider-neutral; TypeSafe/Jev is the default backend.

## Get started

```sh
npx patdown --help
# or from the reviewed tree:
git clone https://github.com/tyler-dot-earth/patdown.git
cd patdown
git checkout fe95dc727e0610d3d2c165ccbeeba844489dcb77
pnpm install --ignore-scripts
pnpm --filter @patdown/jev exec vitest run
pnpm --filter @patdown/rules exec vitest run
```

Live lint/`ask` calls TypeSafe with file or stdin content. Do not pipe secrets. This listing did not run live Jev judgments.

## Examples and demos

- Workspace CLI examples in the README (`patdown --rules`, `ask`, `--stdin`).
- Offline tests under [`packages/patdown-jev/tests`](https://github.com/tyler-dot-earth/patdown/tree/fe95dc727e0610d3d2c165ccbeeba844489dcb77/packages/patdown-jev/tests) and [`packages/patdown-rules/tests`](https://github.com/tyler-dot-earth/patdown/tree/fe95dc727e0610d3d2c165ccbeeba844489dcb77/packages/patdown-rules/tests).

## Limits and data handling

Rule inputs and file/stdin text go to TypeSafe when using the default judge. Node version floors matter (CLI vs older release lines). Thresholds (`--yes-threshold`) are policy knobs, not accuracy guarantees.

## Review and maintenance

Reviewed on **2026-09-20** at [commit fe95dc7](https://github.com/tyler-dot-earth/patdown/tree/fe95dc727e0610d3d2c165ccbeeba844489dcb77): **patdown 0.5.0**, 0BSD. AI-assisted source review of `@patdown/jev` System One client, README, and LICENSE. On Node.js 24.8.0, **`@patdown/jev` vitest: 14 passed**; **`@patdown/rules` vitest: 13 passed**. No live TypeSafe lint runs were performed.

Related: [toolgate](toolgate.md), [Supercov](supercov.md), [jev-pruner](jev-pruner.md).
