# Jevbox by Extend (self-hosted, permission-aware document library searched by Jev through folder trees, with cited chat answers)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Full-stack document library from Extend: upload files, browse them in a Finder-style UI (grid, list, columns, gallery), share with organization members under SpiceDB permissions, and ask source-grounded questions with page and section citations. Search has no keyword or embedding fallback: a decision model does hierarchical beam search through categories, documents and sections, then scores each source passage for usefulness. The decision model can be TypeSafe Jev, Cloudflare Clef or OpenAI Decisions; Extend's API parses PDFs, Office files and images.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/extend-hq/jevbox) |
| Maintainer | [extend-hq](https://github.com/extend-hq). Independently curated. |
| Format | Self-hosted web app (TypeScript, Node, PostgreSQL, SpiceDB) |
| Requirements | Node 24.6+, pnpm and Docker Compose (PostgreSQL and SpiceDB), a decision-model key (TypeSafe, Cloudflare or OpenAI), chat model keys, and an Extend API key for parsing non-text files; S3 and SMTP for production. |
| License | [MIT](https://github.com/extend-hq/jevbox/blob/3213d7b6524037664f91f2fdfa38284580fd9b29/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/jev.ts`](https://github.com/extend-hq/jevbox/blob/3213d7b6524037664f91f2fdfa38284580fd9b29/server/jev.ts) at the pinned commit. |

## When to use

- Host a team document library where search walks your folder structure with typed decisions instead of embeddings.
- Mismatch: a lightweight local search tool; it is a multi-service app with accounts, permissions and storage.

## How it works

`server/jev.ts` sends `jev-latest` decision requests to `https://api.typesafe.ai/v1/systemone` (or Cloudflare's Clef or OpenAI Decisions) for the folder-tree search and passage scoring used by search and chat. Integration evidence: [`server/jev.ts`](https://github.com/extend-hq/jevbox/blob/3213d7b6524037664f91f2fdfa38284580fd9b29/server/jev.ts).

## Get started

Install, create the local env, start PostgreSQL and SpiceDB, run the dev server, then add keys under Settings → Connections.

```sh
git clone https://github.com/extend-hq/jevbox && cd jevbox
pnpm install && pnpm setup:local
pnpm services:up && pnpm dev   # http://localhost:4310
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/extend-hq/jevbox/blob/3213d7b6524037664f91f2fdfa38284580fd9b29/README.md](https://github.com/extend-hq/jevbox/blob/3213d7b6524037664f91f2fdfa38284580fd9b29/README.md)
- Deployment guide: [github.com/extend-hq/jevbox/blob/3213d7b6524037664f91f2fdfa38284580fd9b29/docs/deployment.md](https://github.com/extend-hq/jevbox/blob/3213d7b6524037664f91f2fdfa38284580fd9b29/docs/deployment.md)

## Limits and data handling

Document text and structure go to the chosen decision and chat providers, and files other than plain text go to Extend's parsing API (a separate commercial service; its pricing was not reviewed). Keys are stored encrypted on the server. Bundled UI kits carry their own licenses in `licenses/`.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 3213d7b65240](https://github.com/extend-hq/jevbox/tree/3213d7b6524037664f91f2fdfa38284580fd9b29). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
