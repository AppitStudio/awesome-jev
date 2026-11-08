# Synalinks (Keras-based neuro-symbolic LM framework with TypeSafe Jev decision models)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Keras-style framework for neuro-symbolic language-model systems whose `Decision` module accepts System One decision models such as `typesafe/jev-latest`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SynaLinks/synalinks) |
| Maintainer | [SynaLinks](https://github.com/SynaLinks). Independently curated. |
| Format | Python framework (Apache-2.0) |
| Requirements | Python, `pip install synalinks`, and `TYPESAFE_API_KEY` for hosted Jev. |
| License | [Apache-2.0](https://github.com/SynaLinks/synalinks/blob/1b954f8bf6168eec466cb684959c0f4940d98f0d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`synalinks/src/modules/core/decision.py`](https://github.com/SynaLinks/synalinks/blob/1b954f8bf6168eec466cb684959c0f4940d98f0d/synalinks/src/modules/core/decision.py) at the pinned commit. |

## When to use

- Use Jev as a typed decision step in a Keras-style LM pipeline.
- Swap hosted Jev for a local decision model.
- Mismatch: generation still needs an LM.

## How it works

Decision modules take a decision model (`typesafe/jev-latest` or local models); MLflow observability records the versioned Jev model. Guide 33 walks through decision models. Integration evidence: [`synalinks/src/modules/core/decision.py`](https://github.com/SynaLinks/synalinks/blob/1b954f8bf6168eec466cb684959c0f4940d98f0d/synalinks/src/modules/core/decision.py).

## Get started

Install Synalinks and run `guides/33_decision_models.py` with your key.

```sh
git clone https://github.com/SynaLinks/synalinks.git && cd synalinks
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Guide: [github.com/SynaLinks/synalinks/blob/1b954f8bf6168eec466cb684959c0f4940d98f0d/guides/33_decision_models.py](https://github.com/SynaLinks/synalinks/blob/1b954f8bf6168eec466cb684959c0f4940d98f0d/guides/33_decision_models.py)

## Limits and data handling

Inputs to decision modules are sent to TypeSafe when using hosted Jev.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 1b954f8bf616](https://github.com/SynaLinks/synalinks/tree/1b954f8bf6168eec466cb684959c0f4940d98f0d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
