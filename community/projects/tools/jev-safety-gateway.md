# jev-safety-gateway

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go reverse-proxy in front of LLM backends: extracts user input per request, asks TypeSafe Jev, blocks harmful traffic, passes the rest through.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dark-hxx/jev-safety-gateway) |
| Maintainer | [dark-hxx](https://github.com/dark-hxx). Independently curated. |
| Format | Go · reverse-proxy gateway (AGPL-3.0) |
| Requirements | Go runtime; TypeSafe API access for Jev judgments. |
| License | [AGPL-3.0](https://github.com/dark-hxx/jev-safety-gateway/blob/7763775637c75d555537cec97d14af627421ff28/LICENSE). TypeSafe/provider usage may incur charges. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live paths not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/dark-hxx/jev-safety-gateway.git
cd jev-safety-gateway
git checkout 7763775637c75d555537cec97d14af627421ff28
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 7763775637c7](https://github.com/dark-hxx/jev-safety-gateway/tree/7763775637c75d555537cec97d14af627421ff28). AI-assisted README and license inspection; install/live paths not executed.
