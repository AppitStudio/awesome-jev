# Scruple

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Semantic-aware linter for enforcing team taste: an OXC parser selects candidate code, rules decide what to ask, and a decision provider — TypeSafe Jev by default (pinned to `jev-1.13.0`), or Cloudflare Clef, local Decider, self-hosted Kev or OpenAI Decisions — classifies each one into diagnostics that fail CI on errors.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NAlexPear/scruple) |
| Product homepage | [scruple.dev](https://scruple.dev) |
| Maintainer | [NAlexPear](https://github.com/NAlexPear). Independently curated. |
| Format | Node CLI and plugins (`@scruple/parser-oxc`, `@scruple/provider-jev` 0.3.4 at review, rule plugins); docs at scruple.dev |
| Requirements | Node.js 22.18+ and a `TYPESAFE_API_KEY` for the Jev provider (other providers need their own credentials or local servers). |
| License | [MIT](https://github.com/NAlexPear/scruple/blob/2fc48be1f99fb17680cf0bd87f643d83539b50db/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Check comment quality or other team conventions that regex linters cannot express.
- Run the same rules against Jev, Clef, Kev or OpenAI Decisions via one `DecisionProvider` interface.
- Mismatch: hosted model usage is billed per run; findings are model classifications, not proofs.

## How it works

Pipeline: source → parser → possible targets → rules → selected candidates → decisions → diagnostics. The Jev adapter lives in [`packages/provider-jev`](https://github.com/NAlexPear/scruple/tree/2fc48be1f99fb17680cf0bd87f643d83539b50db/packages/provider-jev); provider docs: [`apps/docs/providers/jev.md`](https://github.com/NAlexPear/scruple/blob/2fc48be1f99fb17680cf0bd87f643d83539b50db/apps/docs/providers/jev.md). Suppressions and team rules are kept in the repository.

## Get started

Follow the README *Use Scruple* example (comments plugin with the Jev provider):

```sh
pnpm add --save-dev @scruple/cli @scruple/comments @scruple/core \
  @scruple/parser-oxc @scruple/provider-jev
export TYPESAFE_API_KEY=...
# create scruple.config.ts (README example), then run Scruple in CI
```

Each candidate classification is a Jev request billed to your TypeSafe key.

## Examples and demos

- Docs: [scruple.dev](https://scruple.dev) (also as an LLM index and Markdown bundle).
- README *Where Scruple fits* and *Use Scruple with coding agents*.

## Limits and data handling

Selected code snippets go to the configured provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 2fc48be1f99f](https://github.com/NAlexPear/scruple/tree/2fc48be1f99fb17680cf0bd87f643d83539b50db). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
