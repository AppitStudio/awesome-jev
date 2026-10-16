# typesafe_rs

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial async Rust client for Jev: send state and typed Choice, Score and Noul questions, attach image assets and try experimental Jev 1.14 Box questions, with typed responses and a configurable retry policy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ppweni/typesafe_rs) |
| Maintainer | [ppweni](https://github.com/ppweni). Independently curated. |
| Format | Rust library (Git dependency, tag `v0.2.0`) |
| Requirements | Rust with Tokio; a TypeSafe API key (`TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/ppweni/typesafe_rs/blob/248601991223b4bab13147deb6b2cd5f2ab086d7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/ppweni/status/2111043006291993064)). |
| Jev evidence | [`src/client.rs`](https://github.com/ppweni/typesafe_rs/blob/248601991223b4bab13147deb6b2cd5f2ab086d7/src/client.rs) at the pinned commit. |

## When to use

- Call Jev from a Rust service or CLI without hand-writing the `/v1/systemone` request and response types.
- Experiment with Jev 1.14 image input and Box answers from Rust.
- Mismatch: unofficial, early (0 stars at review); not on crates.io, so you pin the Git tag. Images and Box are experimental at TypeSafe.

## How it works

`Client::new()` reads `TYPESAFE_API_KEY` and targets `https://api.typesafe.ai`; `client.system_one(state)` builds a request with named questions, sends it with reqwest/Rustls, and returns typed answers (for example `response.noul("billing")`). The default retry policy retries connection errors, timeouts, 408 and 429 responses with backoff. Integration evidence: [`src/client.rs`](https://github.com/ppweni/typesafe_rs/blob/248601991223b4bab13147deb6b2cd5f2ab086d7/src/client.rs).

## Get started

From the upstream README (not run on the review host):

```sh
# Cargo.toml
# typesafe_rs = { git = "https://github.com/ppweni/typesafe_rs.git", tag = "v0.2.0" }
# tokio = { version = "1", features = ["macros", "rt-multi-thread"] }
export TYPESAFE_API_KEY=...
cargo run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Quick start, question types, images and retries are documented in the README.
- Example crate: `examples/type-paranoid`.

## Limits and data handling

State text and any image assets go to TypeSafe on your key; the library stores nothing.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 248601991223](https://github.com/ppweni/typesafe_rs/tree/248601991223b4bab13147deb6b2cd5f2ab086d7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
