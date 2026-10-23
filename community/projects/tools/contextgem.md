# ContextGem (document extraction with LLMs and decision models)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Open-source Python framework for extracting structured data from documents; version 1.0 adds decision models such as Jev, which answer closed questions (yes/no, labels, ratings) with probabilities for each option, alone or in a model group next to LLMs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shcherbak-ai/contextgem) |
| Maintainer | [shcherbak-ai](https://github.com/shcherbak-ai). Independently curated. |
| Format | Python library (PyPI: contextgem) |
| Requirements | Python 3.11+; a TypeSafe API key for Jev (served through litellm), plus LLM keys if you combine models. |
| License | [Apache-2.0](https://github.com/shcherbak-ai/contextgem/blob/264184f44312e93d0045c7e66b602b87b7e43a82/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`contextgem/public/decision_models.py`](https://github.com/shcherbak-ai/contextgem/blob/264184f44312e93d0045c7e66b602b87b7e43a82/contextgem/public/decision_models.py) at the pinned commit. |

## When to use

- Classify paragraphs and sentences into aspects cheaply before an LLM extracts details.
- Get boolean, label and rating concepts with calibrated probabilities instead of generated text.
- Mismatch: decision models cover closed questions only; open-ended extraction still needs an LLM.

## How it works

`contextgem/public/decision_models.py` defines the decision model class: set `model` to `typesafe/jev-latest` and ContextGem asks Jev per paragraph or sentence whether it belongs to an aspect and which option fits each closed concept, storing the probabilities on every extracted item. Integration evidence: [`contextgem/public/decision_models.py`](https://github.com/shcherbak-ai/contextgem/blob/264184f44312e93d0045c7e66b602b87b7e43a82/contextgem/public/decision_models.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv add contextgem             # or: pip install -U contextgem
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Documentation: [contextgem.shcherbak.ai/](https://contextgem.shcherbak.ai/)
- Migration guide for 1.0: [contextgem.shcherbak.ai/migration_v1/](https://contextgem.shcherbak.ai/migration_v1/)

## Limits and data handling

Document text is sent to the configured model providers, including TypeSafe for decision-model calls.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 264184f44312](https://github.com/shcherbak-ai/contextgem/tree/264184f44312e93d0045c7e66b602b87b7e43a82). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
