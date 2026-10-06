# plain

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Write browser, desktop and mobile end-to-end tests in plain English YAML: Playwright, xa11y or Appium perform the actions while Jev reads the accessibility tree to select the element each step describes and to judge each `expect` claim; coding agents can explore a flow via MCP and save it as a spec.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gabe4coding/plain) |
| Product homepage | [www.plainplugins.dev](https://www.plainplugins.dev) |
| Maintainer | [gabe4coding](https://github.com/gabe4coding). Independently curated. |
| Format | CLI (`npx -p @gabe4coding/plain plain spec.yaml`), agent plugins, MCP |
| Requirements | Node 22+, npm, and `TYPESAFE_API_KEY` in `~/.config/plain/.env` (a Vercel AI Gateway key also works). |
| License | [MIT](https://github.com/gabe4coding/plain/blob/a565492fce1c318874906ee3491b8a5359d00222/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Replace brittle selectors with plain-English targets and claims that survive UI changes.
- Let a coding agent explore a flow and save it as a reusable spec.
- Mismatch: each step that needs a pick or judgment is a model call; for tight unit-level UI assertions a classic framework is cheaper.

## How it works

For every step, plain passes Jev the accessibility tree (not screenshots) and asks which element matches the described target, or whether an `expect` claim holds; Playwright (browser), xa11y (desktop) or Appium (iOS/Android/React Native) then acts. The phrasing guide explains how to write targets and claims Jev can judge reliably.

## Get started

Put the key in `~/.config/plain/.env`, then run a spec (live Jev calls per step; first run installs Chromium):

```sh
mkdir -p ~/.config/plain && echo 'TYPESAFE_API_KEY=...' >> ~/.config/plain/.env
# todo.yaml: name/url/steps with goto, fill, press, expect
npx -p @gabe4coding/plain plain todo.yaml
# Claude Code: /plugin marketplace add gabe4coding/plain
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README spec against the Playwright TodoMVC demo (`fill` the new todo input, `expect` a listed item).
- 7-minute explainer video linked from the README (how Jev picks and judges, costs, comparison with classic frameworks).

## Limits and data handling

Accessibility-tree content of the pages/apps under test is sent to TypeSafe (or the gateway). Desktop engine tested on macOS. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit a565492fce1c](https://github.com/gabe4coding/plain/tree/a565492fce1c318874906ee3491b8a5359d00222). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
