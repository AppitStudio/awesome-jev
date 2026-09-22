# unsafe-c-finder

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Classifies C/C++ snippets and staged git hunks with TypeSafe Jev through OpenRouter: first a Noul-style unsafe probability, then a CWE bucket only when that probability crosses a follow-up threshold.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/etnt/unsafe-c-finder) |
| Maintainer | [etnt](https://github.com/etnt). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **`unsafe-c-finder`** (console script) with offline unit tests and labeled fixture eval scaffolding. |
| Requirements | Python 3; `OPENROUTER_API_KEY` for live classify/eval. Optional `UNSAFE_C_MODEL` / `UNSAFE_C_OPENROUTER_URL` for the alpha Decisions endpoint. |
| License | [MPL-2.0](https://github.com/etnt/unsafe-c-finder/blob/83098ecb4609bd8a115ee6a3fc072a894a8691b1/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline pytest inspected; live OpenRouter/Jev classify not run on the review host. |

## When to use

Use it when you want a **fail-closed C/C++ unsafe-change gate** that asks Jev for calibrated probabilities instead of free-form LLM text. Prefer [jev-semgrep](jev-semgrep.md) for Semgrep-oriented workflows, or [is-malicious](is-malicious.md) for broader deceptive-code screening. Do not treat fixture accuracy as a security certification.

## How it works

`OpenRouterClassifier` posts typed decisions to OpenRouter’s Decisions API (default model `~typesafe/jev-latest`). Code owns thresholds, CWE follow-up gating, exit codes (`0` clean, `1` blocking finding, `2` config/network errors), and optional `--on-error warn` fail-open. Staged diffs or stdin snippets become the decision state.

## Get started

```sh
git clone https://github.com/etnt/unsafe-c-finder.git
cd unsafe-c-finder
git checkout 83098ecb4609bd8a115ee6a3fc072a894a8691b1
python3 -m venv .venv && . .venv/bin/activate
pip install -e '.[test]'
pytest -q
# Live: export OPENROUTER_API_KEY=... ; unsafe-c-finder --stdin
```

Live runs send source snippets to OpenRouter (and thus TypeSafe Jev) and may incur charges. This listing did not call live APIs.

## Examples and demos

- Offline on the review host: `pytest -q` → **25 passed**.
- Upstream documents `unsafe-c-finder eval --fixtures tests/fixtures/labeled` for live smoke benchmarks (not run here).

## Limits and data handling

Source text leaves the host on live classify. Default API errors fail closed. OpenRouter Decisions may change while alpha. Eval reports are local artifacts; do not treat seed-fixture scores as production security evidence.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 83098ec](https://github.com/etnt/unsafe-c-finder/tree/83098ecb4609bd8a115ee6a3fc072a894a8691b1): MPL-2.0. AI-assisted source review of README, LICENSE, `src/unsafe_c_finder/classifier.py`. Offline pytest **25 passed**. No live OpenRouter calls on the review host.

Related: [is-malicious](is-malicious.md), [jev-semgrep](jev-semgrep.md), [jev-sec-bench](jev-sec-bench.md).
