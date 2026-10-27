# agemem (project memory for coding agents, with Jev screening notes)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental memory for coding projects: a readable Markdown memory bank, screened SQLite notes and cited source excerpts, exposed to Codex, Cursor or Claude Code over MCP; decision models screen, classify and select memories, with Jev as the default and local QSIV or ollaya models as options.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/illescasDaniel/agemem) |
| Maintainer | [illescasDaniel](https://github.com/illescasDaniel). Independently curated. |
| Format | Python CLI and MCP server |
| Requirements | Git and uv; a TypeSafe API key for the default Jev decider (or a local GPU/ollaya model). |
| License | [MIT](https://github.com/illescasDaniel/agemem/blob/2c04887fd8eb31252ed525a26e3c1e3a9897a51a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`agemem/deciders.py`](https://github.com/illescasDaniel/agemem/blob/2c04887fd8eb31252ed525a26e3c1e3a9897a51a/agemem/deciders.py) at the pinned commit. |

## When to use

- Give coding agents durable, cited project memory.
- Mismatch: 0.1.0 not yet published to PyPI; use the source-testing guide.

## How it works

`agemem/deciders.py` uses the TypeSafe Python SDK with Choice and Noul questions to screen notes and select memories for recall. Integration evidence: [`agemem/deciders.py`](https://github.com/illescasDaniel/agemem/blob/2c04887fd8eb31252ed525a26e3c1e3a9897a51a/agemem/deciders.py).

## Get started

From the upstream README (not run on the review host):

```sh
uvx --python 3.12 agemem@0.1.0 project init   # planned release; see docs/MANUAL_TESTING.md for source testing
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Manual testing guide: [github.com/illescasDaniel/agemem/blob/main/docs/MANUAL_TESTING.md](https://github.com/illescasDaniel/agemem/blob/main/docs/MANUAL_TESTING.md)
- README: [github.com/illescasDaniel/agemem#readme](https://github.com/illescasDaniel/agemem#readme)

## Limits and data handling

With hosted Jev, selected memory and source context go to TypeSafe during screening and recall; file filters are best-effort.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 2c04887fd8eb](https://github.com/illescasDaniel/agemem/tree/2c04887fd8eb31252ed525a26e3c1e3a9897a51a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
