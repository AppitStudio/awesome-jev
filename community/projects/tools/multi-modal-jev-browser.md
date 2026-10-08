# multi-modal-jev-browser

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Browser agent (CLI `mmjb`, Python library and 13-tool MCP server) where a decision model picks each step — Jev via OpenRouter reading the element list, or Clef reading a numbered screenshot — and a vision LLM takes over only when the decision model is unsure, claims nothing can move, or the page stops changing; writes are off by default.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/foklepoint/multi-modal-jev-browser) |
| Maintainer | [foklepoint](https://github.com/foklepoint). Independently curated. |
| Format | Python package with `mmjb` CLI, `Agent` library and `mmjb-mcp` MCP server (via `uvx`) |
| Requirements | Python 3.12+ / uv; an OpenRouter key for Jev (`MMJB_DECIDER=jev`) or Cloudflare credentials for Clef; a LiteLLM model key for the fallback (default DeepSeek v4.1 Flash); Playwright Chromium. |
| License | [MIT](https://github.com/foklepoint/multi-modal-jev-browser/blob/5ae47374985ac0f5aec8ee2d64ffe2d8790b4121/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Fill forms and click through flows at a fraction of an LLM-per-step cost.
- Give Claude Code, opencode, Cursor or Codex a browser through MCP.
- Mismatch: Jev mode reads the element list only, so unlabeled icons need Clef or the LLM.

## How it works

[`src/mmjb/deciders.py`](https://github.com/foklepoint/multi-modal-jev-browser/blob/5ae47374985ac0f5aec8ee2d64ffe2d8790b4121/src/mmjb/deciders.py) implements the Jev (OpenRouter `typesafe/jev-1.13`), Clef and LLM deciders; each step sends the numbered screenshot or element list, page text, your facts and recent effects, and the decider returns operation, target and done/no-move probabilities. Destructive verbs are refused unless the goal names them, and page text is treated as data.

## Get started

Run the MCP server straight from GitHub and check the setup (README *Quick start*):

```sh
uvx --from git+https://github.com/foklepoint/multi-modal-jev-browser mmjb-mcp
uvx --from git+https://github.com/foklepoint/multi-modal-jev-browser mmjb doctor
```

Each step is one decider call (OpenRouter or Cloudflare) plus any LLM fallback, billed by those providers.

## Examples and demos

- Compare deciders: [`examples/compare_deciders.py`](https://github.com/foklepoint/multi-modal-jev-browser/blob/5ae47374985ac0f5aec8ee2d64ffe2d8790b4121/examples/compare_deciders.py).
- README *Results*: per-step cost/time tables and reproduction commands (author-measured).

## Limits and data handling

Page content, element lists and (for Clef/LLM) screenshots go to the configured providers. Benchmark numbers are the author's. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 5ae47374985a](https://github.com/foklepoint/multi-modal-jev-browser/tree/5ae47374985ac0f5aec8ee2d64ffe2d8790b4121). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
