# World Cup Conversational Search (evidence-grounded football Q&A over Solr, with Jev as an optional decision provider)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

LangGraph and FastAPI assistant that resolves follow-up questions, plans bounded Solr searches and streams answers with source links over a fictional World Cup dataset (interface in European Portuguese). Admission, context selection and schema routing are typed decisions: OpenAI's decisions endpoint by default, or Jev through OpenRouter's Decisions API with `DECISION_PROVIDER=jev`; there is no silent fallback. Includes a demo video and tests that run without model credentials.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RodrigoCamposRodrigues/world-cup-conversational-search) |
| Maintainer | [RodrigoCamposRodrigues](https://github.com/RodrigoCamposRodrigues). Independently curated. |
| Format | Docker Compose app (Python, React, Solr) |
| Requirements | Docker Compose v2.24+; an OpenAI account for generation; an OpenRouter key for the Jev decision provider. |
| License | [MIT](https://github.com/RodrigoCamposRodrigues/world-cup-conversational-search/blob/716ee8a355e9cb9b03b631056b72bc63d021ef0d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/backend/decisions/providers/jev.py`](https://github.com/RodrigoCamposRodrigues/world-cup-conversational-search/blob/716ee8a355e9cb9b03b631056b72bc63d021ef0d/src/backend/decisions/providers/jev.py) at the pinned commit. |

## When to use

- See how to keep a multi-turn search assistant grounded by routing admission and context choices through typed decisions.
- Mismatch: Jev is an alternative provider; OpenAI decisions is the default and generation always uses OpenAI.

## How it works

`providers/jev.py` posts the decision state to `openrouter.ai/api/alpha/decisions` with `typesafe/jev-1.13`, validates each noul against the expected names and records usage; failures surface as `DecisionFailure`. Integration evidence: [`src/backend/decisions/providers/jev.py`](https://github.com/RodrigoCamposRodrigues/world-cup-conversational-search/blob/716ee8a355e9cb9b03b631056b72bc63d021ef0d/src/backend/decisions/providers/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env   # set DECISION_PROVIDER=jev and OPENROUTER_API_KEY
docker compose build
docker compose up -d solr
docker compose run --rm initialize
docker compose up -d backend web
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Architecture walkthrough: [github.com/RodrigoCamposRodrigues/world-cup-conversational-search/blob/716ee8a355e9cb9b03b631056b72bc63d021ef0d/docs/architecture.md](https://github.com/RodrigoCamposRodrigues/world-cup-conversational-search/blob/716ee8a355e9cb9b03b631056b72bc63d021ef0d/docs/architecture.md)

## Limits and data handling

With the Jev provider, user questions and conversation context are sent to OpenRouter. The public data is fictional; the original proprietary corpus is not included. Model requests cost money. Not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 716ee8a355e9](https://github.com/RodrigoCamposRodrigues/world-cup-conversational-search/tree/716ee8a355e9cb9b03b631056b72bc63d021ef0d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
