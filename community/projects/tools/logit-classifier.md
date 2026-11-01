# Logit Classifier (local zero-shot classifier that accepts TypeSafe System One requests unchanged)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local zero-shot classifier for text and images: one state and a set of questions go in, a probability per option comes out, read from a general model's logits at a single token position with no generated text. Its HTTP service accepts the System One request format, so a Jev request body works unchanged; the README is explicit that its numbers do not match Jev's.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Blakeem/logit-classifier) |
| Maintainer | [Blakeem](https://github.com/Blakeem). Independently curated. |
| Format | Python package + HTTP service (`logit-classifier serve`) |
| Requirements | Python; a local GPU recommended; Hugging Face model weights. |
| License | [GPL-3.0](https://github.com/Blakeem/logit-classifier/blob/1a30a2f015472770f78d7fad473139d7c75bb251/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/logit_classifier/service.py`](https://github.com/Blakeem/logit-classifier/blob/1a30a2f015472770f78d7fad473139d7c75bb251/src/logit_classifier/service.py) at the pinned commit. |

## When to use

- Prototype Jev-shaped requests offline or on private data with a local model.
- Mismatch: an alternative to hosted Jev, not a client for it, and not calibrated like Jev.

## How it works

`src/logit_classifier/service.py` serves `POST /v1/systemone` and `src/logit_classifier/config.py` maps aliases such as `jev-latest` to the local model, so System One clients can point at it; `examples/http_client.py` shows a request. Integration evidence: [`src/logit_classifier/service.py`](https://github.com/Blakeem/logit-classifier/blob/1a30a2f015472770f78d7fad473139d7c75bb251/src/logit_classifier/service.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install "logit-classifier[hf,service]"
logit-classifier serve
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README section 'Differences From Jev': [github.com/Blakeem/logit-classifier#differences-from-jev](https://github.com/Blakeem/logit-classifier#differences-from-jev)

## Limits and data handling

Runs locally; no data leaves your machine. Not affiliated with TypeSafe; probabilities are the local model's, not Jev's. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 1a30a2f01547](https://github.com/Blakeem/logit-classifier/tree/1a30a2f015472770f78d7fad473139d7c75bb251). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
