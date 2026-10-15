# Decision Model Workbench

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first workbench and guides for bounded decisions: call hosted decision models (TypeSafe Jev, OpenRouter, Perplexity, Cloudflare) with typed validation and fallbacks, or review data and train a CPU baseline domain model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BatuhanYilmaz26/decision-model-workbench) |
| Maintainer | [BatuhanYilmaz26](https://github.com/BatuhanYilmaz26). Independently curated. |
| Format | Python local web app (API + worker + browser UI) with guides |
| Requirements | Python 3.12/3.13; a TypeSafe or other provider key only for hosted-model profiles. |
| License | [Apache-2.0](https://github.com/BatuhanYilmaz26/decision-model-workbench/blob/f70329765c6d15f3df9ca9c7628af893173924aa/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/batuhan3326/status/2110828338277163479)). |
| Jev evidence | [`decision_workbench/platform/hosted_transport.py`](https://github.com/BatuhanYilmaz26/decision-model-workbench/blob/f70329765c6d15f3df9ca9c7628af893173924aa/decision_workbench/platform/hosted_transport.py) at the pinned commit. |

## When to use

- Prototype a support-routing or invoice-category decision against Jev before wiring it into an application.
- Compare a hosted decision model with a small locally trained baseline on your own reviewed examples.
- Mismatch: early project; Jev is one hosted provider among several, and training paths do not use Jev.

## How it works

Hosted profiles map a provider name to its endpoint (TypeSafe `api.typesafe.ai/v1/systemone`, OpenRouter decisions, Perplexity, Cloudflare); responses are validated against the expected typed answer before your rules or fallback decide what happens. Integration evidence: [`decision_workbench/platform/hosted_transport.py`](https://github.com/BatuhanYilmaz26/decision-model-workbench/blob/f70329765c6d15f3df9ca9c7628af893173924aa/decision_workbench/platform/hosted_transport.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/BatuhanYilmaz26/decision-model-workbench.git && cd decision-model-workbench
python3.12 -m venv .venv && . .venv/bin/activate
python -m pip install -r requirements.txt
domain-platform run   # opens http://127.0.0.1:8501
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Guides: `docs/api-integration-guide.md`, `docs/application-blueprints.md`, `docs/benchmarks.md`.

## Limits and data handling

Projects persist locally in `data/local-workspace`; hosted profiles send inputs to the chosen provider on your key.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit f70329765c6d](https://github.com/BatuhanYilmaz26/decision-model-workbench/tree/f70329765c6d15f3df9ca9c7628af893173924aa). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
