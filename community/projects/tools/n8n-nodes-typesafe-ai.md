# n8n-nodes-typesafe-ai

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeSafe-published n8n nodes to Evaluate or Route workflow items with System One models such as Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai) |
| Maintainer | [typesafe-ai](https://github.com/typesafe-ai). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | n8n community node package (`@typesafe-ai/n8n-nodes-typesafe-ai`). |
| Requirements | Self-hosted or desktop n8n that can install community nodes; TypeSafe API key credential. |
| License | [MIT](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai/blob/c12537bbd9ed7159b7bbe23678ca128c7b2fb52b/LICENSE.md). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Published by typesafe-ai. Distinct from community [n8n-nodes-typesafe](n8n-nodes-typesafe.md) and [jev-classification-n8n](jev-classification-n8n.md). |

## When to use

Use for official TypeSafe packaging inside n8n. Prefer Biztactix or khmuhtadin nodes only if you already depend on those packages.

## How it works

Evaluate attaches typed answers to each item; Route picks an output branch from one question’s answer. State can be text, JSON, or the input item. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/typesafe-ai/n8n-nodes-typesafe-ai.git
cd n8n-nodes-typesafe-ai
git checkout c12537bbd9ed7159b7bbe23678ca128c7b2fb52b
# or install @typesafe-ai/n8n-nodes-typesafe-ai via n8n community nodes UI
```

Pin revision `c12537bbd9ed7159b7bbe23678ca128c7b2fb52b` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live n8n/TypeSafe workflows not run on the review host. Distinct from [n8n-nodes-typesafe](n8n-nodes-typesafe.md) (Biztactix) and [Jev Classification for n8n](jev-classification-n8n.md).

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit c12537b](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai/tree/c12537bbd9ed7159b7bbe23678ca128c7b2fb52b). AI-assisted README and LICENSE inspection; install/live paths not executed.
