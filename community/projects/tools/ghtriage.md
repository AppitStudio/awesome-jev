# ghtriage

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub issue classifier (`ghtriage` / package `jev-issue-classifier`): TypeSafe Jev labels type/area/severity and related Noul gates with calibrated confidence, then code-owned policy and write guards apply labels.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev) |
| Maintainer | [KalyanM45](https://github.com/KalyanM45). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **`jev-issue-classifier` 0.1.0** (console script `ghtriage`). |
| Requirements | Python ≥ 3.10; `TYPESAFE_API_KEY` for live classify; optional `GITHUB_TOKEN` to write labels (`--apply` off by default). |
| License | [MIT](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev/blob/e1994acf727d6fa6599cb1093b9e91e13dfa2beb/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline pytest inspected; live TypeSafe/GitHub writes not run on the review host. |

## When to use

Use it when you want **auditable typed triage** on opened issues (Choice/Score/Noul in two batched System One calls) with offline eval gates. Prefer [jev-issue-radar](jev-issue-radar.md) for duplicate-focused dashboards. Do not auto-write labels without reviewing `--apply` budgets and repo allowlists.

## How it works

Adapters call TypeSafe System One; `ghtriage/core/questions.py` defines eight parallel questions; policy and write guards live in Python. Eval suites freeze fixtures so CI can gate without a live key.

## Get started

```sh
git clone https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev.git
cd GitHub-Issue-Classification-Using-Jev
git checkout e1994acf727d6fa6599cb1093b9e91e13dfa2beb
python3 -m venv .venv && . .venv/bin/activate
pip install -e '.[dev]'
ruff check .
PYTHONPATH=. pytest -q
# Live: cp .env.example .env  # TYPESAFE_API_KEY; then ghtriage once <issue>
```

Live classification sends issue title/body metadata to TypeSafe and may incur charges. Label writes need `GITHUB_TOKEN` and `--apply`. This listing did not call TypeSafe or write GitHub labels.

## Examples and demos

- Offline on the review host: `ruff check .` clean; `PYTHONPATH=. pytest -q` → **56 passed, 6 skipped**.
- Upstream README documents Action/watch flows and frozen eval sets.

## Limits and data handling

Issue text leaves the host on live classify. Writing labels is opt-in and repo-scoped. Model answers never authorize writes by themselves—inspect upstream guard layers.

## Review and maintenance

Reviewed on **2026-09-22** at [commit e1994ac](https://github.com/KalyanM45/GitHub-Issue-Classification-Using-Jev/tree/e1994acf727d6fa6599cb1093b9e91e13dfa2beb): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `src/ghtriage/`. Offline ruff + pytest 56 passed / 6 skipped. No live TypeSafe or GitHub writes on the review host.

Related: [jev-issue-radar](jev-issue-radar.md), [jev-pr-judge](jev-pr-judge.md), [Clean Code Review](../apps/clean-code-review.md).
