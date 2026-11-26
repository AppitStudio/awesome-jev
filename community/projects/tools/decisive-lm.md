# DecisiveLM by Mike Richardson (open, local System One decision model on Gemma 4 whose confidence is trained to show which answers to check)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open toolkit and two general "heads" that turn Gemma 4 E4B or 26B A4B into a System One decision model: typed Choice, Score and Noul answers with probabilities in one forward pass, served on a `POST /v1/systemone` endpoint. It is trained on the spread of human ratings rather than majority votes, so its confidence is meant to flag where a person should look; you can fine-tune your own head.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xkiwilabs/decisive-lm) |
| Maintainer | [Mike Richardson](https://github.com/xkiwilabs) (xkiwilabs). Independently curated. |
| Format | Python toolkit, model heads and HTTP server (version 0.1 preview) |
| Requirements | Python 3.13 with uv, the Gemma 4 weights from Hugging Face and a GPU for real-time use (the README's 75 ms E4B figure is on an NVIDIA RTX PRO 6000; the 26B A4B head needs about 72 GiB free). |
| License | [Apache-2.0](https://github.com/xkiwilabs/decisive-lm/blob/54c68449327072a01846c485ec26fc6b520d34e9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`decisivelm/serve.py`](https://github.com/xkiwilabs/decisive-lm/blob/54c68449327072a01846c485ec26fc6b520d34e9/decisivelm/serve.py) at the pinned commit. |

## When to use

- Self-hosted typed decisions where you care about which answers need human review, or research on calibrated System One heads you can fine-tune.
- Mismatch: a hosted drop-in for Jev; this is a 0.1 preview you run on your own GPU.

## How it works

`decisivelm/serve.py` exposes `POST /v1/systemone` with the Jev-style request shape, where `model` names a bundle; each bundle is LoRA weights, three query-token embeddings, a scorer and calibration temperatures on an unchanged Gemma 4 backbone. This is a separate model, not TypeSafe's Jev. Integration evidence: [`decisivelm/serve.py`](https://github.com/xkiwilabs/decisive-lm/blob/54c68449327072a01846c485ec26fc6b520d34e9/decisivelm/serve.py).

## Get started

Clone, sync the pinned environment and run the CPU test suite, then follow the installation and quickstart chapters to fetch Gemma 4 and send a first request.

```sh
git clone https://github.com/xkiwilabs/decisive-lm
cd decisive-lm
uv sync
uv run pytest   # CPU, about a minute
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- E4B model card: [github.com/xkiwilabs/decisive-lm/blob/54c68449327072a01846c485ec26fc6b520d34e9/docs/model-card.md](https://github.com/xkiwilabs/decisive-lm/blob/54c68449327072a01846c485ec26fc6b520d34e9/docs/model-card.md)
- Guide: [github.com/xkiwilabs/decisive-lm/tree/54c68449327072a01846c485ec26fc6b520d34e9/docs/guide](https://github.com/xkiwilabs/decisive-lm/tree/54c68449327072a01846c485ec26fc6b520d34e9/docs/guide)

## Limits and data handling

Not TypeSafe's Jev. Version 0.1 preview; the model cards list the checks each head misses against the same Gemma 4 prompted directly (for example, worse review readiness on one task for E4B, and multilingual intent accuracy 5 points below that baseline for 26B A4B). All results are the author's own. Code and heads are Apache-2.0; Gemma 4 and the training datasets keep their own terms (see NOTICE).

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 54c684493270](https://github.com/xkiwilabs/decisive-lm/tree/54c68449327072a01846c485ec26fc6b520d34e9). Inspected the README, LICENSE, model-card links and `decisivelm/serve.py` at the pinned commit; models were not downloaded or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
