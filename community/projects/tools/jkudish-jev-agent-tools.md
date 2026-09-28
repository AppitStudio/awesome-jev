# jev-agent-tools

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Jev transport/provider layer with fail-closed validation; shared by jkudish/jev-browser and jkudish/jev-mcp

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jkudish/jev-agent-tools) |
| Maintainer | [jkudish](https://github.com/jkudish). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | JavaScript · transport library (MIT). |
| Requirements | Node.js; provider credentials for live calls. |
| License | [MIT](https://github.com/jkudish/jev-agent-tools/blob/55f2ed49d35c6abf28cceba8a8b551a917ffd3ed/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when building Jev clients that need validated multi-provider transport. Related to listed @jkudish/jev-mcp.

## How it works

Library validates questions and routes to providers fail-closed. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/jkudish/jev-agent-tools.git
cd jev-agent-tools
git checkout 55f2ed49d35c6abf28cceba8a8b551a917ffd3ed
```

Pin revision `55f2ed49d35c6abf28cceba8a8b551a917ffd3ed` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 55f2ed4](https://github.com/jkudish/jev-agent-tools/tree/55f2ed49d35c6abf28cceba8a8b551a917ffd3ed). AI-assisted README and LICENSE inspection; install/live paths not executed.
