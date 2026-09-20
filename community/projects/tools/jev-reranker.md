# jev-reranker

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Rust CLI that pipes JSON candidate arrays through TypeSafe Jev to **rerank**, **filter** (evidence), or **compress** (passage extract) results for LLM context. Distinct from [llama-index-jev](llama-index-jev.md) (LlamaIndex Python postprocessors) and from other same-named experiments not listed here.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shinpr/jev-reranker) |
| Maintainer | [shinpr](https://github.com/shinpr). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust binary published via npm as **jev-reranker 0.1.1** (platform packages); stdin/stdout JSON. |
| Requirements | Node.js **≥ 14** for the npm-distributed binary path, or a Rust toolchain to build from source. Live runs need `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/shinpr/jev-reranker/blob/9462061cd3fe5782739b33a437ad96497751532f/LICENSE). TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; `cargo test` could not run on the review host (rustc 1.85 vs crates requiring 1.88+). No live TypeSafe calls. |

## When to use

Use it when you already have BM25/vector/search JSON and want a **Unix-pipeable Jev stage** before the LLM. Prefer [llama-index-jev](llama-index-jev.md) inside LlamaIndex pipelines; prefer [jegrep](jegrep.md) when you need intent search over a codebase rather than reranking an existing candidate list.

## How it works

[`src/http.rs`](https://github.com/shinpr/jev-reranker/blob/9462061cd3fe5782739b33a437ad96497751532f/src/http.rs) posts Noul batches to `https://api.typesafe.ai/v1/systemone`. Modes (`rerank` / `filter` / `compress`) are separate invocations; metadata fields pass through. Default batching is sequential per ~30 candidates; compression scores sentence/line units.

## Get started

```sh
npm install --global jev-reranker
# or from the reviewed tip:
git clone https://github.com/shinpr/jev-reranker.git
cd jev-reranker
git checkout 9462061cd3fe5782739b33a437ad96497751532f
# cargo test   # needs a newer rustc than 1.85 on this review host
printf '%s\n' '[{"text":"Build artifacts are cached locally."},{"text":"Access tokens expire after one hour."}]' \
  | jev-reranker --query "How long do access tokens last?"
```

Set `TYPESAFE_API_KEY` before live runs. Candidate text leaves the host; this listing did not execute live reranks.

## Examples and demos

- Upstream README stdin examples and mode table.
- Agent skill folder `skills/jev-reranker/` for harness install notes.

## Limits and data handling

Each mode invocation bills its own batches; piping modes multiplies requests. HTTP 429/529 retry twice; other errors fail the run. Upstream quality/cost figures were not independently measured. Review-host `cargo test` blocked by rustc version.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 9462061](https://github.com/shinpr/jev-reranker/tree/9462061cd3fe5782739b33a437ad96497751532f): **0.1.1**, MIT. AI-assisted source review of README, LICENSE, `Cargo.toml`, and `src/http.rs`. `cargo test` not completed (toolchain). No live TypeSafe calls.

Related: [llama-index-jev](llama-index-jev.md), [jegrep](jegrep.md), [jsort](jsort.md), [jev-mcp](jev-mcp.md).
