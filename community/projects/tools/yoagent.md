# yoagent

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust agent loop (7 LLM protocols, tools, MCP) with a `decision` feature: `DecisionModel::jev()` Noul/Choice/Score answers, an opt-in tool gate, and an input guard backed by TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yologdev/yoagent) |
| Product homepage | [yologdev.github.io](https://yologdev.github.io/yoagent/) |
| Maintainer | [yologdev](https://github.com/yologdev). Independently curated. |
| Format | Rust library crate (agent loop) with an optional decision-model module |
| Requirements | Rust toolchain and Tokio; the `decision` feature; `TYPESAFE_API_KEY` for Jev, or a logprob-capable local LLM as a fallback backend. |
| License | [MIT](https://github.com/yologdev/yoagent/blob/b72be7c6e3f8a53ff5e9f8db9590ece4d1a6cf39/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Add cheap typed checks (urgency, tool safety, injection) to a Rust agent without another generative call.
- Fail closed on destructive, unrequested tool calls with `ToolGate`.
- Mismatch: if you only need a raw Jev client, a dedicated SDK crate is smaller.

## How it works

The `decision/` module defines a `DecisionBackend` trait with a SystemOne (Jev) backend and a logprob backend for local LLMs, plus fallbacks and calibration. `with_decision_model` gives advisory skill/tool hints; `ToolGate` and `InputGuard` are opt-in and fail closed ([README](https://github.com/yologdev/yoagent/blob/b72be7c6e3f8a53ff5e9f8db9590ece4d1a6cf39/README.md)).

## Get started

Add the crate with the decision feature and set your key (live Jev calls):

```sh
# Cargo.toml
# yoagent = { version = "0.24", features = ["decision"] }
# tokio = { version = "1", features = ["full"] }
export TYPESAFE_API_KEY=...
# let jev = DecisionModel::jev();
# let urgent = jev.noul(message, "Does this convey urgency?").await?;
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README quick start and module map; hosted docs at [yologdev.github.io/yoagent](https://yologdev.github.io/yoagent/).

## Limits and data handling

Decision calls send the question state to TypeSafe and incur usage charges; the gate and guard reject when uncertain or unavailable (fail closed). The rest of the agent loop works without Jev.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit b72be7c6e3f8](https://github.com/yologdev/yoagent/tree/b72be7c6e3f8a53ff5e9f8db9590ece4d1a6cf39). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
