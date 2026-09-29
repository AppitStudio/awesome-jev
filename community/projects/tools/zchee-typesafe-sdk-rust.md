# typesafe-sdk-rust (zchee)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial async Rust SDK for the TypeSafe AI System One API—typed questions via `#[derive(QuestionSet)]`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zchee/typesafe-sdk-rust) |
| Maintainer | [zchee](https://github.com/zchee). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust crate `typesafe-sdk-rust` (library name `typesafe_sdk`). |
| Requirements | Rust ≥1.98 (edition 2024); Tokio with time driver; `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/zchee/typesafe-sdk-rust/blob/deed292e69ddd085f0833924a4499966b81072b5/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when a Rust async app needs typed System One calls. Prefer official Python/JS SDKs when those languages fit.

## How it works

Async port of typesafe-sdk-python 0.7.1 for `POST /v1/systemone` and `GET /v1/models`, with optional hyper/macros/tracing/sonic features. Unofficial; deviations documented upstream. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/zchee/typesafe-sdk-rust.git
cd typesafe-sdk-rust
git checkout deed292e69ddd085f0833924a4499966b81072b5
# Cargo.toml: typesafe-sdk-rust = "0.2.0" — see crates.io / docs.rs
```

Pin revision `deed292e69ddd085f0833924a4499966b81072b5` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Unofficial SDK. Live TypeSafe calls not run on the review host. Name `typesafe-sdk` is taken on crates.io—use `typesafe-sdk-rust`.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit deed292](https://github.com/zchee/typesafe-sdk-rust/tree/deed292e69ddd085f0833924a4499966b81072b5). AI-assisted README and LICENSE inspection; install/live paths not executed.
