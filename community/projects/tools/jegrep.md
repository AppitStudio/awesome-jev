# jegrep

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Semantic grep CLI: describe the code you want in natural language; TypeSafe Jev (or OpenRouter→Jev) scores candidates without an embedding index.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/can1357/jegrep) |
| Maintainer | [can1357](https://github.com/can1357). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust crate / CLI **jegrep 0.1.1** (`cargo install jegrep` or GitHub release binaries). |
| Requirements | Rust toolchain for source builds, or a release binary; `OPENROUTER_API_KEY` and/or `TYPESAFE_API_KEY` (OpenRouter preferred when both exist; automatic failover on auth/credit/timeout/5xx). |
| License | [MIT](https://github.com/can1357/jegrep/blob/a280f14f6da8163bde67e0c49f58b23517a02882/LICENSE). |

## When to use

Use it to find code by intent (“where do we handle authentication?”) when regex/embeddings are a poor fit. Prefer [pg-jev](pg-jev.md) or [llama-index-jev](llama-index-jev.md) for database/RAG retrieval rather than local tree search.

## How it works

[`src/jev.rs`](https://github.com/can1357/jegrep/blob/a280f14f6da8163bde67e0c49f58b23517a02882/src/jev.rs) posts to TypeSafe `https://api.typesafe.ai/v1/systemone` (model `jev-latest`) or the OpenRouter path with the same contract. The walker collects candidate snippets; Jev scores them. `--json` emits ranked matches for agents.

## Get started

```sh
cargo install jegrep
# or: download a release binary from GitHub Releases
export TYPESAFE_API_KEY=…   # and/or OPENROUTER_API_KEY
cd my-repo
jegrep "where do we handle authentication?"
```

Inspected revision:

```sh
git clone https://github.com/can1357/jegrep.git
cd jegrep
git checkout a280f14f6da8163bde67e0c49f58b23517a02882
```

Live searches call TypeSafe/OpenRouter and send code snippets. This listing did not run a live search. `cargo test` on the review host needed rustc ≥ 1.88 (host had 1.85); tests were not executed here.

## Examples and demos

- README quick start and `--json` agent integration.
- Unit coverage inside [`src/jev.rs`](https://github.com/can1357/jegrep/blob/a280f14f6da8163bde67e0c49f58b23517a02882/src/jev.rs) (mock HTTP paths for Typesafe endpoint selection).
- Release archives with `SHA256SUMS` for Linux/macOS/Windows.

## Limits and data handling

Query text and candidate code snippets are sent to the configured provider. Prefer excluding secrets from trees you search. Ranking quality is operational, not a measured recall@k for your corpus. Linux glibc ≥ 2.39 for official binaries.

## Review and maintenance

Reviewed on **2026-09-20** at [commit a280f14](https://github.com/can1357/jegrep/tree/a280f14f6da8163bde67e0c49f58b23517a02882): **0.1.1**, MIT (`Cargo.toml` + LICENSE). AI-assisted source review of `src/jev.rs`, README, and license. **`cargo test` not run** (rustc 1.85 host vs dependency requirement 1.88). No live TypeSafe/OpenRouter searches were performed.

Related: [JevSQL](jevsql.md), [llama-index-jev](llama-index-jev.md), [pg-jev](pg-jev.md).
