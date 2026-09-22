# Auto Mode for Paseo

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Paseo plugin that classifies each Codex turn with TypeSafe Jev (default) or optional local Laya, then starts the turn with the selected model, reasoning effort, work mode, and speed in the same Codex thread.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/obetomuniz/auto-mode-for-paseo) |
| Maintainer | [obetomuniz](https://github.com/obetomuniz). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Paseo plugin (TypeScript; `paseo-plugin.json`) with Node server/client surfaces. |
| Requirements | Paseo **0.8.0+** with plugins; Node.js **24+** (upstream engines); Codex CLI **0.153.4+** logged in; TypeSafe key for Jev (Laya needs a local Python env with Laya 0.3.5). |
| License | [MIT](https://github.com/obetomuniz/auto-mode-for-paseo/blob/d09232d556dba010f49abd1b9575cb9083ce3f18/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline `npm test` on the review host (Node 22 ran the suite); Paseo Desktop install and live Jev/Laya routing not tested. |

## When to use

Use it when Paseo should **pick Codex model/effort/mode per message** with a TypeSafe-first classifier while keeping the chat thread. Prefer [codex-jev-router](codex-jev-router.md) for a standalone local Responses proxy outside Paseo.

## How it works

[`server/jev.ts`](https://github.com/obetomuniz/auto-mode-for-paseo/blob/d09232d556dba010f49abd1b9575cb9083ce3f18/server/jev.ts) posts routing questions to `https://api.typesafe.ai/v1/systemone`. [`server/routing.ts`](https://github.com/obetomuniz/auto-mode-for-paseo/blob/d09232d556dba010f49abd1b9575cb9083ce3f18/server/routing.ts) chooses Jev or Laya from settings (Jev default), then the provider starts a Codex turn with the selected parameters. Permission/plan policy stays in TypeScript.

## Get started

```sh
git clone https://github.com/obetomuniz/auto-mode-for-paseo.git
cd auto-mode-for-paseo
git checkout d09232d556dba010f49abd1b9575cb9083ce3f18
npm ci
npm test
# With Paseo CLI available: paseo plugin install .
```

Configure **Settings → Plugins → Auto Mode for Paseo** (Jev default). Live classification sends prompts/context to TypeSafe (or runs local Laya) and can incur charges. This listing did not install into Paseo Desktop.

## Examples and demos

- Offline on the review host: `npm test` → **50 passed** (Node v22.23.2; upstream engines list ≥24).
- Architecture notes in upstream `ARCHITECTURE.md`.

## Limits and data handling

Laya quality for this routing task is experimental. Oversized Laya context stops the turn. Secrets stay in local settings; legacy settings filenames migrate on save. Not a general multi-agent supervisor.

## Review and maintenance

Reviewed on **2026-09-22** at [commit d09232d](https://github.com/obetomuniz/auto-mode-for-paseo/tree/d09232d556dba010f49abd1b9575cb9083ce3f18): MIT **0.2.0**. AI-assisted source review of README, LICENSE, `server/jev.ts`, and routing/settings. Offline tests **50 passed**. No live TypeSafe spend.

Related: [codex-jev-router](codex-jev-router.md), [codex-jev-preflight](codex-jev-preflight.md), [Jev Model Router](jev-model-router.md).
