# PerfectRecall

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jev-powered agent memory provider (Mnemosyne-compatible): typed evidence questions over local SQLite memories for Hermes and Python/MCP callers—no embedding index in the production package.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/arslanr-com/perfectrecall) |
| Maintainer | [arslanr-com](https://github.com/arslanr-com). Independently curated; this page is not an upstream submission or endorsement. Fork lineage from Mnemosyne is documented upstream. |
| Format | Python package installable from GitHub; Hermes memory provider plug-in; optional MCP/`sync` extras. |
| Requirements | Python **≥ 3.10**. Hermes path needs Hermes installed and typically `OPENROUTER_API_KEY` (or configured Jev HTTP endpoint). Direct Python use configures Jev HTTP (OpenRouter decisions default; TypeSafe `/v1/systemone` supported in [mnemosyne/core/jev.py](https://github.com/arslanr-com/perfectrecall/blob/c8619c204165ca3ba5cbbb22fcb8f662e0d7899b/mnemosyne/core/jev.py)). |
| License | [MIT](https://github.com/arslanr-com/perfectrecall/blob/c8619c204165ca3ba5cbbb22fcb8f662e0d7899b/LICENSE) (Mnemosyne + PerfectRecall notices). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Offline pytest passed; Hermes install and live recall were **not** run. Upstream LongMemEval figures are historical predecessor results, not revalidated here. No live TypeSafe/OpenRouter calls. |

## When to use

Use it when an agent needs memory retrieval driven by short yes/no evidence questions instead of embeddings, especially as a Hermes `memory.provider`. Prefer [invalidate](invalidate.md) when you only need to mark facts superseded against new evidence. Prefer vector RAG when you already operate an embedding store.

## How it works

Eligible memories stay in local SQLite. Recall batches native Jev questions (criteria supplied by the caller), with pooling and parallel duplicate checks. Prefetch injects relevant memories into Hermes context under a cooperative deadline. Post-turn sync can store user messages; assistant messages default off. Failures surface as failures, not silent partial success.

## Get started

```sh
# Into the Hermes venv (adjust path):
python -m pip install 'git+https://github.com/arslanr-com/perfectrecall.git'
python -m perfectrecall.install
python -m perfectrecall jev-status   # config/key presence only; no API call
```

Library sketch:

```python
from perfectrecall import PerfectRecall
memory = PerfectRecall(session_id="project-cedar")
memory.remember("Project Cedar uses PostgreSQL.")
hits = memory.recall(
    "Which database does Cedar use?",
    evidence_questions=["Does this memory name Project Cedar's database?"],
)
```

Pinned offline tests:

```sh
git clone https://github.com/arslanr-com/perfectrecall.git
cd perfectrecall
git checkout c8619c204165ca3ba5cbbb22fcb8f662e0d7899b
python3 -m venv .venv && . .venv/bin/activate
pip install -e '.[dev]'
pytest -q
```

Live recall sends memory text and queries to the configured Jev HTTP API and may incur charges.

## Examples and demos

- Upstream [docs/INSTALLATION.md](https://github.com/arslanr-com/perfectrecall/blob/c8619c204165ca3ba5cbbb22fcb8f662e0d7899b/docs/INSTALLATION.md), [docs/TOOLS.md](https://github.com/arslanr-com/perfectrecall/blob/c8619c204165ca3ba5cbbb22fcb8f662e0d7899b/docs/TOOLS.md), [SECURITY.md](https://github.com/arslanr-com/perfectrecall/blob/c8619c204165ca3ba5cbbb22fcb8f662e0d7899b/SECURITY.md).
- Offline tests including `tests/test_jev*.py`: **141 passed** on Python 3.13 in this review.
- Benchmark notes under `benchmarks/` describe a frozen predecessor experiment—not re-run here.

## Limits and data handling

SQLite is local; eligible memory text and queries go to the configured Jev API. Alpha release; concurrency (`PERFECTRECALL_JEV_WORKERS`) and prefetch budgets trade cost for latency. Optional Hermes consolidation may also use the host LLM. Not an offline/zero-cloud memory system.

## Review and maintenance

Reviewed on **2026-09-21** at [commit c8619c2](https://github.com/arslanr-com/perfectrecall/tree/c8619c204165ca3ba5cbbb22fcb8f662e0d7899b): MIT. AI-assisted source review of README, LICENSE/NOTICE, `mnemosyne/core/jev.py`, and tests. **`pytest`: 141 passed**. No Hermes install, no live Jev HTTP.

Related: [invalidate](invalidate.md) (semantic TTL), [Hermes Jev Skills](hermes-jev-skills.md) (broader Hermes Jev skill pack).
