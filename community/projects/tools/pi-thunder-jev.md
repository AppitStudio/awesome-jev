# pi-thunder-jev

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

`jev_find` for Pi: ask where the code for something lives and TypeSafe Jev ranks the relevant files with best excerpts and line numbers in about a second.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Mandalorian007/pi-thunder-jev) |
| Maintainer | [Mandalorian007](https://github.com/Mandalorian007). Independently curated. |
| Format | Pi extension |
| Requirements | Pi coding agent; TypeSafe key. |
| License | [MIT](https://github.com/Mandalorian007/pi-thunder-jev/blob/4e67b0a0eb1733302cb6acfce53cb0947248d86a/LICENSE) |
| Jev evidence | [`find.ts`](https://github.com/Mandalorian007/pi-thunder-jev/blob/4e67b0a0eb1733302cb6acfce53cb0947248d86a/find.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Replace slow grep-and-read exploration with one ranked lookup.
- Mismatch: savings figures come from the author's Thunder Foundry runs.

## How it works

Candidate files and excerpts are scored by Jev; thresholds stay in code and the tool returns ranked paths with line numbers. (Summarized from the upstream [README](https://github.com/Mandalorian007/pi-thunder-jev/blob/4e67b0a0eb1733302cb6acfce53cb0947248d86a/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the extension in Pi per the README.

## Limits and data handling

Code excerpts go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 4e67b0a0eb17](https://github.com/Mandalorian007/pi-thunder-jev/tree/4e67b0a0eb1733302cb6acfce53cb0947248d86a). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
