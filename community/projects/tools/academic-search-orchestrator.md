# academic-search-orchestrator (Jev-based scholarly provider selection with dedupe and rank fusion)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Scaffold package that uses TypeSafe Jev to pick academic search providers, then runs independent scholarly searches, identity-aware deduplication, RRF ranking and citation-provenance structures for Academic Harness / academic-search consumers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/raktim-mondol/academic-search-orchestrator) |
| Maintainer | [raktim-mondol](https://github.com/raktim-mondol). Independently curated. |
| Format | JavaScript package (MIT) |
| Requirements | Node.js, academic provider credentials as needed, and `TYPESAFE_API_KEY` for classifyWithJev. |
| License | [MIT](https://github.com/raktim-mondol/academic-search-orchestrator/blob/00a430bbbf23fffd6e22b897a93bb23fe81aa656/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/route.js`](https://github.com/raktim-mondol/academic-search-orchestrator/blob/00a430bbbf23fffd6e22b897a93bb23fe81aa656/src/route.js) at the pinned commit. |

## When to use

- Route a research query across many scholarly providers.
- Keep provider choice typed and confidence-gated.
- Mismatch: scaffold with documentation toward Academic Harness; not a full UI.

## How it works

`src/route.js` `classifyWithJev` imports `@typesafe-ai/sdk` and asks Jev which providers are eligible above a confidence floor. Integration evidence: [`src/route.js`](https://github.com/raktim-mondol/academic-search-orchestrator/blob/00a430bbbf23fffd6e22b897a93bb23fe81aa656/src/route.js).

## Get started

Clone the scaffold and wire `TYPESAFE_API_KEY` plus provider keys per the README.

```sh
git clone https://github.com/raktim-mondol/academic-search-orchestrator.git
export TYPESAFE_API_KEY=...
# see README / Academic Harness docs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/raktim-mondol/academic-search-orchestrator/blob/00a430bbbf23fffd6e22b897a93bb23fe81aa656/README.md](https://github.com/raktim-mondol/academic-search-orchestrator/blob/00a430bbbf23fffd6e22b897a93bb23fe81aa656/README.md)

## Limits and data handling

Query text is sent to TypeSafe for provider selection; provider APIs receive their own requests.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 00a430bbbf23](https://github.com/raktim-mondol/academic-search-orchestrator/tree/00a430bbbf23fffd6e22b897a93bb23fe81aa656). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
