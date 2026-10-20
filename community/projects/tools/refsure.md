# refsure (browser judgment for coding agents)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

CLI and agent skill that coding agents in Orca terminals or next to an agent-browser session call to answer browser questions they often get wrong (which control means X, how to pass a banner, whether a click landed), using Jev decisions over a hidden page in the agent's own tab.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/leovvay/leovvayRefsure) |
| Maintainer | [leovvay](https://github.com/leovvay). Independently curated. |
| Format | CLI and agent skill (TypeScript, Node.js) |
| Requirements | Node.js; Orca or agent-browser; your own Jev key (OpenRouter or TypeSafe). |
| License | [MIT](https://github.com/leovvay/leovvayRefsure/blob/212889bf2a6a4a4d1ed79158e5af1cff656162ae/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/providers/jev/jev-wire.ts`](https://github.com/leovvay/leovvayRefsure/blob/212889bf2a6a4a4d1ed79158e5af1cff656162ae/src/providers/jev/jev-wire.ts) at the pinned commit. |

## When to use

- Let Claude Code or Codex do a whole browser step (fill, click, check) in one call.
- Check page state without moving your own view.
- Mismatch: built around Orca and agent-browser; not on npm yet at review time.

## How it works

`refsure do` reads the agent's tab, asks Jev typed questions about the page (target control, page state, whether the expected result appeared) through the provider in `src/providers/jev/`, and performs the step; the default endpoint is OpenRouter with `jev-1.13`. Integration evidence: [`src/providers/jev/jev-wire.ts`](https://github.com/leovvay/leovvayRefsure/blob/212889bf2a6a4a4d1ed79158e5af1cff656162ae/src/providers/jev/jev-wire.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/leovvay/leovvayRefsure && cd leovvayRefsure
npm ci && npm run build && npm i -g .
refsure doctor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Agent benchmark results: [github.com/leovvay/leovvayRefsure/blob/master/tools/bench/agent/RESULTS-fast-path-2026-10-17.md](https://github.com/leovvay/leovvayRefsure/blob/master/tools/bench/agent/RESULTS-fast-path-2026-10-17.md)

## Limits and data handling

Page content is sent to your Jev provider. Speed-up figures come from the author's own benchmark.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 212889bf2a6a](https://github.com/leovvay/leovvayRefsure/tree/212889bf2a6a4a4d1ed79158e5af1cff656162ae). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
