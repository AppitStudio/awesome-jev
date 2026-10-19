# Jev Skills Retrieval

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding agent extension that retrieves skills per request: Jev scores skill metadata once per turn, and Pi then reads only the selected skills' bodies, with pinned skills and explicit `/skill:name` taking priority.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aimmetal-tech/jev-skills-retrieval) |
| Maintainer | [aimmetal-tech](https://github.com/aimmetal-tech). Independently curated. |
| Format | Pi extension (TypeScript) |
| Requirements | Node.js 22.19+, Pi 1.3.0; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/aimmetal-tech/jev-skills-retrieval/blob/bf5dc48b717020acbac7952ac06097cd394699d0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev-client.ts`](https://github.com/aimmetal-tech/jev-skills-retrieval/blob/bf5dc48b717020acbac7952ac06097cd394699d0/src/jev-client.ts) at the pinned commit. |

## When to use

- Keep a large skill library without loading every skill into context.
- Route skills once per turn and reuse the choice in tool follow-ups.
- Mismatch: Chinese-language docs; Pi only.

## How it works

Each turn the extension sends skill metadata to Jev through `src/jev-client.ts` for scoring, then exposes only the chosen skills to Pi's normal reading flow. Zero hits keep an empty auto list, service errors fall back with a clear message, and missing credentials block the task. Integration evidence: [`src/jev-client.ts`](https://github.com/aimmetal-tech/jev-skills-retrieval/blob/bf5dc48b717020acbac7952ac06097cd394699d0/src/jev-client.ts).

## Get started

From the upstream README: build and load the adapter in Pi, then set the key with `/jev-skill apikey`.

```sh
npm ci && npm run build
pi -e ./dist/pi-adapter.js
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- docs/configuration.md
- benchmark/ (routing diagnostics)

## Limits and data handling

Skill metadata and the request go to TypeSafe each turn.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit bf5dc48b7170](https://github.com/aimmetal-tech/jev-skills-retrieval/tree/bf5dc48b717020acbac7952ac06097cd394699d0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
