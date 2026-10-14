# jiwo

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Small open decision models (0.8B and 4B) served behind a Jev-compatible `POST /v1/systemone` API, returning option probabilities in one forward pass.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jiwidi/jiwo) |
| Maintainer | [jiwidi](https://github.com/jiwidi). Independently curated. |
| Format | Models + FastAPI server (Python) |
| Requirements | Python 3.12; GPU recommended for the documented latency; Hugging Face weights. |
| License | [MIT](https://github.com/jiwidi/jiwo/blob/e64d36227e02a36c0ea1bc3ec669003eb5a30c29/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/aigeeknews/status/2110363690109456545)). |
| Jev evidence | [`src/jiwo/serving/app.py`](https://github.com/jiwidi/jiwo/blob/e64d36227e02a36c0ea1bc3ec669003eb5a30c29/src/jiwo/serving/app.py) at the pinned commit. |

## When to use

- Self-host a Jev-API-compatible decision model for latency-critical paths.
- Mismatch: independent project; TypeSafe does not endorse it; leaderboard figures are author/board-reported.

## How it works

The server accepts the Jev request format and scores each option in one forward pass; no text is generated. Integration evidence: [`src/jiwo/serving/app.py`](https://github.com/jiwidi/jiwo/blob/e64d36227e02a36c0ea1bc3ec669003eb5a30c29/src/jiwo/serving/app.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install "jiwo @ git+https://github.com/jiwidi/jiwo"
JIWO_CHECKPOINT=eljiwo/jiwo-0.8b jiwo serve
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Weights: [huggingface.co/eljiwo/jiwo-0.8b](https://huggingface.co/eljiwo/jiwo-0.8b) and jiwo-4b.
- Tests: `tests/`.

## Limits and data handling

Runs locally; no TypeSafe calls.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit e64d36227e02](https://github.com/jiwidi/jiwo/tree/e64d36227e02a36c0ea1bc3ec669003eb5a30c29). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
