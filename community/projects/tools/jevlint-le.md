# JevLint-LE

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

VS Code/Open VSX extension, CLI and MCP server that lint the questions you send to Jev (and OpenAI Decisions) offline.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nolindnaidoo/jevlint-le) |
| Maintainer | [nolindnaidoo](https://github.com/nolindnaidoo). Independently curated. |
| Format | VS Code extension, npm CLI, MCP server |
| Requirements | Node.js for CLI/MCP; optional Jev/OpenAI key only for the model-check command. |
| License | [MIT](https://github.com/nolindnaidoo/jevlint-le/blob/a703d982c76ceb3667634b7d01f92dfc5525531a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Catch badly phrased Jev questions before they ship.
- Mismatch: heuristic rules, not an accuracy guarantee.

## How it works

Parses `/v1/systemone` request shapes and AI SDK `decide()` calls in JSON, JS/TS, Python, Rust and Go and reports question patterns flagged as error-prone, with quick fixes. (Summarized from the upstream [README](https://github.com/nolindnaidoo/jevlint-le/blob/a703d982c76ceb3667634b7d01f92dfc5525531a/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `npx jevlint-le` or install `nolindnaidoo.jevlint-le` in VS Code / Open VSX.

## Limits and data handling

Linting is offline; the optional check command sends the file to the model with your key. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit a703d982c76c](https://github.com/nolindnaidoo/jevlint-le/tree/a703d982c76ceb3667634b7d01f92dfc5525531a). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
