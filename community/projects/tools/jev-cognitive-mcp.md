# jev-cognitive-mcp (advisory MCP server for coding agents with a deterministic screen first and optional Jev guard, route, rerank and verify)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python MCP server and toolkit for Codex CLI, Claude Code, Cursor and Antigravity. Layer 0 runs free regex screens for destructive commands and secret leaks; optional System 1 (Jev) adds `guard`, `route`, `rerank` and `verify` over typed questions; a five-factor controller decides when to escalate to the host frontier model. All verdicts are advisory.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/17671454333/jev-cognitive-mcp) |
| Maintainer | [17671454333](https://github.com/17671454333). Independently curated. |
| Format | Python package and stdio MCP server |
| Requirements | Python and `pip install -e .`; the Jev layer needs an external JevBridge runtime and key. |
| License | [MIT](https://github.com/17671454333/jev-cognitive-mcp/blob/08bbc97202bbcdd092a71f24de1314415bdec728/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_kit/core.py`](https://github.com/17671454333/jev-cognitive-mcp/blob/08bbc97202bbcdd092a71f24de1314415bdec728/jev_kit/core.py) at the pinned commit. |

## When to use

- Add a cheap pre-screen and optional Jev triage to a coding agent without giving it authority.
- Mismatch: Jev calls go through an external JevBridge that is not in this repo, so Jev behaviour was not reviewed beyond the client code.

## How it works

`jev_kit/core.py` defaults to the `~typesafe/jev-latest` model, applies DLP redaction before egress and wraps responses in typed results; `guard.py`, `router.py`, `reranker.py` and `verifier.py` build the four tools. Integration evidence: [`jev_kit/core.py`](https://github.com/17671454333/jev-cognitive-mcp/blob/08bbc97202bbcdd092a71f24de1314415bdec728/jev_kit/core.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/17671454333/jev-cognitive-mcp.git
cd jev-cognitive-mcp
pip install -e ".[dev]"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the 3+1 architecture and Codex config: [github.com/17671454333/jev-cognitive-mcp/blob/08bbc97202bbcdd092a71f24de1314415bdec728/README.md](https://github.com/17671454333/jev-cognitive-mcp/blob/08bbc97202bbcdd092a71f24de1314415bdec728/README.md)

## Limits and data handling

With `reflex_only=false` text is sent to Jev through your bridge; verdicts are advisory only and not a security boundary. Install and live calls were not run.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 08bbc97202bb](https://github.com/17671454333/jev-cognitive-mcp/tree/08bbc97202bbcdd092a71f24de1314415bdec728). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
