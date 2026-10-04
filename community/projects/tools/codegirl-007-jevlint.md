# Jevlint (codegirl-007)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go linter that checks code against plain-language team rules: Tree-sitter extracts code units and TypeSafe Jev judges whether each passes (distinct from huntedman/JevLint and the jev-lint projects).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/codegirl-007/jevlint) |
| Maintainer | [codegirl-007](https://github.com/codegirl-007). Independently curated. |
| Format | CLI linter with starter config, doctor command, and rule-pack plugins |
| Requirements | Go toolchain (`go install`) or a release binary; `TYPESAFE_API_KEY` from console.typesafe.ai for live checks. |
| License | [MIT](https://github.com/codegirl-007/jevlint/blob/73a7a94ab08a4e314709d68c2863687a4646f29b/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Enforce conventions that regex/AST linters cannot express (naming intent, layering, review taste) as plain-language rules in CI or pre-commit.
- Share rule packs across repositories with `jevlint plugin init`.
- Mismatch: purely syntactic rules are cheaper in a conventional linter.

## How it works

Jevlint parses source with Tree-sitter, extracts code units, and asks Jev a constrained question per unit and rule; code aggregates the answers into lint results. Jev returns a constrained choice, not a free-form explanation.

## Get started

Install the CLI, write a starter config, verify credentials, then lint (live Jev calls):

```sh
go install github.com/codegirl-007/jevlint/cmd/jevlint@latest
jevlint init
export TYPESAFE_API_KEY=...   # from console.typesafe.ai
jevlint doctor
jevlint check .
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Upstream README: config format, rule-pack plugins, and an evals file (`jevlint-evals.json`).

## Limits and data handling

Each checked unit sends code text to TypeSafe and may incur charges; scope runs to changed files to bound cost. Results are model judgments, not proofs.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 73a7a94ab08a](https://github.com/codegirl-007/jevlint/tree/73a7a94ab08a4e314709d68c2863687a4646f29b). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
