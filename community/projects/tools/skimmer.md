# skimmer

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Go CLI that splits pages, files or lists into chunks and asks Jev one yes/no relevance question per chunk, keeping only what helps with your goal to save agent tokens.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dorkitude/skimmer) |
| Maintainer | [dorkitude](https://github.com/dorkitude). Independently curated. |
| Format | Go CLI (Homebrew, apt, `go install`) |
| Requirements | TypeSafe API key. |
| License | [MIT](https://github.com/dorkitude/skimmer/blob/6ede87c0c1d77fcff823a1d2d36051ab120b3eaf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/jev/client.go`](https://github.com/dorkitude/skimmer/blob/6ede87c0c1d77fcff823a1d2d36051ab120b3eaf/internal/jev/client.go) at the pinned commit. |

## When to use

- Cut a long web page, grep output or search result list down before an agent reads it.
- Filter JSON/JSONL lists by a natural-language goal.
- Mismatch: distinct from the already-listed pi-skimmer extension; savings depend on content.

## How it works

Input is cut into ~2,000-character overlapping chunks (or list items); each gets a 'does this help with the goal?' Noul question to Jev, batched and run in parallel, and only chunks above the threshold are returned with their line ranges. Integration evidence: [`internal/jev/client.go`](https://github.com/dorkitude/skimmer/blob/6ede87c0c1d77fcff823a1d2d36051ab120b3eaf/internal/jev/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
brew install dorkitude/tap/skimmer
# or: go install github.com/dorkitude/skimmer@latest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Chunk filter originally from dorkitude's webctl: [github.com/dorkitude/webctl](https://github.com/dorkitude/webctl)

## Limits and data handling

Skimmed text is sent to TypeSafe and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 6ede87c0c1d7](https://github.com/dorkitude/skimmer/tree/6ede87c0c1d77fcff823a1d2d36051ab120b3eaf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
