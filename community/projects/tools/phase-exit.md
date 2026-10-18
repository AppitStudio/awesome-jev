# phase-exit

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust phase-completion engine with evidence-backed exit checks that call TypeSafe Jev (`jev-1.14.0` on `https://api.typesafe.ai/v1/systemone`), plus Agent Skills and native harness hooks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Know-Me-Tools/phase-exit) |
| Maintainer | [Know-Me-Tools](https://github.com/Know-Me-Tools). Independently curated. |
| Format | Rust crates + skills/hooks |
| Requirements | Rust toolchain; TYPESAFE_API_KEY; agent harness that can load the hooks. |
| License | [Apache-2.0](https://github.com/Know-Me-Tools/phase-exit/blob/b25a4e256353ec8d6114eec531a34ecc514b915f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/phase-exit-core/src/jev.rs`](https://github.com/Know-Me-Tools/phase-exit/blob/b25a4e256353ec8d6114eec531a34ecc514b915f/crates/phase-exit-core/src/jev.rs) at the pinned commit. |

## When to use

- Bound agent phase completion with typed Jev judgments and evidence.
- Want pinned `jev-1.14.0` responses checked in Rust.
- Mismatch: preview-complexity harness; integrate carefully.

## How it works

`jev.rs` POSTs to `https://api.typesafe.ai/v1/systemone` and asserts the response model is `jev-1.14.0` before accepting a phase-exit judgment. Integration evidence: [`crates/phase-exit-core/src/jev.rs`](https://github.com/Know-Me-Tools/phase-exit/blob/b25a4e256353ec8d6114eec531a34ecc514b915f/crates/phase-exit-core/src/jev.rs).

## Get started

Build the crates, set TYPESAFE_API_KEY, and hook phase-exit into your agent skills as documented.

```sh
git clone https://github.com/Know-Me-Tools/phase-exit && cd phase-exit
cargo build -p phase-exit-core
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README phase-exit overview
- crates/phase-exit-core/src/jev.rs

## Limits and data handling

Preview surface; live calls require TypeSafe. Complex hook setup.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit b25a4e256353](https://github.com/Know-Me-Tools/phase-exit/tree/b25a4e256353ec8d6114eec531a34ecc514b915f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
