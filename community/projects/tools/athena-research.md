# Athena Research (pre-registered experiments on AutoML decisions, including whether Jev can choose explanation methods and search depth)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Evidence repo for articles on LLM-assisted decisions in tabular machine learning: designs, pre-registrations, prompts, code, run records and statistics. The JEV study asks whether Jev can make bounded AutoML choices; richer semantic descriptions lifted one decision from 22.6% to 58.1% on the original benchmark, but on six unseen datasets nothing it added was significant after correction. Other studies compare chain, tree and graph prompting and semantic context with local and hosted LLMs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ercanholasoglu/athena-research) |
| Maintainer | [ercanholasoglu](https://github.com/ercanholasoglu). Independently curated. |
| Format | Research repository (Python harness, data manifests, results) |
| Requirements | Python; reproducing the LLM studies needs Ollama and hosted model keys. The JEV study's harness is not public; its evidence files are. |
| License | [Apache-2.0 (code); CC BY 4.0 (text and results)](https://github.com/ercanholasoglu/athena-research/blob/96ea4e7dc860720d086d9c46c211a402f8e3385c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`research/jev/README.md`](https://github.com/ercanholasoglu/athena-research/blob/96ea4e7dc860720d086d9c46c211a402f8e3385c/research/jev/README.md) at the pinned commit. |

## When to use

- Read pre-registered, negative-result-friendly evidence before using Jev for AutoML configuration choices.
- Mismatch: the JEV study is retrospective and its harness is not in the repo.

## How it works

`research/jev/README.md` records the model (`jev-1.13.0` via `jev-latest`), access through TypeSafe `POST /v1/systemone` on the author's own credential, and links the per-case evidence files. Integration evidence: [`research/jev/README.md`](https://github.com/ercanholasoglu/athena-research/blob/96ea4e7dc860720d086d9c46c211a402f8e3385c/research/jev/README.md).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ercanholasoglu/athena-research && cd athena-research
# see docs/REPRODUCIBILITY.md for each study
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- JEV study: [github.com/ercanholasoglu/athena-research/tree/main/research/jev](https://github.com/ercanholasoglu/athena-research/tree/main/research/jev)

## Limits and data handling

Code is Apache-2.0; text, tables and figures are CC BY 4.0. Datasets are not redistributed.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 96ea4e7dc860](https://github.com/ercanholasoglu/athena-research/tree/96ea4e7dc860720d086d9c46c211a402f8e3385c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
