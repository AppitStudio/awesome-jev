# llmClassificR (R toolkit for LLM text classification with native TypeSafe Jev calls)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

R package for text classification with LLM APIs and local models that calls TypeSafe Jev System One directly from pure R, plus calibration tools and a DIY Jev-like classifier.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hfgolino/llmClassificR) |
| Maintainer | [hfgolino](https://github.com/hfgolino). Independently curated. |
| Format | R package (GPL (>= 3) declared in DESCRIPTION; no LICENSE file) |
| Requirements | R, `devtools::install_github("hfgolino/llmClassificR")`, and a `TYPESAFE_API_KEY`. |
| License | [GPL (>= 3) (declared in DESCRIPTION)](https://github.com/hfgolino/llmClassificR/blob/2b44ce3f856b4ced5ace3bc5b8974c2afdd862a6/DESCRIPTION) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`R/jev.R`](https://github.com/hfgolino/llmClassificR/blob/2b44ce3f856b4ced5ace3bc5b8974c2afdd862a6/R/jev.R) at the pinned commit. |

## When to use

- Classify survey or social text with Jev from R.
- Compare Jev with Groq LLMs and embedding baselines.
- Mismatch: license is only declared in DESCRIPTION.

## How it works

`R/jev.R` posts to `https://api.typesafe.ai/v1/systemone` one text per request; `set_typesafe_key()` stores the key and `verify_setup(test_apis = TRUE)` checks access. Integration evidence: [`R/jev.R`](https://github.com/hfgolino/llmClassificR/blob/2b44ce3f856b4ced5ace3bc5b8974c2afdd862a6/R/jev.R).

## Get started

Install from GitHub, call `set_typesafe_key()`, then use the Jev classification functions documented in the package.

```sh
R -e 'devtools::install_github("hfgolino/llmClassificR")'
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/hfgolino/llmClassificR/blob/2b44ce3f856b4ced5ace3bc5b8974c2afdd862a6/README.md](https://github.com/hfgolino/llmClassificR/blob/2b44ce3f856b4ced5ace3bc5b8974c2afdd862a6/README.md)

## Limits and data handling

Texts you classify are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 2b44ce3f856b](https://github.com/hfgolino/llmClassificR/tree/2b44ce3f856b4ced5ace3bc5b8974c2afdd862a6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
