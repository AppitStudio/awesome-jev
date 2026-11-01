# gated-llm-pipeline (social-post triage where code owns the flow, Jev gates each step, and an LLM sees only unsure items)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Eight-step triage pipeline for inbound social posts: code owns the control flow, a cheap classifier (Jev, or a deterministic mock) makes the narrow judgment at every gate, and a reasoning model only sees items the classifier is unsure about. Answers are cached, and backtest and QA-eval scripts check the gates.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/s0yabean/gated-llm-pipeline) |
| Maintainer | [s0yabean](https://github.com/s0yabean). Independently curated. |
| Format | Python package + scripts |
| Requirements | Python; a TypeSafe or Vercel AI Gateway key for `CLASSIFIER=jev`; optional Anthropic key. |
| License | [MIT](https://github.com/s0yabean/gated-llm-pipeline/blob/6dffc985401f0e63ac065bcc83d32d1e6153795e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`gated_pipeline/classifier.py`](https://github.com/s0yabean/gated-llm-pipeline/blob/6dffc985401f0e63ac065bcc83d32d1e6153795e/gated_pipeline/classifier.py) at the pinned commit. |

## When to use

- Decide which inbound posts deserve a considered reply without an LLM call per post.
- Mismatch: the default mock classifier says nothing about Jev; set `CLASSIFIER=jev` for real answers.

## How it works

`gated_pipeline/classifier.py` sends one System One request per post with all gate questions (pinned to `jev-1.13.0` with a direct key), caches answers on disk, and runs requests in parallel via `ask_many`. Integration evidence: [`gated_pipeline/classifier.py`](https://github.com/s0yabean/gated-llm-pipeline/blob/6dffc985401f0e63ac065bcc83d32d1e6153795e/gated_pipeline/classifier.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/s0yabean/gated-llm-pipeline && cd gated-llm-pipeline
cp .env.example .env   # CLASSIFIER=jev, TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README backtest section: [github.com/s0yabean/gated-llm-pipeline#readme](https://github.com/s0yabean/gated-llm-pipeline#readme)

## Limits and data handling

Post text is sent to TypeSafe (and Anthropic for unsure items). Backtest numbers are the author's. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 6dffc985401f](https://github.com/s0yabean/gated-llm-pipeline/tree/6dffc985401f0e63ac065bcc83d32d1e6153795e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
