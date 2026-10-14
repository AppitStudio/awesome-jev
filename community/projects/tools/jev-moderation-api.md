# Jev Moderation API

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Small FastAPI proof of concept that moderates text against configurable policies with Jev Noul questions via the official TypeSafe Python SDK.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Noah-Haf/jev-moderation-api) |
| Maintainer | [Noah-Haf](https://github.com/Noah-Haf). Independently curated. |
| Format | Python FastAPI service |
| Requirements | Python with uv; TypeSafe API key. |
| License | [MIT](https://github.com/Noah-Haf/jev-moderation-api/blob/d4e5e74998e9dc82f59e18dd2df2dba5ee9838d0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/noah_hafner/status/2110483284484649207)). |
| Jev evidence | [`routers/text.py`](https://github.com/Noah-Haf/jev-moderation-api/blob/d4e5e74998e9dc82f59e18dd2df2dba5ee9838d0/routers/text.py) at the pinned commit. |

## When to use

- Prototype a policy-based text moderation endpoint backed by Jev.
- See a minimal use of `AsyncTypeSafeClient` with Noul answers.
- Mismatch: author describes it as a primitive proof of concept built in about 90 minutes.

## How it works

Each policy defines what counts as violating text; the router sends the submitted text to Jev with one Noul question per policy through `typesafe_sdk.AsyncTypeSafeClient` and returns the probabilities. Integration evidence: [`routers/text.py`](https://github.com/Noah-Haf/jev-moderation-api/blob/d4e5e74998e9dc82f59e18dd2df2dba5ee9838d0/routers/text.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv venv
uv sync
cp .env.example .env
uv run fastapi dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Creator's X post describing realtime moderation latency (author-reported).

## Limits and data handling

Submitted text is sent to TypeSafe and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit d4e5e74998e9](https://github.com/Noah-Haf/jev-moderation-api/tree/d4e5e74998e9dc82f59e18dd2df2dba5ee9838d0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
