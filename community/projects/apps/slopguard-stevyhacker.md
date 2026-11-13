# SlopGuard by stevyhacker (Chrome extension that folds AI-bot replies on X, with Jev among benchmarked decision-model presets)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that reads the replies under an X post, asks a decision model two yes/no questions per reply (written by an AI reply bot? assistant tone?) and folds the ones scoring at least 90% into a one-line bar, with per-account trust and a 14-day verdict cache. Jev 1.14 via OpenRouter is one of the presets; the default is Perplexity Decider, chosen from the author's benchmark.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/stevyhacker/SlopGuard) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/stevyhacker/SlopGuard#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; OpenRouter usage on your key (the default preset uses a free tier with paid fallback). Checked 2026-11-13. |
| Jev evidence | [`src/settings.js`](https://github.com/stevyhacker/SlopGuard/blob/32bdea3bf9e186efb67f56cba8a69409b836e639/src/settings.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [stevyhacker](https://github.com/stevyhacker). Independently curated. |
| Format | Chrome MV3 extension loaded unpacked (JavaScript, MIT) |
| Platform and availability | Desktop Chrome (load unpacked); no Chrome Web Store listing verified |
| Jev's role | Optional preset: Jev scores whether each reply is AI-bot slop; the default judge is Perplexity Decider. |
| Requirements | Desktop Chrome and an OpenRouter key (or a Gemini/OpenAI key for the LLM presets). |
| License | [MIT](https://github.com/stevyhacker/SlopGuard/blob/32bdea3bf9e186efb67f56cba8a69409b836e639/LICENSE) |

## When to use

- Hide low-effort AI-generated replies under X posts.
- Mismatch: if you need Jev as the default judge; it is an optional preset.

## How it works

`src/settings.js` defines the presets; the Jev preset sends batches of up to 10 replies to OpenRouter's Decisions API (`https://openrouter.ai/api/alpha/decisions`) with `typesafe/jev-1.14`. The author's bench (`bench/results/jev-1.14.json`) notes Jev ranks replies well but its probabilities stay under 90%, so the threshold should be lowered to about 60% when using it. Integration evidence: [`src/settings.js`](https://github.com/stevyhacker/SlopGuard/blob/32bdea3bf9e186efb67f56cba8a69409b836e639/src/settings.js).

## Get started

Clone, load the folder unpacked, paste an OpenRouter key in settings and choose the TypeSafe Jev 1.14 preset if you want Jev.

```sh
git clone https://github.com/stevyhacker/SlopGuard
# chrome://extensions → Developer mode → Load unpacked → SlopGuard
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/stevyhacker/SlopGuard/blob/32bdea3bf9e186efb67f56cba8a69409b836e639/README.md](https://github.com/stevyhacker/SlopGuard/blob/32bdea3bf9e186efb67f56cba8a69409b836e639/README.md)
- Benchmark results: [github.com/stevyhacker/SlopGuard/blob/32bdea3bf9e186efb67f56cba8a69409b836e639/bench/results/summary.json](https://github.com/stevyhacker/SlopGuard/blob/32bdea3bf9e186efb67f56cba8a69409b836e639/bench/results/summary.json)

## Limits and data handling

The post and its reply texts go to OpenRouter (and the chosen model provider) on your key.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 32bdea3bf9e1](https://github.com/stevyhacker/SlopGuard/tree/32bdea3bf9e186efb67f56cba8a69409b836e639). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
