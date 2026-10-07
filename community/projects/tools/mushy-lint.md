# mushy-lint

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Semantic code linter that extracts complete constructs with tree-sitter, asks Jev (TypeSafe or OpenRouter) narrow yes/no questions about them, and reports the raw probability of yes with the source evidence — for conventions that depend on meaning rather than syntax.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/napisani/mushy-lint) |
| Maintainer | [napisani](https://github.com/napisani). Independently curated. |
| Format | Bun-built CLI binary from source (not published to npm); YAML rule configuration |
| Requirements | Bun 1.3+ and Git to build; `TYPESAFE_API_KEY` (native, e.g. `jev-latest`) or an OpenRouter key (`typesafe/jev-1.13`). |
| License | [MIT](https://github.com/napisani/mushy-lint/blob/6b3485765f38922b7ae4ef92e9ad8428ba3997c7/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Check that comments explain why, that function names match responsibilities, or that failures are handled, across a TypeScript codebase.
- Write rules that separate where to look (target), eligibility (condition) and the semantic question.
- Mismatch: TS/TSX grammar today; raw probabilities need thresholds you choose.

## How it works

Rules declare a tree-sitter target, a condition and a question; [`src/jev.ts`](https://github.com/napisani/mushy-lint/blob/6b3485765f38922b7ae4ef92e9ad8428ba3997c7/src/jev.ts) sends each captured construct to Jev and the report shows the probability and evidence location. The README's *Rule examples and their limits* section documents each example rule.

## Get started

Build the CLI from source:

```sh
git clone https://github.com/napisani/mushy-lint.git && cd mushy-lint
bun install --frozen-lockfile
bun run build:bin
./dist/mushy-lint --help
```

Each captured construct checked is a Jev request billed to your key.

## Examples and demos

- README *Complete configuration example* and *Rule examples and their limits*.
- README *Configuration reference* (targets, conditions, sections, rules).

## Limits and data handling

Captured source constructs are sent to TypeSafe or OpenRouter. Not published to npm (source build). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 6b3485765f38](https://github.com/napisani/mushy-lint/tree/6b3485765f38922b7ae4ef92e9ad8428ba3997c7). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
