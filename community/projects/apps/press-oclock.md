# Press O'Clock (agentic RAG assistant for journalists that screens incoming press-release emails with Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Full-stack assistant that collects press releases sent by email and lets journalists query them in natural language with source links back to each email; before a mail is stored or indexed, Jev screens it as a triage step, while answers, extraction and embeddings use OpenAI and pgvector.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alvillalta/press-oclock) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/alvillalta/press-oclock#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (MIT, based on the Full Stack FastAPI Template); OpenAI and TypeSafe usage on your keys plus hosting. Checked 2026-11-14. |
| Jev evidence | [`backend/app/integrations/typesafe_client.py`](https://github.com/alvillalta/press-oclock/blob/c7f7ba8e6ea36247bfffe0dfe77ef2bc4d779591/backend/app/integrations/typesafe_client.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [alvillalta](https://github.com/alvillalta). Independently curated. |
| Format | Self-hosted web app (FastAPI + React, Docker Compose; MIT) |
| Platform and availability | Self-hosted web app (Docker Compose); no hosted instance verified |
| Jev's role | Jev screens each incoming press-release email before it is stored and indexed. |
| Requirements | Docker Compose, PostgreSQL with pgvector (included), an OpenAI key, a TypeSafe key, and an email webhook source. |
| License | [MIT](https://github.com/alvillalta/press-oclock/blob/c7f7ba8e6ea36247bfffe0dfe77ef2bc4d779591/LICENSE) |

## When to use

- Keep a searchable, sourced archive of press releases arriving by email.
- Mismatch: if you cannot send email contents to OpenAI and TypeSafe.

## How it works

`backend/app/integrations/typesafe_client.py` uses `langchain-typesafe`'s `TypeSafeClassifier` with `jev-1.14.0`, a 15-second timeout and up to 3 attempts; `MailTriageService` sends a body bounded to 5,000 characters. If the classifier fails, triage fails open and ingestion continues. Integration evidence: [`backend/app/integrations/typesafe_client.py`](https://github.com/alvillalta/press-oclock/blob/c7f7ba8e6ea36247bfffe0dfe77ef2bc4d779591/backend/app/integrations/typesafe_client.py).

## Get started

Copy the environment file, fill in the keys and start the stack with Docker Compose, as the README describes.

```sh
git clone https://github.com/alvillalta/press-oclock && cd press-oclock
cp .env-example .env   # add OPENAI and TYPESAFE keys
docker compose up --build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/alvillalta/press-oclock/blob/c7f7ba8e6ea36247bfffe0dfe77ef2bc4d779591/README.md](https://github.com/alvillalta/press-oclock/blob/c7f7ba8e6ea36247bfffe0dfe77ef2bc4d779591/README.md)
- Deployment: [github.com/alvillalta/press-oclock/blob/c7f7ba8e6ea36247bfffe0dfe77ef2bc4d779591/deployment.md](https://github.com/alvillalta/press-oclock/blob/c7f7ba8e6ea36247bfffe0dfe77ef2bc4d779591/deployment.md)

## Limits and data handling

Incoming email text goes to TypeSafe (triage) and OpenAI (chat, extraction, embeddings) on your keys; data is stored in your own database.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit c7f7ba8e6ea3](https://github.com/alvillalta/press-oclock/tree/c7f7ba8e6ea36247bfffe0dfe77ef2bc4d779591). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
