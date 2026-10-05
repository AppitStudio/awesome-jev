# Decision Model Rust SDK

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Async Rust SDK for decision models served through the System One API (TypeSafe Jev and compatible vendors): typed question builders or `#[derive(QuestionSet)]`, one HTTP/2 connection per client, and an adapter crate for OpenAI/Anthropic/Gemini.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zchee/decision-model-sdk-rust) |
| Product homepage | [crates.io](https://crates.io/crates/decision-model-sdk) |
| Maintainer | [zchee](https://github.com/zchee). Independently curated. |
| Format | Rust library crates (port of typesafe-sdk-python 0.7.2) |
| Requirements | Rust toolchain and Tokio; an API key and base URL for TypeSafe Jev or another System One vendor. |
| License | [Apache-2.0](https://github.com/zchee/decision-model-sdk-rust/blob/c5d4459f2e01bf72ccbf1b2cd55a801c039e7b07/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Use Jev from a Rust service with typed structs instead of hand-written JSON.
- Ask the same System One questions of a chat model through the adapter crate for comparison.
- Mismatch: yoagent or other frameworks already wrap a client if you need a full agent loop.

## How it works

The client posts named questions about a state to `POST /v1/systemone` and lists models via `GET /v1/models`; responses decode into the declared struct. It keeps the Python SDK's retry defaults within a 30 s budget, obeys `Retry-After`, and redacts the key from logs. Deliberate deviations from the Python SDK are documented upstream.

## Get started

Add the crate (live calls need a key and base URL):

```sh
cargo add decision-model-sdk
cargo add tokio --features macros,rt-multi-thread
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README quickstart, typed answers, and [docs.rs](https://docs.rs/decision-model-sdk) API reference.

## Limits and data handling

Unofficial port, early version (0.1.x). Requests are billed by the vendor you configure.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit c5d4459f2e01](https://github.com/zchee/decision-model-sdk-rust/tree/c5d4459f2e01bf72ccbf1b2cd55a801c039e7b07). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
