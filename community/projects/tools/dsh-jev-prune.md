# dsh-jev-prune

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin that replaces size-only tool-result pruning and model-written compaction summaries with TypeSafe Jev keep/drop judgments plus deterministic, code-generated receipts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yangyu666/dsh-jev-prune) |
| Maintainer | [yangyu666](https://github.com/yangyu666). Independently curated; this page is not an upstream submission or endorsement. |
| Format | JavaScript Cordis/DSH plugin (`dsh-jev-prune` 0.1.0); peer deps `@deepseek-ai/schemastery`, `@deepseek-ai/dsh-tools`. |
| Requirements | Node.js 22.19+ or 24+; DSH profile with base tool-result-pruner/compaction bundles; `TYPESAFE_API_KEY`. Tested against `@deepseek-ai/dsh` 0.1.5-rc.2 (pre-release; shapes may drift). |
| License | [MIT](https://github.com/yangyu666/dsh-jev-prune/blob/9c7476a7a37265c71ddff1b5d321f9991fde64fe/LICENSE). TypeSafe inference billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `node check.js` → **ok**. Live DSH apply / TypeSafe prune not run. Distinct from [dsh-jev](dsh-jev.md) (`jev_ask`) and [dsh-jev-verify](dsh-jev-verify.md). |

## When to use

Use it when a DSH agent fills context with large tool outputs and you want semantic keep/drop plus receipt compaction instead of mid-string truncation or LLM summaries. Prefer [dsh-jev](dsh-jev.md) for on-demand `jev_ask`; prefer [fast-jev-compaction](fast-jev-compaction.md) / [jev-pruner](jev-pruner.md) outside DSH.

## How it works

[`jev.js`](https://github.com/yangyu666/dsh-jev-prune/blob/9c7476a7a37265c71ddff1b5d321f9991fde64fe/jev.js) posts noul/choice questions to `https://api.typesafe.ai/v1/systemone`. [`prune.js`](https://github.com/yangyu666/dsh-jev-prune/blob/9c7476a7a37265c71ddff1b5d321f9991fde64fe/prune.js) / [`index.js`](https://github.com/yangyu666/dsh-jev-prune/blob/9c7476a7a37265c71ddff1b5d321f9991fde64fe/index.js) hook `toolResultPruner` and compaction; [`receipt.js`](https://github.com/yangyu666/dsh-jev-prune/blob/9c7476a7a37265c71ddff1b5d321f9991fde64fe/receipt.js) builds deterministic receipts (tool name, paths, sizes, seqs) with no model prose. Tool-result text leaves the host when judging live. Without a key, pruning falls back toward native DSH behavior.

## Get started

```sh
git clone https://github.com/yangyu666/dsh-jev-prune.git
cd dsh-jev-prune
git checkout 9c7476a7a37265c71ddff1b5d321f9991fde64fe
node check.js
# install into a DSH profile (needs local DSH):
# dsh plugin --profile web add link:/absolute/path/dsh-jev-prune
```

Live judgments need `TYPESAFE_API_KEY` and bill TypeSafe. Re-run `jev_probe_shapes` after DSH upgrades.

## Examples and demos

- Upstream `check.js` pure-function self-check; `smoke_apply.mjs` / `verify_real_shapes.mjs` for host-shaped sessions.
- This listing: `node check.js` → **ok**. No live TypeSafe or DSH host apply.

## Limits and data handling

Tool results and effect metadata are sent to TypeSafe when enabled. Compaction of spent tool pairs is gated (quantile intersection, never-compact tools, error/assert guards, recent preserve window). DSH 0.1.x is pre-release—field drift is expected. Cost/quality claims were not measured here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 9c7476a](https://github.com/yangyu666/dsh-jev-prune/tree/9c7476a7a37265c71ddff1b5d321f9991fde64fe): MIT; AI-assisted source review of README, LICENSE, plugin modules, and offline `check.js`. No live TypeSafe/DSH session. Note: `package.json` repository URL still shows a placeholder `your-handle`; catalog Source uses the public GitHub owner `yangyu666`.

Related: [dsh-jev](dsh-jev.md), [dsh-jev-verify](dsh-jev-verify.md), [fast-jev-compaction](fast-jev-compaction.md), [jev-pruner](jev-pruner.md).
