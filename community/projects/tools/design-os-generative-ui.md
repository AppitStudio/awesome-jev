# DESIGN:OS Generative UI

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Streaming generative-UI runtime for agent webviews whose engine includes a TypeSafe Jev adapter (with a Laya-MLX path) for its decision cascade.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jangtrinh/design-os-generative-ui) |
| Maintainer | [jangtrinh](https://github.com/jangtrinh). Independently curated. |
| Format | Agent plugin + TypeScript library |
| Requirements | Node.js; `TYPESAFE_API_KEY` for the Jev adapter. |
| License | [MIT](https://github.com/jangtrinh/design-os-generative-ui/blob/3de9c88b90100ec3aa5ae3bd8571e19c06d9a865/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/engine/jev-adapter.ts`](https://github.com/jangtrinh/design-os-generative-ui/blob/3de9c88b90100ec3aa5ae3bd8571e19c06d9a865/src/engine/jev-adapter.ts) at the pinned commit. |

## When to use

- Render streaming interactive HTML widgets in agent hosts without flicker.
- Mismatch: Jev is one adapter in the routing cascade; most of the runtime is UI rendering.

## How it works

The composer first asks a local Laya-MLX model; when its confidence is below the threshold (and local-only mode is off) it escalates to the Jev adapter, which posts typed System One requests to `api.typesafe.ai/v1/systemone`. DOM diffing and sanitizing are done in code. Integration evidence: [`src/engine/jev-adapter.ts`](https://github.com/jangtrinh/design-os-generative-ui/blob/3de9c88b90100ec3aa5ae3bd8571e19c06d9a865/src/engine/jev-adapter.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jangtrinh/design-os-generative-ui.git
cd design-os-generative-ui
npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Playground: `playground/`.
- Privacy notes: `PRIVACY.md`.

## Limits and data handling

Upstream performance claims (e.g. sub-50 ms) are not verified here. Jev requests send content to TypeSafe.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 3de9c88b9010](https://github.com/jangtrinh/design-os-generative-ui/tree/3de9c88b90100ec3aa5ae3bd8571e19c06d9a865). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
