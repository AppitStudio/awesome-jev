# DecisionPivot (contrast-pair benchmark for decision models, with Jev runs)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Diagnostic benchmark (formerly DecideBench) of contrast pairs that differ in one decisive detail, comparing open 27B decision models with hosted Jev on whether decisions stay right when the case changes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/StartLuxLabs/DecisionPivot) |
| Maintainer | [StartLuxLabs](https://github.com/StartLuxLabs). Independently curated. |
| Format | Benchmark data, runner and scoring (Python, Apache-2.0) |
| Requirements | Python, the dataset from the repo or Hugging Face, and a `/v1/systemone` endpoint (a TypeSafe key for Jev) to rerun. |
| License | [Apache-2.0](https://github.com/StartLuxLabs/DecisionPivot/blob/fd57688f033864e64c452561ffdfcba9739d1811/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`runner/bench_http.py`](https://github.com/StartLuxLabs/DecisionPivot/blob/fd57688f033864e64c452561ffdfcba9739d1811/runner/bench_http.py) at the pinned commit. |

## When to use

- Compare decision models on pair accuracy, not just public scores.
- Test a Jev-compatible endpoint before trusting it at a control point.
- Mismatch: research benchmark; results are the authors'.

## How it works

`runner/bench_http.py` sends each task to `<url>/v1/systemone` and stores the answers; `scoring/score.py` produces the tables, including the published `jev-1.13` runs. Integration evidence: [`runner/bench_http.py`](https://github.com/StartLuxLabs/DecisionPivot/blob/fd57688f033864e64c452561ffdfcba9739d1811/runner/bench_http.py).

## Get started

Read the runner README, then point the runner at Jev or another System One endpoint.

```sh
git clone https://github.com/StartLuxLabs/DecisionPivot.git && cd DecisionPivot
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Paper: [arxiv.org/abs/2610.28522](https://arxiv.org/abs/2610.28522)
- Dataset: [huggingface.co/datasets/startlux-models/DecisionPivot](https://huggingface.co/datasets/startlux-models/DecisionPivot)

## Limits and data handling

Benchmark items go to whichever endpoint you point the runner at.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit fd57688f0338](https://github.com/StartLuxLabs/DecisionPivot/tree/fd57688f033864e64c452561ffdfcba9739d1811). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
