# System One Playground by dasultras (web playground that asks Choice, Noul and Score questions and compares Jev with local System One models)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local web playground for asking atomic questions and seeing probability distributions, confidence, margin, entropy and a traffic-light verdict. It compares up to three models per run, including hosted TypeSafe Jev and System One models served by Ollama or vLLM, shows the raw request, averages option order to reduce position bias, keeps history with JSON and CSV export, and includes an evaluation script reporting Brier, NLL, ECE and risk-coverage on synthetic items.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dasultras/systemone-playground) |
| Maintainer | [dasultras](https://github.com/dasultras). Independently curated. |
| Format | Next.js web app (TypeScript) with Docker Compose image and an evaluation script |
| Requirements | Docker or Node.js; a `TYPESAFE_API_KEY` for hosted Jev (Ollama or vLLM for local models). |
| License | [MIT](https://github.com/dasultras/systemone-playground/blob/bffb0d02a30bc6be16bc043c0876adf0ce523f7c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/backend.ts`](https://github.com/dasultras/systemone-playground/blob/bffb0d02a30bc6be16bc043c0876adf0ce523f7c/lib/backend.ts) at the pinned commit. |

## When to use

- Compare how Jev and local System One models answer the same typed question, and inspect calibration before wiring one into code.
- Mismatch: the README says to use hosted TypeSafe with synthetic data only, and the evaluation set is synthetic.

## How it works

`lib/backend.ts` builds a `TypeSafeClient` from `@typesafe-ai/sdk` for the hosted `api.typesafe.ai` backend (daily request budget via `TYPESAFE_DAILY_REQUESTS`, default 200) and `/v1/systemone` clients for Ollama and vLLM. Integration evidence: [`lib/backend.ts`](https://github.com/dasultras/systemone-playground/blob/bffb0d02a30bc6be16bc043c0876adf0ce523f7c/lib/backend.ts).

## Get started

From the upstream README (not run on the review host):

```sh
docker compose up   # http://localhost:3000
# or: npm ci && npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with features, quick start and environment variables: [github.com/dasultras/systemone-playground#readme](https://github.com/dasultras/systemone-playground#readme)

## Limits and data handling

Hosted runs send your question and state to TypeSafe on your key (the README says synthetic data only; TypeSafe is hosted in the US). Local models stay on your machine. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit bffb0d02a30b](https://github.com/dasultras/systemone-playground/tree/bffb0d02a30bc6be16bc043c0876adf0ce523f7c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
