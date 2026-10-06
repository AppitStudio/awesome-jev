# QAJev

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Test a website, game or app the way a person uses it: write a plain-language goal and Jev (TypeSafe or OpenRouter) clicks through a real Chrome, iOS Simulator, Android emulator or Godot/Electron game, while your expectations — not Jev's "done" — decide pass/fail; read-only by default with a hard cost cap.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HanamoriLabs/qajev) |
| Product homepage | [qajev.com](https://qajev.com) |
| Maintainer | [HanamoriLabs](https://github.com/HanamoriLabs). Independently curated. |
| Format | CLI (uv/pipx install from Git) with MCP entry for agents |
| Requirements | macOS or Linux, Python 3.12+, Chrome/Chromium; one key for Jev — `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY` (not needed for the free smoke crawl). |
| License | [MIT](https://github.com/HanamoriLabs/qajev/blob/a09ea317e5aa6c17bf60493cc8042048b52310d3/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Check a key user journey ("open pricing, stop when prices are visible") without writing selectors, and keep the test working after a redesign.
- Let several agents share one machine's test queue through MCP.
- Mismatch: Jev reads pages as text — shadow DOM, iframes, canvas UIs, file uploads and pop-ups are out of reach today.

## How it works

Jev, given the goal and a text rendering of the current page, chooses the next action in real Chrome (or taps through mobile apps / works game menus while the game's own bot plays). Jev saying "done" is never proof: `--expect-url` and other expectations decide the verdict, and failures are classified as **fail** (product), **harness** (tool) or a lost visitor. Dangerous buttons are hidden, passwords and payment details are never typed by Jev, and each run has a cost cap.

## Get started

Install, add a key, and run a goal check (live Jev calls; `smoke` is free):

```sh
uv tool install git+https://github.com/hanamorilabs/qajev
mkdir -p ~/.qajev && echo 'TYPESAFE_API_KEY=...' >> ~/.qajev/.env   # or OPENROUTER_API_KEY
qajev doctor
qajev check http://localhost:3000 --goal "Open the pricing page. Stop when the prices are visible." --expect-url /pricing
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- `qajev smoke URL` free crawl (HTTP/script errors, broken links, accessibility/SEO basics).
- `qajev top` / `qajev dashboard` live views with screenshots and costs.

## Limits and data handling

Page text and goals are sent to TypeSafe or OpenRouter. iOS Simulator cannot read web pages inside Safari yet. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit a09ea317e5aa](https://github.com/HanamoriLabs/qajev/tree/a09ea317e5aa6c17bf60493cc8042048b52310d3). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
