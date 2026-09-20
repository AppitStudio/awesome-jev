# invalidate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Semantic TTL for agent memory: each stored fact gets a lease; new evidence is checked against every memory with TypeSafe Jev, then code marks superseded facts without rewriting their text.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chopratejas/invalidate) |
| Maintainer | [chopratejas](https://github.com/chopratejas). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **invalidate 0.1.0** (`pip install invalidate`) with CLI (`invalidate demo` / `invalidate ui`) and optional memory-store adapters. |
| Requirements | Python ≥ 3.10; live judgment needs `TYPESAFE_API_KEY` (`typesafe-sdk`). |
| License | [Apache-2.0](https://github.com/chopratejas/invalidate/blob/d6ade60108b8064bafaee425fd8f9e78683dbd82/LICENSE). |

## When to use

Use it when an agent or RAG cache must *un-remember* facts that new evidence contradicts, instead of only appending. Prefer embedding search alone when you only need retrieval ranking. Prefer [Hermes Jev Skills](hermes-jev-skills.md) memory filtering when you already run Hermes skill packs rather than a dedicated invalidation library.

## How it works

[`src/invalidate/judge.py`](https://github.com/chopratejas/invalidate/blob/d6ade60108b8064bafaee425fd8f9e78683dbd82/src/invalidate/judge.py) wraps `typesafe_sdk.TypeSafeClient` for batched yes/no votes; policy code in the package decides superseded vs keep vs human review. Memory text is never edited—stale rows are marked and replacements stored verbatim. Adapters cover Chroma, Mem0, Letta, Graphiti, pgvector, Qdrant, and related stores.

## Get started

```sh
pip install invalidate
export TYPESAFE_API_KEY=…   # or .env in the working directory
invalidate demo             # small offline-shaped demo path; live Jev when keyed
invalidate ui               # local UI at http://127.0.0.1:7411
# or inspect:
git clone https://github.com/chopratejas/invalidate.git
cd invalidate
git checkout d6ade60108b8064bafaee425fd8f9e78683dbd82
```

Hosted playground: [invalidate-playground.vercel.app](https://invalidate-playground.vercel.app). Live checks send memory/event text to TypeSafe. This listing did not run the playground or call the API.

## Examples and demos

- README two-minute demo and Python `Invalidate` snippet.
- Upstream eval notes under [`evals/`](https://github.com/chopratejas/invalidate/tree/d6ade60108b8064bafaee425fd8f9e78683dbd82/evals) (vendor-reported; not re-run here).
- Optional adapters under `src/invalidate/adapters/`.

## Limits and data handling

Event and memory text leave the machine for TypeSafe on each observe/recall path. Upstream cost/latency figures and eval percentages are vendor-reported, not catalog benchmarks. Questions and instructions are treated as non-evidence by policy—confirm behavior before production trust.

## Review and maintenance

Reviewed on **2026-09-20** at [commit d6ade60](https://github.com/chopratejas/invalidate/tree/d6ade60108b8064bafaee425fd8f9e78683dbd82): **0.1.0**, Apache-2.0. AI-assisted source review of README, `judge.py`, `pyproject.toml`, and license. Offline pytest / live TypeSafe calls were not run on the review host.

Related: [Hermes Jev Skills](hermes-jev-skills.md), [llama-index-jev](llama-index-jev.md).
