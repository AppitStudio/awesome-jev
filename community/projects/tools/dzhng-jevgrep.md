# jevgrep (dzhng)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Find code by asking what it does—Jev judges relevance across folders, files, and declarations.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dzhng/jevgrep) |
| Maintainer | [dzhng](https://github.com/dzhng). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package `@dzhng/jevgrep` (bin `jg`); TypeScript monorepo. |
| Requirements | Node.js 22+; macOS or Linux; provider key for Vercel AI Gateway, TypeSafe, or OpenRouter. |
| License | [MIT](https://github.com/dzhng/jevgrep/blob/762028fa076d2d823235d74e5687bea5d070e4c5/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when a coding agent needs a starting place in an unfamiliar repo. Prefer classical grep when you already know the symbol name.

## How it works

CLI walks the tree and asks Jev which folders/files/declarations match the question; stdout returns leads and excerpts for the agent to implement. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
npm install -g @dzhng/jevgrep
jg auth
jg skill
jg \"How are telemetry events recorded and sent?\" ./my-project
```

Pin revision `762028fa076d2d823235d74e5687bea5d070e4c5` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Sends repository text chunks to the chosen provider. Skill install is separate from the CLI. Live retrieval not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 762028f](https://github.com/dzhng/jevgrep/tree/762028fa076d2d823235d74e5687bea5d070e4c5). AI-assisted README and LICENSE inspection; install/live paths not executed.
