# hunch

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python verbs on TypeSafe Jev—`classify`, `score`, `check`, `pick`, `rank`, `ask`, `where`—over scalars, lists, and pandas columns, with optional LLM draft generation that Jev then chooses among.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/steven-shoemaker/hunch) |
| Maintainer | [steven-shoemaker](https://github.com/steven-shoemaker). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package (`hunch-jev` 0.6.0) on PyPI; pandas helpers via `.hunch` accessor when pandas is installed. |
| Requirements | Python **≥ 3.10**, `TYPESAFE_API_KEY` (or `hunch.configure(api_key=...)`). Optional `pandas` for DataFrame verbs; LLM provider config for `generate`. |
| License | [MIT](https://github.com/steven-shoemaker/hunch/blob/22d5a7ba82a335d2d8e99c9992b70a5910880611/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Offline pytest passed with fakes; live TypeSafe and LLM calls were **not** run. |

## When to use

Use it when you want row-wise or list-wise typed judgments without hand-building System One payloads—ticket triage, ICP scoring, semantic filters on DataFrames. Prefer raw `typesafe-sdk` or Advocaat when you need lower-level batch control in TypeScript.

## How it works

Each verb maps to Choice, Score, or Noul (and combinations via `ask`). Duplicate values are asked once and fan out in a thread pool. `generate` may call an LLM to propose candidates; `pick`/`rank` let Jev decide. Thresholds and workflows stay in your code.

## Get started

```sh
pip install hunch-jev
export TYPESAFE_API_KEY=...
python -c 'import hunch; print(hunch.classify("great product", ["positive","negative","neutral"]))'
```

Pinned source review:

```sh
git clone https://github.com/steven-shoemaker/hunch.git
cd hunch
git checkout 22d5a7ba82a335d2d8e99c9992b70a5910880611
python3 -m venv .venv && . .venv/bin/activate
pip install -e '.[dev]'
pytest -q
```

Live verbs send row/evidence text to TypeSafe and may incur charges.

## Examples and demos

- README recipes for engineering triage, GTM ICP fit, SEO intent, and finance categorization.
- Offline [tests/](https://github.com/steven-shoemaker/hunch/tree/22d5a7ba82a335d2d8e99c9992b70a5910880611/tests) with fakes: **51 passed** on Python 3.13 in this review.

## Limits and data handling

Judged text goes to TypeSafe. Predictions without row evidence often cluster mid-probability—prefer ranking over hard thresholds for speculative statements. `generate` involves a separate LLM and its data policies.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 22d5a7b](https://github.com/steven-shoemaker/hunch/tree/22d5a7ba82a335d2d8e99c9992b70a5910880611): package **hunch-jev 0.6.0**, MIT. AI-assisted source review of README, LICENSE, `pyproject.toml`, and test fakes. **`pytest`: 51 passed**. No live TypeSafe or LLM calls.

Related: [Advocaat](advocaat.md) batches typed questions from TypeScript; [daf-jev](daf-jev.md) is a broader Python toolkit with MCP options.
