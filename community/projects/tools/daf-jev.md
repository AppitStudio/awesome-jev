# daf-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Composable Python toolkit for TypeSafe Jev (System One): typed question builders, client with retries, confidence gates / routing compose helpers, batch evaluator, calibration stats, CLI, optional MCP server, and an agent skill.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/docxology/daf-jev) |
| Maintainer | [docxology](https://github.com/docxology). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **daf-jev 0.3.0** (`pip` / `uv`; CLI `daf-jev`). |
| Requirements | Python **≥ 3.10**; `httpx`, `pyyaml`. Live calls need `JEV_API_KEY` or `TYPESAFE_API_KEY`. Optional extras: `mcp`, `matplotlib`, bench tooling. |
| License | [MIT](https://github.com/docxology/daf-jev/blob/ff7b28515d7f60c9f7182b128b76b90fbfcba66f/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline unit tests inspected; live TypeSafe / MCP sessions were not run. |

## When to use

Use it when you want a **batteries-included Python client and composition layer** around `/v1/systemone` (batching, gates, evaluation, calibration, MCP) rather than a single-purpose agent hook. Prefer [Advocaat](advocaat.md) for a TypeScript `ask` batch client; prefer [SemDecide](semdecide.md) for Unix CLI exit-code predicates; prefer [TypeSafe MCP](typesafe-mcp.md) for a thinner MCP surface.

## How it works

[`src/daf_jev/client.py`](https://github.com/docxology/daf-jev/blob/ff7b28515d7f60c9f7182b128b76b90fbfcba66f/src/daf_jev/client.py) wraps `POST https://api.typesafe.ai/v1/systemone` with retries and typed errors. Primitives (`noul` / `choice` / `score`), compose helpers (`confidence_gate`, `route` / `pick`, `composite_score`), `Evaluator`, `Decider`, `UsageLedger`, and optional `daf-jev serve` MCP tools live alongside. Live markers are skipped when no API key is present.

## Get started

```sh
git clone https://github.com/docxology/daf-jev.git
cd daf-jev
git checkout ff7b28515d7f60c9f7182b128b76b90fbfcba66f
python3 -m venv .venv && . .venv/bin/activate
pip install -e '.[dev]'
pytest -q -m 'not live'
```

Set `JEV_API_KEY` (or `TYPESAFE_API_KEY`) before live `ask` / MCP use. Live calls send question state to TypeSafe and can incur charges; this listing ran offline unit tests only.

## Examples and demos

- Offline `pytest -m 'not live'` — **320 passed**, 2 live deselected on the review host.
- Upstream README mermaid decision flow, manuscript/figures pipeline, and MCP tool list.

## Limits and data handling

Question `state` and instructions leave the host on live asks. Manuscript benchmarks and cost anecdotes were not independently re-run. MCP extra requires installing optional dependencies.

## Review and maintenance

Reviewed on **2026-09-20** at [commit ff7b285](https://github.com/docxology/daf-jev/tree/ff7b28515d7f60c9f7182b128b76b90fbfcba66f): **0.3.0**, MIT. AI-assisted source review of README, LICENSE, `client.py`, `config.py`, `pyproject.toml`, and tests. Ran editable install + `pytest -m 'not live'` (320 pass). No live TypeSafe calls.

Related: [Advocaat](advocaat.md), [SemDecide](semdecide.md), [TypeSafe MCP](typesafe-mcp.md).
