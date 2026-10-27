# DERVA (AI gateway for regulated teams with a Jev decision layer)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Gateway built on the LiteLLM proxy that sits between AI agents and models for regulated teams: before a request reaches a model, a fast decision layer answers typed questions (prompt injection, client data leaving the firm, regulated advice, which model tier it needs), with Presidio masking, versioned policy, human approval for actions and a hash-chained audit log; the decision layer is vendor-neutral, and the author adopted Jev after it passed all 15 pre-set criteria on held-out data.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TomaIjatomi/derva-ai-gateway) |
| Maintainer | [TomaIjatomi](https://github.com/TomaIjatomi). Independently curated. |
| Format | Python gateway (LiteLLM proxy) with evaluation harness |
| Requirements | uv and Python; a TypeSafe API key for the Jev decider (an offline mock runs without keys). |
| License | [MIT](https://github.com/TomaIjatomi/derva-ai-gateway/blob/94e0ebeaa6488028681fd6c3f289ce5b9ec739ad/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/Toma_Ij/status/2115061255203430791)). |
| Jev evidence | [`src/derva/deciders/systemone.py`](https://github.com/TomaIjatomi/derva-ai-gateway/blob/94e0ebeaa6488028681fd6c3f289ce5b9ec739ad/src/derva/deciders/systemone.py) at the pinned commit. |

## When to use

- Put typed policy checks and an audit trail in front of every LLM call.
- Mismatch: v0.1; evaluation numbers are the author's.

## How it works

`src/derva/deciders/systemone.py` posts the request's questions to `https://api.typesafe.ai` (`/v1/systemone`, pinned `typesafe/jev-1.13.0` in the staging config) and the versioned policy turns probabilities into block, review, decline, clarify or a model tier. Integration evidence: [`src/derva/deciders/systemone.py`](https://github.com/TomaIjatomi/derva-ai-gateway/blob/94e0ebeaa6488028681fd6c3f289ce5b9ec739ad/src/derva/deciders/systemone.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/TomaIjatomi/derva-ai-gateway && cd derva-ai-gateway
uv sync --all-extras
uv run derva mock-server   # offline demo; see the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/TomaIjatomi/derva-ai-gateway#readme](https://github.com/TomaIjatomi/derva-ai-gateway#readme)

## Limits and data handling

Masked request text goes to the configured decider. Discovered on X from the creator's post.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 94e0ebeaa648](https://github.com/TomaIjatomi/derva-ai-gateway/tree/94e0ebeaa6488028681fd6c3f289ce5b9ec739ad). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
