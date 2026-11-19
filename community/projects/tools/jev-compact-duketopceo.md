# jev-compact by duketopceo (context compaction for agent harnesses where Jev scores transcript spans and the rest are tombstoned, restorable on demand)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Retention filter, not a summarizer, for long agent sessions: it splits the transcript into spans, tracks the conversation's moving topic, has Jev score each span for relevance and whether it is load-bearing, keeps the top spans verbatim under a token budget and replaces the rest with tombstones that an MCP `context-restore` server can bring back. Stdlib-only Python with adapters for Claude Code, Codex and OpenCode; a heuristic scorer works offline. The core library behind the separately listed Agent Zero plugin.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/duketopceo/jev-compact) |
| Maintainer | [duketopceo](https://github.com/duketopceo). Independently curated. |
| Format | Python library, CLI and MCP restore server (stdlib only) |
| Requirements | Python 3.11+; `TYPESAFE_API_KEY` for Jev scoring (the heuristic scorer needs no key); one of the supported harnesses for the adapters. |
| License | [MIT](https://github.com/duketopceo/jev-compact/blob/202e478368416fc24f5cae16795b466b25665e55/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_compact/scorer.py`](https://github.com/duketopceo/jev-compact/blob/202e478368416fc24f5cae16795b466b25665e55/src/jev_compact/scorer.py) at the pinned commit. |

## When to use

- Compact long coding-agent sessions without losing exact code, errors and paths.
- Mismatch: Agent Zero users; see the separate a0-plugin-jev-compact listing.

## How it works

`src/jev_compact/scorer.py` sends spans to Jev (`jev-latest`) with two score questions (`relevance_to_current`, `load_bearing`) and falls back to the heuristic scorer without a key; `compact.py` runs the budgeted selection. Integration evidence: [`src/jev_compact/scorer.py`](https://github.com/duketopceo/jev-compact/blob/202e478368416fc24f5cae16795b466b25665e55/src/jev_compact/scorer.py).

## Get started

Install the package, then wire the adapter for your harness and register the restore MCP server.

```sh
git clone https://github.com/duketopceo/jev-compact && cd jev-compact
pip install -e .
# then follow adapters/ for Claude Code, Codex or OpenCode
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/duketopceo/jev-compact/blob/202e478368416fc24f5cae16795b466b25665e55/README.md](https://github.com/duketopceo/jev-compact/blob/202e478368416fc24f5cae16795b466b25665e55/README.md)
- Agent Zero plugin listing: [jevlist.ai/projects/a0-plugin-jev-compact](https://jevlist.ai/projects/a0-plugin-jev-compact)

## Limits and data handling

Transcript spans go to TypeSafe on your key when Jev scoring is on. Retention quality depends on the budget and highlight; not measured here.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 202e47836841](https://github.com/duketopceo/jev-compact/tree/202e478368416fc24f5cae16795b466b25665e55). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
