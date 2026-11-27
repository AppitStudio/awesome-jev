# jev-rs by Yijun Yu (Rust engine that answers Jev-style typed questions from any LLM's logprobs, with a wire-compatible server and MCP tool)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Rust engine that answers `noul`, `choice` and `score` questions from any decoder's next-token log-probabilities in one prefill, with per-bucket temperature calibration and option-order permutations. Ships a `jev` CLI, a server wire-compatible with TypeSafe's `POST /v1/systemone`, an MCP tool for coding agents, and an eval/calibrate stack; the README reports measured accuracy, calibration and latency for three local models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yijunyu/jev-rs) |
| Maintainer | [Yijun Yu](https://github.com/yijunyu) (yijunyu). Independently curated. |
| Format | Rust CLI + server + MCP tool (crate `jev-rs`) |
| Requirements | A `llama-server` (any GGUF) or an OpenAI-compatible endpoint with logprobs; prebuilt binaries for macOS and Linux or Rust to build. |
| License | [MIT or Apache-2.0](https://github.com/yijunyu/jev-rs/blob/a56901b67358796c74d6a4e86f89aec78339ea35/LICENSE-MIT) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/server.rs`](https://github.com/yijunyu/jev-rs/blob/a56901b67358796c74d6a4e86f89aec78339ea35/src/server.rs) at the pinned commit. |

## When to use

- Developers who want Jev-shaped decisions from local or hosted LLMs, or to compare open decision models with one metric stack.
- Mismatch: more than 26 options per question (single-letter labels).

## How it works

`src/server.rs` exposes `POST /v1/systemone` and `GET /v1/models`, so TypeSafe SDKs can use it via `TYPESAFE_BASE_URL`; scoring reads label logprobs from the backend and applies a restricted softmax. It does not call TypeSafe's hosted Jev. Integration evidence: [`src/server.rs`](https://github.com/yijunyu/jev-rs/blob/a56901b67358796c74d6a4e86f89aec78339ea35/src/server.rs).

## Get started

Install the binary, start llama-server with a model, and ask a question.

```sh
cargo install jev-rs   # or the install.sh in the README
llama-server -hf Qwen/Qwen3-4B-GGUF --port 8089 -np 2 -c 8192
jev --backend http://127.0.0.1:8089 ask --state "Refund the duplicate charge" --noul "churn=Does the customer threaten to leave?"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Measured results: [github.com/yijunyu/jev-rs#measured-not-claimed](https://github.com/yijunyu/jev-rs#measured-not-claimed)
- Examples: [github.com/yijunyu/jev-rs/tree/main/examples](https://github.com/yijunyu/jev-rs/tree/main/examples)

## Limits and data handling

Independent project. Quality depends on the backend model; the README says small models need `jev calibrate` before their probabilities are trusted. The README's one-line installer pipes a script to `sh`; review it first or use `cargo install`.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit a56901b67358](https://github.com/yijunyu/jev-rs/tree/a56901b67358796c74d6a4e86f89aec78339ea35). Inspected the README, both licence files and `src/server.rs` at the pinned commit and confirmed the `jev-rs` crate on crates.io; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
