# GoEventBus

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

High-performance Go event bus with deterministic rules, a decision cache, and an optional `JevSelector` that asks Jev (via OpenRouter's Decisions API) to choose an event type only on a cache miss.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Protocol-Lattice/GoEventBus) |
| Product homepage | [goeventbus.vercel.app](https://goeventbus.vercel.app) |
| Maintainer | [Protocol-Lattice](https://github.com/Protocol-Lattice). Independently curated. |
| Format | Go library with examples (`routing_cache`, `routing_jev`) |
| Requirements | Go toolchain. Jev routing uses `OPENROUTER_API_KEY` (model `typesafe/jev-1.13`) through the standard library, with no SDK dependency. |
| License | [MIT](https://github.com/Protocol-Lattice/GoEventBus/blob/b22f02bdee67f092be67dddf7cb77792b67e660c/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Pick an event handler for free-text or ambiguous inputs while keeping the fast path deterministic.
- Reuse cached decisions so repeated states never reach the model.
- Mismatch: if rules cover every input, leave the Jev selector out.

## How it works

Selection runs rules first, then the decision cache, then `JevSelector` with a bounded candidate set; the choice is cached and the event is dispatched by GoEventBus. If a rule matches or the state is cached, Jev is never called ([`jev.go` selector](https://github.com/Protocol-Lattice/GoEventBus/blob/b22f02bdee67f092be67dddf7cb77792b67e660c/jev.go)).

## Get started

Add the module and configure the selector (live OpenRouter/Jev calls on cache misses):

```sh
go get github.com/Protocol-Lattice/GoEventBus
export OPENROUTER_API_KEY=...
# jev := &GoEventBus.JevSelector{APIKey: os.Getenv("OPENROUTER_API_KEY")}
# selector with Rules, Cache, Fallback: jev
```

Jev fallback calls go through OpenRouter and may incur charges.

## Examples and demos

- [`examples/routing_jev`](https://github.com/Protocol-Lattice/GoEventBus/tree/b22f02bdee67f092be67dddf7cb77792b67e660c/examples/routing_jev) for the full rules → cache → Jev flow.

## Limits and data handling

Fallback decisions send event state to OpenRouter (Jev). Performance figures in the README are maintainer-reported.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit b22f02bdee67](https://github.com/Protocol-Lattice/GoEventBus/tree/b22f02bdee67f092be67dddf7cb77792b67e660c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
