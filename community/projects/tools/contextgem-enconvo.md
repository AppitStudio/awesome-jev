# contextgem-enconvo (Enconvo plugin for ContextGem extraction that routes closed questions to Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Enconvo plugin that wraps ContextGem for aspect-based retrieval and typed concept extraction over text and documents, using the LLM providers you already have in Enconvo. A decision bridge, on by default, sends booleans, labels and ratings to Jev through Enconvo Cloud for calibrated probabilities, falling back to the LLM when Jev is unavailable.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Iteractive-Development/contextgem-enconvo) |
| Maintainer | [Iteractive-Development](https://github.com/Iteractive-Development). Independently curated. |
| Format | Enconvo plugin (TypeScript) with a private Python venv |
| Requirements | Enconvo with a signed-in account (Jev runs on Enconvo Cloud points); `uv` for the managed venv. |
| License | [MIT](https://github.com/Iteractive-Development/contextgem-enconvo/blob/cb93e6d6fb65c90d2059ce1f2a052949dcba3175/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lib/bridge.ts`](https://github.com/Iteractive-Development/contextgem-enconvo/blob/cb93e6d6fb65c90d2059ce1f2a052949dcba3175/src/lib/bridge.ts) at the pinned commit. |

## When to use

- Extract structured fields from documents inside Enconvo with calibrated yes/no and label answers.
- Mismatch: Jev is reached only through Enconvo Cloud, not your own TypeSafe key.

## How it works

`src/lib/bridge.ts` opens a localhost bridge that translates LiteLLM's System One wire format to Enconvo Cloud's Jev gateway (`/typesafe/v1/systemone`, `typesafe/jev-latest`); with `engine: "auto"` closed questions go to Jev and the rest to the chat model. Integration evidence: [`src/lib/bridge.ts`](https://github.com/Iteractive-Development/contextgem-enconvo/blob/cb93e6d6fb65c90d2059ce1f2a052949dcba3175/src/lib/bridge.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install --include=dev
npm run build   # builds into Enconvo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- ContextGem: [contextgem.shcherbak.ai](https://contextgem.shcherbak.ai)

## Limits and data handling

Document text for closed questions is sent to Enconvo Cloud and TypeSafe; usage bills Enconvo points. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit cb93e6d6fb65](https://github.com/Iteractive-Development/contextgem-enconvo/tree/cb93e6d6fb65c90d2059ce1f2a052949dcba3175). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
