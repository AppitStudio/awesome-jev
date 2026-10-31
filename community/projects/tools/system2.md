# system2 (idiomatic Rust SDK for Jev with typed questions and derive macros)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust SDK for TypeSafe's System One API: declare yes/no, choice and score questions with macros and a `Levels` derive on your own enums, ask them against a state in one call, and get typed answers with helpers such as `is_likely()` and `most_likely()`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jhartquist/system2) |
| Maintainer | [jhartquist](https://github.com/jhartquist). Independently curated. |
| Format | Rust crate (async, tokio) |
| Requirements | Rust toolchain; `TYPESAFE_API_KEY` (optional `TYPESAFE_DEFAULT_MODEL`). |
| License | [MIT OR Apache-2.0](https://github.com/jhartquist/system2/blob/c28e128d2362df7c2797ebdeb40cb96457c0d6bb/LICENSE-APACHE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`system2/src/client.rs`](https://github.com/jhartquist/system2/blob/c28e128d2362df7c2797ebdeb40cb96457c0d6bb/system2/src/client.rs) at the pinned commit. |

## When to use

- Call Jev from Rust services with compile-time typed questions and answers.
- Mismatch: early 0.1.0 crate; check the roadmap for unsupported API features.

## How it works

`system2/src/client.rs` posts to `https://api.typesafe.ai` with `jev-latest` by default (overridable by env), compresses request bodies with zstd and maps API errors (for example unknown models) to typed errors. Integration evidence: [`system2/src/client.rs`](https://github.com/jhartquist/system2/blob/c28e128d2362df7c2797ebdeb40cb96457c0d6bb/system2/src/client.rs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jhartquist/system2.git && cd system2
cargo build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README example (ticket triage): [github.com/jhartquist/system2#readme](https://github.com/jhartquist/system2#readme)

## Limits and data handling

States and questions are sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit c28e128d2362](https://github.com/jhartquist/system2/tree/c28e128d2362df7c2797ebdeb40cb96457c0d6bb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
