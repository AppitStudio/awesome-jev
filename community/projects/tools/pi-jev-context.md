# pi-jev-context

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Trim long tool outputs for the [pi](https://pi.dev) coding agent **before** they enter context, so prompt-cache prefixes stay intact: comparison-based collapses for already-seen reads, then TypeSafe Jev only where comparison cannot decide, with lossless `context_recall`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nyarlathoteppppp/pi-jev-context) |
| Maintainer | [Nyarlathoteppppp](https://github.com/Nyarlathoteppppp). Independently curated; this page is not an upstream submission or endorsement. |
| Format | TypeScript Pi extension (`pi-jev-context`); npm package with `node --test` suite. |
| Requirements | Pi coding agent (`@earendil-works/pi-coding-agent`); Node.js with TypeScript. Live Jev judgments need `TYPESAFE_API_KEY` or OpenRouter; without a key, outputs pass through unchanged. Offline tests need no account. |
| License | [MIT](https://github.com/Nyarlathoteppppp/pi-jev-context/blob/ecc46944a24e8cc4389b7c3920db17ca80a7676a/LICENSE). TypeSafe/OpenRouter usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline tests inspected; live Pi sessions and live Jev calls not run. |

## When to use

Use it when pi tool results dominate context and rewriting older messages would bust the provider cache. Prefer local truncation alone when you do not want any model judgment. Distinct from [fast-jev-compaction](fast-jev-compaction.md) / [jev-pruner](jev-pruner.md) (post-hoc history edits) and from [pi-jev](pi-jev.md) (gate/judge/`jev_ask`).

## How it works

[`src/jev.ts`](https://github.com/Nyarlathoteppppp/pi-jev-context/blob/ecc46944a24e8cc4389b7c3920db17ca80a7676a/src/jev.ts) posts to `https://api.typesafe.ai/v1/systemone` (or OpenRouter `~typesafe/jev-latest`) only in layer-2 sieve paths. Layer 1 collapses already-shown file reads by comparison with no model. Kept lines stay verbatim; omitted spans are recoverable via `context_recall`. Fail-open: missing key, error, timeout, low confidence, or little to gain leaves the output untouched. The `context` hook returns nothing so earlier messages stay byte-identical.

## Get started

```sh
# Install into pi per upstream README (pi install / extension path).
export TYPESAFE_API_KEY=...   # optional; without it, trimming that needs Jev is skipped
```

Pinned review checkout:

```sh
git clone https://github.com/Nyarlathoteppppp/pi-jev-context.git
cd pi-jev-context
git checkout ecc46944a24e8cc4389b7c3920db17ca80a7676a
npm ci --ignore-scripts
npm test
```

## Examples and demos

- Upstream README excerpt of a failing test log shortened with verbatim kept lines.
- [`results/`](https://github.com/Nyarlathoteppppp/pi-jev-context/tree/ecc46944a24e8cc4389b7c3920db17ca80a7676a/results) and [`docs/experiments/`](https://github.com/Nyarlathoteppppp/pi-jev-context/tree/ecc46944a24e8cc4389b7c3920db17ca80a7676a/docs/experiments): measured write-time trimming notes (upstream evidence, not re-run live here).
- This listing ran `npm test`: **46 passed / 0 failed**. Live Pi + billable Jev not run.

## Limits and data handling

When Jev is used, selected tool-output excerpts and question state go to TypeSafe or OpenRouter. Prefer no-key pass-through for sensitive logs. Do not treat README token-savings anecdotes as catalog guarantees.

## Review and maintenance

Reviewed on **2026-09-21** at [commit ecc4694](https://github.com/Nyarlathoteppppp/pi-jev-context/tree/ecc46944a24e8cc4389b7c3920db17ca80a7676a): MIT; AI-assisted source review of README, LICENSE, `src/jev.ts`, `src/writetime.ts`, `src/seen.ts`, `src/sieve.ts`; `npm test` **46 pass**. No live TypeSafe call.

Related: [pi-jev](pi-jev.md), [pi-jev-sentinel](pi-jev-sentinel.md), [fast-jev-compaction](fast-jev-compaction.md), [jev-pruner](jev-pruner.md).
