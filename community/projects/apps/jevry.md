# Jevry

[All projects](../README.md) · [Web apps](README.md#web-apps)

Desktop browser agent: the browser observes state, offers executable actions, and TypeSafe Jev chooses the next step while a separate text/vision model plans and writes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/michaelswissa/jevry) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/michaelswissa/jevry](https://github.com/michaelswissa/jevry) |
| Pricing and access | MIT source build (Electron desktop; macOS/Windows CI). Requires TypeSafe API key for Jev plus a connected text/vision provider (Codex, Claude Code, or API keys per README). No app purchase fee. Checked 2026-09-25. |
| Jev evidence | [README](https://github.com/michaelswissa/jevry/blob/40301a6d920bd32dcf31c61e557e16b5340da78f/README.md) documents Choice-based action loop (`CLICK:n`, `TYPE_TEXT:n`, `SCROLL_DOWN`, `DONE`, `BLOCKED`); launch demos and CI evidence linked upstream. |
| Disclosure | Open source MIT source build. Provider costs are separate (BYOK). Independently curated; no affiliation. Listing is not an endorsement. Packaged installers/notarization unfinished per README; live agent runs not executed on the review host. |
| Maintainer | [michaelswissa](https://github.com/michaelswissa). Independently curated. |
| Format | Application (Electron desktop + optional web UI preview). |
| Platform and availability | Node.js 22.12+; `npm ci && npm run dev` for desktop. Source preview 0.4.0-beta.13. |
| Jev's role | Jev chooses the next supported browser action from observed controls; text/vision models plan and generate missing text; deterministic code validates and executes. |
| Requirements | `TYPESAFE_API_KEY` (or equivalent TypeSafe access) plus a connected planning/vision provider as documented in setup. |
| License | [MIT](https://github.com/michaelswissa/jevry/blob/40301a6d920bd32dcf31c61e557e16b5340da78f/LICENSE). |

## When to use

Use for **desktop browser tasks** where each click/type should be a typed Choice over real page controls (games, research, website chores). Prefer thinner MCP browser loops when you only need a coding-agent sub-tool.

## How it works

Jevry builds an action space from the live page, asks Jev Choice for the next operation, and keeps planning/language in a separate model. Code owns execution, cancellation, and receipts; Jev output never becomes arbitrary JavaScript or shell (per README).

## Get started

```sh
git clone https://github.com/michaelswissa/jevry.git
cd jevry
git checkout 40301a6d920bd32dcf31c61e557e16b5340da78f
npm ci
npm run dev
```

Connect TypeSafe and a text/vision provider in the setup screen.

## Examples and demos

- Upstream intro video and 2048 realtime clip linked from the README.
- Workspace screenshots in `docs/media/`.

## Limits and data handling

Page state and chosen actions go to TypeSafe for Jev; planning/vision traffic goes to the connected provider. Use disposable accounts for mutating demos. Signed installers not yet shipped.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 40301a6](https://github.com/michaelswissa/jevry/tree/40301a6d920bd32dcf31c61e557e16b5340da78f). AI-assisted README and LICENSE inspection; desktop agent not run live.
