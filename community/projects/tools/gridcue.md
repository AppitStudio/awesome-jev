# GridCue (headless toolkit that turns a plain-language request into a previewed, undoable data-grid view, with Jev resolving the choices)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Intent-to-view compiler for dense data tables: a typed or dictated request ("group by advisor, sort the largest concentration first") is resolved into a typed view plan, validated against the host's declared columns and permissions, previewed and applied through a grid adapter. Jev is the first provider and only picks among closed candidate choices; code compiles and validates the plan, and it never edits records.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JH3lou/GridCue) |
| Maintainer | [JH3lou](https://github.com/JH3lou). Independently curated. |
| Format | npm package `gridcue` (TypeScript; React hooks, server handler, TanStack Table adapter, shadcn registry; MIT) |
| Requirements | Node.js with a TanStack Table or rows-in-memory app; a TypeSafe key on the server for the Jev provider (a mock provider needs none). |
| License | [MIT](https://github.com/JH3lou/GridCue/blob/d3f63b2e07dba3a92273c3fa37d3cce79912e199/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/gridcue/src/server/jev.ts`](https://github.com/JH3lou/GridCue/blob/d3f63b2e07dba3a92273c3fa37d3cce79912e199/packages/gridcue/src/server/jev.ts) at the pinned commit. |

## When to use

- Add a plain-language command bar to a dense table (advisor desktops, ops consoles) without letting a model touch the UI or the data.
- Mismatch: natural-language SQL, row editing or chat over data; GridCue is view-only by design.

## How it works

`packages/gridcue/src/server/jev.ts` builds Choice/Noul questions per request clause with the official TypeSafe SDK (`TypeSafeClient`, SDK logging off, 4 s timeout, one retry), defaulting to `jev-1.13.0` because its confidence bands are tuned against it. The provider runs only in the server entry, so the key stays off the browser; low confidence produces clarification or a no-op. Integration evidence: [`packages/gridcue/src/server/jev.ts`](https://github.com/JH3lou/GridCue/blob/d3f63b2e07dba3a92273c3fa37d3cce79912e199/packages/gridcue/src/server/jev.ts).

## Get started

Try the mock provider in the browser, then mount the server handler with the Jev provider.

```sh
npm install gridcue
# server (Next.js route): createGridCueHandler({ provider: createJevProvider({ apiKey: process.env.JEV_API_KEY }) })
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/JH3lou/GridCue/blob/d3f63b2e07dba3a92273c3fa37d3cce79912e199/README.md](https://github.com/JH3lou/GridCue/blob/d3f63b2e07dba3a92273c3fa37d3cce79912e199/README.md)
- Docs site: [gridcue.dev](https://gridcue.dev)
- npm package: [www.npmjs.com/package/gridcue](https://www.npmjs.com/package/gridcue)

## Limits and data handling

With the Jev provider, the request text and the column labels, aliases and descriptions you declare go to TypeSafe on your key; rows are not required. The mock provider stays in the browser.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit d3f63b2e07db](https://github.com/JH3lou/GridCue/tree/d3f63b2e07dba3a92273c3fa37d3cce79912e199). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
