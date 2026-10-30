# dsh-intent-recognition (DeepSeek Harness plugin with a five-layer intent pipeline where Jev scores the candidates)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin for intent recognition: keyword rules first, pgvector retrieval to narrow the intent library to the top 5 to 10, Jev probability scoring (high confidence routes straight away, middle goes to a fine-tuned model, low to an LLM fallback), with a scenario and intent management UI, PostgreSQL storage and an API for other services. It can also generate the Jev question config for a scenario. English and Chinese docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lilixinsniper/dsh-intent-recognition) |
| Maintainer | [lilixinsniper](https://github.com/lilixinsniper). Independently curated. |
| Format | DeepSeek Harness plugin (TypeScript) + PostgreSQL/pgvector |
| Requirements | DeepSeek Harness, PostgreSQL with pgvector (Docker Compose provided), and a Jev endpoint and key configured in the model settings page. |
| License | [MIT](https://github.com/lilixinsniper/dsh-intent-recognition/blob/dce049a1d1638aa16ecff7e2ecaea9d69a6e59e2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/models.ts`](https://github.com/lilixinsniper/dsh-intent-recognition/blob/dce049a1d1638aa16ecff7e2ecaea9d69a6e59e2/src/models.ts) at the pinned commit. |

## When to use

- Route user queries to intents with calibrated confidence and only call larger models for unclear cases.
- Mismatch: needs DeepSeek Harness and a PostgreSQL instance; each layer's models are yours to configure.

## How it works

`models.ts` posts the query and candidate intents in the System One wire format when a Jev model's extra config carries question sets and normalizes the answers map; `jev-draft.ts` drafts score, choice and noul question configs from a scenario. Integration evidence: [`src/models.ts`](https://github.com/lilixinsniper/dsh-intent-recognition/blob/dce049a1d1638aa16ecff7e2ecaea9d69a6e59e2/src/models.ts).

## Get started

From the upstream README (not run on the review host):

```sh
docker compose up -d   # PostgreSQL + pgvector
# install the plugin in DeepSeek Harness, then configure the Jev model (api_style=http) in the plugin UI
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev extra-config generation (systemone wire format): [github.com/lilixinsniper/dsh-intent-recognition/blob/dce049a1d1638aa16ecff7e2ecaea9d69a6e59e2/README.md#jev-extra-config-auto-generation-systemone-wire-format](https://github.com/lilixinsniper/dsh-intent-recognition/blob/dce049a1d1638aa16ecff7e2ecaea9d69a6e59e2/README.md#jev-extra-config-auto-generation-systemone-wire-format)

## Limits and data handling

User queries and candidate intent names are sent to the configured Jev endpoint. Ships a large prebuilt `lib/index.js` bundle alongside `src/`. Not affiliated with TypeSafe or DeepSeek.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit dce049a1d163](https://github.com/lilixinsniper/dsh-intent-recognition/tree/dce049a1d1638aa16ecff7e2ecaea9d69a6e59e2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
