# Jev Does Not Play Dice by Kanta Hayashi (probability-calibration experiments on Jev and three other decision APIs, with saved outputs)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code, saved outputs and analysis for 1,942 probability-output requests: fair dice and coin draws, Noul yes/no questions and forecast documents that state a probability. On a hidden fair die roll Jev's Choice output reported about 83% for its pick while being right 19% of the time; Noul was closer but still over-reported low probabilities. The same requests were repeated on Liquid, OpenAI and Gemini decision APIs for comparison. English and Japanese write-ups.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KantaHayashiAI/jev-does-not-play-dice) |
| Maintainer | [Kanta Hayashi](https://github.com/KantaHayashiAI) (KantaHayashiAI). Independently curated. |
| Format | Research write-up + Node.js runner and Python analysis |
| Requirements | Python 3.10+ to re-analyse saved results (no key); Node.js 22.16+ and a Vercel AI Gateway key (Jev) or Liquid, OpenAI or Gemini keys for live runs. |
| License | [MIT](https://github.com/KantaHayashiAI/jev-does-not-play-dice/blob/34bb6954e064df49fc07f681894421879b00880c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/runner.mjs`](https://github.com/KantaHayashiAI/jev-does-not-play-dice/blob/34bb6954e064df49fc07f681894421879b00880c/src/runner.mjs) at the pinned commit. |

## When to use

- Builders who plan to threshold on Jev's reported probabilities and want to see where they do and do not behave like probabilities.
- Mismatch: a general accuracy benchmark; the author says the results are specific to these prompts.

## How it works

`src/runner.mjs` sends each experiment request to Jev as `typesafe-ai/jev` through the Vercel AI Gateway by default and records the reported probability and confidence; adapters map the same requests to Liquid, OpenAI and Gemini decision APIs without rewording. `scripts/analyze.py` recomputes the tables from the saved runs. Integration evidence: [`src/runner.mjs`](https://github.com/KantaHayashiAI/jev-does-not-play-dice/blob/34bb6954e064df49fc07f681894421879b00880c/src/runner.mjs).

## Get started

Recompute every table from the saved results, without any key.

```sh
git clone https://github.com/KantaHayashiAI/jev-does-not-play-dice && cd jev-does-not-play-dice
python3 scripts/analyze.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Write-up (English): [kantahayashiai.github.io/posts/jev-does-not-play-dice/](https://kantahayashiai.github.io/posts/jev-does-not-play-dice/)
- Provider notes: [github.com/KantaHayashiAI/jev-does-not-play-dice/blob/main/docs/providers.md](https://github.com/KantaHayashiAI/jev-does-not-play-dice/blob/main/docs/providers.md)

## Limits and data handling

Results are specific to the prompts and dates in the repository, and none of the APIs reported a model revision. Live runs go through Vercel AI Gateway with your own gateway key (billed), not TypeSafe's API directly.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 34bb6954e064](https://github.com/KantaHayashiAI/jev-does-not-play-dice/tree/34bb6954e064df49fc07f681894421879b00880c). Inspected the README, LICENSE, `docs/providers.md` and `src/runner.mjs` at the pinned commit; nothing was run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
