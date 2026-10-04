# ldraw-nova

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Agent tooling that turns a model idea into an LDraw LEGO model; part and example-model search is re-ranked by TypeSafe Jev through jev-rerank (AGPL-3.0).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/anteloc/ldraw-nova) |
| Maintainer | [anteloc](https://github.com/anteloc). Independently curated. |
| Format | Dockerized web app and agent tooling (requires sibling `ldraw-nova-docker` repo) |
| Requirements | Git and Docker; clone `ldraw-nova` and `ldraw-nova-docker` at the same tag. Set `TYPESAFE_API_KEY` in the web app Settings for Jev reranking; agent LLM credentials per upstream README. |
| License | [AGPL-3.0](https://github.com/anteloc/ldraw-nova/blob/5919d2289e023eeacc2ffc03cbe750e447a024dd/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Generate LEGO-style models from a prompt, with exportable LDraw source and glTF.
- See a worked example of Jev reranking inside a larger agent pipeline.
- Mismatch: without a TypeSafe key the Jev reranker is skipped and agents use full-text search.

## How it works

Agents plan and write generator scripts; their part- and model-search tools call [jev-rerank](https://github.com/anteloc/jev-rerank) (same author), which uses Jev to re-rank semantic search hits. Generation and building are handled by the agent LLM and code, not Jev.

## Get started

Clone both repos at the same tag, then build and start with Docker Compose:

```sh
git clone --branch v0.6.0 https://github.com/anteloc/ldraw-nova.git
git clone --branch v0.6.0 https://github.com/anteloc/ldraw-nova-docker.git
# follow upstream README, then:
docker compose build
docker compose up -d
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Upstream [demo video](https://youtu.be/YDjjxGqWpgU) and `examples/` plans/generator scripts.

## Limits and data handling

Reranking sends search text to TypeSafe; agent runs also use a separate LLM provider with its own charges. AGPL-3.0 applies to network use of modified versions.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 5919d2289e02](https://github.com/anteloc/ldraw-nova/tree/5919d2289e023eeacc2ffc03cbe750e447a024dd). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
