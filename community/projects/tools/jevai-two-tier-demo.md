# JevAI by Jamel de la Fuente (Flask demo where Jev triages each request and Claude is called only when language is needed)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

A small Flask app for a two-tier design: Jev, via `langchain-typesafe`, sorts each customer message (easy or tricky, which department) and only easy ones reach Claude for a reply; an agent route uses a Jev guardrail to classify each tool call as safe or risky. Companion to the author's essay "Most AI work is a decision, not an essay".

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/superjammy/JevExperiment) |
| Maintainer | [superjammy](https://github.com/superjammy). Independently curated. |
| Format | Python Flask demo |
| Requirements | Python; TypeSafe and Anthropic API keys. |
| License | [MIT](https://github.com/superjammy/JevExperiment/blob/0bd1a2948c89c9abaab1fef9ee9aa0d678604a37/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app.py`](https://github.com/superjammy/JevExperiment/blob/0bd1a2948c89c9abaab1fef9ee9aa0d678604a37/app.py) at the pinned commit. |

## When to use

- Show a team the decide-first, generate-second pattern in a few files.
- Mismatch: RAG, skills and harness levels from the essay are not implemented.

## How it works

`app.py` uses `TypeSafeClassifier` and `AutoModeMiddleware` from `langchain-typesafe` for triage and tool-call gating, with Claude through LangChain. Integration evidence: [`app.py`](https://github.com/superjammy/JevExperiment/blob/0bd1a2948c89c9abaab1fef9ee9aa0d678604a37/app.py).

## Get started

Install requirements, set keys in `.env`, run.

```sh
git clone https://github.com/superjammy/JevExperiment.git && cd JevExperiment
pip install -r requirements.txt
cp .env.example .env   # TYPESAFE_API_KEY, ANTHROPIC_API_KEY
python app.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Essay: [www.linkedin.com/pulse/most-ai-work-decision-essay-jamel-de-la-fuente-gwjhe/](https://www.linkedin.com/pulse/most-ai-work-decision-essay-jamel-de-la-fuente-gwjhe/)
- README: [github.com/superjammy/JevExperiment/blob/0bd1a2948c89c9abaab1fef9ee9aa0d678604a37/README.md](https://github.com/superjammy/JevExperiment/blob/0bd1a2948c89c9abaab1fef9ee9aa0d678604a37/README.md)

## Limits and data handling

Messages are sent to TypeSafe and Anthropic. Demo only.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 0bd1a2948c89](https://github.com/superjammy/JevExperiment/tree/0bd1a2948c89c9abaab1fef9ee9aa0d678604a37). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
