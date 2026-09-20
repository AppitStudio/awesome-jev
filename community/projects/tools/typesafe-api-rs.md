# typesafe-api (Rust)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Ergonomic Rust client crate (`typesafe-api`) for TypeSafe System One: name-keyed questions, typed question/answer structs, and layered APIs that stay close to the HTTP wire format.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/noahbclarkson/typesafe-api-rs) |
| Maintainer | [noahbclarkson](https://github.com/noahbclarkson). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust workspace publishing crates.io **typesafe-api** **0.1.0** (MSRV **1.88**); dual MIT OR Apache-2.0. |
| Requirements | Rustc ≥ 1.88; live calls via `Client::from_env` / API key env as documented upstream. |
| License | [Apache-2.0](https://github.com/noahbclarkson/typesafe-api-rs/blob/d2c926fbccecdfcd1dfa9ee9475e0a5e35a513df/LICENSE-APACHE) (also MIT per workspace metadata). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and upstream CI inspected; local `cargo test` could not compile on rustc 1.85 (below MSRV). Live TypeSafe calls were not run. |

## When to use

Use it when a Rust service wants System One judgments with enums/structs as both request and answer types. Prefer the official Python/JS SDKs or other language clients when you are not on Rust 1.88+.

## How it works

The crate builds Noul/Choice/Score questions (including a `questions!` macro path) and evaluates them through an async `Client` against the TypeSafe System One API. Higher layers add stronger typing without hiding the wire shape—drop a level when you need raw control. Application code still owns thresholds, retries beyond the client’s policy, and downstream actions.

## Get started

```sh
cargo add typesafe-api
# or from the reviewed checkout (needs rustc ≥ 1.88):
git clone https://github.com/noahbclarkson/typesafe-api-rs.git
cd typesafe-api-rs
git checkout d2c926fbccecdfcd1dfa9ee9475e0a5e35a513df
cargo test
```

Live evaluation requires a TypeSafe key and incurs usage. See the upstream README for `Client::from_env` and typed triage examples.

## Examples and demos

- README quickstarts for name-keyed and typed evaluation.
- Workspace tests and trybuild macros under the crate tree (run with MSRV toolchain).

## Limits and data handling

Serialized state and questions leave the host on live calls. MSRV 1.88 is strict on the review host’s older rustc. Dual license means consumers pick MIT or Apache-2.0 terms per the repository files.

## Review and maintenance

Reviewed on **2026-09-20** at [commit d2c926f](https://github.com/noahbclarkson/typesafe-api-rs/tree/d2c926fbccecdfcd1dfa9ee9475e0a5e35a513df): Apache-2.0/MIT workspace. AI-assisted source review of README, Cargo workspace, and license files. Local rustc **1.85.1** rejected the build (MSRV 1.88); upstream GitHub Actions **CI** succeeded on related recent SHAs including this tip’s update workflow. No live TypeSafe calls.

Related: [TypeSafe.AI (.NET SDK)](typesafe-sdk-csharp.md), [TypeSafeAI.Net](typesafeai-net.md), [jear](jear.md).
