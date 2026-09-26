# jev-guard (rudra72r)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Fast, cheap guardrails for LLM apps powered by TypeSafe Jev (with offline try path).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rudra72r/jev-guard) |
| Maintainer | [rudra72r](https://github.com/rudra72r). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package with builtin policies, offline try, and optional local model backend. |
| Requirements | Python; `pip install jev-guard` (+ `[local]` for offline); optional `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/rudra72r/jev-guard/blob/d7417ac0ee7de2e1b43e6e41b9d2e0709c65b782/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use to wrap chat/support bots with typed injection and policy checks before/after the LLM.

## How it works

Policy questions → backend judgments → allow/review/block with reasons and suggested refusal text. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
pip install \"jev-guard[local]\"
jev-guard try
# or: export TYPESAFE_API_KEY=… && pip install jev-guard
```

Pin revision `d7417ac0ee7de2e1b43e6e41b9d2e0709c65b782` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Distinct from coding-agent jev-guard hooks (leepokai et al.). Live TypeSafe path not run on the review host; offline try downloads models.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit d7417ac](https://github.com/rudra72r/jev-guard/tree/d7417ac0ee7de2e1b43e6e41b9d2e0709c65b782). AI-assisted README and LICENSE inspection; install/live paths not executed.
