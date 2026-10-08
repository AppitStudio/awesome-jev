# jev-router (Covre81)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local Anthropic-compatible gateway for Claude Code (or any Messages-API client): on each new human turn TypeSafe Jev answers one ordinal score, sending simple work to a cheap OpenAI-compatible provider (Ollama Cloud free plan by default, Groq or OpenRouter) and structural work byte-for-byte to Anthropic; tool-result turns reuse the route, Jev failures fall back to the primary, and an `x-jev-route` header plus statusline show each decision.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Covre81/JEV-APP-PC) |
| Maintainer | [Covre81](https://github.com/Covre81). Independently curated. |
| Format | Node service + CLI (`jev-router serve / stats / statusline`) on :8787 |
| Requirements | Node/npm; `TYPESAFE_API_KEY` (or `CLASSIFIER=heuristic` offline), an Anthropic key/subscription and a cheap-provider key. |
| License | [MIT](https://github.com/Covre81/JEV-APP-PC/blob/8811bdee0e8cdc4ccdf96f36ccf9ab742c27a79e/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Stretch a Claude subscription by offloading questions and one-line edits.
- Inspect per-route telemetry with `jev-router stats`.
- Mismatch: cheap free tiers have rate limits; routing quality depends on the score threshold.

## How it works

[`src/classifier/jev-classifier.ts`](https://github.com/Covre81/JEV-APP-PC/blob/8811bdee0e8cdc4ccdf96f36ccf9ab742c27a79e/src/classifier/jev-classifier.ts) calls `/v1/systemone`; the gateway translates simple turns to `/chat/completions` and keeps telemetry in `~/.jev-router/telemetry.db`. Eval script: [`scripts/eval-jev.ts`](https://github.com/Covre81/JEV-APP-PC/blob/8811bdee0e8cdc4ccdf96f36ccf9ab742c27a79e/scripts/eval-jev.ts).

## Get started

Build and run from source (README):

```sh
git clone https://github.com/Covre81/JEV-APP-PC.git && cd JEV-APP-PC
npm ci
# ~/.jev-router/.env: TYPESAFE_API_KEY=... (or CLASSIFIER=heuristic)
npm run build && npm start
# point Claude Code at http://localhost:8787
```

One Jev score per human turn (TypeSafe) plus the chosen provider's usage.

## Examples and demos

- README route table and `x-jev-route` header notes.

## Limits and data handling

Prompt text goes to TypeSafe and the chosen upstream. Repository name is JEV-APP-PC; the package is `jev-router`. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 8811bdee0e8c](https://github.com/Covre81/JEV-APP-PC/tree/8811bdee0e8cdc4ccdf96f36ccf9ab742c27a79e). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
