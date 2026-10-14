# train-jev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open training recipe for JEV-style System 1 models on Qwen3.5 with LoRA decision head and System One-compatible serve.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shibing624/train-jev) |
| Maintainer | [shibing624](https://github.com/shibing624). Independently curated. |
| Format | Python training + serve stack |
| Requirements | Python 3.12+; GPU for training; optional System One serve. |
| License | [Apache-2.0](https://github.com/shibing624/train-jev/blob/6f902935f20976283eb67a5adcde206e35112e28/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |
| Jev evidence | [`trainjev/train.py`](https://github.com/shibing624/train-jev/blob/6f902935f20976283eb67a5adcde206e35112e28/trainjev/train.py) at the pinned commit. |

## When to use

- Use when you need: Open training recipe for JEV-style System 1 models on Qwen3.5 with LoRA decision head and …
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `trainjev/train.py`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: trainjev/train.py.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 6f902935f209](https://github.com/shibing624/train-jev/tree/6f902935f20976283eb67a5adcde206e35112e28). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
