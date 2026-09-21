# NeuroLink

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeScript AI SDK unifying many text providers under one API, with a third inference type — `decide` / `tryDecide` — that returns calibrated boolean/choice/score judgments via TypeSafe Jev for routing, compaction, and tool selection.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/juspay/neurolink) |
| Maintainer | [Juspay Technologies](https://github.com/juspay) (`@juspay/neurolink`). Independently curated; this page is not an upstream submission or endorsement. |
| Format | TypeScript SDK/CLI npm package `@juspay/neurolink` (MIT). |
| Requirements | Node ≥ 22, pnpm ≥ 10 for from-source builds. `TYPESAFE_API_KEY` (or Vercel AI Gateway) enables `decide`; other providers need their own keys. |
| License | [MIT](https://github.com/juspay/neurolink/blob/8abce7b79ab825408277960472c453b687ab4ef4/LICENSE). Provider inference has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspection of decide/TypeSafe provider paths; full `test:decide` suite not run here (needs package build). No live TypeSafe spend. |

## When to use

Use it when an application already needs a multi-provider generate/stream SDK and also wants fail-open typed decisions for routing and gating. Prefer a thin client ([Advocaat](advocaat.md), [typesafe-cli](typesafe-cli.md), [jev-java](jev-java.md)) when you only need Jev without the broader NeuroLink surface.

## How it works

[`providers/typesafe.ts`](https://github.com/juspay/neurolink/blob/8abce7b79ab825408277960472c453b687ab4ef4/src/lib/providers/typesafe.ts) implements the TypeSafe/Jev decision provider. Public `neurolink.decide()` / `tryDecide()` return typed judgments; without a decision key, decide paths fail open as documented. Internal classifier/router and compaction flows may call `decide` when configured. Text generation remains separate `generate`/`stream` providers.

## Get started

```sh
# package consumers
npm install @juspay/neurolink
# export TYPESAFE_API_KEY=...
```

Pinned review checkout (from-source):

```sh
git clone https://github.com/juspay/neurolink.git
cd neurolink
git checkout 8abce7b79ab825408277960472c453b687ab4ef4
```

Follow upstream Decide Guide for live `tryDecide` examples (incurs TypeSafe charges).

## Examples and demos

- Upstream README “Decide: Calibrated Judgments” section and `docs/features/decide-inference-type.md`.
- Continuous suite `test/continuous-test-suite-decide.ts` (live tests skip without key; degradation tests intend to run offline after build).
- This listing: source review only — **did not** run `pnpm install`/`pnpm run test:decide` in this hour (heavy build). No live TypeSafe call.

## Limits and data handling

Decision state and questions reach TypeSafe (or gateway) when decide is configured. Generate/stream traffic goes to whichever text provider you select. Treat upstream latency/cost figures as vendor/docs claims unless you re-measure.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 8abce7b](https://github.com/juspay/neurolink/tree/8abce7b79ab825408277960472c453b687ab4ef4): MIT; AI-assisted source review of README, LICENSE, `src/lib/providers/typesafe.ts`, decide docs. Offline decide suite not executed. No live TypeSafe call.

Related: [Advocaat](advocaat.md), [jev-java](jev-java.md), [typesafe-cli](typesafe-cli.md), [JevRouter](jevrouter.md).
