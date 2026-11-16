# BrowserHelm (macOS MCP gateway for BrowserOS Neo that compacts browser context and can delegate bounded navigation to Jev)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Native macOS companion for an installed BrowserOS Neo: Claude Desktop, Codex or another MCP client talks to BrowserHelm's stdio MCP server, Neo performs the browser actions, and BrowserHelm controls how much browser context comes back. `browserhelm_navigate` can observe links, ask Jev (or another configured decision provider) to choose, recheck and follow the link and verify a phrase before returning, avoiding planner round trips; `browserhelm_execute` runs one bounded read-only plan. Optional local or OpenRouter vision grounds visual targets, and proven routes can be reused without a model call. The maker publishes its own small benchmarks and says broad savings remain unproven.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RaDeleon/BrowserHelm) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/RaDeleon/BrowserHelm#readme) (source-built; no separate product site verified). |
| Pricing and access | Free download (Apache-2.0, preview DMGs on GitHub Releases). You pay TypeSafe or other providers for your own calls. Checked 2026-11-16. |
| Jev evidence | [`neo-personal/vision.py`](https://github.com/RaDeleon/BrowserHelm/blob/5998aa288de1d479daec7e8c201e4a0b04ace7cb/neo-personal/vision.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [RaDeleon](https://github.com/RaDeleon). Independently curated. |
| Format | macOS app (Swift/SwiftUI) with a Python MCP engine (Apache-2.0); preview DMGs on GitHub Releases |
| Platform and availability | macOS 14+ on Apple Silicon (preview DMG, ad-hoc signed); requires BrowserOS Neo |
| Jev's role | Optional decision provider: Jev picks which observed link to follow during delegated navigation. |
| Requirements | Apple Silicon Mac on macOS 14+, BrowserOS Neo running with its MCP server, an MCP client, and for Jev a TypeSafe key (other providers optional). |
| License | [Apache-2.0](https://github.com/RaDeleon/BrowserHelm/blob/5998aa288de1d479daec7e8c201e4a0b04ace7cb/LICENSE) |

## When to use

- Cut browser context and planner turns when an AI client drives BrowserOS Neo.
- Mismatch: Intel Macs or other systems, and forms or arbitrary workflows; Jev delegation covers public same-origin links.

## How it works

Providers include TypeSafe AI/Jev at `https://api.typesafe.ai/v1` (pinned `jev-1.13.0` for decisions, `jev-1.14.0` for experimental vision in `neo-personal/vision.py`), OpenRouter, Ollama, LM Studio and custom OpenAI-compatible endpoints; keys live in macOS Keychain. Integration evidence: [`neo-personal/vision.py`](https://github.com/RaDeleon/BrowserHelm/blob/5998aa288de1d479daec7e8c201e4a0b04ace7cb/neo-personal/vision.py).

## Get started

Install the DMG, start BrowserOS Neo, choose a provider in Settings and connect your MCP client.

```sh
# download the DMG: https://github.com/RaDeleon/BrowserHelm/releases/latest
# drag BrowserHelm.app to Applications, start BrowserOS Neo (MCP at http://127.0.0.1:9010/mcp)
# Settings -> provider TypeSafe, model jev-1.13.0, key -> Test provider -> Connect Claude Desktop
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/RaDeleon/BrowserHelm/blob/5998aa288de1d479daec7e8c201e4a0b04ace7cb/README.md](https://github.com/RaDeleon/BrowserHelm/blob/5998aa288de1d479daec7e8c201e4a0b04ace7cb/README.md)
- Releases: [github.com/RaDeleon/BrowserHelm/releases](https://github.com/RaDeleon/BrowserHelm/releases)

## Limits and data handling

Jev is optional: direct browser tools need no decision provider. With Jev on, observed link text goes to TypeSafe on your key. Preview builds are ad-hoc signed, not notarized; the maker calls it an experimental portfolio project.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 5998aa288de1](https://github.com/RaDeleon/BrowserHelm/tree/5998aa288de1d479daec7e8c201e4a0b04ace7cb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
