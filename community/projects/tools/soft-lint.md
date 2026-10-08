# soft-lint

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin and npm CLI that asks a System One classifier — TypeSafe Jev by default, or Jev / Clef on Cloudflare Workers AI — plain-English yes/no rules about the lines a diff adds (comments that restate code, a getter that writes, swallowed errors) and reports each 'yes' over the rule's cutoff; an incomplete check exits 2, never a silent pass.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/c9r-dev/plugins) |
| Maintainer | [c9r-dev](https://github.com/c9r-dev). Independently curated. |
| Format | Claude Code plugin (`/plugin install soft-lint@c9r`, after-edit hook + rule-writing skill) and npm CLI `soft-lint` (reads a unified diff on stdin) |
| Requirements | Node 24+; `TYPESAFE_API_KEY` (or Cloudflare Workers AI credentials for `cloudflare:typesafe/jev`); a `rules.json` of yes/no questions with cutoffs. |
| License | [MIT](https://github.com/c9r-dev/plugins/blob/05d7283319b268ad5db93a6620dd9def6faa5cd4/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Enforce review habits (no restating comments, no hidden writes, no swallowed errors) on code an agent just wrote.
- Apply a new rule forward only — it judges added lines, never the existing code.
- Mismatch: scores drift by a few hundredths between runs, so rules right at their cutoff can flip.

## How it works

[`plugins/soft-lint/check.ts`](https://github.com/c9r-dev/plugins/blob/05d7283319b268ad5db93a6620dd9def6faa5cd4/plugins/soft-lint/check.ts) splits the diff into hunks and asks one `noul` question per rule; the shared [`shared/classifier.ts`](https://github.com/c9r-dev/plugins/blob/05d7283319b268ad5db93a6620dd9def6faa5cd4/shared/classifier.ts) picks TypeSafe (`typesafe:jev-latest`) or Cloudflare (`cloudflare:typesafe/jev`) from the credentials present and refuses to guess when both are set. The plugin's after-edit hook ([`hooks/hooks.json`](https://github.com/c9r-dev/plugins/blob/05d7283319b268ad5db93a6620dd9def6faa5cd4/plugins/soft-lint/hooks/hooks.json)) runs it on every agent edit.

## Get started

Install the plugin, or add the CLI to a project and pipe a diff in (README *Install* / *Run it*):

```sh
# Claude Code
/plugin marketplace add c9r-dev/plugins
/plugin install soft-lint@c9r

# or as a CLI (Node 24+)
yarn add -D @c9r-dev/soft-lint
git diff -W origin/main...HEAD | soft-lint rules.json
```

Each hunk × rule is a Jev question billed to your TypeSafe (or Cloudflare) account.

## Examples and demos

- Sample rules: [`plugins/soft-lint/rules.json`](https://github.com/c9r-dev/plugins/blob/05d7283319b268ad5db93a6620dd9def6faa5cd4/plugins/soft-lint/rules.json).
- Plugin README: [`plugins/soft-lint/README.md`](https://github.com/c9r-dev/plugins/blob/05d7283319b268ad5db93a6620dd9def6faa5cd4/plugins/soft-lint/README.md).
- npm package: [`@c9r-dev/soft-lint`](https://www.npmjs.com/package/@c9r-dev/soft-lint) (0.1.0).

## Limits and data handling

Added diff lines and the enclosing function context go to TypeSafe or Cloudflare. Exit code 2 means no verdict (offline, timeout, bad rules) and must not be read as a pass. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 05d7283319b2](https://github.com/c9r-dev/plugins/tree/05d7283319b268ad5db93a6620dd9def6faa5cd4). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
