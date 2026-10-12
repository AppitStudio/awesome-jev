# DeciLabel

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that classifies Issues and pull requests with a typed Decisions API (TypeSafe Jev, OpenRouter, or OpenAI Decisions) and adds only labels supported by the evidence—never removing or creating labels.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/EvanProgramming/decilabel) |
| Maintainer | [EvanProgramming](https://github.com/EvanProgramming). Independently curated. |
| Format | TypeScript · GitHub Action (Node 24) |
| Requirements | GitHub Actions; provider credentials depending on backend (`TYPESAFE_API_KEY` for direct Jev). |
| License | [MIT](https://github.com/EvanProgramming/decilabel/blob/a1bbdd8b60d35ecdc82c99345e1141d41fc77f50/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Auto-label triage on busy repos where you already have a fixed label set.
- Mismatch: Will not invent labels or re-label existing ones away.

## How it works

On issue/PR events it builds a state from title/body, asks the configured decision model which allowed labels fit, and applies additions only. Jev/Decisions client: [`src/decisions.ts`](https://github.com/EvanProgramming/decilabel/blob/a1bbdd8b60d35ecdc82c99345e1141d41fc77f50/src/decisions.ts).

## Get started

From the upstream README (not run on the review host):

```sh
Uses: EvanProgramming/decilabel@main
# configure secrets and label allow-list per upstream README
```

## Limits and data handling

Issue/PR text goes to the chosen provider; TypeSafe usage is billed when Jev is selected. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit a1bbdd8b60d3](https://github.com/EvanProgramming/decilabel/tree/a1bbdd8b60d35ecdc82c99345e1141d41fc77f50). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
