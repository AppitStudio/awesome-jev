# ReadyCode Reader

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

MCP and browser Reader: retrieve PDF/DOCX/XLSX passages locally, then TypeSafe Jev checks relevance, sufficiency, conflicts, and spreadsheet plan fit before cited answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ReadycodeAI/readycode-reader) |
| Maintainer | [ReadycodeAI](https://github.com/ReadycodeAI). Independently curated. |
| Format | Node.js · MCP (`@readycode/reader`) + browser demo (Apache-2.0) |
| Requirements | Node.js; OpenRouter key for Jev checks (BYOK). |
| License | [Apache-2.0](https://github.com/ReadycodeAI/readycode-reader/blob/de29e115526aea64336e3ea33880f6c27898cf14/LICENSE). TypeSafe/provider usage may incur charges. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live paths not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/ReadycodeAI/readycode-reader.git
cd readycode-reader
git checkout de29e115526aea64336e3ea33880f6c27898cf14
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.
- Product: [https://readycode.ai/reader](https://readycode.ai/reader)

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit de29e115526a](https://github.com/ReadycodeAI/readycode-reader/tree/de29e115526aea64336e3ea33880f6c27898cf14). AI-assisted README and license inspection; install/live paths not executed.
