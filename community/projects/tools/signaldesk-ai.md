# SignalDesk AI by Usama Saeed (compare Jev, an LLM and Azure CLU on customer feedback, then export reviewed product briefs)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Self-hosted dashboard that classifies customer feedback into six labels (bug, feature request, billing, onboarding, praise, other) with TypeSafe Jev, an OpenAI-compatible LLM or Azure conversational language understanding, side by side. Import a CSV, compare each provider's predictions and confidence against reviewer labels, review disagreements and failures, and export approved findings as a product brief. Independent provider workers share rate limits through Redis, and optional per-call prices give cost estimates. A demo mode uses simulated responses on synthetic feedback.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ranausama420/signaldesk-ai) |
| Maintainer | [Ranausama420](https://github.com/Ranausama420). Independently curated. |
| Format | FastAPI + React app with PostgreSQL and Redis via Docker Compose (no license file) |
| Requirements | Docker; `TYPESAFE_API_KEY` (model defaults to `jev-latest`), LLM and/or Azure CLU credentials for live comparisons, and an operator token. Demo mode needs no keys. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`backend/providers.py`](https://github.com/Ranausama420/signaldesk-ai/blob/3303e336da213a1ccecba5185c7bb0ba51911cc8/backend/providers.py) at the pinned commit. |

## When to use

- Measure how Jev compares with an LLM and Azure CLU on your own labelled feedback before choosing one.
- Mismatch: a hosted feedback tool; it is a single-workspace self-hosted app.

## How it works

`backend/providers.py` posts each message as a six-option choice to `https://api.typesafe.ai/v1/systemone` with your key, and the Jev worker stores the label and confidence next to the LLM and Azure results for the same message. Integration evidence: [`backend/providers.py`](https://github.com/Ranausama420/signaldesk-ai/blob/3303e336da213a1ccecba5185c7bb0ba51911cc8/backend/providers.py).

## Get started

Start the stack with Docker Compose and load the sample; set `SIGNALDESK_DEMO=0` and provider keys for live runs.

```sh
git clone https://github.com/Ranausama420/signaldesk-ai
cd signaldesk-ai
cp .env.example .env
docker compose build app
docker compose up -d --wait   # http://127.0.0.1:8009/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Ranausama420/signaldesk-ai/blob/3303e336da213a1ccecba5185c7bb0ba51911cc8/README.md](https://github.com/Ranausama420/signaldesk-ai/blob/3303e336da213a1ccecba5185c7bb0ba51911cc8/README.md)

## Limits and data handling

Feedback text is sent to every provider you configure. The dashboard screenshot shows simulated results, not measured accuracy. Single operator token; the README advises TLS and backups for shared deployments. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 3303e336da21](https://github.com/Ranausama420/signaldesk-ai/tree/3303e336da213a1ccecba5185c7bb0ba51911cc8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
