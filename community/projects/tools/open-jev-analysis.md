# open-jev-analysis (study of Open-Jev 2B and 9B for safety classification, guardrails and search reranking)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research code testing how well the open Open-Jev 2B and 9B decision models handle six safety targets (prompt injection, harmful requests, toxicity, jailbreaks, XSTest, moderation categories) and BEIR reranking on top of BM25 and EmbeddingGemma 2. Reports accuracy, per-class recall, false positives, calibration and latency; the author finds task-dependent strengths and cases where high accuracy hides poor detection of rare positives.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/iosifidisvasileios/open-jev-analysis) |
| Maintainer | [iosifidisvasileios](https://github.com/iosifidisvasileios). Independently curated. |
| Format | Python experiment code and configs |
| Requirements | Python 3.12+, uv, a GPU and the Open-Jev checkpoints (downloaded separately). |
| License | [MIT](https://github.com/iosifidisvasileios/open-jev-analysis/blob/2aa737f4bb8afe18231385a9e0a56231e3eb9fad/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`run_openjev_experiments.py`](https://github.com/iosifidisvasileios/open-jev-analysis/blob/2aa737f4bb8afe18231385a9e0a56231e3eb9fad/run_openjev_experiments.py) at the pinned commit. |

## When to use

- Check Open-Jev on safety and reranking tasks before choosing it as a local guardrail.
- Mismatch: evaluates Open-Jev, not TypeSafe's Jev; reports and run outputs are not in the repo.

## How it works

`run_openjev_experiments.py` starts a local Open-Jev server per checkpoint and `jev_guardrails/` sends each case to its `/v1/systemone` endpoint. Integration evidence: [`run_openjev_experiments.py`](https://github.com/iosifidisvasileios/open-jev-analysis/blob/2aa737f4bb8afe18231385a9e0a56231e3eb9fad/run_openjev_experiments.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync
# download Open-Jev checkpoints into checkpoints/ (see upstream instructions)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Open-Jev upstream: [github.com/Zefan-Cai/Open-Jev](https://github.com/Zefan-Cai/Open-Jev)

## Limits and data handling

Runs locally; no data goes to TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 2aa737f4bb8a](https://github.com/iosifidisvasileios/open-jev-analysis/tree/2aa737f4bb8afe18231385a9e0a56231e3eb9fad). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
