# Nirnay (CPU-only decision model compatible with the Jev / Laya /v1/systemone format)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent small decision model that classifies, rates and answers yes or no about text or JSON on CPU in one pass, with calibrated probabilities and a server that speaks the Jev / Laya `/v1/systemone` wire format; the README compares it with Laya checkpoints and with Jev's published figures.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nandukmelath/nirnay) |
| Maintainer | [nandukmelath](https://github.com/nandukmelath). Independently curated. |
| Format | Python package, HTTP server and Hugging Face model |
| Requirements | Python 3.10+; CPU only; no TypeSafe key (it does not call Jev). |
| License | [Apache-2.0](https://github.com/nandukmelath/nirnay/blob/9cb525c73f1b7a6cf8c54ad0b3609ad0a336a322/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`nirnay/server.py`](https://github.com/nandukmelath/nirnay/blob/9cb525c73f1b7a6cf8c54ad0b3609ad0a336a322/nirnay/server.py) at the pinned commit. |

## When to use

- Run Jev-style questions locally on CPU for tests or offline use.
- Swap a local endpoint into code written for `/v1/systemone`.
- Mismatch: not Jev and does not call TypeSafe; Jev comparisons use published third-party figures.

## How it works

`nirnay/server.py` serves `POST /v1/systemone` (and `/batch`) with the same state and questions format that Jev and Laya use, answering from the local model. Integration evidence: [`nirnay/server.py`](https://github.com/nandukmelath/nirnay/blob/9cb525c73f1b7a6cf8c54ad0b3609ad0a336a322/nirnay/server.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install -e .
python -m nirnay.server --port 8000   # POST /v1/systemone
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Model: [huggingface.co/nandukmelath/nirnay](https://huggingface.co/nandukmelath/nirnay)
- README: [github.com/nandukmelath/nirnay#readme](https://github.com/nandukmelath/nirnay#readme)

## Limits and data handling

Runs locally; nothing is sent to TypeSafe. Benchmark figures are the author's. Independent; not affiliated with TypeSafe or Liquid AI.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 9cb525c73f1b](https://github.com/nandukmelath/nirnay/tree/9cb525c73f1b7a6cf8c54ad0b3609ad0a336a322). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
