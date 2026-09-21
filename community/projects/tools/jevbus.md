# jevbus

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust streaming event bus whose routing, subscription match, and delivery disposition are decided by a probabilistic judge—defaulting to TypeSafe Jev System One over HTTPS.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zkjoie/jevbus) |
| Maintainer | [zkjoie](https://github.com/zkjoie). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust crate **jevbus 0.1.0** (docs.rs); default feature `jev` enables HTTPS System One. |
| Requirements | Rust toolchain (crate `rust-version` **1.85**; some transitive deps may need newer rustc on the review host). Live judge needs `TYPESAFE_API_KEY`. |
| License | [MIT OR Apache-2.0](https://github.com/zkjoie/jevbus/blob/ca3021e0ec08a88376ee508ff0d4e6521ceb8ace/LICENSE-MIT). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source and examples inspected. Offline `cargo test` was **not** run on the review host (rustc 1.85 vs transitive crates requiring 1.88+). No live TypeSafe calls. |

## When to use

Use it when you want an **async event bus** where each subscription is a typed question set and dispositions (`Drop` / `Review` / `Deliver`) come from calibrated probabilities rather than keyword filters. Prefer lighter SDKs when you only need a one-shot System One call without streaming fan-out.

## How it works

Pure `routing` plans questions and decides verdicts from an answer set with no IO. [`HttpSystemOne`](https://github.com/zkjoie/jevbus/blob/ca3021e0ec08a88376ee508ff0d4e6521ceb8ace/src/jev/http.rs) implements the System One protocol against `https://api.typesafe.ai/v1/systemone`; `JevJudge` adapts it to the bus `Judge` trait. Thresholds are policy (not model weights). Ledgers and bounded channels provide backpressure and auditability.

## Get started

```sh
# In your Cargo.toml: jevbus = "0.1"
export TYPESAFE_API_KEY=...   # do not paste secrets into chat
```

See upstream [`examples/`](https://github.com/zkjoie/jevbus/tree/ca3021e0ec08a88376ee508ff0d4e6521ceb8ace/examples) (`stream.rs`, `merge.rs`) for wiring a bus to `JevJudge::from_env()`.

From the reviewed tip:

```sh
git clone https://github.com/zkjoie/jevbus.git
cd jevbus
git checkout ca3021e0ec08a88376ee508ff0d4e6521ceb8ace
# cargo test   # needs a rustc new enough for current lockfile deps
```

Live judging sends event payloads and subscription questions to TypeSafe and can incur charges.

## Examples and demos

- Upstream README architecture table and lifecycle docs.
- Offline-oriented tests under `tests/` (not executed on this host due to MSRV/transitive rustc).
- This listing: source inspection only; no live calls.

## Limits and data handling

Event payloads and subscription text leave the host on live judgments. Dual MIT/Apache-2.0 licensing—pick one when redistributing. Confirm TypeSafe billing separately. Unofficial community crate—not affiliated with TypeSafe.

## Review and maintenance

Reviewed on **2026-09-21** at [commit ca3021e](https://github.com/zkjoie/jevbus/tree/ca3021e0ec08a88376ee508ff0d4e6521ceb8ace): **0.1.0**, MIT OR Apache-2.0. AI-assisted source review of README, licenses, `src/jev/http.rs`, routing/judge traits, and examples. `cargo test` skipped (rustc 1.85). No live provider calls.

Related: [jevkit](jevkit.md), [typesafe-api-rs](typesafe-api-rs.md), [Formanator](formanator.md).
