# pi-heed

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension that turns conversational user constraints into structured policy and checks side-effecting tool calls against that policy before they run, with TypeSafe Jev helping classify policy changes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nyarlathoteppppp/pi-heed) |
| Maintainer | [Nyarlathoteppppp](https://github.com/Nyarlathoteppppp). Independently curated; this page is not an upstream submission or endorsement. |
| Format | TypeScript Pi extension (`pi-heed` npm package / `pi` extensions entry). |
| Requirements | Node ≥ 22.18, peer `@earendil-works/pi-coding-agent` ≥ 0.85.1, `TYPESAFE_API_KEY` (or OpenRouter→Jev) for Jev-backed understanding. |
| License | [MIT](https://github.com/Nyarlathoteppppp/pi-heed/blob/b7b3c56093395a6a1af5157dc02ca6eda45afb5e/LICENSE). TypeSafe/OpenRouter usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline node:test run; live Jev smoke and billed sessions not run. |

## When to use

Use it when Pi should remember evolving “don’t modify / ask before push” style instructions across compaction. Prefer [pi-jev-permit](pi-jev-permit.md) / [pi-jev-sentinel](pi-jev-sentinel.md) for simpler per-call risk gates without conversational policy lifecycle. Complements [pi-jev](pi-jev.md) and [pi-jev-context](pi-jev-context.md) from the same author ecosystem.

## How it works

User messages update a structured constraint ledger (DENY/ALLOW/REQUIRE_* with scopes and exceptions). [`judge.ts`](https://github.com/Nyarlathoteppppp/pi-heed/blob/b7b3c56093395a6a1af5157dc02ca6eda45afb5e/src/judge.ts) calls TypeSafe System One (or OpenRouter Jev) for narrow classifications; code applies only confident answers and enforces tool calls against the ledger without sending free-form policy text from the model. Replayable offline benches live under `bench/`.

## Get started

```sh
git clone https://github.com/Nyarlathoteppppp/pi-heed.git
cd pi-heed
git checkout b7b3c56093395a6a1af5157dc02ca6eda45afb5e
npm ci
npm test
```

Install into Pi per upstream README (`pi` package extensions). Live enforcement needs a TypeSafe (or OpenRouter) key.

## Examples and demos

- Upstream README constraint table and benchmark method (`bench/README.md`).
- This listing ran `npm test`: **166 passed**. `scripts/smoke-jev.ts` not run (would bill).

## Limits and data handling

User messages and tool-call summaries may reach TypeSafe/OpenRouter when Jev understanding is enabled. Policy state is local to the Pi session. Upstream benchmark tables are reported, not re-run here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit b7b3c56](https://github.com/Nyarlathoteppppp/pi-heed/tree/b7b3c56093395a6a1af5157dc02ca6eda45afb5e): MIT; AI-assisted source review of README, LICENSE, `judge.ts`/`understand.ts`, tests; node:test **166 pass**. No live TypeSafe call.

Related: [pi-jev](pi-jev.md), [pi-jev-permit](pi-jev-permit.md), [pi-jev-sentinel](pi-jev-sentinel.md), [pi-jev-context](pi-jev-context.md).
