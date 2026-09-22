# jev-ood-calibration

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Independent calibration study of TypeSafe Jev: published raw responses for three public benchmarks plus 900 rule-generated support tickets (choice / boolean / score) that cannot be in training data.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/scienthoon/jev-ood-calibration) |
| Maintainer | [scienthoon](https://github.com/scienthoon). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node scripts + Python metrics helpers; private package `jev-ood-calibration`; committed `data/` and `results/` dumps. |
| Requirements | Node for `scripts/jev_eval.mjs` (AI SDK); Python + torch for `scripts/metrics.py` summarization. Live re-runs need a Vercel AI Gateway / TypeSafe-capable key. |
| License | [MIT](https://github.com/scienthoon/jev-ood-calibration/blob/e092d3f1ef8baa5fd213443862b04d1db6fb63aa/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Inspected README, LICENSE, scripts, and committed result JSONL line counts; did **not** re-run live Gateway calls or torch metrics on the review host. Upstream accuracy/ECE tables are author-reported for the dated 2026-09-19 run—not independently re-measured here. |

## When to use

Use it when you want a **reproducible OOD calibration ledger** for official Jev (public benches + synthetic unknowable-priority tickets) with raw dumps. Prefer [jev-calibrate](jev-calibrate.md) to tune your own labelled gates, or [jeval](jeval.md) for provider-neutral calibration tooling. Do not treat a single upstream table as a permanent product claim.

## How it works

`scripts/jev_eval.mjs` calls Vercel AI Gateway model `typesafe-ai/jev` via AI SDK `experimental_evaluate`. Synthetic tickets live under `data/`; published responses under `results/*.jsonl`. `scripts/metrics.py` computes accuracy/NLL/ECE/refit temperature (requires torch).

## Get started

```sh
git clone https://github.com/scienthoon/jev-ood-calibration.git
cd jev-ood-calibration
git checkout e092d3f1ef8baa5fd213443862b04d1db6fb63aa
wc -l results/*.jsonl data/val.jsonl
# Live re-eval (not run here): npm i && node scripts/jev_eval.mjs ...
```

Re-running evaluations sends ticket/benchmark text to the Gateway/TypeSafe and incurs charges. This listing only verified committed artifacts offline.

## Examples and demos

- Offline on the review host: line counts `results/jev_openbookqa.jsonl` 500, `jev_commonsense_qa.jsonl` 1221, `jev_hellaswag.jsonl` 2000, `jev_synth.jsonl` 900, `data/val.jsonl` 900 (matches README tables).
- Upstream README result tables and relation notes to other independent benches.

## Limits and data handling

Gateway/model id quirks and rounding notes are documented upstream. Synthetic priority labels intentionally cannot be recovered from text. Catalog review did not execute `metrics.py` (torch missing on host) or live calls.

## Review and maintenance

Reviewed on **2026-09-22** at [commit e092d3f](https://github.com/scienthoon/jev-ood-calibration/tree/e092d3f1ef8baa5fd213443862b04d1db6fb63aa): MIT. AI-assisted source review of README, LICENSE, `scripts/jev_eval.mjs`, committed `results/`. No live TypeSafe/Gateway spend; torch metrics not executed.

Related: [jev-calibrate](jev-calibrate.md), [jeval](jeval.md), [jevals](jevals.md).
