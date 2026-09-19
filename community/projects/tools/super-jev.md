# super-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small TypeScript harness that turns evidence into typed Jev judgments, permitted actions, and verified outcomes, with local JSONL traces and zero runtime dependencies.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Kevthetech143/super-jev) |
| Maintainer | [Kevthetech143](https://github.com/Kevthetech143). Independently curated; this entry is not an upstream submission or endorsement. Upstream states it is an independent community project, not affiliated with TypeSafe AI. |
| Format | Experimental TypeScript harness **0.2.0** (Node runs `.ts` directly; no build step). Includes demos, JSONL journal replay, and optional skill-search CLI helpers. |
| Requirements | **Node.js ≥ 24**. Offline demos and tests use scripted fixtures. Live demos need `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/Kevthetech143/super-jev/blob/03db61fe757357261a84a938173a703c96c27dc7/LICENSE). |

## When to use

Use it when you want a domain-pluggable loop—observe → typed questions → decide → permit → tool → verify—with inspectable journals, without adopting a full agent framework. Prefer a thinner client or one-shot CLI when you only need a single Jev call.

## How it works

Domains implement hooks in [src/types.ts](https://github.com/Kevthetech143/super-jev/blob/03db61fe757357261a84a938173a703c96c27dc7/src/types.ts). The [Jev evaluator](https://github.com/Kevthetech143/super-jev/blob/03db61fe757357261a84a938173a703c96c27dc7/src/jev.ts) batches Choice/Score/Noul questions to TypeSafe. Application code selects actions, checks permissions and arguments, executes one registered tool with cancellation and idempotency keys, then verifies outcomes. Journals record the sequence for replay without re-running effects. Domains supply action candidates in code; Jev does not invent arbitrary commands.

## Get started

```sh
git clone https://github.com/Kevthetech143/super-jev.git
cd super-jev
git checkout 03db61fe757357261a84a938173a703c96c27dc7
# Requires Node.js 24+
npm run demo
npm test
```

Live demos: `npm run demo -- --live` (billable). Optional `.env` via `.env.example`—never commit filled secrets. This listing did not run live Jev.

## Examples and demos

- [examples/demo.ts](https://github.com/Kevthetech143/super-jev/blob/03db61fe757357261a84a938173a703c96c27dc7/examples/demo.ts) and [examples/domains.ts](https://github.com/Kevthetech143/super-jev/blob/03db61fe757357261a84a938173a703c96c27dc7/examples/domains.ts): recovery and document-review domains with fixture evaluators by default.
- [test/](https://github.com/Kevthetech143/super-jev/tree/03db61fe757357261a84a938173a703c96c27dc7/test): Node test runner coverage for harness and CLI paths.
- Upstream notes historical live smoke tests; those were not re-run here.

## Limits and data handling

On the live path, evidence/state projections and questions go to TypeSafe under your key. Fixture demos stay local. Permission and verifier logic are domain code—not model guarantees. Experimental V0.2 surface may change. Node engines declare ≥24; older Node versions can cancel or fail parts of the suite.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 03db61f](https://github.com/Kevthetech143/super-jev/tree/03db61fe757357261a84a938173a703c96c27dc7): **0.2.0**, MIT. AI-assisted source review of `src/jev.ts`, loop/types, demos, README, and license. On **Node.js 24.8.0**, **`npm test`: 579 passed**. On Node.js 22.19.0 the same suite reported 569 passed with 10 cancelled (engine mismatch). No live TypeSafe calls were performed.

Related: [Advocaat](advocaat.md).
