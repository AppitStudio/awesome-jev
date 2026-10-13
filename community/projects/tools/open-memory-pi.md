# Open Memory (pi)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first SQLite memory for Pi agents with hybrid retrieval and a hard token budget; an optional TypeSafe Jev judge decides which sentences are worth remembering.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/codersdfs/open-memory) |
| Maintainer | [codersdfs](https://github.com/codersdfs). Independently curated. |
| Format | Pi package + HTTP/MCP server |
| Requirements | Node.js (node:sqlite); optional TypeSafe key. |
| License | [MIT](https://github.com/codersdfs/open-memory/blob/5ceda369b26e4368b0f49334cc0e02caeed7622f/LICENSE) |
| Jev evidence | [`src/core/judgment/judge.ts`](https://github.com/codersdfs/open-memory/blob/5ceda369b26e4368b0f49334cc0e02caeed7622f/src/core/judgment/judge.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Give Pi durable memory without Docker while keeping retrieval within a token budget.
- Mismatch: beta; Jev judge is optional.

## How it works

Candidate sentences pass heuristics, then one Jev `noul` per sentence estimates future usefulness; the probability sets importance and decay. (Summarized from the upstream [README](https://github.com/codersdfs/open-memory/blob/5ceda369b26e4368b0f49334cc0e02caeed7622f/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the package per the README and add the key file to enable the judge.

## Limits and data handling

Judged sentences go to TypeSafe when enabled. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 5ceda369b26e](https://github.com/codersdfs/open-memory/tree/5ceda369b26e4368b0f49334cc0e02caeed7622f). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
