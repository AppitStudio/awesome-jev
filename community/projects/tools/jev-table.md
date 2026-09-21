# jev-table

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first CLI that adds AI columns to CSV/JSONL rows with TypeSafe Jev: typed answers, confidence, review queue, resume cache, and a dry-run cost preview before any spend.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dtduc-git/jev-table) |
| Maintainer | [dtduc-git](https://github.com/dtduc-git) (Duke - Duc Dinh). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python CLI (`jev-table` **0.1.1**) via `uv` / PyPI; Apache-2.0. |
| Requirements | Python ≥ 3.10; `TYPESAFE_API_KEY`; column specs as [jev-packs](https://github.com/dtduc-git/jev-packs)-compatible YAML. Depends on `typesafe-sdk` and `jevassert`. |
| License | [Apache-2.0](https://github.com/dtduc-git/jev-table/blob/94c5cce8d1d342478f643daddd00d44de985cccd/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline pytest inspected. Live TypeSafe labeling was not run on the review host. |

## When to use

Use it when you want spreadsheet-friendly Jev labels with automation thresholds and an explicit review column. Prefer raw SDK scripts for one-off experiments, or [jev-packs](https://github.com/dtduc-git/jev-packs) alone when you only need golden packs/benchmarks without CSV I/O.

## How it works

[`src/jev_table/transport.py`](https://github.com/dtduc-git/jev-table/blob/94c5cce8d1d342478f643daddd00d44de985cccd/src/jev_table/transport.py) uses `AsyncTypeSafeClient.system_one` against `https://api.typesafe.ai` (overridable `--base-url`). The engine deduplicates states, applies pack thresholds, writes `*.jev.csv` plus corrections/stats/cache, and dry-run mode estimates cost without calling the API.

## Get started

```sh
git clone https://github.com/dtduc-git/jev-table.git
cd jev-table
git checkout 94c5cce8d1d342478f643daddd00d44de985cccd
uv sync --no-sources
uv run pytest -q
# Live (TypeSafe charges):
# export TYPESAFE_API_KEY=…
# uvx jev-table examples/sms-triage/sample.csv --spec examples/sms-triage/pack.yaml --dry-run
# uvx jev-table examples/sms-triage/sample.csv --spec examples/sms-triage/pack.yaml
```

## Examples and demos

- `examples/sms-triage/` sample CSV + pack.
- Upstream `docs/demo.gif` / `docs/demo.sh` asciinema path.
- Offline **`uv run --no-sources pytest`**: **51 passed** on the review host.

## Limits and data handling

Row state fields named in the pack leave the machine on live runs. Low-confidence or `unknown` answers land in `review` rather than auto-accepting. Dry-run sends nothing. Confirm TypeSafe pricing separately; README cost figures are illustrative.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 94c5cce](https://github.com/dtduc-git/jev-table/tree/94c5cce8d1d342478f643daddd00d44de985cccd): **0.1.1**, Apache-2.0. AI-assisted source review of README, `transport.py`, CLI/engine, and LICENSE. **51** offline tests passed. No live TypeSafe calls.

Related: [jeval](jeval.md), [Typed Evals](typed-evals.md), [dbt_jev](dbt-jev.md).
