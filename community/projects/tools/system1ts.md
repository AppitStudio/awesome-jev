# system1ts (TypeScript SDK for System One and OpenAI Decisions APIs)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Dependency-light TypeScript client with presets for TypeSafe Jev and OpenAI Decisions, shared adapters, and examples that call `jev({ apiKey, model }).decide(...)`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/3inch-ai/system1ts) |
| Maintainer | [3inch-ai](https://github.com/3inch-ai). Independently curated. |
| Format | TypeScript SDK (MIT) |
| Requirements | Node.js/TypeScript toolchain and a TypeSafe or OpenAI Decisions key for live calls. |
| License | [MIT](https://github.com/3inch-ai/system1ts/blob/dc55f0786d3383da9c807a8ebb114226bcf72108/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/presets.ts`](https://github.com/3inch-ai/system1ts/blob/dc55f0786d3383da9c807a8ebb114226bcf72108/src/presets.ts) at the pinned commit. |

## When to use

- Call System One or Decisions from TypeScript with one client shape.
- Switch between Jev and OpenAI Decisions presets.
- Mismatch: SDK only; bring your own product logic.

## How it works

`src/presets.ts` exports `jev` (and other presets) that configure the System One adapter for TypeSafe endpoints and models such as `jev-1.14.0`. Integration evidence: [`src/presets.ts`](https://github.com/3inch-ai/system1ts/blob/dc55f0786d3383da9c807a8ebb114226bcf72108/src/presets.ts).

## Get started

Install the package per README, set TYPESAFE_API_KEY, and run a decide example.

```sh
git clone https://github.com/3inch-ai/system1ts.git && cd system1ts
export TYPESAFE_API_KEY=...
npm install && npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/3inch-ai/system1ts/blob/dc55f0786d3383da9c807a8ebb114226bcf72108/README.md](https://github.com/3inch-ai/system1ts/blob/dc55f0786d3383da9c807a8ebb114226bcf72108/README.md)

## Limits and data handling

State and questions you pass are sent to the configured System One or Decisions endpoint on your key.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit dc55f0786d33](https://github.com/3inch-ai/system1ts/tree/dc55f0786d3383da9c807a8ebb114226bcf72108). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
