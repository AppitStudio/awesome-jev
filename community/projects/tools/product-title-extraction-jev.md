# Product title brand extraction study (Jev zero-shot against a rebuilt CRF and Claude Haiku on Amazon product titles)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Write-up and code comparing Jev, given no training examples, with a rebuilt CRF from More (2016) and Claude Haiku on pulling brand names from messy product titles. Jev picks the brand from every phrase of up to five words plus NONE in one Choice question. With all labeled titles, the CRF ties Jev overall; on titles where the brand is not the first word, the CRF falls to 55.8 F1 while Jev scores 79.9. Claude Haiku does about as well as Jev there, slightly better overall, at about twice Jev's price. The author documents where the rebuild differs from the paper.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Will-Alger/product-title-extraction-jev) |
| Maintainer | [Will-Alger](https://github.com/Will-Alger). Independently curated. |
| Format | Python research code (uv) with results and write-up |
| Requirements | Python with uv, a TypeSafe key (and an Anthropic key to rerun the Claude baseline), and the labeled title data built by the scripts. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`research/src/pte/jev.py`](https://github.com/Will-Alger/product-title-extraction-jev/blob/12cde0b7c2b1665feaf2f88d224d11e0e0729d93/research/src/pte/jev.py) at the pinned commit. |

## When to use

- See how a zero-shot Jev Choice compares with a trained sequence model on entity extraction.
- Mismatch: production brand extraction; it is a single-dataset study with automatic labels.

## How it works

`research/src/pte/jev.py` uses `AsyncTypeSafeClient` from the TypeSafe Python SDK with one Choice question per title (`jev-latest`, recorded as `jev-1.14.0` in `research/results/jev.json`) and caches answers locally. Integration evidence: [`research/src/pte/jev.py`](https://github.com/Will-Alger/product-title-extraction-jev/blob/12cde0b7c2b1665feaf2f88d224d11e0e0729d93/research/src/pte/jev.py).

## Get started

Install the research package, add keys and rerun the Jev scorer.

```sh
git clone https://github.com/Will-Alger/product-title-extraction-jev && cd product-title-extraction-jev/research
uv sync
export TYPESAFE_API_KEY=...
uv run python scripts/run_jev.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (write-up): [github.com/Will-Alger/product-title-extraction-jev/blob/12cde0b7c2b1665feaf2f88d224d11e0e0729d93/README.md](https://github.com/Will-Alger/product-title-extraction-jev/blob/12cde0b7c2b1665feaf2f88d224d11e0e0729d93/README.md)

## Limits and data handling

Titles go to TypeSafe (and Anthropic for the baseline) on your keys. Labels are automatic and the CRF is a rebuild, not a replication, as the author states. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 12cde0b7c2b1](https://github.com/Will-Alger/product-title-extraction-jev/tree/12cde0b7c2b1665feaf2f88d224d11e0e0729d93). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
