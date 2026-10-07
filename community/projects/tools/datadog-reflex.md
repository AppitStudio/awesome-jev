# Reflex (Datadog Labs)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Datadog Labs' Rust library for control loops on observability data: Datadog metrics and Toto forecasts become typed state, a judge such as TypeSafe Jev recommends an action (open, probe or leave a circuit), and Reflex's state machine applies it only if guards and invariants pass; includes a circuit-breaker simulator and a `reflex-typesafe` judge crate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/datadog-labs/reflex) |
| Maintainer | [Datadog Labs](https://github.com/datadog-labs) (README: owned by Datadog, Inc.). Independently curated. |
| Format | Rust workspace: core `reflex` crate, `reflex-typesafe` judge, simulator (`reflex-sim`) with web UI and Datadog dashboards |
| Requirements | Rust 1.92+ (Node.js for the simulator UI); `TYPESAFE_API_KEY` for live Jev recommendations; optional `DD_API_KEY`/`DD_APP_KEY`/`DD_SITE` for Datadog and a local Toto service for forecasts. |
| License | [Apache-2.0](https://github.com/datadog-labs/reflex/blob/7db760fa21f23d48bac086fcb81f20b0b309c36e/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Put a model's judgment in an operational control loop without letting it bypass cooldowns, probe limits or capacity bounds.
- Attach the Datadog evidence, observation time and revision to every recommended transition for audit.
- Mismatch: the simulator's services are simulated; running with Datadog needs your own Datadog account and keys.

## How it works

Your application builds typed state and calls a `Judge<S, A>`; [`crates/reflex-typesafe`](https://github.com/datadog-labs/reflex/tree/7db760fa21f23d48bac086fcb81f20b0b309c36e/crates/reflex-typesafe) implements it with Jev (see the [live example](https://github.com/datadog-labs/reflex/blob/7db760fa21f23d48bac086fcb81f20b0b309c36e/crates/reflex-typesafe/examples/jev.rs)). The controller enforces an inference deadline, and the executor commits a transition only if its guard passes and invariants hold. In the simulator, [`crates/reflex-sim/src/jev.rs`](https://github.com/datadog-labs/reflex/blob/7db760fa21f23d48bac086fcb81f20b0b309c36e/crates/reflex-sim/src/jev.rs) asks Jev every 10 s whether each service's circuit should Open, Probe or stay unchanged. SDK notes: [`TYPESAFE_SDK.md`](https://github.com/datadog-labs/reflex/blob/7db760fa21f23d48bac086fcb81f20b0b309c36e/TYPESAFE_SDK.md).

## Get started

Try the credential-free example, then the Jev simulator without Datadog:

```sh
git clone https://github.com/datadog-labs/reflex.git && cd reflex
cargo run -p reflex --example circuit_breaker    # deterministic judge, no keys
npm ci --prefix crates/reflex-sim/ui && npm run build --prefix crates/reflex-sim/ui
export TYPESAFE_API_KEY=...
cargo run -p reflex-sim --locked                 # see README for scenario flags
```

Live simulator runs call Jev every 10 s per service (billed to your TypeSafe key); Datadog usage is billed by Datadog. An OpenAI Decisions provider is also supported.

## Examples and demos

- README *A circuit breaker* walkthrough and simulator GIF (Cyclical load · Toto scenario).
- Datadog control loop and forecasting guides: [`crates/reflex-sim/DATADOG.md`](https://github.com/datadog-labs/reflex/blob/7db760fa21f23d48bac086fcb81f20b0b309c36e/crates/reflex-sim/DATADOG.md), [`FORECASTING.md`](https://github.com/datadog-labs/reflex/blob/7db760fa21f23d48bac086fcb81f20b0b309c36e/crates/reflex-sim/FORECASTING.md).

## Limits and data handling

Typed state and Datadog evidence are sent to TypeSafe (or OpenAI with `--provider openai`). Vendor-maintained project; AppitStudio has no affiliation with Datadog. Not built or run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 7db760fa21f2](https://github.com/datadog-labs/reflex/tree/7db760fa21f23d48bac086fcb81f20b0b309c36e). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
