# grev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

"Thinking coreutils": Unix filters (`grev`, `isv`, `tagv`, `rank`, `sortv`, `pickv`) that ask TypeSafe Jev typed questions, so output is always your input with labels or scores only as explicit columns.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aurorainfra/grev) |
| Maintainer | [aurorainfra](https://github.com/aurorainfra). Independently curated. |
| Format | CLI tools (Go install, packages, or `make install`) |
| Requirements | `go install github.com/aurorainfra/grev/cmd/...@latest` or a package; a TypeSafe key via `grev-settings key set` or `TYPESAFE_API_KEY` (OpenRouter also supported). |
| License | [Apache-2.0](https://github.com/aurorainfra/grev/blob/ec7c32a13ce0fac6b792edd9af77278f37447fdf/LICENSE-APACHE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Search logs or commit history by meaning in a shell pipeline.
- Add a semantic pre-commit guard that exits non-zero on a yes.
- Mismatch: exact patterns are cheaper and deterministic with grep.

## How it works

Each tool sends lines with a typed question to Jev and uses calibrated probabilities to filter, label, rank, or sort; the original lines are emitted unchanged. Config precedence is flags > environment > config file, and `grev-settings spend` reports spend ([README](https://github.com/aurorainfra/grev/blob/ec7c32a13ce0fac6b792edd9af77278f37447fdf/README.md)).

## Get started

Install, store a key, and filter by meaning (live Jev calls):

```sh
go install github.com/aurorainfra/grev/cmd/...@latest
grev-settings key set
grev 'is a vegan meal' examples/menu.txt
git diff --cached | isv 'adds a secret or credential' && echo 'refusing to commit'
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README examples: log search, commit guard, `tagv` routing, `rank` urgency, semantic bisect and edit.

## Limits and data handling

Input lines go to TypeSafe (or OpenRouter) and are billed per input token; the README quotes per-file cost estimates from the maintainer. Answers are probabilistic.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit ec7c32a13ce0](https://github.com/aurorainfra/grev/tree/ec7c32a13ce0fac6b792edd9af77278f37447fdf). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
