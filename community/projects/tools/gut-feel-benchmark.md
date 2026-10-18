# Gut Feel Benchmark

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark of snap probabilities at deadlines from a quarter second to 16 seconds: 703 boolean items in four packs (poker equity, base-rate puzzles, heart disease, Hacker News outcomes), sent to Jev, other decision models and chat models through AI SDK's `experimental_decide`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pragmaticfrontier/gut-feel-benchmark) |
| Maintainer | [pragmaticfrontier](https://github.com/pragmaticfrontier). Independently curated. |
| Format | TypeScript benchmark (Node) with packs, results and report generator |
| Requirements | Node.js; a Vercel AI Gateway key for the contestants; no key for the offline tests. |
| License | [MIT](https://github.com/pragmaticfrontier/gut-feel-benchmark/blob/53a2d56bb9344330963fb6ede87727651acf0691/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/contestants.ts`](https://github.com/pragmaticfrontier/gut-feel-benchmark/blob/53a2d56bb9344330963fb6ede87727651acf0691/src/contestants.ts) at the pinned commit. |

## When to use

- Compare how good and how fast decision models and chat models are at expert-style quick judgments on one scale.
- Add your own model, or a person, as a contestant on the same items.
- Mismatch: boolean questions only, so choice and score answers are not tested.

## How it works

Every item is one `experimental_decide` request with a boolean question; native decision models answer directly and chat models go through `llm-decision-model.ts`, which asks for P(true) as structured output. Scores compare the forecast with exact probabilities (poker, Bayes) or real outcomes against each pack's base rate, at each deadline. Integration evidence: [`src/contestants.ts`](https://github.com/pragmaticfrontier/gut-feel-benchmark/blob/53a2d56bb9344330963fb6ede87727651acf0691/src/contestants.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm test                        # offline suite, no key
npm run bench -- --limit 25     # 25 items per pack, every default contestant
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results and predictions in `results/2026-10-17/`.

## Limits and data handling

Item text goes to every contestant's provider through AI Gateway on your key.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 53a2d56bb934](https://github.com/pragmaticfrontier/gut-feel-benchmark/tree/53a2d56bb9344330963fb6ede87727651acf0691). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
