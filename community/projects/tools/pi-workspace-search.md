# Pi Workspace Search (bounded code retrieval with optional Jev classification)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Pi extension that gives the agent bounded workspace search: ripgrep for literal and regex queries, a local zvec index for concepts when present, and Jev to classify which code chunks answer a concept query when local results are not enough, keeping output small for the main model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rodrigojager/pi-workspace-search) |
| Maintainer | [rodrigojager](https://github.com/rodrigojager). Independently curated. |
| Format | Pi extension (TypeScript and Node.js) |
| Requirements | Pi 1.0+ with the TypeSafe classifier in its catalog; Node.js 22+ and npm; a TypeSafe key via Pi's `/login typesafe`; optional zvec. |
| License | [MIT](https://github.com/rodrigojager/pi-workspace-search/blob/aaba286c69689929dce51e14118dc427accd9c6a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/runtime.mjs`](https://github.com/rodrigojager/pi-workspace-search/blob/aaba286c69689929dce51e14118dc427accd9c6a/lib/runtime.mjs) at the pinned commit. |

## When to use

- Cut the code context that reaches your main Pi model.
- Fall back to Jev when local search does not find a concept.
- Mismatch: README is in Portuguese; Jev must be enabled per workspace.

## How it works

`lib/runtime.mjs` sets the Jev defaults (`jev-latest`, a 0.72 threshold, chunk and output limits); chunks are sent to TypeSafe only for workspaces you explicitly enable, and the key stays in Pi's native login. Integration evidence: [`lib/runtime.mjs`](https://github.com/rodrigojager/pi-workspace-search/blob/aaba286c69689929dce51e14118dc427accd9c6a/lib/runtime.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
pi install git:github.com/rodrigojager/pi-workspace-search@v0.1.1
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Portuguese): [github.com/rodrigojager/pi-workspace-search#readme](https://github.com/rodrigojager/pi-workspace-search#readme)

## Limits and data handling

Code excerpts from enabled workspaces are sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit aaba286c6968](https://github.com/rodrigojager/pi-workspace-search/tree/aaba286c69689929dce51e14118dc427accd9c6a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
