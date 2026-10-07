# painpoints

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI, MCP server and native viewer that score every source file on layering, complexity, data-access cost, failure handling, UI cost and trust-boundary risk with a System One model (TypeSafe Jev or Cloudflare Clef), then hand coding agents a ranked, self-explaining technical-debt report.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/prodBirdy/painpoints) |
| Maintainer | [prodBirdy](https://github.com/prodBirdy). Independently curated. |
| Format | Rust binary via `cargo install --git` (CLI, MCP server, native viewer) |
| Requirements | Rust toolchain; `TYPESAFE_API_KEY` (Jev, default when set) or `CLOUDFLARE_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID` (Clef). |
| License | [MIT](https://github.com/prodBirdy/painpoints/blob/8dddb65d9089d428254ecf5e466e50800cfba243/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Rank technical debt across a codebase before a refactor and give an agent the worst files first.
- Detect specific bad decisions such as raw errors sent to clients, with the evidence for each.
- Mismatch: scores are model judgments over file text; review before acting.

## How it works

[`src/systemone.rs`](https://github.com/prodBirdy/painpoints/blob/8dddb65d9089d428254ecf5e466e50800cfba243/src/systemone.rs) sends each file's state with typed questions to the configured provider; [`src/decisions.rs`](https://github.com/prodBirdy/painpoints/blob/8dddb65d9089d428254ecf5e466e50800cfba243/src/decisions.rs) defines the detectors. An optional larger confirm model re-answers unsure questions. Saved results record the question set, model and exact state per file.

## Get started

Install and configure a provider:

```sh
cargo install --git https://github.com/prodBirdy/painpoints
export TYPESAFE_API_KEY=...      # or CLOUDFLARE_API_TOKEN + CLOUDFLARE_ACCOUNT_ID
painpoints --help
```

Each file analysed is a request billed to your TypeSafe or Cloudflare account.

## Examples and demos

- README *What it scores* and *Bad decisions* tables.
- README *For agents* and *Agent rules* sections.

## Limits and data handling

Source file contents are sent to TypeSafe or Cloudflare. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 8dddb65d9089](https://github.com/prodBirdy/painpoints/tree/8dddb65d9089d428254ecf5e466e50800cfba243). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
