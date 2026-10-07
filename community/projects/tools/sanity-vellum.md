# Vellum (Sanity Labs)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Sanity Labs experiment that maps Markdown into Sanity documents with a classifier instead of an LLM: code does everything mechanical and TypeSafe Jev answers choice and yes/no questions about which schema field each block fills; hosted playground and npm package `@sanity-labs/vellum`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sanity-labs/vellum) |
| Product homepage | [vellum.sanity.dev](https://vellum.sanity.dev) |
| Maintainer | [Sanity Labs](https://github.com/sanity-labs). Independently curated. |
| Format | Hosted playground (vellum.sanity.dev), self-hostable Vite app, npm package `@sanity-labs/vellum` (0.1.0 at review) with a server request handler |
| Requirements | None for the hosted playground; self-hosting needs Node.js 22.12+, pnpm 12 and `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY`. |
| License | [MIT](https://github.com/sanity-labs/vellum/blob/a1a3ab4b7bc87bf4f16003d34565ce0565e0209c/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Import Markdown posts, docs or landing pages into a Sanity schema without hand-mapping fields.
- Study a classifier-only mapping pipeline whose limits are measured on 72 real-document fixtures.
- Mismatch: upstream calls it an experiment, not a product — mapping is incomplete and the same input can map differently twice.

## How it works

Code splits the Markdown into id-tagged blocks; [`src/engine/jev/jev.ts`](https://github.com/sanity-labs/vellum/blob/a1a3ab4b7bc87bf4f16003d34565ce0565e0209c/src/engine/jev/jev.ts) sends them with questions asked from three directions (which field holds this part, which part supplies this field, and — only on disagreement — whether a pairing is right). Code assembles the document from the answers; edits are diffed so only new blocks are re-asked and existing `_key`s survive. An offline fake ([`fake.ts`](https://github.com/sanity-labs/vellum/blob/a1a3ab4b7bc87bf4f16003d34565ce0565e0209c/src/engine/jev/fake.ts)) backs the tests.

## Get started

Self-host the playground:

```sh
git clone https://github.com/sanity-labs/vellum.git && cd vellum
pnpm install
cp .env.example .env   # add TYPESAFE_API_KEY or OPENROUTER_API_KEY
pnpm dev               # http://localhost:5173
```

Self-hosted runs bill Jev calls to your key; the hosted playground is run by Sanity Labs.

## Examples and demos

- Hosted playground: [vellum.sanity.dev](https://vellum.sanity.dev) (paste Markdown, pick a schema, create a document).
- README *Limitations* (measured mapping accuracy on 72 fixtures, latency by document depth).

## Limits and data handling

Markdown text goes to TypeSafe (or OpenRouter). Images stay as URLs; references, files and custom validators are skipped. Hosted playground checked reachable only; not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit a1a3ab4b7bc8](https://github.com/sanity-labs/vellum/tree/a1a3ab4b7bc87bf4f16003d34565ce0565e0209c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
