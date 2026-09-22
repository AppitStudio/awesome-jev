# dsh-jev-decide

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin that registers agent tool `jev_decide`: TypeSafe Jev noul/choice/score over a text `state`, returning calibrated probabilities for routing, triage, and guardrails (no text generation).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nanami-0713/dsh-jev-decide) |
| Maintainer | [nanami-0713](https://github.com/nanami-0713). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package **`dsh-jev-decide` 0.1.1** (ESM plugin; peer `@deepseek-ai/dsh-tools`). |
| Requirements | DeepSeek Harness / DSH tools; `TYPESAFE_API_KEY`, plugin `config.apiKey`, or DSH credential ref `TYPESAFE_AI_API_KEY`. |
| License | [MIT](https://github.com/nanami-0713/dsh-jev-decide/blob/7209540b15c045701f420c89b58a36d31d242f56/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Source and offline payload builders inspected; no DSH runtime or live TypeSafe calls on the review host. Distinct from [dsh-jev](dsh-jev.md) (`jev_ask`), [dsh-jev-verify](dsh-jev-verify.md), and [dsh-jev-prune](dsh-jev-prune.md). |

## When to use

Use it when a **DSH agent** should call a dedicated `jev_decide` tool for typed judgments instead of asking a chat model to invent labels. Prefer [dsh-jev](dsh-jev.md) if you already standardize on `jev_ask`, or [dsh-jev-verify](dsh-jev-verify.md) when you need a bundled live verification benchmark.

## How it works

`lib/index.js` builds a `/v1/systemone` body (`model` default `jev-latest`, `baseUrl` default `https://api.typesafe.ai/v1`), validates choice `options` / score `levels`, and summarizes `answers.decision` plus usage for the agent. Credentials resolve in order: plugin config → `TYPESAFE_API_KEY` → `~/.dsh/.credentials.yaml` ref.

## Get started

```sh
git clone https://github.com/nanami-0713/dsh-jev-decide.git
cd dsh-jev-decide
git checkout 7209540b15c045701f420c89b58a36d31d242f56
npm ci --ignore-scripts
node --input-type=module -e "import { buildPayload } from './lib/index.js'; console.log(JSON.stringify(buildPayload({state:'outage', question:'Is this urgent?', type:'noul'})))"
# Install into DSH per upstream README; set TYPESAFE_API_KEY for live calls
```

Live `jev_decide` sends `state`/questions to TypeSafe and may incur charges. This listing did not run DSH or live TypeSafe.

## Examples and demos

- Offline on the review host: Node import of `buildQuestion` / `buildPayload` / `summarize` succeeded; package has no `npm test` script.
- Upstream README documents DSH marketplace install and credential reuse.

## Limits and data handling

Agent-supplied `state` leaves the host on live calls. Plugin focuses on a single `jev_decide` tool—multi-gateway/retry features live in related community plugins listed upstream. Peer DSH tools version must satisfy `>=0.1.0-rc.6`.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 7209540](https://github.com/nanami-0713/dsh-jev-decide/tree/7209540b15c045701f420c89b58a36d31d242f56): **0.1.1**, MIT. AI-assisted source review of README, LICENSE, `lib/index.js`. Offline payload builder smoke OK; no DSH/TypeSafe live run on the review host.

Related: [dsh-jev](dsh-jev.md), [dsh-jev-verify](dsh-jev-verify.md), [dsh-jev-prune](dsh-jev-prune.md), [askjev](askjev.md).
