# jear

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust CLI/library that routes NEAR AI Cloud inference and IronClaw agent choices by budget, quality, and sensitivity using TypeSafe Jev structured decisions—users never pick a model manually.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/iJ03l/jear) |
| Maintainer | [iJ03l](https://github.com/iJ03l). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust crate/CLI **jear 0.1.0** (offline demo + `--live` HTTP helpers). |
| Requirements | Rust ≥ 1.70; live Jev needs `TYPESAFE_API_KEY` and `TYPESAFE_BASE_URL`; live NEAR needs `NEAR_API_KEY`. |
| License | Dual [MIT](https://github.com/iJ03l/jear/blob/e6323baec5fa238d2ba28a9dc0943c298934206b/LICENSE-MIT) OR [Apache-2.0](https://github.com/iJ03l/jear/blob/e6323baec5fa238d2ba28a9dc0943c298934206b/LICENSE-APACHE). |

## When to use

Use it to study budget-aware routing into NEAR AI Cloud tiers (TEE / anonymized / any) with offline fixtures first. Prefer [Jev Model Router](jev-model-router.md) / [jev-codex-router](jev-codex-router.md) for Claude Code or Codex turn routing rather than NEAR/IronClaw. Without both TypeSafe env vars, live mode keeps offline answers by design.

## How it works

[`src/jev.rs`](https://github.com/iJ03l/jear/blob/e6323baec5fa238d2ba28a9dc0943c298934206b/src/jev.rs) and [`src/jev_wire.rs`](https://github.com/iJ03l/jear/blob/e6323baec5fa238d2ba28a9dc0943c298934206b/src/jev_wire.rs) define Choice / Score / Noul types and System One JSON. [`src/route.rs`](https://github.com/iJ03l/jear/blob/e6323baec5fa238d2ba28a9dc0943c298934206b/src/route.rs) / [`src/policy.rs`](https://github.com/iJ03l/jear/blob/e6323baec5fa238d2ba28a9dc0943c298934206b/src/policy.rs) combine Jev answers with client-controlled monthly caps and NEAR catalog filters. Application code owns verification-before-display and TEE attestation fail-closed behavior in `--live`.

## Get started

```sh
git clone https://github.com/iJ03l/jear.git
cd jear
git checkout e6323baec5fa238d2ba28a9dc0943c298934206b
cargo test
cargo run -- "brief in plain English" --monthly-cents 5000
# live (optional):
# export NEAR_API_KEY=… TYPESAFE_API_KEY=… TYPESAFE_BASE_URL=https://…
# cargo run -- "brief in plain English" --monthly-cents 5000 --live
```

Offline `cargo test` / `cargo run` need no keys. Live flags send briefs to TypeSafe and/or NEAR and can incur charges. This listing did not run `cargo test` or live calls on the review host.

## Examples and demos

- README and `docs/NEWBIE.md` offline routing walkthrough.
- `tests/routing.rs` end-to-end offline Jev→route→catalog loop (upstream reports 60 passed).
- `docs/KEYS.md` key sources; `docs/SERVER.md` future proxy design (not built).

## Limits and data handling

Live routing sends task text to TypeSafe and completions to NEAR. Keys must not be logged (HTTP helper design). Upstream TEE/marketplace claims beyond the reviewed CLI path were not verified. Pin endpoints when comparing confidence gates.

## Review and maintenance

Reviewed on **2026-09-20** at [commit e6323bae](https://github.com/iJ03l/jear/tree/e6323baec5fa238d2ba28a9dc0943c298934206b): **0.1.0**, MIT OR Apache-2.0. AI-assisted source review of README, `jev.rs`, `jev_wire.rs`, `route.rs`, licenses, and test inventory. `cargo test` and live NEAR/TypeSafe calls were not executed on the review host.

Related: [Jev Model Router](jev-model-router.md), [jev-codex-router](jev-codex-router.md), [Distill](distill.md).
