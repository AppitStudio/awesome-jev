# jev-dom

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

TypeScript research package: TypeSafe Jev operates any web page through its DOM action space (buttons, links, fields)—no WebMCP required. Complements [jev-webmcp-extension](../apps/jev-webmcp-extension.md) and [Jev Ultrafast](jev-ultrafast.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eralabs-ai/jev-dom) |
| Maintainer | [eralabs-ai](https://github.com/eralabs-ai). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Source-only npm package **jev-dom 0.1.0** (install from GitHub pin; Node 22+). Playwright is a peer you supply. |
| Requirements | Node 22+; `TYPESAFE_API_KEY` for live runs. Install via `npm i github:eralabs-ai/jev-dom#<commit>`. |
| License | [Apache-2.0](https://github.com/eralabs-ai/jev-dom/blob/04e84b66742b880f0a9b99a5a8d85b6181127b0b/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, agent/page layout). Package install, Playwright, and live Jev were **not** executed on the review host. Upstream eval tables were not re-run. |

## When to use

Use it when you want Jev to pick DOM targets on ordinary sites that do not ship WebMCP tools. Prefer the WebMCP extension when the origin already exposes WebMCP schemas; prefer [Jev Ultrafast](jev-ultrafast.md) for a fuller Python browser agent.

## How it works

The page snapshot becomes an action space; Jev chooses operations/targets; your Playwright `page` executes via `jev-dom/page/playwright`. Optional confirm callback before shaky or consequential steps. Subpaths: `jev-dom/agent`, `jev-dom/jev`, `jev-dom/webmcp`, `jev-dom/core/*`.

## Get started

```sh
npm i github:eralabs-ai/jev-dom#04e84b66742b880f0a9b99a5a8d85b6181127b0b
# Then from your Playwright page (see upstream README for runRequest example)
```

Pin for review: [commit 04e84b6](https://github.com/eralabs-ai/jev-dom/tree/04e84b66742b880f0a9b99a5a8d85b6181127b0b).

## Examples and demos

- README `runRequest` Playwright fragment.
- Upstream Basketful WebMCP-vs-DOM eval notes (not reproduced here).

## Limits and data handling

Research surface; pin commits. Live Jev receives DOM-derived state. Confirm hooks are caller-owned. This listing did not install or drive a browser.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 04e84b6](https://github.com/eralabs-ai/jev-dom/tree/04e84b66742b880f0a9b99a5a8d85b6181127b0b) (**0.1.0**, Apache-2.0). AI-assisted review of README and LICENSE. No live TypeSafe spend.

Related: [Jev Ultrafast](jev-ultrafast.md), [jev-webmcp-extension](../apps/jev-webmcp-extension.md), [Footwork](footwork.md).
