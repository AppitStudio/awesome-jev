# Lightpanda Browser (headless browser for AI agents whose classify, cookie-banner and sign-in tools ask TypeSafe Jev)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Headless browser written from scratch in Zig for agents and automation, served over CDP, WebDriver BiDi and a built-in MCP server. Its agent tools now include three that ask a decision model: `classify` answers category or typed questions about a page or element subtree, the cookie tool offers a consent banner's own controls to the model, clicks the one it picks and checks the banner went, and the sign-in tool asks only what the markup leaves ambiguous before filling `$LP_*` credential placeholders and submitting. TypeSafe Jev is the default provider; Gemini Decisions is the alternative.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lightpanda-io/browser) |
| Maintainer | [lightpanda-io](https://github.com/lightpanda-io). Independently curated. |
| Format | Headless browser binary with CDP, WebDriver BiDi and MCP servers (Zig, AGPL-3.0) |
| Requirements | Lightpanda nightly build (Linux, macOS or Docker; Windows via WSL) and `TYPESAFE_API_KEY` for the decision tools (`LIGHTPANDA_DECISION_PROVIDER=gemini` switches to Gemini). |
| License | [AGPL-3.0](https://github.com/lightpanda-io/browser/blob/88fb36db0a6ce4c0011c6cb31cf53e3d3b4a4fbf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/lightpanda_io/status/2122237921084203041)). |
| Jev evidence | [`src/browser/tools/decisions.zig`](https://github.com/lightpanda-io/browser/blob/88fb36db0a6ce4c0011c6cb31cf53e3d3b4a4fbf/src/browser/tools/decisions.zig) at the pinned commit. |

## When to use

- Let an agent's browser handle page checks, cookie walls and logins with a fast typed decision instead of a chat-model call.
- Mismatch: sites that need a full Chromium rendering stack; Lightpanda implements its own engine.

## How it works

`src/browser/tools/decisions.zig` is the decision-model layer shared by `classify.zig`, `consent.zig` and `login.zig`; it calls TypeSafe System One through the `zenai` client, and `src/App.zig` makes TypeSafe the provider unless `LIGHTPANDA_DECISION_PROVIDER` says otherwise. The test server mocks `/v1/systemone` with `jev-latest`. Integration evidence: [`src/browser/tools/decisions.zig`](https://github.com/lightpanda-io/browser/blob/88fb36db0a6ce4c0011c6cb31cf53e3d3b4a4fbf/src/browser/tools/decisions.zig).

## Get started

Install a nightly build, set the TypeSafe key and run the MCP server for your agent.

```sh
brew install lightpanda-io/browser/lightpanda   # or download a nightly binary
export TYPESAFE_API_KEY=...
lightpanda mcp
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/lightpanda-io/browser/blob/88fb36db0a6ce4c0011c6cb31cf53e3d3b4a4fbf/README.md](https://github.com/lightpanda-io/browser/blob/88fb36db0a6ce4c0011c6cb31cf53e3d3b4a4fbf/README.md)
- Tool definitions: [github.com/lightpanda-io/browser/blob/88fb36db0a6ce4c0011c6cb31cf53e3d3b4a4fbf/src/browser/tools/definitions.zig](https://github.com/lightpanda-io/browser/blob/88fb36db0a6ce4c0011c6cb31cf53e3d3b4a4fbf/src/browser/tools/definitions.zig)

## Limits and data handling

Page content sent to the decision tools goes to TypeSafe (or Gemini) on your key. Credentials stay as `$LP_*` placeholders and are never sent to the model. The decision tools ship in the nightly builds reviewed here.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 88fb36db0a6c](https://github.com/lightpanda-io/browser/tree/88fb36db0a6ce4c0011c6cb31cf53e3d3b4a4fbf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
