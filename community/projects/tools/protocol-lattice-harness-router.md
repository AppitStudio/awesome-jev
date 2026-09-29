# harness-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Fast decision routing for agent harnesses — native MCP with Jev for tool selection and MCTS for multi-step decisions

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Protocol-Lattice/harness-router) |
| Maintainer | [Protocol-Lattice](https://github.com/Protocol-Lattice). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python · MCP router (MIT). |
| Requirements | Python; TypeSafe credentials for live MCP routing. |
| License | [MIT](https://github.com/Protocol-Lattice/harness-router/blob/4d06d9e51af8151c581e9bad7c7a6d0703766746/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when harnesses need calibrated tool-selection judgments before heavier planning.

## How it works

MCP server asks Jev for tool-routing decisions; MCTS optional for multi-step. Homepage: <\1>ss-router.vercel.app. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/Protocol-Lattice/harness-router.git
cd harness-router
git checkout 4d06d9e51af8151c581e9bad7c7a6d0703766746
```

Pin revision `4d06d9e51af8151c581e9bad7c7a6d0703766746` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 4d06d9e](https://github.com/Protocol-Lattice/harness-router/tree/4d06d9e51af8151c581e9bad7c7a6d0703766746). AI-assisted README and LICENSE inspection; install/live paths not executed.
