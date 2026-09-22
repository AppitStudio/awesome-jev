# s1 (s1-rs)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust derive layer for TypeSafe System One: turn enums/structs into Choice/Score/Noul question sets with compile-time-checked, confidence-gated answers. HTTP is delegated to optional `typesafe-rs` (distinct from [typesafe-api](typesafe-api-rs.md)).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AbdelStark/s1-rs) |
| Maintainer | [AbdelStark](https://github.com/AbdelStark) (Abdel Bakhta). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Cargo workspace crates **`s1` / `s1-derive` / `s1-test`** (workspace version **0.1.0**, MSRV **1.85**, edition 2024). Dual MIT OR Apache-2.0. |
| Requirements | Rust **1.85+**; optional feature `backend-typesafe-rs` for crates.io `typesafe-rs` 0.1 + `TYPESAFE_API_KEY` for live calls. Default tests use `s1-test::FakeClient` (no network). |
| License | [MIT](https://github.com/AbdelStark/s1-rs/blob/b9168979a9beaeb74878483ff2876958acb98b86/LICENSE) OR [Apache-2.0](https://github.com/AbdelStark/s1-rs/blob/b9168979a9beaeb74878483ff2876958acb98b86/LICENSE-APACHE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline `cargo test --workspace` inspected; live TypeSafe HTTP not run on the review host. |

## When to use

Use it when you want **Rust enums and structs** to become typed System One questions with derive macros and policy helpers, while keeping HTTP in `typesafe-rs`. Prefer [typesafe-api (Rust)](typesafe-api-rs.md) for a lower-level wire-oriented client without the derive DSL. Prefer [jevgo](jevgo.md) / [TypeSafe Go](typesafe-go.md) for Go clients.

## How it works

`#[derive(Choice)]`, `Score`, `Questions`, and related macros build question sets. `S1` asks a `DecisionBackend`; `s1-test::FakeClient` serves offline tests. With `backend-typesafe-rs`, [`typesafe_rs::Client`](https://github.com/AbdelStark/s1-rs/blob/b9168979a9beaeb74878483ff2876958acb98b86/crates/s1/src/typesafe_rs.rs) maps requests through `system_one_with`. This workspace does not reimplement the HTTP transport.

## Get started

```sh
git clone https://github.com/AbdelStark/s1-rs.git
cd s1-rs
git checkout b9168979a9beaeb74878483ff2876958acb98b86
cargo test --workspace
# Live (optional): enable backend-typesafe-rs and set TYPESAFE_API_KEY per upstream docs
```

Live backend use sends application state to TypeSafe and may incur charges. This listing did not call live APIs.

## Examples and demos

- Offline on the review host: `cargo test --workspace` → library suites **ask 4**, **decode 8**, **golden 5**, **policy 10**, **ui 1** passed, plus doc-tests (**2** s1 + **1** s1-test; some ignored). FakeClient path only.
- Upstream examples and SPEC/PRD describe the derive surface; crates are marked `publish = false` at the reviewed workspace tip (source-build).

## Limits and data handling

MSRV and edition 2024 requirements apply. Optional LLM/cascade backends described in SPEC were not exercised here. Confidence gates are application policy, not provider SLAs.

## Review and maintenance

Reviewed on **2026-09-22** at [commit b916897](https://github.com/AbdelStark/s1-rs/tree/b9168979a9beaeb74878483ff2876958acb98b86): **0.1.0**, MIT OR Apache-2.0. AI-assisted source review of README, licenses, `crates/s1`, derive/test crates. Offline `cargo test --workspace` green on rustc **1.85.1**. No live TypeSafe calls.

Related: [typesafe-api (Rust)](typesafe-api-rs.md), [jevgo](jevgo.md), [TypeSafe Go](typesafe-go.md), [jev4k](jev4k.md).
