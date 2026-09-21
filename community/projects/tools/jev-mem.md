# Jev-Mem

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

System-One–controlled agentic memory: TypeSafe Jev steers admission, multi-relational graph linking, and adaptive retrieval over preserved observations; a separate System-Two model synthesizes answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/libingzheren/Jev-Mem) |
| Maintainer | [libingzheren](https://github.com/libingzheren). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package (`jev-mem` 0.1.0) with CLI/demo/eval entry points; uses `typesafe_sdk`. |
| Requirements | Python **≥ 3.11**; `TYPESAFE_API_KEY` for live Jev (mock mode available). Answer-model keys for full LoCoMo/LongMemEval runs as documented upstream. |
| License | [MIT](https://github.com/libingzheren/Jev-Mem/blob/9fc5b9349ff892cd9523ab217bd18230351074df/LICENSE) (+ NOTICE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Offline pytest (excluding a broken public-release collection import) passed; live LoCoMo/LongMemEval and live Jev were **not** run. Paper metrics are upstream-reported, not revalidated here. Distinct from [PerfectRecall](perfectrecall.md) / [jevmory](jevmory.md). |

## When to use

Use it when you want inspectable System-One control over writing and retrieving a multi-view memory graph (semantic/temporal/causal/entity) before a text model answers. Prefer [PerfectRecall](perfectrecall.md) for Hermes SQLite evidence-question recall without a graph controller; prefer [invalidate](invalidate.md) for semantic TTL only.

## How it works

[`memory/jev_client.py`](https://github.com/libingzheren/Jev-Mem/blob/9fc5b9349ff892cd9523ab217bd18230351074df/memory/jev_client.py) calls TypeSafe Jev (`jev-latest`, base `https://api.typesafe.ai`) for typed noul/choice decisions that admit memories, choose relations, route retrieval budgets, and stop search. Observations stay local with provenance; queries and memory text leave the host when Jev is live. Config defaults live in [`memory/jev_mem_config.py`](https://github.com/libingzheren/Jev-Mem/blob/9fc5b9349ff892cd9523ab217bd18230351074df/memory/jev_mem_config.py).

## Get started

```sh
git clone https://github.com/libingzheren/Jev-Mem.git
cd Jev-Mem
git checkout 9fc5b9349ff892cd9523ab217bd18230351074df
python3 -m venv .venv && . .venv/bin/activate
pip install -e . pytest
pytest -q tests/ --ignore=tests/test_public_release.py
# Optional demo / eval: see upstream README (needs keys for live runs)
```

Live evaluation sends memory content and queries to TypeSafe and may call an answer LLM—budget carefully.

## Examples and demos

- Upstream README LoCoMo tables and architecture figure (author-reported).
- Offline pytest on the review host: **134 passed** (ignored `tests/test_public_release.py` due to `ModuleNotFoundError: scripts` on collection).

## Limits and data handling

Default write/read/admission flags are off until configured. Live Jev receives structured state and questions derived from memories/queries. Alpha research release; paper speed/quality claims are not reproduced here. Fallback-to-MAGMA and budget knobs trade coverage for cost.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 9fc5b93](https://github.com/libingzheren/Jev-Mem/tree/9fc5b9349ff892cd9523ab217bd18230351074df): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `memory/jev_client.py`, `memory/jev_mem_config.py`, and tests. **`pytest --ignore=tests/test_public_release.py`: 134 passed**. No live TypeSafe or benchmark runs.

Related: [PerfectRecall](perfectrecall.md), [jevmory](jevmory.md), [invalidate](invalidate.md).
