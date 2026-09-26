# JEV ADK

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Agent Development Kit patterns for TypeSafe Jev: guardrails, dual-brain routing, and PR triage blueprints (System One decisions in code).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/abyakod/JEV_ADK) |
| Maintainer | [abyakod](https://github.com/abyakod). Independently curated. |
| Format | Python Agent Development Kit examples and primitives. |
| Requirements | Python 3.10+; TypeSafe API key for live Jev calls. |
| License | [MIT](https://github.com/abyakod/JEV_ADK/blob/bec3469258c49d06ad00b414996df3c1e762e121/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use when scaffolding **Jev-first agent decisions** (guards, routers, triage) instead of LLM-as-if. Prefer thinner SDKs when you only need evaluate wrappers.

## How it works

Documents dual-brain patterns and ships blueprints where Jev answers typed micro-decisions and application code enforces policy.

## Get started

```sh
git clone https://github.com/abyakod/JEV_ADK.git
cd JEV_ADK
git checkout bec3469258c49d06ad00b414996df3c1e762e121
# Follow README quickstart blueprints; needs TypeSafe key for live paths
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit bec3469](https://github.com/abyakod/JEV_ADK/tree/bec3469258c49d06ad00b414996df3c1e762e121). AI-assisted README and license inspection; install/live paths not executed.
