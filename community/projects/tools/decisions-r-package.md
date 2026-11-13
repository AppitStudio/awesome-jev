# decisions (R package on CRAN that sends texts and images to Jev and other decision models and returns tidymodels-style tibbles)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

R package that asks a decision model a typed question (true/false, a choice or an ordered score) about each text or image and returns one row per input with a predicted class and a probability per answer, ready for yardstick and probably; it supports TypeSafe's Jev, OpenAI, OpenRouter, Microsoft Foundry and local System One servers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fmegahed/decisions) |
| Maintainer | [fmegahed](https://github.com/fmegahed). Independently curated. |
| Format | R package on CRAN (MIT); free hosted demo on Hugging Face Spaces |
| Requirements | R with `TYPESAFE_API_KEY` (or the key of another supported provider); none for a local System One server. |
| License | [MIT](https://github.com/fmegahed/decisions/blob/e614b6743b0659f9e2a2138f5ed549cb6e968c9f/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`R/deciders.R`](https://github.com/fmegahed/decisions/blob/e614b6743b0659f9e2a2138f5ed549cb6e968c9f/R/deciders.R) at the pinned commit. |

## When to use

- Label or screen a column of texts or a folder of images with calibrated probabilities from R.
- Compare Jev with OpenAI, OpenRouter or a local open model on the same setup.
- Mismatch: production serving outside R.

## How it works

`R/deciders.R` defines `decider_typesafe()`, which posts to `https://api.typesafe.ai/v1/systemone`; `decide()` sends inputs in chunks, keeps failed calls as rows with `NA` answers and the reason in `.error`, and the package can save, score and calibrate a complete decision setup. The maintainers also run a free Shiny demo Space (repository fmegahed/decisions-space) that pays for calls within daily caps. Integration evidence: [`R/deciders.R`](https://github.com/fmegahed/decisions/blob/e614b6743b0659f9e2a2138f5ed549cb6e968c9f/R/deciders.R).

## Get started

Install from CRAN, put your key in `.Renviron`, then create a TypeSafe decider and call `decide()` on your inputs.

```sh
install.packages("decisions")
# .Renviron: TYPESAFE_API_KEY=your-key
library(decisions)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/fmegahed/decisions/blob/e614b6743b0659f9e2a2138f5ed549cb6e968c9f/README.md](https://github.com/fmegahed/decisions/blob/e614b6743b0659f9e2a2138f5ed549cb6e968c9f/README.md)
- CRAN page: [CRAN.R-project.org/package=decisions](https://CRAN.R-project.org/package=decisions)
- Documentation site: [fmegahed.github.io/decisions/](https://fmegahed.github.io/decisions/)
- Free demo Space (no key needed): [huggingface.co/spaces/fmegahed/decisions](https://huggingface.co/spaces/fmegahed/decisions)

## Limits and data handling

Texts and images go to the provider you choose on your key; the hosted demo sends uploads to TypeSafe on the maintainers' key and keeps only daily totals.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit e614b6743b06](https://github.com/fmegahed/decisions/tree/e614b6743b0659f9e2a2138f5ed549cb6e968c9f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
