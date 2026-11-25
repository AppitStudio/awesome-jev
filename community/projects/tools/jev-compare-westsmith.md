# jev-compare by Westsmith (local web app that sends the same labelled item to Jev and to Gemini Flash and compares requests, answers, time and cost)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local FastAPI app with a one-call page and batch runs: the same item goes to Jev as typed questions and to Gemini Flash as a prompt with a JSON schema, side by side, with probabilities versus self-reported confidence, latency, billed cost and accuracy. Ships phishing, job-posting and recipe task sets. Distinct from the separately listed sixdjango/jev-compare.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/westsmith-open/jev-compare) |
| Maintainer | [Westsmith](https://github.com/westsmith-open). Independently curated. |
| Format | Python web app (FastAPI, uv) |
| Requirements | uv and an OpenRouter key (runs both models), or a TypeSafe key for direct Jev; a simulated mode works without keys. |
| License | [MIT](https://github.com/westsmith-open/jev-compare/blob/48337f7d2eaa9068c9586811bd145b47c2c4bf68/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_compare/providers.py`](https://github.com/westsmith-open/jev-compare/blob/48337f7d2eaa9068c9586811bd145b47c2c4bf68/jev_compare/providers.py) at the pinned commit. |

## When to use

- Show a team how a decision model differs from a prompted LLM on the same data.
- Mismatch: if you need a rigorous benchmark; task sets are small.

## How it works

`jev_compare/providers.py` calls `https://api.typesafe.ai/v1/systemone` when `TYPESAFE_API_KEY` is set, otherwise OpenRouter's Decisions API; Gemini goes through OpenRouter. Integration evidence: [`jev_compare/providers.py`](https://github.com/westsmith-open/jev-compare/blob/48337f7d2eaa9068c9586811bd145b47c2c4bf68/jev_compare/providers.py).

## Get started

Copy the env file, add a key, then start the server.

```sh
cp .env.example .env   # add OPENROUTER_API_KEY
uv run uvicorn jev_compare.server:app --port 8765
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Task sets: [github.com/westsmith-open/jev-compare/tree/48337f7d2eaa9068c9586811bd145b47c2c4bf68/tasks](https://github.com/westsmith-open/jev-compare/tree/48337f7d2eaa9068c9586811bd145b47c2c4bf68/tasks)

## Limits and data handling

By default items go to OpenRouter (a third-party host); Gemini is a non-TypeSafe model. Simulated-mode numbers are made up and labelled as such. Unofficial, not affiliated with TypeSafe or Google.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 48337f7d2eaa](https://github.com/westsmith-open/jev-compare/tree/48337f7d2eaa9068c9586811bd145b47c2c4bf68). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
