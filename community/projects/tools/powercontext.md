# PowerContext by OceanBase (context service for AI agents, with optional Jev memory reranking and advisory decisions)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Open-source context service that keeps an agent's decisions, constraints, evidence and progress outside any one conversation so the next session, agent or person can pick up from the current state. Python deployments can add an optional Jev reranker that filters retrieved memory candidates, and an example adapter plugs Jev (or the open Laya model) into the Runtime's advisory `DecisionModel` port to review code against recalled project rules. The README reports LoCoMo Plus gains of about 4 to 9 points with Jev filtering, scores supplied by the project owner without public run artifacts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/oceanbase/powercontext) |
| Maintainer | [oceanbase](https://github.com/oceanbase). Independently curated. |
| Format | Python library, CLI and server (uv, `powercontext` on PyPI) |
| Requirements | Python via uv; a TypeSafe key and a pinned Jev model such as `jev-1.13.0` only for the Jev reranker or decision example. |
| License | [Apache-2.0](https://github.com/oceanbase/powercontext/blob/90355b8e96d68e2932d7980b3e76957f35ea2b44/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/powercontext/builtin/artifacts/memory/jev_reranking.py`](https://github.com/oceanbase/powercontext/blob/90355b8e96d68e2932d7980b3e76957f35ea2b44/src/powercontext/builtin/artifacts/memory/jev_reranking.py) at the pinned commit. |

## When to use

- Give coding or chat agents durable project memory and let Jev drop irrelevant recalled items before answering.
- Mismatch: Jev is optional and off by default; the core service works without it.

## How it works

`jev_reranking.py` asks Jev, over a caller-owned HTTPX client with a total deadline, whether each retrieved memory candidate is relevant to the query and keeps the relevant ones; `examples/systemone/adapter.py` maps a `DecisionRequest` to the System One protocol for Jev or Laya. Integration evidence: [`src/powercontext/builtin/artifacts/memory/jev_reranking.py`](https://github.com/oceanbase/powercontext/blob/90355b8e96d68e2932d7980b3e76957f35ea2b44/src/powercontext/builtin/artifacts/memory/jev_reranking.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv tool install --force "powercontext[cli,server]==1.4.1"
# Jev decision example: see examples/systemone/README.md and jev.env.example
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev and Laya coding-decision example: [github.com/oceanbase/powercontext/tree/90355b8e96d68e2932d7980b3e76957f35ea2b44/examples/systemone](https://github.com/oceanbase/powercontext/tree/90355b8e96d68e2932d7980b3e76957f35ea2b44/examples/systemone)
- LoCoMo Jev evaluation notes: [github.com/oceanbase/powercontext/blob/90355b8e96d68e2932d7980b3e76957f35ea2b44/evaluation/memory/locomo/JEV_EVALUATION.md](https://github.com/oceanbase/powercontext/blob/90355b8e96d68e2932d7980b3e76957f35ea2b44/evaluation/memory/locomo/JEV_EVALUATION.md)

## Limits and data handling

With the reranker or example enabled, queries and retrieved memory text are sent to TypeSafe. The README states the LoCoMo Plus Jev scores were supplied by the project owner and their run artifacts are not public. Windows support is experimental. Not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 90355b8e96d6](https://github.com/oceanbase/powercontext/tree/90355b8e96d68e2932d7980b3e76957f35ea2b44). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
