# Parallax (arXiv literature search plugin with Jev screening)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

DeepSeek Harness plugin that harvests arXiv metadata into local SQLite and lets the agent build auditable paper sets with keyword recall, set operations and Jev screening and classification, where each paper gets an inclusion probability.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Zilize/parallax-dsh) |
| Maintainer | [Zilize](https://github.com/Zilize). Independently curated. |
| Format | DeepSeek Harness (dsh) plugin (TypeScript) |
| Requirements | DeepSeek Harness with the web UI; Node.js 22.5+; optional Jev API key for AI screening. |
| License | [Apache-2.0](https://github.com/Zilize/parallax-dsh/blob/023ffadd6dea3af30587b89feb6073ffdd142c68/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev-defaults.ts`](https://github.com/Zilize/parallax-dsh/blob/023ffadd6dea3af30587b89feb6073ffdd142c68/src/jev-defaults.ts) at the pinned commit. |

## When to use

- Find all the arXiv papers on a topic rather than a search engine's top results.
- Screen thousands of papers cheaply with a probability per paper.
- Mismatch: rule filters and set operations work without a key; AI screening needs one.

## How it works

Screening criteria become typed questions, and Jev (`jev-1.13.0` at `https://api.typesafe.ai` by default, see `src/jev-defaults.ts`) returns an inclusion probability for each paper, kept at p of 0.5 or more by default; results are cached so a paper is never paid for twice. Integration evidence: [`src/jev-defaults.ts`](https://github.com/Zilize/parallax-dsh/blob/023ffadd6dea3af30587b89feb6073ffdd142c68/src/jev-defaults.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Zilize/parallax-dsh.git
cd parallax-dsh
npm install
npm run build
dsh plugin --profile desktop add .
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Online version: [parallax.ink](https://parallax.ink)
- Development notes: [github.com/Zilize/parallax-dsh/blob/main/docs/development.md](https://github.com/Zilize/parallax-dsh/blob/main/docs/development.md)

## Limits and data handling

Paper titles and abstracts are sent to TypeSafe for screening. Speed comparisons are the author's estimates.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 023ffadd6dea](https://github.com/Zilize/parallax-dsh/tree/023ffadd6dea3af30587b89feb6073ffdd142c68). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
