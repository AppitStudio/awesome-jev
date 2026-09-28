# jev-broker

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Local HTTP MCP broker for Hermes agents: validate questions, call TypeSafe Jev via OpenRouter, return structured judgments (agent still decides)

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AlekseiUL/jev-broker) |
| Maintainer | [AlekseiUL](https://github.com/AlekseiUL). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go local HTTP MCP tool for Hermes agents. |
| Requirements | Go; OpenRouter key for TypeSafe Jev via OpenRouter. |
| License | [MIT](https://github.com/AlekseiUL/jev-broker/blob/972a2ce23db7a9d61d6a4c44e97846b90bdc8610/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when Hermes agents should evaluate Noul/Choice/Score batches through OpenRouter-hosted Jev with local logging. Prefer direct TypeSafe SDK if you are not on Hermes/OpenRouter.

## How it works

Broker validates input, logs attempt metadata, calls Jev through OpenRouter, returns judgments; agent must re-check evidence. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/AlekseiUL/jev-broker.git
cd jev-broker
git checkout 972a2ce23db7a9d61d6a4c44e97846b90bdc8610
```

Pin revision `972a2ce23db7a9d61d6a4c44e97846b90bdc8610` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 972a2ce](https://github.com/AlekseiUL/jev-broker/tree/972a2ce23db7a9d61d6a4c44e97846b90bdc8610). AI-assisted README and LICENSE inspection; install/live paths not executed.
