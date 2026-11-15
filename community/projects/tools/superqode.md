# SuperQode (coding-agent harness layer whose SystemOne harness uses Jev for tool gates, tool routing, decision packs and rubric grading)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Harness layer for coding agents (CLI, terminal UI and a macOS app) that discovers, runs, evaluates and optimizes agent harnesses over ACP, A2A, MCP and UHP. Its SystemOne harness connects TypeSafe Jev as a typed decision service: Jev shadows tool-permission gates, recommends tools during deferred discovery, can trim which tool schemas reach the coding model (shadow first, then enforce), runs reviewed Choice/Score/Noul question packs, and grades rubric results. The coding model still writes the code. Version 2.31.17 adds OpenAI and Google decision models as alternative providers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SuperagenticAI/superqode) |
| Maintainer | [SuperagenticAI](https://github.com/SuperagenticAI). Independently curated. |
| Format | Python CLI/TUI (uv tool) and macOS app (Apache-2.0) |
| Requirements | Python 3.13 with uv (or the macOS 14+ Apple Silicon app), your usual coding-model provider, and `TYPESAFE_API_KEY` for live Jev calls. |
| License | [Apache-2.0](https://github.com/SuperagenticAI/superqode/blob/8620f128bd51e51d226290de6e9516aabf9c9dae/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/SuperagenticAI/status/2121881773697040789)). |
| Jev evidence | [`src/superqode/systemone/providers.py`](https://github.com/SuperagenticAI/superqode/blob/8620f128bd51e51d226290de6e9516aabf9c9dae/src/superqode/systemone/providers.py) at the pinned commit. |

## When to use

- Add Jev tool gates, tool routing or typed decision packs to an existing coding-agent workflow.
- Mismatch: a coding model itself; Jev only makes the typed decisions around it.

## How it works

`src/superqode/systemone/providers.py` and `live.py` call `https://api.typesafe.ai/v1/systemone` with the key from `TYPESAFE_API_KEY`; packs are validated and redacted before the call and answers are bound to typed outputs under a confidence policy. Without a key, Jev is skipped and the normal permission policy and lexical tool search continue. Integration evidence: [`src/superqode/systemone/providers.py`](https://github.com/SuperagenticAI/superqode/blob/8620f128bd51e51d226290de6e9516aabf9c9dae/src/superqode/systemone/providers.py).

## Get started

Install with uv, export your key, and start the SystemOne harness (or turn on tool routing in shadow mode).

```sh
uv tool install --python 3.13 superqode
export TYPESAFE_API_KEY=...
superqode --harness systemone
# or: SUPERQODE_TOOL_ROUTING=shadow superqode
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- SystemOne docs: [github.com/SuperagenticAI/superqode/blob/8620f128bd51e51d226290de6e9516aabf9c9dae/docs/advanced/systemone.md](https://github.com/SuperagenticAI/superqode/blob/8620f128bd51e51d226290de6e9516aabf9c9dae/docs/advanced/systemone.md)
- Jev tool routing: [github.com/SuperagenticAI/superqode/blob/8620f128bd51e51d226290de6e9516aabf9c9dae/docs/advanced/jev-tool-routing.md](https://github.com/SuperagenticAI/superqode/blob/8620f128bd51e51d226290de6e9516aabf9c9dae/docs/advanced/jev-tool-routing.md)
- Maker's X post (with demo video): [x.com/SuperagenticAI/status/2121881773697040789](https://x.com/SuperagenticAI/status/2121881773697040789)

## Limits and data handling

With Jev enabled, redacted pack state, requests and tool descriptions are sent to TypeSafe on your key; coding runs go to your configured provider. The maker also runs a hosted tool-routing service (jev.superqode.dev) that uses its own service token; it is optional and not needed for local use.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 8620f128bd51](https://github.com/SuperagenticAI/superqode/tree/8620f128bd51e51d226290de6e9516aabf9c9dae). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
