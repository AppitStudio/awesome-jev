# hyalo

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust CLI for Markdown knowledgebases (LLM Wiki pattern, frontmatter queries, links) whose `hyalo-tidy` agent skill can, when you explicitly ask, have TypeSafe Jev suggest missing types and existing folders for selected documents — audit-only suggestions the agent checks against local schemas.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ractive/hyalo) |
| Maintainer | [ractive](https://github.com/ractive). Independently curated. |
| Format | CLI plus agent plugin with the `hyalo-tidy` skill and a small `jev.mjs` helper |
| Requirements | The hyalo CLI. The optional Jev path needs Bun or Node.js and `TYPESAFE_API_KEY`; ordinary tidy calls no model API. |
| License | [MIT](https://github.com/ractive/hyalo/blob/52043d2f80946564811f8504c93f42f77562b1a5/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Classify a batch of inbox notes (type, destination folder) with calibrated suggestions before an agent reorganises your wiki.
- Keep a knowledgebase consistent with explicit schemas while still using a model for judgment calls.
- Mismatch: Jev only runs when you ask for it on selected documents; it is not used for search or ordinary tidy.

## How it works

When you ask tidy to "use Jev" for specific documents and fields, the skill runs the bundled helper (`hyalo init` ships `jev.md` + `jev.mjs` templates) with selected document evidence and approved classification rubrics; Jev returns suggestions with probabilities, and the agent reviews them against local schemas before proposing changes. The scope, setup and preview requirements are in the [Jev workflow reference](https://github.com/ractive/hyalo/blob/52043d2f80946564811f8504c93f42f77562b1a5/plugins/hyalo/skills/hyalo-tidy/references/jev.md).

## Get started

Install the CLI, add the agent plugin, then ask tidy explicitly to use Jev (live TypeSafe calls only on that path):

```sh
brew trust --formula ractive/tap/hyalo   # Homebrew 6+: one-time trust for third-party taps
brew install ractive/tap/hyalo
# in your agent: /hyalo-tidy  →  "Use Jev to suggest missing types and existing folders for these five inbox notes; audit only."
export TYPESAFE_API_KEY=...
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README section on `hyalo-tidy` and the Jev workflow reference.
- `crates/hyalo-cli/tests/e2e/jev_init.rs` end-to-end test of the Jev asset templates.

## Limits and data handling

The Jev path sends selected document evidence and rubrics to TypeSafe; ordinary tidy and all CLI commands stay local. Suggestions are reviewed by the agent and proposed, not applied blindly. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 52043d2f8094](https://github.com/ractive/hyalo/tree/52043d2f80946564811f8504c93f42f77562b1a5). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
