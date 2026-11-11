# Enrutador de Contenido (hybrid search CLI with Jev category routing)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Spanish-language Node.js CLI that indexes saved content with BM25, multilingual E5 and RRF, and can ask Jev for the main category with a policy that auto-confirms or sends items to human review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/manuel-arguelles-ai/enrutador-contenido) |
| Maintainer | [manuel-arguelles-ai](https://github.com/manuel-arguelles-ai). Independently curated. |
| Format | Node.js CLI (JavaScript, MIT) |
| Requirements | Node.js 22+, and `TYPESAFE_API_KEY` for the Jev decision engine (the demo runs offline). |
| License | [MIT](https://github.com/manuel-arguelles-ai/enrutador-contenido/blob/034ce1db9e881ab01c5dbc893bd8ce699bd0a275/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision-engine.mjs`](https://github.com/manuel-arguelles-ai/enrutador-contenido/blob/034ce1db9e881ab01c5dbc893bd8ce699bd0a275/src/decision-engine.mjs) at the pinned commit. |

## When to use

- Route saved content to categories with an auditable confidence policy.
- Mismatch: docs are in Spanish; small project.

## How it works

`src/decision-engine.mjs` posts to `{base_url}/v1/systemone` using `config/decision-engine.json`; the policy confirms automatically above a threshold or flags the item for review. OpenClaw and Claude Code integrations call the same engine. Integration evidence: [`src/decision-engine.mjs`](https://github.com/manuel-arguelles-ai/enrutador-contenido/blob/034ce1db9e881ab01c5dbc893bd8ce699bd0a275/src/decision-engine.mjs).

## Get started

Run the offline demo first, then add a key to try Jev routing.

```sh
git clone https://github.com/manuel-arguelles-ai/enrutador-contenido.git && cd enrutador-contenido
npm ci && npm run demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/manuel-arguelles-ai/enrutador-contenido/blob/034ce1db9e881ab01c5dbc893bd8ce699bd0a275/README.md](https://github.com/manuel-arguelles-ai/enrutador-contenido/blob/034ce1db9e881ab01c5dbc893bd8ce699bd0a275/README.md)

## Limits and data handling

Content text goes to TypeSafe on your key when the decision engine runs; the search index stays local.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 034ce1db9e88](https://github.com/manuel-arguelles-ai/enrutador-contenido/tree/034ce1db9e881ab01c5dbc893bd8ce699bd0a275). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
