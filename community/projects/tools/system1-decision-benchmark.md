# System-1 decision benchmark

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Common-ground benchmark of 50 System-1 decision-model configurations — Jev, Clef, Clef-flash, Kev, Nimble and Tev1 against embedding, reranker, NLI and prompted-LLM baselines — on 22 BTZSC datasets (500 test items each), with saved scores, a living report and a paper draft.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sj0605-DataSci/system1-decision-benchmark) |
| Maintainer | [Sj0605-DataSci](https://github.com/Sj0605-DataSci). Independently curated. |
| Format | Research repository: Python runners, saved per-example scores, report and LaTeX paper draft |
| Requirements | Python; recomputing tables needs only the saved scores; re-running models needs a GPU, the `btzsc` package (patched as described upstream) and, for Jev, a TypeSafe API key. |
| License | [MIT](https://github.com/Sj0605-DataSci/system1-decision-benchmark/blob/6570e88cfdd6ebc0b7e2e3262d61a4b6c222b6a0/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Judge Jev against Clef, Kev, Nimble, Tev1, NLI and rerankers on the same splits before choosing a decision backbone.
- Reuse `decision_bench.py` to run Choice or Noul over HTTP against any typed-decision service, including Jev.
- Mismatch: 500 items per dataset and one run; maintainer measurements with protocol-sensitive rankings, not an independent leaderboard.

## How it works

[`decision_bench.py`](https://github.com/Sj0605-DataSci/system1-decision-benchmark/blob/6570e88cfdd6ebc0b7e2e3262d61a4b6c222b6a0/decision_bench.py) runs Choice and Noul questions over HTTP against typed-decision services (Jev, Kev, Ollama), and [`decision_chunk.py`](https://github.com/Sj0605-DataSci/system1-decision-benchmark/blob/6570e88cfdd6ebc0b7e2e3262d61a4b6c222b6a0/decision_chunk.py) splits label sets above 26 options into a hierarchical Choice. [`common_bench.py`](https://github.com/Sj0605-DataSci/system1-decision-benchmark/blob/6570e88cfdd6ebc0b7e2e3262d61a4b6c222b6a0/common_bench.py) covers embedding, reranker, NLI and LLM baselines. Every model uses the same 100-item calibration / 500-item test split per dataset; [`final_report.py`](https://github.com/Sj0605-DataSci/system1-decision-benchmark/blob/6570e88cfdd6ebc0b7e2e3262d61a4b6c222b6a0/final_report.py) rebuilds [`results/common/REPORT.md`](https://github.com/Sj0605-DataSci/system1-decision-benchmark/blob/6570e88cfdd6ebc0b7e2e3262d61a4b6c222b6a0/results/common/REPORT.md) from the saved scores.

## Get started

Rebuild every table from the committed scores (no model calls):

```sh
git clone https://github.com/Sj0605-DataSci/system1-decision-benchmark.git && cd system1-decision-benchmark
python final_report.py      # rebuilds results/common/REPORT.md
./paper/build.sh            # figures + paper/paper.pdf (needs pdflatex)
```

Rebuilding reports is offline. Re-running Jev sends benchmark items to TypeSafe and is billed to your key.

## Examples and demos

- Living report with every table: [`results/common/REPORT.md`](https://github.com/Sj0605-DataSci/system1-decision-benchmark/blob/6570e88cfdd6ebc0b7e2e3262d61a4b6c222b6a0/results/common/REPORT.md).
- Pre-registered plan and criteria: [`RESEARCH_PLAN.md`](https://github.com/Sj0605-DataSci/system1-decision-benchmark/blob/6570e88cfdd6ebc0b7e2e3262d61a4b6c222b6a0/RESEARCH_PLAN.md); paper draft in [`paper/`](https://github.com/Sj0605-DataSci/system1-decision-benchmark/tree/6570e88cfdd6ebc0b7e2e3262d61a4b6c222b6a0/paper).

## Limits and data handling

All numbers are the maintainer's measurements (jev-1.13.0 through the public API), one run of 500 items per dataset; CIs cover item sampling only and training overlap is unknown for several models. The repo's own model section is a plan, not a trained model. Not re-run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 6570e88cfdd6](https://github.com/Sj0605-DataSci/system1-decision-benchmark/tree/6570e88cfdd6ebc0b7e2e3262d61a4b6c222b6a0). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
