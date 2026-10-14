# jevcrawl

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

MCP server and CLI that crawls websites for AI agents, using Jev to pick which links to follow and which passages answer the agent's question.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RayenMlayeh/jevcrawl) |
| Maintainer | [RayenMlayeh](https://github.com/RayenMlayeh). Independently curated. |
| Format | Python CLI and MCP server (PyPI `jevcrawl`) |
| Requirements | Python 3.11+ (or `uvx`), TypeSafe API key. |
| License | [Apache-2.0](https://github.com/RayenMlayeh/jevcrawl/blob/d8b7828ff7eee3ab77076ff74e6b5a1c332041c1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevcrawl/models.py`](https://github.com/RayenMlayeh/jevcrawl/blob/d8b7828ff7eee3ab77076ff74e6b5a1c332041c1/jevcrawl/models.py) at the pinned commit. |

## When to use

- Give a coding or research agent a crawler that returns only the passages that answer its question.
- Cut LLM reading cost on documentation sites by letting a decision model filter pages first.
- Mismatch: benchmark and cost figures are the author's; not reproduced here.

## How it works

For each page, jevcrawl asks Jev typed questions about candidate links and passages; the crawler follows the top-scored links and returns the selected passages to the agent through MCP or the CLI. Integration evidence: [`jevcrawl/models.py`](https://github.com/RayenMlayeh/jevcrawl/blob/d8b7828ff7eee3ab77076ff74e6b5a1c332041c1/jevcrawl/models.py).

## Get started

From the upstream README (not run on the review host):

```sh
claude mcp add jevcrawl -e TYPESAFE_API_KEY=<your key> -- uvx jevcrawl
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmarks section in the upstream README (WebWalkerQA comparison, author-reported).

## Limits and data handling

Crawled page text is sent to TypeSafe for each decision and billed to your key; crawl targets are fetched from your machine.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit d8b7828ff7ee](https://github.com/RayenMlayeh/jevcrawl/tree/d8b7828ff7eee3ab77076ff74e6b5a1c332041c1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
