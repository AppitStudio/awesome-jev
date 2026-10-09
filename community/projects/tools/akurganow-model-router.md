# model-router (Claude Code)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod that asks TypeSafe Jev one Score question about each redacted subagent task before it starts and sets the subagent model to haiku, sonnet or opus; `suggest` mode only logs, and the hook runs no commands and writes no files.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Akurganow/model-router) |
| Maintainer | [Akurganow](https://github.com/Akurganow). Independently curated. |
| Format | Claude Code mod (`agent.spawn` hook) |
| Requirements | Claude Code; TypeSafe API key. |
| License | [MIT](https://github.com/Akurganow/model-router/blob/60515f115a1228980080c7c9e2e75fb266436009/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Lower subagent cost without hand-picking models.
- Mismatch: routing quality depends on the shipped calibration seed.

## How it works

See the upstream [README](https://github.com/Akurganow/model-router/blob/60515f115a1228980080c7c9e2e75fb266436009/README.md) at the pinned commit for architecture and the Jev integration.

## Get started

From the README:

```sh
git clone https://github.com/Akurganow/model-router.git   # install per README
```

## Limits and data handling

Condensed, redacted task text goes to api.typesafe.ai (see PRIVACY.md). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 60515f115a12](https://github.com/Akurganow/model-router/tree/60515f115a1228980080c7c9e2e75fb266436009). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
