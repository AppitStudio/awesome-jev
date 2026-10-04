# zenai

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Zig client for AI APIs (Gemini, OpenAI, and others) with a TypeSafe System One client for typed Jev questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lightpanda-io/zenai) |
| Maintainer | [lightpanda-io](https://github.com/lightpanda-io). Independently curated. |
| Format | Zig library (multi-provider AI client) |
| Requirements | Zig toolchain; `zig fetch --save git+https://github.com/lightpanda-io/zenai`; `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/lightpanda-io/zenai/blob/63df800afc438c0e90603270a4696689eb339ccc/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Add Jev decisions to Zig services or CLIs without a Python/JS runtime.
- Use one client library for both generative providers and System One.
- Mismatch: other languages should prefer the official SDKs.

## How it works

The `typesafe` module builds System One requests (state plus a map of typed questions) and parses one typed answer per question; application code owns policy and actions.

## Get started

Add the dependency and create a client (see upstream README for the full example):

```sh
zig fetch --save git+https://github.com/lightpanda-io/zenai
export TYPESAFE_API_KEY='your-api-key'
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Upstream README section "TypeSafe (System One)" with a Zig example.

## Limits and data handling

Requests send state text to TypeSafe and are billed per call. Community client, not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 63df800afc43](https://github.com/lightpanda-io/zenai/tree/63df800afc438c0e90603270a4696689eb339ccc). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
