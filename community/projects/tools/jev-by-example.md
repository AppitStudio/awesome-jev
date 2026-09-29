# Jev by Example

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Ten runnable JavaScript lessons on agent decisions between steps—memory conflicts, evidence gaps, tool-result completion, retries, context budget, handoffs, and question stress—where Jev supplies Choice/Score/Noul and application code owns policy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ReallyArtificial/jev-by-example) |
| Tags | Open source · Free source build · BYOK |
| Maintainer | [ReallyArtificial](https://github.com/ReallyArtificial) / [josharsh](https://github.com/josharsh). Author submission via issue [#298](https://github.com/AppitStudio/awesome-jev/issues/298). |
| Format | Source-only Node.js teaching kit (`jev-by-example` **0.1.0**): ten examples with fixtures, policies, and a zero-dependency CLI. |
| Requirements | Node.js ≥ 20.17. Default runs are offline fixtures. Live calls need `TYPESAFE_API_KEY` in a local `.env`. |
| License | [MIT](https://github.com/ReallyArtificial/jev-by-example/blob/088ae72890be5855a054b1d367589b3977c16c24/LICENSE). Provider usage may incur charges when live. |
| Disclosure | Author submission (issue #298). Catalog review is AI-assisted source inspection; no live TypeSafe spend on the review host. Listing is not an endorsement. Teaching material, not a benchmark. |

## When to use

Use when learning how to separate Jev judgments from application policy on familiar agent edges (memory updates, completion checks, handoff compression). Prefer [Ten Levels of Jev](ten-levels-of-jev.md) for a progressive lab that ends inside a pi agent, or production gate libraries when you need a shippable integration.

## How it works

Each example builds state, applies hard preflight rules in code, asks independent typed questions, then combines answers with explicit JavaScript policy into a proposed action and reason. Shared client/runner code targets `POST https://api.typesafe.ai/v1/systemone` (default model `jev-1.13.0`) with validation and bounded backoff. Fixture mode never hits the network. Integration evidence: [`src/client.mjs`](https://github.com/ReallyArtificial/jev-by-example/blob/088ae72890be5855a054b1d367589b3977c16c24/src/client.mjs), [`src/runner.mjs`](https://github.com/ReallyArtificial/jev-by-example/blob/088ae72890be5855a054b1d367589b3977c16c24/src/runner.mjs), and `examples/*/example.mjs` at the pinned commit.

## Get started

```sh
git clone https://github.com/ReallyArtificial/jev-by-example.git
cd jev-by-example
git checkout 088ae72890be5855a054b1d367589b3977c16c24
npm start -- list
npm start -- run 02
npm run demo
```

No install, account, or network is required for fixture mode. For a live opt-in (sends example state to TypeSafe and incurs charges): set `TYPESAFE_API_KEY` in `.env`, inspect with `npm start -- request 02`, then `npm start -- run 02 --live`. This listing did not run live calls.

## Examples and demos

- [memory reconciliation](https://github.com/ReallyArtificial/jev-by-example/tree/088ae72890be5855a054b1d367589b3977c16c24/examples/02-memory-reconciliation) — keep a scoped temporary exception instead of replacing a durable preference.
- [handoff readiness](https://github.com/ReallyArtificial/jev-by-example/tree/088ae72890be5855a054b1d367589b3977c16c24/examples/08-handoff-readiness) — detect lost prohibitions or invented certainty after compression.
- Upstream reports 34 authored cases and a passing `Verify examples` GitHub Actions workflow at the pinned tip; offline `npm test` / `npm run check` were not re-executed on the review host.

## Limits and data handling

The 34 fictional cases and illustrative thresholds are teaching material, not a validated operating policy. Model explanations are not generated—decision reasons come from application code. Live `--live` runs send case state to TypeSafe. No third-party telemetry or downstream action execution. Authenticated live Jev behavior was not measured for this catalog review.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) against [commit 088ae72](https://github.com/ReallyArtificial/jev-by-example/tree/088ae72890be5855a054b1d367589b3977c16c24) for issue [#298](https://github.com/AppitStudio/awesome-jev/issues/298): MIT LICENSE, package **0.1.0**, README, `examples/`, and client/runner inspected via GitHub API; upstream Actions `Verify examples` SUCCESS on that tip. No local `npm test` and no live TypeSafe calls on the review host.

Related: [Ten Levels of Jev](ten-levels-of-jev.md), [Jev Starter](yanflizi56-jev-starter.md).
