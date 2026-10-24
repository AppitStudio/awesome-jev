# Emc² (desktop email client with Jev sorting)

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Desktop email client for Windows (macOS build from source) with a bundled mail service and encrypted SQLite storage; Jev sorts mail into Important and Other and gives each row a fixed label such as "Needs a reply".

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/collection-of-things/aggregate-mail) |
| Tags | `Open source` · `Free` |
| Product homepage | [Repository README](https://github.com/collection-of-things/aggregate-mail#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free download. Jev sorting uses your own provider key. Checked 2026-10-24. |
| Jev evidence | [`server/sorting.ts`](https://github.com/collection-of-things/aggregate-mail/blob/03de40fd02bdf6ba7db20d21824b6ce9297f10bd/server/sorting.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [collection-of-things](https://github.com/collection-of-things). Independently curated. |
| Format | Desktop app (Electron, React, TypeScript) |
| Platform and availability | Windows installer from GitHub Releases (unsigned); macOS build from source. |
| Jev's role | Classifies each message and rates relevance in one call; sender rules and Teach corrections take priority. |
| Requirements | Windows installer, or Node.js 24+ to build on macOS; a TypeSafe, Vercel AI Gateway or OpenRouter key for Jev sorting. |
| License | [MIT](https://github.com/collection-of-things/aggregate-mail/blob/03de40fd02bdf6ba7db20d21824b6ce9297f10bd/LICENSE) |

## When to use

- Get an Important/Other inbox with fixed labels on Windows.
- Switch between TypeSafe, Vercel and OpenRouter by changing one setting.
- Mismatch: the Windows installer is unsigned.

## How it works

`server/sorting.ts` picks the endpoint from `shared/types.ts` (`https://api.typesafe.ai/v1/systemone`, `jev-latest`, or the Vercel and OpenRouter routes) and asks Jev to choose a label from a closed set. Integration evidence: [`server/sorting.ts`](https://github.com/collection-of-things/aggregate-mail/blob/03de40fd02bdf6ba7db20d21824b6ce9297f10bd/server/sorting.ts).

## Get started

From the upstream README (not run on the review host): download the Windows installer from Releases, or build:

```sh
npm install
npm run package
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/collection-of-things/aggregate-mail/releases](https://github.com/collection-of-things/aggregate-mail/releases)

## Limits and data handling

Message content is sent to the chosen Jev provider for sorting. Mail is stored locally in encrypted SQLite.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 03de40fd02bd](https://github.com/collection-of-things/aggregate-mail/tree/03de40fd02bdf6ba7db20d21824b6ce9297f10bd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
