# Noma

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Noma (Blackdrome AI Labs): open-weight MPL-2.0 System One decision model served by `pip install blackdrome-noma` / `noma serve` on the same `/v1/systemone` API as Jev, returning per-option probabilities plus abstain and uncertainty signals, with a paper on Zenodo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/blackdromeai-labs/noma) |
| Product homepage | [blackdrome.tech](https://blackdrome.tech/noma) |
| Maintainer | [blackdromeai-labs](https://github.com/blackdromeai-labs). Independently curated. |
| Format | Model + server + playground (PyPI `blackdrome-noma`, 1.0.0 at review) |
| Requirements | Python 3.10+; GPU recommended; no TypeSafe account. |
| License | [MPL-2.0](https://github.com/blackdromeai-labs/noma/blob/b097a8e1dc558c4ac9e7f2256f4543f91217f2f9/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run a Jev-shaped decision endpoint locally and route `abstain`/uncertain cases elsewhere.
- Read an architecture paper with ablations on sliced decoders and trained heads.
- Mismatch: English text only, states up to 4,096 tokens (upstream scope).

## How it works

`noma serve` downloads the weights once and starts `/v1/systemone` plus a browser playground; answers come from trained heads on a sliced decoder ([`noma/serve/app.py`](https://github.com/blackdromeai-labs/noma/blob/b097a8e1dc558c4ac9e7f2256f4543f91217f2f9/noma/serve/app.py)).

## Get started

Install and serve locally:

```sh
pip install blackdrome-noma
noma serve      # http://127.0.0.1:8000/v1/systemone and playground
```

No hosted calls; local compute only.

## Examples and demos

- [Paper](https://doi.org/10.5281/zenodo.23186353) and the vendor's comparison page (upstream claims).

## Limits and data handling

Latency and accuracy (e.g. ~16 ms on one GPU) are maintainer-reported; not reproduced. Independent of TypeSafe; not a validated substitute. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit b097a8e1dc55](https://github.com/blackdromeai-labs/noma/tree/b097a8e1dc558c4ac9e7f2256f4543f91217f2f9). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
