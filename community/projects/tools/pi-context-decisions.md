# pi-context-decisions

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension that uses decision models (TypeSafe Jev, OpenRouter decision models, OpenAI Luna) to filter which skill advertisements enter context for each prompt.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/championswimmer/pi-context-decisions) |
| Maintainer | [championswimmer](https://github.com/championswimmer). Independently curated. |
| Format | Pi extension (npm `pi-context-decisions`) |
| Requirements | Pi 1.1.0+, Node 22.18+; TypeSafe, OpenRouter or OpenAI key. |
| License | [MIT](https://github.com/championswimmer/pi-context-decisions/blob/9b1796c04f9fdefce756e571e58b7c1bd3aec859/LICENSE) |
| Jev evidence | [`src/core/backends/typesafe.ts`](https://github.com/championswimmer/pi-context-decisions/blob/9b1796c04f9fdefce756e571e58b7c1bd3aec859/src/core/backends/typesafe.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Trim skill clutter from Pi's context on each prompt.
- Mismatch: pre-alpha; tool/MCP filtering not implemented; no backend selected by default.

## How it works

In `before_agent_start`, bounded task and skill metadata go to the selected decision backend, which keeps or drops each skill advertisement. (Summarized from the upstream [README](https://github.com/championswimmer/pi-context-decisions/blob/9b1796c04f9fdefce756e571e58b7c1bd3aec859/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `pi install npm:pi-context-decisions` and pick a backend in its settings.

## Limits and data handling

Bounded task/skill metadata goes to the selected provider once opted in. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 9b1796c04f9f](https://github.com/championswimmer/pi-context-decisions/tree/9b1796c04f9fdefce756e571e58b7c1bd3aec859). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
