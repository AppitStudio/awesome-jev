# WaterSheep

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

An open, Apache-2.0 decision model with a local server that accepts Jev's `/v1/systemone` requests, for people who want Jev-style typed answers without sending text to a hosted API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SamratDuttaOfficial/WaterSheep) |
| Maintainer | [Samrat Dutta](https://github.com/SamratDuttaOfficial), who also submitted this listing. |
| Format | Python package and CLI with a local HTTP server; weights on [Hugging Face](https://huggingface.co/samratduttaofficial/WaterSheep); ONNX export for the browser demo. |
| Requirements | Python and PyTorch for the package. No account or API key; the local server accepts any key value. Weights download from Hugging Face on first run. |
| License | [`Apache-2.0`](https://github.com/SamratDuttaOfficial/WaterSheep/blob/3ccf02b3839fd2d72e6fb29750488010c7d76360/LICENSE) for code and weights. Dataset credits in [`NOTICE`](https://github.com/SamratDuttaOfficial/WaterSheep/blob/3ccf02b3839fd2d72e6fb29750488010c7d76360/NOTICE). |
| Jev evidence | [`watersheep/cli.py`](https://github.com/SamratDuttaOfficial/WaterSheep/blob/3ccf02b3839fd2d72e6fb29750488010c7d76360/watersheep/cli.py#L24-L32) serves `POST /v1/systemone` (and `/v1/decisions`) and passes the request to the model. |
| Disclosure | Submitted by the maintainer. Not affiliated with TypeSafe AI and not an official Jev release. A compatible request format does not mean Jev's accuracy or calibration. Listing is not an endorsement. |

## When to use

- Text you would rather not send to a hosted API, such as support tickets or internal documents: the model runs on your machine.
- Trying or testing code written for Jev without a key: point TypeSafe's Python SDK at the local server and run it unchanged.
- Questions where more than one answer applies: WaterSheep adds a multi-label type (`"type": "multi"`) next to `noul`, `choice` and `score`.

If you need Jev's own quality, use hosted Jev: thresholds tuned on Jev do not carry over to this model.

## How it works

WaterSheep is a fine-tune of ModernBERT-base that scores all options of a question together and returns a probability for every option. It was calibrated with one temperature per question type. The CLI's `--serve` mode starts a small HTTP server whose `do_POST` maps a Jev-format request (`state` plus named `questions`) to the model and answers in the same `answers` shape, so code reads the same fields it reads from Jev.

## Get started

From any directory, with Python installed:

```sh
pip install git+https://github.com/SamratDuttaOfficial/WaterSheep
watersheep --model samratduttaofficial/WaterSheep --serve
```

That serves `http://127.0.0.1:8766`. In the shell where your Jev code runs:

```sh
export TYPESAFE_BASE_URL=http://127.0.0.1:8766
```

Requests now go to the local model instead of TypeSafe; no charges and no text leaves the machine. The upstream README shows plain-JSON calls, including multi-label questions, which TypeSafe's SDK does not have.

## Examples and demos

- [Browser demo](https://samratduttaofficial.github.io/WaterSheep/): runs the ONNX model in the page, no install.
- [Hugging Face Space](https://huggingface.co/spaces/samratduttaofficial/WaterSheep) with the same demo.
- The README's "Using Jev?" section has an SDK example. For the ticket "I was charged twice for order #4411. Refund the duplicate today.", a three-question script printed `refund: 0.9451` and `team: billing` (0.8817).

## Limits and data handling

- English only. Long inputs are truncated.
- The README reports 77.8% accuracy on its own test split and 61.2% on datasets held out of training; rating (`score`) questions are its weakest type. Test it on your own text before relying on it.
- Everything runs locally once the weights are downloaded. TypeSafe's JavaScript SDK has not been tested against the server.
- It should not make medical, legal, financial or hiring decisions on its own.

## Review and maintenance

Reviewed **2026-10-03** at [commit 3ccf02b](https://github.com/SamratDuttaOfficial/WaterSheep/tree/3ccf02b3839fd2d72e6fb29750488010c7d76360) by the maintainer. Ran `python tests/selftest.py` (offline, toy data) and served the model locally, sending `/v1/systemone` requests in TypeSafe's format (`noul` and `choice` answered with probabilities). The accuracy figures above come from the upstream README, not from a separate review.

Related: [gutsy](gutsy.md) and [Decis](chaitin-decis.md) also serve Jev-compatible APIs locally.
