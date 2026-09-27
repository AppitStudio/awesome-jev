# polyjev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Typed, calibrated decisions from any LLM with a drop-in Jev-compatible API server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PraveenAShukla/polyjev) |
| Maintainer | [PraveenAShukla](https://github.com/PraveenAShukla). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python library/CLI with optional System One–compatible serve. |
| Requirements | Python 3.10+; provider or local model credentials per backend. |
| License | [Apache-2.0](https://github.com/PraveenAShukla/polyjev/blob/76c3bdab49d6751e769ca8e1680248006f83e6ea/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Independent of hosted Jev weights. |

## When to use

Use when you want Jev-shaped typed decisions from your own LLMs. Prefer hosted TypeSafe Jev when you need the official model.

## How it works

Reads option probabilities from any supported LLM backend with calibration helpers; `polyjev serve` speaks POST `/v1/systemone` so Jev clients can target your models. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/PraveenAShukla/polyjev.git
cd polyjev
git checkout 76c3bdab49d6751e769ca8e1680248006f83e6ea
# or: pip install polyjev
# follow upstream README for decide/serve
```

Pin revision `76c3bdab49d6751e769ca8e1680248006f83e6ea` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Independent of hosted Jev; quality depends on the chosen backend. Live provider paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 76c3bda](https://github.com/PraveenAShukla/polyjev/tree/76c3bdab49d6751e769ca8e1680248006f83e6ea). AI-assisted README and LICENSE inspection; install/live paths not executed.
