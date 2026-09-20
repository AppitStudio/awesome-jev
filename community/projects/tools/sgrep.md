# sgrep

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Semantic grep for codebases: chunk a tree (AST / tree-sitter / window), optionally pre-filter locally, then ask TypeSafe Jev whether each chunk matches a plain-English query.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Lagnajit09/sgrep) |
| Maintainer | [Lagnajit09](https://github.com/Lagnajit09) / Lm09. Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package/CLI (`sgrep` / `sgrep-jev` on PyPI metadata). |
| Requirements | Python ≥ 3.10; live scans need `TYPESAFE_API_KEY` (default TypeSafe direct) or optional Vercel AI Gateway. Offline `--mock` needs no key. First live-ish prefilter may download a small local embedding model. |
| License | [MIT](https://github.com/Lagnajit09/sgrep/blob/af54cc1da5164289337e4198b2f69a67fe93ddea/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `--mock` scan inspected. Live TypeSafe calls were not run. Distinct from [jegrep](jegrep.md) and [jev-semgrep](jev-semgrep.md). |

## When to use

Use it when you want meaning-based file hits without maintaining a vector index, and you are willing to pay per-chunk Jev calls (mitigated by cache and top-k prefilter). Prefer classical grep for exact strings, or [jegrep](jegrep.md) if you want the Rust CLI sibling workflow.

## How it works

[`sgrep/clients/typesafe.py`](https://github.com/Lagnajit09/sgrep/blob/af54cc1da5164289337e4198b2f69a67fe93ddea/sgrep/clients/typesafe.py) fans out typed questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`). Local code owns discovery, chunking, hybrid prefilter, ranking, and caching. `--provider mock` substitutes an offline judge for plumbing checks.

## Get started

```sh
git clone https://github.com/Lagnajit09/sgrep.git
cd sgrep
git checkout af54cc1da5164289337e4198b2f69a67fe93ddea
python -m pip install -e .
python -m sgrep scan "which code handles authentication" . --mock
```

Live scans: put `TYPESAFE_API_KEY` in `.env` (gitignored) and omit `--mock`. That incurs TypeSafe usage and may download the local prefilter model.

## Examples and demos

- README mermaid flow and `FLOW.md` / `DECISIONS.md` architecture notes.
- Offline mock scan (credential-free).

## Limits and data handling

Chunk text leaves the host on live provider calls. Prefilter embeddings run locally when enabled. Upstream throughput/cost figures are author-reported. Packaging metadata may still mention an older `Lm09/sgrep-jev` homepage—use this GitHub URL as canonical.

## Review and maintenance

Reviewed on **2026-09-20** at [commit af54cc1](https://github.com/Lagnajit09/sgrep/tree/af54cc1da5164289337e4198b2f69a67fe93ddea): MIT. AI-assisted source review of clients, engine, and README. **`python -m sgrep scan "auth" . --mock`** completed offline. No dedicated pytest suite found at this revision; no live TypeSafe calls.

Related: [jegrep](jegrep.md), [jev-semgrep](jev-semgrep.md), [jgrep](jgrep.md).
