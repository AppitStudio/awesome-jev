# jev-tree

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Recursive TypeSafe Jev Choice over a JSON taxonomy so you can select among more than 255 leaves without truncating the catalog.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/reachjalil/jev-tree) |
| Maintainer | [reachjalil](https://github.com/reachjalil). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package **`jev-tree` 0.1.0** (library + CLI); explainer at https://reachjalil.github.io/jev-tree/. |
| Requirements | Node.js ≥ 22; `AI_GATEWAY_API_KEY` for live `typesafe-ai/jev` via Vercel AI Gateway. |
| License | [MIT](https://github.com/reachjalil/jev-tree/blob/95bff63bd653fee4dc71f33f9431dce0f81e2ca3/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline tests inspected; live Gateway/Jev not run on the review host. Same author stack as [Jev Logs](jevlogs.md). |

## When to use

Use it when a flat Choice would exceed TypeSafe’s **255-option cap** (SKUs, incident types, workflow ids) and you can express the catalog as a tree or forest. Prefer a single Choice when the list already fits. Prefer [Jev Logs](jevlogs.md) for log triage rather than taxonomy selection.

## How it works

[`src/index.ts`](https://github.com/reachjalil/jev-tree/blob/95bff63bd653fee4dc71f33f9431dce0f81e2ca3/src/index.ts) walks the shape and calls `experimental_evaluate` with model `typesafe-ai/jev` (Gateway, zeroDataRetention) once per level or partition. Default fan-out is 32 options per call (configurable up to 255). Application code owns tree construction, redaction, and assembling the path of chosen nodes.

## Get started

```sh
git clone https://github.com/reachjalil/jev-tree.git
cd jev-tree
git checkout 95bff63bd653fee4dc71f33f9431dce0f81e2ca3
npm install --ignore-scripts
npm test
# Live (not run here): set AI_GATEWAY_API_KEY and follow upstream CLI --live
```

Live selection sends redacted state to the AI Gateway/TypeSafe and may incur charges.

## Examples and demos

- Offline on the review host: `npm test` → **14 passed**.
- Explainer: [reachjalil.github.io/jev-tree](https://reachjalil.github.io/jev-tree/).
- Dataset card: Hugging Face `reachjalil/jev-tree-choice-cap` (linked upstream).

## Limits and data handling

State leaves the host on live selects. Splitting large sibling lists adds calls and can lose cross-chunk context. Depth/`maxFanout` are application policy, not model guarantees.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 95bff63](https://github.com/reachjalil/jev-tree/tree/95bff63bd653fee4dc71f33f9431dce0f81e2ca3): **0.1.0**, MIT. AI-assisted source review of README, `src/index.ts`, `src/cli.ts`, LICENSE. Offline: `npm test` → 14 passed. No live Gateway/TypeSafe on the review host.

Related: [Jev Logs](jevlogs.md), [Advocaat](advocaat.md).
