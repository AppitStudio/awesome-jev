# Jev LLM Quality Tester

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Prototype dashboard and FastAPI service that scores LLM-generated answers against explicit criteria with a Jev/TypeSafe structured-scoring adapter, SQLite history and a no-key deterministic demo mode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aydinozcekic-maker/jev-llm-quality-tester) |
| Maintainer | [aydinozcekic-maker](https://github.com/aydinozcekic-maker). Independently curated. |
| Format | Python FastAPI app + browser dashboard (Docker optional) |
| Requirements | Python; `TYPESAFE_API_KEY` for Jev scoring; optional OpenAI key to generate answers. |
| License | [MIT](https://github.com/aydinozcekic-maker/jev-llm-quality-tester/blob/7f213a2f9940898350d255cbebe33f3645a802c8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/core.py`](https://github.com/aydinozcekic-maker/jev-llm-quality-tester/blob/7f213a2f9940898350d255cbebe33f3645a802c8/app/core.py) at the pinned commit. |

## When to use

- Rubric-score a batch of LLM answers and keep the history for comparison.
- Start from a small, tested FastAPI reference for calling Jev Score questions.
- Mismatch: prototype; demo-mode scores are lexical heuristics and Jev scores are model judgments, not verified truth.

## How it works

`app/core.py` reads `TYPESAFE_API_KEY`, posts rubric questions to `JEV_API_URL` (default `https://api.typesafe.ai/v1/systemone`) and stores the typed scores in SQLite; without a key the demo scorer runs offline. Integration evidence: [`app/core.py`](https://github.com/aydinozcekic-maker/jev-llm-quality-tester/blob/7f213a2f9940898350d255cbebe33f3645a802c8/app/core.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/aydinozcekic-maker/jev-llm-quality-tester.git && cd jev-llm-quality-tester
python -m pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- REST API reference and scoring notes in the README.

## Limits and data handling

Questions and answers being scored go to TypeSafe (and OpenAI if enabled) on your keys; history stays in local SQLite.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 7f213a2f9940](https://github.com/aydinozcekic-maker/jev-llm-quality-tester/tree/7f213a2f9940898350d255cbebe33f3645a802c8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
