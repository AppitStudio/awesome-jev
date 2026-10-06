# Jev Moderation

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeScript and Python SDKs for text moderation with TypeSafe Jev: a bundled, versioned community policy or your own filters, each rule compiled to a Noul question, with review/block thresholds and a policy test CLI (validate, eval, compare with quality gates).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/abishakkodi/jev-moderation) |
| Maintainer | [abishakkodi](https://github.com/abishakkodi). Independently curated. |
| Format | TypeScript + Python SDKs and CLI (source install; npm/PyPI packages not yet published at review) |
| Requirements | Node.js and/or Python 3; `TYPESAFE_API_KEY`; calls go from your server to TypeSafe (no hosted service). |
| License | [MIT](https://github.com/abishakkodi/jev-moderation/blob/c00545d51ec8939c1496613e0b1747f963674ded/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Moderate comments or chat with the community preset (harassment, hate, threats, explicit content, self-harm encouragement, scams, spam).
- Extend or replace filters and run `compare` with quality gates to catch regressions before rollout.
- Mismatch: thresholds are uncalibrated starting values; text only; packages must be built from source.

## How it works

Each filter becomes a Noul question about the message ([`packages/typescript/src/core.ts`](https://github.com/abishakkodi/jev-moderation/blob/c00545d51ec8939c1496613e0b1747f963674ded/packages/typescript/src/core.ts), [`packages/python/src/jev_moderation/core.py`](https://github.com/abishakkodi/jev-moderation/blob/c00545d51ec8939c1496613e0b1747f963674ded/packages/python/src/jev_moderation/core.py)); code applies `review >= 0.5` / `block >= 0.9` defaults with block winning over review. Requests are capped at 24,000 UTF-8 bytes and oversized input raises instead of truncating. Both SDKs share policy schemas and conformance fixtures.

## Get started

Build both SDKs locally (packages are not yet on npm/PyPI):

```sh
git clone https://github.com/abishakkodi/jev-moderation.git && cd jev-moderation
npm ci && npm run build
python3 -m venv .venv && .venv/bin/pip install -e 'packages/python[dev]'
export TYPESAFE_API_KEY=...
node packages/typescript/dist/cli.js eval --cases shared/examples.jsonl --output report.json
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- `shared/examples.jsonl` cases with `validate`, `eval` and `compare` CLI commands; `examples/custom-policy.json` and `examples/quality-gates.json`.
- [Release guide](https://github.com/abishakkodi/jev-moderation/blob/c00545d51ec8939c1496613e0b1747f963674ded/docs/releasing.md) including opt-in live evaluation.

## Limits and data handling

Message text is sent to TypeSafe. Default model `jev-1.13.0`. Probabilities are violation likelihoods, not severity. The SDK does not log bodies (the upstream Python SDK can at debug level). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit c00545d51ec8](https://github.com/abishakkodi/jev-moderation/tree/c00545d51ec8939c1496613e0b1747f963674ded). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
