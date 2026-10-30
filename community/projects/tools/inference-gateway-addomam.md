# infer (self-hosted inference gateway that routes LLM, Decisions and System One / Jev calls through one place)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust gateway for watching and managing inference API calls centrally: native passthrough to providers including TypeSafe's `/v1/systemone`, model resolution for chat, OpenAI Decisions and System One requests, translation between Decisions and System One question types, and support for local Jev-style models on llama.cpp. Configured with a TOML file and separate proxy and control tokens.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/addomam/inference-gateway) |
| Maintainer | [addomam](https://github.com/addomam). Independently curated. |
| Format | Rust binary |
| Requirements | Rust toolchain and the provider keys you route to (TYPESAFE_API_KEY for Jev). |
| License | [CC0-1.0](https://github.com/addomam/inference-gateway/blob/41f05d49946908ad5fb800510713f7a95b8d95cd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/route.rs`](https://github.com/addomam/inference-gateway/blob/41f05d49946908ad5fb800510713f7a95b8d95cd/src/route.rs) at the pinned commit. |

## When to use

- Put all your apps' model calls, including Jev, behind one gateway you control and can observe.
- Mismatch: you operate it yourself; no hosted version.

## How it works

`src/route.rs` and `src/backend.rs` resolve System One requests to the configured provider; the example config sets `https://api.typesafe.ai` with `TYPESAFE_API_KEY`. Integration evidence: [`src/route.rs`](https://github.com/addomam/inference-gateway/blob/41f05d49946908ad5fb800510713f7a95b8d95cd/src/route.rs).

## Get started

From the upstream README (not run on the review host):

```sh
cargo build --release --locked
export INFER_PROXY_TOKEN="$(openssl rand -hex 32)" INFER_CONTROL_TOKEN="$(openssl rand -hex 32)"
./target/release/infer --config infer.toml serve
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with provider sections: [github.com/addomam/inference-gateway#readme](https://github.com/addomam/inference-gateway#readme)

## Limits and data handling

Requests pass through your gateway to the providers you configure.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 41f05d499469](https://github.com/addomam/inference-gateway/tree/41f05d49946908ad5fb800510713f7a95b8d95cd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
