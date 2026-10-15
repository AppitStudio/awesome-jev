# TraceRoot

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open-source agent tracing and improvement platform that auto-instruments TypeSafe Jev SDK calls as decision spans (model version, questions, answers, probabilities, cost) and uses Jev in its detection worker.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/traceroot-ai/traceroot) |
| Maintainer | [traceroot-ai](https://github.com/traceroot-ai). Independently curated. |
| Format | Self-hostable platform (TypeScript/Python) with SDKs; hosted service also offered |
| Requirements | Docker for self-hosting; `@traceroot-ai/traceroot` 0.5.0+ and Node.js 20+ for the Jev instrumentation; TypeSafe key for Jev-backed detection. |
| License | [Apache-2.0 (except `ee/` directories)](https://github.com/traceroot-ai/traceroot/blob/b1cc53b94952ef5195f26aa69a7dfd33b6fea152/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/xinwei_97/status/2110501481929670961)). |
| Jev evidence | [`frontend/worker/src/detection/typesafe-client.ts`](https://github.com/traceroot-ai/traceroot/blob/b1cc53b94952ef5195f26aa69a7dfd33b6fea152/frontend/worker/src/detection/typesafe-client.ts) at the pinned commit. |

## When to use

- Trace production agents that call Jev and inspect each decision with its probabilities and cost.
- Turn production failures into signals and offline evals for a coding agent to act on.
- Mismatch: a broad observability platform; Jev is one integration and one detector backend. Directories named `ee` are under a separate enterprise license.

## How it works

Passing the TypeSafe SDK to `TraceRoot.initialize({ instrumentModules: { typeSafe } })` records every `systemOne` call as a decision span. Separately, the detection worker's minimal System One client sends typed questions to Jev and treats missing or out-of-range answers as errors rather than findings. Integration evidence: [`frontend/worker/src/detection/typesafe-client.ts`](https://github.com/traceroot-ai/traceroot/blob/b1cc53b94952ef5195f26aa69a7dfd33b6fea152/frontend/worker/src/detection/typesafe-client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install @traceroot-ai/traceroot @typesafe-ai/sdk
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev integration guide: `docs/integrations/typesafe.mdx`.
- Project site: [traceroot.ai](https://traceroot.ai)

## Limits and data handling

Traced inputs and outputs are stored in your TraceRoot deployment (or TraceRoot's hosted service, whose pricing was not reviewed); detections send trace content to TypeSafe on the configured key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit b1cc53b94952](https://github.com/traceroot-ai/traceroot/tree/b1cc53b94952ef5195f26aa69a7dfd33b6fea152). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
