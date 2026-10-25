# decision-model-audit (reproducible field test of Jev and other decision models against small LLMs)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible comparison of decision models (Jev, GLiNER2.5-Decide, Laya, Clef and thirteen more in part 2) against small LLMs with structured output on fresh September 2026 data: accuracy and calibration, label-wording sensitivity, long inputs, no-fitting-label behaviour and cost per 1,000 decisions, with all raw outputs committed and blog write-ups in English and German.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/oborchers/decision-model-audit) |
| Maintainer | [oborchers](https://github.com/oborchers). Independently curated. |
| Format | Python research code (uv) with committed raw results |
| Requirements | uv; an OpenRouter key for API runs (Jev through OpenRouter), plus Cloudflare, Perplexity or Fastino keys for some part 2 runs; analysis reruns offline from committed outputs. |
| License | [MIT](https://github.com/oborchers/decision-model-audit/blob/67f3ba8f4394b0941a873c52a519c677d802bf39/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/dma/runners/api.py`](https://github.com/oborchers/decision-model-audit/blob/67f3ba8f4394b0941a873c52a519c677d802bf39/src/dma/runners/api.py) at the pinned commit. |

## When to use

- Decide whether a decision model beats a small LLM for your classification task.
- Rerun the analysis from cached outputs without any API key.
- Mismatch: a September and October 2026 snapshot; numbers are the author's.

## How it works

`src/dma/runners/api.py` runs Jev as `typesafe/jev-1.13` through OpenRouter's decision route next to the other decision models and LLMs; every response is cached so reports regenerate offline. Integration evidence: [`src/dma/runners/api.py`](https://github.com/oborchers/decision-model-audit/blob/67f3ba8f4394b0941a873c52a519c677d802bf39/src/dma/runners/api.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync
uv run python -m dma.analysis.report   # offline, from committed raw outputs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Write-up: [www.drborchers.com/en/blog/jev-field-test/](https://www.drborchers.com/en/blog/jev-field-test/)
- Part 2: [www.drborchers.com/en/blog/do-you-need-a-decision-model/](https://www.drborchers.com/en/blog/do-you-need-a-decision-model/)

## Limits and data handling

New runs send evaluation items to OpenRouter and other providers. Independent research; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 67f3ba8f4394](https://github.com/oborchers/decision-model-audit/tree/67f3ba8f4394b0941a873c52a519c677d802bf39). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
