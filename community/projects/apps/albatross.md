# Albatross

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Terminal-first coding harness (bring your own model, key or MCP server) with an experimental Jev Mode that puts TypeSafe's decision model before the main LLM.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/morganlinton/Albatross) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/morganlinton/Albatross#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-15. |
| Jev evidence | [`src/jev.rs`](https://github.com/morganlinton/Albatross/blob/e458e4277f463a4688f127ea6ea61f5a344b64b8/src/jev.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [morganlinton](https://github.com/morganlinton). Independently curated. |
| Format | Terminal coding agent (Rust) |
| Platform and availability | macOS / Linux terminal (Homebrew or source) |
| Jev's role | Optional pre-LLM decision layer for supported questions. |
| Requirements | OpenAI/OpenRouter key or local model; `TYPESAFE_API_KEY` for Jev Mode. |
| License | [MIT](https://github.com/morganlinton/Albatross/blob/e458e4277f463a4688f127ea6ea61f5a344b64b8/LICENSE) |

## When to use

- Run a terminal coding agent with local or hosted models.
- Try Jev Mode in shadow (`/jev shadow`) before enabling direct answers (`/jev on`).
- Mismatch: Jev Mode is experimental and off by default.

## How it works

In Jev Mode supported questions about supplied errors can get a fixed direct answer from Jev; explanations, coding, tools and uncertain cases fall back to the normal agent loop. Integration evidence: [`src/jev.rs`](https://github.com/morganlinton/Albatross/blob/e458e4277f463a4688f127ea6ea61f5a344b64b8/src/jev.rs).

## Get started

From the upstream README (not run on the review host):

```sh
brew install morganlinton/tap/albatross
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev Mode design: `docs/JEV_HARNESS.md`.

## Limits and data handling

With Jev Mode on, prompts are sent to TypeSafe and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit e458e4277f46](https://github.com/morganlinton/Albatross/tree/e458e4277f463a4688f127ea6ea61f5a344b64b8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
