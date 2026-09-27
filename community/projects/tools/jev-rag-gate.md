# jev-rag-gate

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Semantic gating for RAG retrieval candidates (relevance, premise contradiction, prompt injection) with TypeSafe Jev System One.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/breaker364/jev-rag-gate) |
| Maintainer | [breaker364](https://github.com/breaker364). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python gating library. |
| Requirements | Python; TypeSafe API key for live gates. |
| License | [MIT](https://github.com/breaker364/jev-rag-gate/blob/05e30f71aa635cfdd430b527c1350c1ba53f95eb/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use after similarity retrieval when you need typed semantic gates before context assembly.

## How it works

Issues System One questions over candidate passages and applies thresholds in code for keep/drop decisions. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/breaker364/jev-rag-gate.git
cd jev-rag-gate
git checkout 05e30f71aa635cfdd430b527c1350c1ba53f95eb
# follow upstream README for install/run; configure credentials as documented
```

Pin revision `05e30f71aa635cfdd430b527c1350c1ba53f95eb` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live calls send task/context text to the configured provider (TypeSafe and/or OpenRouter/Cloudflare per upstream).  Live paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 05e30f71aa63](https://github.com/breaker364/jev-rag-gate/tree/05e30f71aa635cfdd430b527c1350c1ba53f95eb). AI-assisted README and LICENSE inspection; install/live paths not executed.
