# DecisionForge (build Jev-style decision data and train your own decision models, compared with Jev)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Toolkit that turns a decision scenario into an evaluated decision model: it builds Jev-format choice, yes/no and score data from your materials, trains native decision models with backends such as Unsloth, ms-swift and Laya, and compares them with Jev and training-free methods on the same evaluation set.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Blackteaxx/DecisionForge) |
| Maintainer | [Blackteaxx](https://github.com/Blackteaxx). Independently curated. |
| Format | Python toolkit with agent skills (Apache-2.0; README in Chinese and English) |
| Requirements | Python 3.11+ and uv; GPU for training; `TYPESAFE_API_KEY` to evaluate against Jev. |
| License | [Apache-2.0](https://github.com/Blackteaxx/DecisionForge/blob/26eef3a7bb39a05d771f09e75e189b44f4e9085b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decisionforge/eval/models.py`](https://github.com/Blackteaxx/DecisionForge/blob/26eef3a7bb39a05d771f09e75e189b44f4e9085b/src/decisionforge/eval/models.py) at the pinned commit. |

## When to use

- Train a small domain decision model and check it against Jev.
- Generate checked Jev-format question data from documents.
- Mismatch: research toolkit; training needs a GPU.

## How it works

`src/decisionforge/eval/models.py` configures an HTTP model client with base URL `https://api.typesafe.ai` and the `/v1/systemone` path (or `/api/alpha/decisions`), so Jev is one of the baselines on each benchmark; project skills walk an agent through data, training and evaluation. Integration evidence: [`src/decisionforge/eval/models.py`](https://github.com/Blackteaxx/DecisionForge/blob/26eef3a7bb39a05d771f09e75e189b44f4e9085b/src/decisionforge/eval/models.py).

## Get started

Clone the repo, sync the environment and let your coding agent follow the project skills.

```sh
git clone https://github.com/Blackteaxx/DecisionForge.git && cd DecisionForge && uv sync
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo: [blackteaxx.github.io/DecisionForge/](https://blackteaxx.github.io/DecisionForge/)

## Limits and data handling

Evaluation cases go to TypeSafe on your key when Jev is a baseline; training runs locally.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 26eef3a7bb39](https://github.com/Blackteaxx/DecisionForge/tree/26eef3a7bb39a05d771f09e75e189b44f4e9085b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
