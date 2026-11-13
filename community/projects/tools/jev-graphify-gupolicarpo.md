# Jev + Graphify by gupolicarpo (MCP server where Graphify clusters your code locally and Jev picks the module, file, memory or skill an agent needs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP server for Claude Code, Codex and other agent hosts: Graphify organises the codebase into clusters with local analysis (no LLM), and Jev picks the module, cluster and file, the agent memory note or the skill that matches a request, so the agent gets a short answer instead of searching and re-reading.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gupolicarpo/jev-graphify) |
| Maintainer | [gupolicarpo](https://github.com/gupolicarpo). Independently curated. |
| Format | MCP server and CLI (Node.js with a pinned Python Graphify environment, MIT; detailed docs in Portuguese) |
| Requirements | Node.js, Python 3 for Graphify, an MCP host, and a TypeSafe key (`TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/gupolicarpo/jev-graphify/blob/134bcc582b7d77ef85082353407399c1ed78769e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/gupolicarpo/jev-graphify/blob/134bcc582b7d77ef85082353407399c1ed78769e/src/jev.mjs) at the pinned commit. |

## When to use

- Cut agent token spend on code search, memory recall or skill selection in a large repository.
- Mismatch: tiny repos where plain grep is already cheap.

## How it works

`src/jev.mjs` posts `choice` questions with a `none` option to `https://api.typesafe.ai/v1/systemone` with `jev-latest`, scrubbing the state first and refusing redirects. The author reports top-3 hits in 22 of 24 Portuguese questions on a ~2,000-file C# project (about $0.003 per query) and 18 of 18 skill picks; these are single small author runs, not a benchmark. Integration evidence: [`src/jev.mjs`](https://github.com/gupolicarpo/jev-graphify/blob/134bcc582b7d77ef85082353407399c1ed78769e/src/jev.mjs).

## Get started

Install the Node and Graphify dependencies, add `.jev-graphify.json` to your project, build the index and connect the MCP server.

```sh
npm ci --ignore-scripts
python3 -m venv .venv-graphify
./.venv-graphify/bin/python -m pip install -r requirements-graphify.lock
node src/cli.mjs update --project /path/to/your-project
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gupolicarpo/jev-graphify/blob/134bcc582b7d77ef85082353407399c1ed78769e/README.md](https://github.com/gupolicarpo/jev-graphify/blob/134bcc582b7d77ef85082353407399c1ed78769e/README.md)
- Measurements and limits (Portuguese): [github.com/gupolicarpo/jev-graphify/blob/134bcc582b7d77ef85082353407399c1ed78769e/docs/COMPATIBILIDADE.md](https://github.com/gupolicarpo/jev-graphify/blob/134bcc582b7d77ef85082353407399c1ed78769e/docs/COMPATIBILIDADE.md)

## Limits and data handling

File paths, symbol names and cluster summaries from your project go to TypeSafe on your key; indexing is local.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 134bcc582b7d](https://github.com/gupolicarpo/jev-graphify/tree/134bcc582b7d77ef85082353407399c1ed78769e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
