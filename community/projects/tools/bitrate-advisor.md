# bitrate-advisor

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Library/CLI that asks TypeSafe Jev (via OpenRouter decisions) for live-stream encoder rungs and steps from telemetry plus session history, then clamps answers inside a deterministic safety envelope.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/affirmitv/bitrate-advisor) |
| Maintainer | [affirmitv](https://github.com/affirmitv). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript module **@affirmi/bitrate-advisor 0.2.7** (Deno / Node 20+ / edge; no runtime deps). |
| Requirements | Deno or Node ≥ 20; live advice needs an OpenRouter API key (default model `typesafe/jev-1.13`). |
| License | [MIT](https://github.com/affirmitv/bitrate-advisor/blob/4974664feb8611c04245a6a4e340fd7617b23da9/LICENSE). |

## When to use

Use it when an encoder must pick start bitrate, ceiling, resolution, or next up/down/hold from uplink/thermal/history signals with inspectable clamps. Prefer fixed ABR ladders when you do not want a network decision model in the loop. Upstream cost/latency tables were not remeasured here.

## How it works

[`src/advisor.ts`](https://github.com/affirmitv/bitrate-advisor/blob/4974664feb8611c04245a6a4e340fd7617b23da9/src/advisor.ts) builds Choice questions over structured state, calls `askJev` against OpenRouter’s decisions API, then `applyGuardrails` may only match or further constrain Jev—never loosen the policy envelope. Timeouts fall back to policy so a stalled provider cannot block go-live.

## Get started

```sh
git clone https://github.com/affirmitv/bitrate-advisor.git
cd bitrate-advisor
git checkout 4974664feb8611c04245a6a4e340fd7617b23da9
# Deno: import advise from ./mod.ts with OPENROUTER_API_KEY
```

Live advice sends telemetry-derived state to OpenRouter/Jev and can incur charges. This listing did not run live calls.

## Examples and demos

- README start/tick `advise` snippets and measured-cost table (vendor-reported).
- Offline Deno tests in `test/` with mocked fetch.

## Limits and data handling

Telemetry fields in the decision state leave the host for OpenRouter. Guardrail text explains clamps; do not treat probabilities as guaranteed stall-free streaming. Pin model/version when calibrating ladders.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 4974664f](https://github.com/affirmitv/bitrate-advisor/tree/4974664feb8611c04245a6a4e340fd7617b23da9): **0.2.7**, MIT. AI-assisted source review of README, `advisor.ts`, tests inventory, and license. Deno test suite and live OpenRouter calls were not executed on the review host.

Related: [SemDecide](semdecide.md), [Distill](distill.md).
