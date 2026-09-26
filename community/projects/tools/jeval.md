# jeval

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Calibration and cost-threshold CLI for probabilistic classifiers (including Jev confidence): measure whether stated confidence matches observed accuracy, then set human hand-off thresholds from mistake cost. Provider-neutral by design; offline synthetic demo included.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rlaope/jeval) |
| Maintainer | [rlaope](https://github.com/rlaope) / jeval contributors. Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python CLI/library **0.1.0** (`uv` / Hatch). |
| Requirements | Python ≥ 3.10; optional labeled decision JSONL from your Jev (or other) classifier. No TypeSafe key required for calibration itself. |
| License | [Apache-2.0](https://github.com/rlaope/jeval/blob/783b8241b46f2d3cb2a9b26b6b0498002f3d8fa7/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline tests/demo inspected. Does not call TypeSafe; it evaluates recorded confidences. |

## When to use

Use it when you already have labeled Jev (or other) decisions with confidences and need reliability curves, ECE/MCE, and cost-optimal auto vs hand-off thresholds. Prefer [jev-align](jev-align.md) when you are building calibrated AI Functions from feedback with GEPA. Do not treat the synthetic demo numbers as measured TypeSafe calibration.

## How it works

Ingest JSONL decisions, bin confidences (quantile bins), compare stated vs observed accuracy with Wilson intervals, and optimize thresholds under user-supplied mistake costs. The HTML report (see committed `examples/report-example.html`) shows verdict, reliability, and cost curves. Upstream states the tool is provider-neutral; the Jev name reflects the motivating model family.

## Get started

```sh
git clone https://github.com/rlaope/jeval.git
cd jeval
git checkout 783b8241b46f2d3cb2a9b26b6b0498002f3d8fa7
uv sync --group dev
uv run pytest -q
uv run jeval demo --out-dir /tmp/jeval-demo --seed 11 --scale 0.5
```

## Examples and demos

- Offline `jeval demo` rebuilds a seeded synthetic report (review host ran this successfully).
- Committed example report: [`examples/report-example.html`](https://github.com/rlaope/jeval/blob/783b8241b46f2d3cb2a9b26b6b0498002f3d8fa7/examples/report-example.html).
- Feed your own labeled decisions via upstream CLI (`jeval report` / collect paths).

## Limits and data handling

Calibration quality depends on honest labels and enough per-bin samples; wide Wilson intervals are expected on small bins. Cost tables use your supplied costs (demo costs are synthetic). The tool does not verify vendor calibration claims.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 783b824](https://github.com/rlaope/jeval/tree/783b8241b46f2d3cb2a9b26b6b0498002f3d8fa7): **0.1.0**, Apache-2.0. AI-assisted source review of README, LICENSE, and package layout. Ran `uv sync --group dev`, `uv run pytest` (**488** collected tests, all passed), and `uv run jeval demo` (report written). No TypeSafe calls.

Related: [jev-align](jev-align.md), [JevScope](jevscope.md), [Advocaat](advocaat.md).

<!-- knowledge:backlinks:start -->
## Knowledge guides

- [Jev decision audits: validate the business case](../../knowledge-base/articles/jev-decision-audit.md) — Independently suggested by JevList; not an endorsement by barnyx. Join outcomes to predictions and compare threshold policies.
<!-- knowledge:backlinks:end -->
