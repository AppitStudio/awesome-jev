# Switchboard by Gaurav Lahoti (IT service desk agent where Jev screens each ticket and Gemini reasons only when needed)

[All projects](../README.md) · [Web apps](README.md#web-apps)

A self-service IT triage agent built with Google ADK 2.0: Jev runs the fast checks (is this a real IT request, an injection or abuse attempt, in scope, which of eight intents, does this action need approval), code applies the rules, and Gemini at one of three tiers handles only the steps that need reasoning. Risky actions wait for a human, and every step goes to a masked, append-only audit log.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gauravlahoti/Switchboard) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/gauravlahoti/Switchboard#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build run locally with your own TypeSafe key and Google Cloud (Vertex AI) account. The README says MIT but the repository has no license file, so reuse terms are not formally granted. Synthetic data only. Checked 2026-11-22. |
| Jev evidence | [`app/jev.py`](https://github.com/gauravlahoti/Switchboard/blob/02818d97ce0db63212b0cba68a23e020b12ff5de/app/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [gauravlahoti](https://github.com/gauravlahoti). Independently curated. |
| Format | Python web app (Google ADK + FastAPI) |
| Platform and availability | Local web UI (FastAPI + SSE) on 127.0.0.1:5180; Dockerfile for Cloud Run. |
| Jev's role | System 1: an input guardrail (two attack checks and a scope check in one call), intent understanding (eight questions in one call) and approval decisions; code routes on the probabilities. |
| Requirements | Python with uv, a TypeSafe API key and Google Cloud auth for Vertex AI Gemini (`gcloud auth application-default login`). |
| License | No license file (the README says MIT, but no license text is in the repository) on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- A worked example of a two-speed agent: typed judgments for guardrails and routing, an LLM only where reasoning is needed.
- Mismatch: a production help desk; it uses synthetic data and demo tools.

## How it works

`app/jev.py` calls Jev through the TypeSafe Python SDK (`jev-latest`) for named bundles of questions and records token usage and cost; the questions are in `app/questions.py` and thresholds and routing in `app/nodes.py`. Integration evidence: [`app/jev.py`](https://github.com/gauravlahoti/Switchboard/blob/02818d97ce0db63212b0cba68a23e020b12ff5de/app/jev.py).

## Get started

Copy `.env.example` to `.env`, add your keys, then install and serve.

```sh
git clone https://github.com/gauravlahoti/Switchboard && cd Switchboard
cp .env.example .env   # TYPESAFE_API_KEY, GCP project
make install
make serve   # http://127.0.0.1:5180
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Animated tour: [github.com/gauravlahoti/Switchboard/tree/02818d97ce0db63212b0cba68a23e020b12ff5de/tour](https://github.com/gauravlahoti/Switchboard/tree/02818d97ce0db63212b0cba68a23e020b12ff5de/tour)
- Tour script: [github.com/gauravlahoti/Switchboard/blob/02818d97ce0db63212b0cba68a23e020b12ff5de/docs/tour-script.md](https://github.com/gauravlahoti/Switchboard/blob/02818d97ce0db63212b0cba68a23e020b12ff5de/docs/tour-script.md)

## Limits and data handling

Each request's text is sent to TypeSafe and, when reasoning is needed, to Google Vertex AI. Synthetic data only. No license file: reuse terms are not granted despite the README's MIT note.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 02818d97ce0d](https://github.com/gauravlahoti/Switchboard/tree/02818d97ce0db63212b0cba68a23e020b12ff5de). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
