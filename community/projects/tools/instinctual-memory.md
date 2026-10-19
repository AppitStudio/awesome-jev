# mem (instinctual-memory)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Git-first durable memory for coding agents: turns past Claude Code, Codex and OpenCode sessions and your AGENTS.md files into sourced facts in a plain Git repo, searchable over MCP, with Jev reranking search results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sahilshingate01/instinctual-memory) |
| Maintainer | [sahilshingate01](https://github.com/sahilshingate01). Independently curated. |
| Format | Rust CLI + MCP server |
| Requirements | Rust 1.88+, Git 2.28+; `OPENROUTER_API_KEY` (or `MEM_JEV_API_KEY`) for Jev reranking, else a local reranker. |
| License | [Apache-2.0](https://github.com/sahilshingate01/instinctual-memory/blob/af903f05ae4abf83240ff98974aabcc18399a751/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.rs`](https://github.com/sahilshingate01/instinctual-memory/blob/af903f05ae4abf83240ff98974aabcc18399a751/src/jev.rs) at the pinned commit. |

## When to use

- Give agents memory of decisions from earlier sessions without a database.
- Keep that memory reviewable as Git history.
- Mismatch: build from source with Cargo; reranking is optional.

## How it works

`mem` backfills local sessions and project docs, consolidates them into curated facts in `memory.git`, and serves search over MCP. `src/jev.rs` sends the query and top rows to the OpenRouter Decisions API with `~typesafe/jev-latest` to rerank; without a key it uses a downloadable local reranker. Integration evidence: [`src/jev.rs`](https://github.com/sahilshingate01/instinctual-memory/blob/af903f05ae4abf83240ff98974aabcc18399a751/src/jev.rs).

## Get started

From the upstream README: `cargo install --path .`, then `mem init`, `mem backfill-local` and `mem consolidate` in a project.

```sh
cargo install --path .
mem init && mem backfill-local && mem consolidate
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README command reference

## Limits and data handling

With Jev on, the query and candidate rows go to OpenRouter. Extracted facts depend on the LLM extractor you configure.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit af903f05ae4a](https://github.com/sahilshingate01/instinctual-memory/tree/af903f05ae4abf83240ff98974aabcc18399a751). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
