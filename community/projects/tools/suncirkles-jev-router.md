# JevRoute (suncirkles)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Decision-only coding-task model routing (JevRoute) with a separate evaluation harness and recorded experiment evidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/suncirkles/jev-router) |
| Maintainer | [suncirkles](https://github.com/suncirkles). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Router library + evaluation harness. |
| Requirements | Python; OpenRouter/TypeSafe keys for live classification arms per upstream docs. |
| License | [MIT](https://github.com/suncirkles/jev-router/blob/7c3d036c23ef97c83cd26210df30198fd5fe71fe/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from gargpratyush/jev-router and peptidehackers/jev-router. |

## When to use

Use when you want a decision-only router (caller owns the agent loop). Prefer gargpratyush/jev-router for Claude Code/Codex turn routing.

## How it works

Returns a model recommendation from typed decisions; evaluation package records frozen pilots. Distinct from other jev-router packages. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/suncirkles/jev-router.git
cd jev-router
git checkout 7c3d036c23ef97c83cd26210df30198fd5fe71fe
# follow upstream README for install/run; configure credentials as documented
```

Pin revision `7c3d036c23ef97c83cd26210df30198fd5fe71fe` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live calls send task/context text to the configured provider (TypeSafe and/or OpenRouter/Cloudflare per upstream). Distinct from gargpratyush/jev-router and peptidehackers/jev-router. Live paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 7c3d036c23ef](https://github.com/suncirkles/jev-router/tree/7c3d036c23ef97c83cd26210df30198fd5fe71fe). AI-assisted README and LICENSE inspection; install/live paths not executed.
