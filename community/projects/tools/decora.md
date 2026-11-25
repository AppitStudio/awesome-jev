# Decora by Yan (Rust gateway that serves one decision contract across the TypeSafe Jev, OpenAI, Gemini and OpenRouter Decisions dialects)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Single-tenant Decisions protocol gateway in Rust: clients call any of four dialects (OpenAI, Google Gemini, TypeSafe Jev or OpenRouter) and Decora passes the request through or translates it to another backend, with per-attempt failover. Every upstream answer is checked (probabilities sum to 1, every option covered) and rejected with a 502 if not; a live WebAssembly demo shows the translation without any keys.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Yan-Zero/decora) |
| Maintainer | [Yan](https://github.com/Yan-Zero). Independently curated. |
| Format | Rust server (2024 edition) with a WebAssembly playground |
| Requirements | Rust 2024 toolchain; API keys for the backends you configure (TypeSafe, OpenRouter, OpenAI or Gemini). |
| License | [MIT](https://github.com/Yan-Zero/decora/blob/9f35e679a0257a41738c7309d00cde798d4a1aae/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/adapter.rs`](https://github.com/Yan-Zero/decora/blob/9f35e679a0257a41738c7309d00cde798d4a1aae/src/adapter.rs) at the pinned commit. |

## When to use

- Put one decision API in front of Jev and other decision models, with verified probabilities and failover.
- Mismatch: if you only call Jev directly; the official SDK is simpler.

## How it works

`src/dialect.rs` parses each inbound dialect into a canonical decision IR and `src/adapter.rs` adapts it to each backend, including a `typesafe` backend that calls `https://api.typesafe.ai/v1/systemone` with `jev-latest` and records TypeSafe's billable-input usage; `config.example.yaml` shows `jev-official` and OpenRouter `typesafe/jev-1.13` routes. Built as a Kiroween 2026 entry. Integration evidence: [`src/adapter.rs`](https://github.com/Yan-Zero/decora/blob/9f35e679a0257a41738c7309d00cde798d4a1aae/src/adapter.rs).

## Get started

Copy the example config, set your keys as environment variables, and run the gateway.

```sh
git clone https://github.com/Yan-Zero/decora
cd decora
cp config.example.yaml config.yaml   # enable the jev-official backend
cargo run --locked --release -- config.yaml
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live WASM protocol converter: [decora.lyanyixin2533.workers.dev/](https://decora.lyanyixin2533.workers.dev/)
- Protocol notes: [github.com/Yan-Zero/decora/blob/9f35e679a0257a41738c7309d00cde798d4a1aae/docs/PROTOCOL.md](https://github.com/Yan-Zero/decora/blob/9f35e679a0257a41738c7309d00cde798d4a1aae/docs/PROTOCOL.md)

## Limits and data handling

Fallback routes can send your state to non-TypeSafe providers (OpenAI, Gemini, OpenRouter) when configured. Cross-dialect translation drops capabilities a backend lacks. Hackathon project; the test and audit badges are the author's own.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 9f35e679a025](https://github.com/Yan-Zero/decora/tree/9f35e679a0257a41738c7309d00cde798d4a1aae). Inspected the README, `docs/PROTOCOL.md`, the example config and the adapter code at the pinned commit; the gateway was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
