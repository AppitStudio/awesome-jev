# jev-map

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Maps each Python function to the tests that run it for coding agents; optional TypeSafe Jev scores candidate links that static analysis misses, checked against real test runs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/krishhgg/jev-map) |
| Product homepage | [jev-map.vercel.app](https://jev-map.vercel.app) |
| Maintainer | [krishhgg](https://github.com/krishhgg). Independently curated. |
| Format | CLI and MCP server |
| Requirements | Python; `pip install "jev-map @ git+https://github.com/krishhgg/jev-map"` (add `[mcp]` for the server); `TYPESAFE_API_KEY` only for `--jev`. |
| License | [MIT](https://github.com/krishhgg/jev-map/blob/99ca63b56f7d7b741706e18896922d5a49afc1e0/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give coding agents the tests to run after changing a function.
- Fill gaps in static call analysis with bounded Jev link scoring.
- Mismatch: the static map works without Jev.

## How it works

jev-map builds a function-to-test map by reading code (without running it). With `--jev`, keyword search proposes candidate tests and Jev scores which are real links; upstream validated yeses against real test runs (81–87% precision reported by the maintainer).

## Get started

Install and build the map, then query it:

```sh
pip install "jev-map @ git+https://github.com/krishhgg/jev-map"
jev-map --repo /path/to/repo refresh
jev-map --repo /path/to/repo related-tests 'src/pkg/core.py::normalize'
# optional: refresh --jev --max-calls 20
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- [Live demo](https://jev-map.vercel.app) on Flask.

## Limits and data handling

`--jev` sends function and test snippets to TypeSafe; use `--max-calls` to bound spend.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 99ca63b56f7d](https://github.com/krishhgg/jev-map/tree/99ca63b56f7d7b741706e18896922d5a49afc1e0). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
