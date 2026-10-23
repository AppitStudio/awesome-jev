# Jev vs. LLM (Banking77)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Small, fair test of the "up to 200x faster" claim: 100 real Banking77 customer messages sorted into 77 categories by Jev, Claude Haiku 5.5 and Claude Fable 5.1, measuring accuracy, off-list answers, median and p90 latency, and cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/0xGondarxyz/jev-vs-llm) |
| Maintainer | [0xGondarxyz](https://github.com/0xGondarxyz). Independently curated. |
| Format | TypeScript benchmark script plus a Next.js side-by-side viewer |
| Requirements | Node.js 22+; a TypeSafe key and an OpenRouter key. |
| License | [MIT](https://github.com/0xGondarxyz/jev-vs-llm/blob/8f80717e347eb5c041c1ff3e551905c836573312/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/sorters.ts`](https://github.com/0xGondarxyz/jev-vs-llm/blob/8f80717e347eb5c041c1ff3e551905c836573312/lib/sorters.ts) at the pinned commit. |

## When to use

- Check Jev's speed and accuracy against a small and a frontier LLM on intent classification before choosing one.
- Reuse the seeded 100-message sample and the side-by-side viewer.
- Mismatch: 100 messages, run from one location; the LLMs go through OpenRouter, which adds a network hop.

## How it works

`sorters.ts` sends each message to Jev as a Choice question with the 77 category names and to the LLMs with the same list; answers are checked against the label, the first call per sorter is a warm-up, and Jev cost is computed from input tokens at list price. Integration evidence: [`lib/sorters.ts`](https://github.com/0xGondarxyz/jev-vs-llm/blob/8f80717e347eb5c041c1ff3e551905c836573312/lib/sorters.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
cp .env.example .env    # fill in both keys
npx tsx --env-file=.env scripts/bench.ts
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Runs are written to `results/run-<time>.json`.

## Limits and data handling

Public Banking77 messages go to TypeSafe and OpenRouter on your keys.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 8f80717e347e](https://github.com/0xGondarxyz/jev-vs-llm/tree/8f80717e347eb5c041c1ff3e551905c836573312). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.

<!-- knowledge:backlinks:start -->
## Knowledge guides

- [Replace hand-written routing rules with Jev: a migration test](../../knowledge-base/articles/jev-replace-routing-rules.md) — Independently suggested by JevList; not an endorsement by Mo Al Mamun (Mamun). Run a small, quick Banking77 comparison of Jev against LLMs before building a full migration study.
<!-- knowledge:backlinks:end -->
