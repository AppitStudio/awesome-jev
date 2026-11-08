# Laminar TypeScript SDK (OpenTelemetry tracing with TypeSafe Jev SDK instrumentation)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Laminar's TypeScript SDK auto-instruments `@typesafe-ai/sdk` so System One / Jev calls appear as traced spans with usage and answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lmnr-ai/lmnr-ts) |
| Maintainer | [lmnr-ai](https://github.com/lmnr-ai). Independently curated. |
| Format | TypeScript SDK (Apache-2.0) |
| Requirements | Node, `@lmnr-ai/lmnr`, a Laminar project key, and the TypeSafe SDK in your app. |
| License | [Apache-2.0](https://github.com/lmnr-ai/lmnr-ts/blob/15c4977517786bf0054b973eefcd5e10b35755ca/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/lmnr/src/opentelemetry-lib/instrumentation/typesafe/index.ts`](https://github.com/lmnr-ai/lmnr-ts/blob/15c4977517786bf0054b973eefcd5e10b35755ca/packages/lmnr/src/opentelemetry-lib/instrumentation/typesafe/index.ts) at the pinned commit. |

## When to use

- Trace Jev decisions next to LLM calls.
- Inspect usage and answers per request.
- Mismatch: tracing only; needs Laminar.

## How it works

The instrumentation wraps `@typesafe-ai/sdk` and parses the raw `/v1/systemone` body (`model`, `usage`, `answers`) in `utils.ts`; pass the TypeSafe module via `instrumentModules` in `Laminar.initialize`. Integration evidence: [`packages/lmnr/src/opentelemetry-lib/instrumentation/typesafe/index.ts`](https://github.com/lmnr-ai/lmnr-ts/blob/15c4977517786bf0054b973eefcd5e10b35755ca/packages/lmnr/src/opentelemetry-lib/instrumentation/typesafe/index.ts).

## Get started

Install `@lmnr-ai/lmnr`, initialize Laminar with the TypeSafe client module, and run your Jev calls.

```sh
npm install @lmnr-ai/lmnr @typesafe-ai/sdk
export LMNR_PROJECT_API_KEY=... TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/lmnr-ai/lmnr-ts/blob/15c4977517786bf0054b973eefcd5e10b35755ca/README.md](https://github.com/lmnr-ai/lmnr-ts/blob/15c4977517786bf0054b973eefcd5e10b35755ca/README.md)

## Limits and data handling

Jev requests/answers are exported to your Laminar project.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 15c497751778](https://github.com/lmnr-ai/lmnr-ts/tree/15c4977517786bf0054b973eefcd5e10b35755ca). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
