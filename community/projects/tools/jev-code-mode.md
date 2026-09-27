# jev-code-mode

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Typed Jev judgments behind two MCP tools: search and execute.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/acoyfellow/jev-code-mode) |
| Maintainer | [acoyfellow](https://github.com/acoyfellow). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | MCP server. |
| Requirements | MCP host; TypeSafe/provider credentials per upstream README. |
| License | [MIT](https://github.com/acoyfellow/jev-code-mode/blob/8d5189f9fef840e2d061d63d40b674bcfc9c4b2a/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when agents should run cheap typed checks (injection, evidence support, option pick) via MCP before acting.

## How it works

MCP tools wrap System One judgments for search/execute paths; application/host still owns tool execution policy. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/acoyfellow/jev-code-mode.git
cd jev-code-mode
git checkout 8d5189f9fef840e2d061d63d40b674bcfc9c4b2a
# follow upstream README for install/run; configure credentials as documented
```

Pin revision `8d5189f9fef840e2d061d63d40b674bcfc9c4b2a` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live calls send task/context text to the configured provider (TypeSafe and/or OpenRouter/Cloudflare per upstream).  Live paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 8d5189f9fef8](https://github.com/acoyfellow/jev-code-mode/tree/8d5189f9fef840e2d061d63d40b674bcfc9c4b2a). AI-assisted README and LICENSE inspection; install/live paths not executed.
