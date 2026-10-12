# codeforces-tag-prediction

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Research benchmark for multi-label tagging of Codeforces problems comparing TypeSafe Jev against zero-shot LLMs, fine-tuned encoders, dense embeddings, and TF-IDF under one leak-free protocol.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/msobroza/codeforces-tag-prediction) |
| Maintainer | [msobroza](https://github.com/msobroza). Independently curated. |
| Format | Python/Jupyter · benchmark |
| Requirements | Python; TypeSafe key to reproduce Jev legs; frozen assets included for inspection. |
| License | [MIT](https://github.com/msobroza/codeforces-tag-prediction/blob/82df6e647e12dbf623047d2f74fb20363eb24aaf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Compare System One tagging quality on a public coding dataset.
- Mismatch: Offline research—not a production tagger service.

## How it works

Frozen Jev method assets and notebooks evaluate predictions under a shared protocol. Evidence: [`assets/methods/jev-statement-code-gepa-platt/model/jev.json`](https://github.com/msobroza/codeforces-tag-prediction/blob/82df6e647e12dbf623047d2f74fb20363eb24aaf/assets/methods/jev-statement-code-gepa-platt/model/jev.json).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/msobroza/codeforces-tag-prediction.git
# open notebooks / reproduce per README
```

## Limits and data handling

Provider-bound inputs may be billed by TypeSafe/OpenRouter when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 82df6e647e12](https://github.com/msobroza/codeforces-tag-prediction/tree/82df6e647e12dbf623047d2f74fb20363eb24aaf). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
