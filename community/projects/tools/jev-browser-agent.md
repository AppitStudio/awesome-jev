# Jev Browser Agent

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Bun and TypeScript browser agent with an indexed action space: a typed decision model (Jev, local or cloud) picks the operation and element each step, a chat helper writes a checklist, and a live inspector streams Chromium as it works.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ali-master/jev-browser-agent) |
| Maintainer | [ali-master](https://github.com/ali-master). Independently curated. |
| Format | Bun app + TypeScript library |
| Requirements | Bun 1.4.3+; Chromium (installed by the setup script); a System One endpoint (TypeSafe cloud or a local server) and a chat model. |
| License | [MIT](https://github.com/ali-master/jev-browser-agent/blob/35df9bc7a27583c4f50962ac8dca48cdf529997c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/config.ts`](https://github.com/ali-master/jev-browser-agent/blob/35df9bc7a27583c4f50962ac8dca48cdf529997c/src/config.ts) at the pinned commit. |

## When to use

- Run goal-driven web tasks with a fast typed model choosing each action.
- Watch and debug each step in a live browser inspector.
- Mismatch: TypeScript rewrite of browser-use's Jev Ultrafast; acts on real sites, so review what it may click.

## How it works

Every observation builds a fresh table of visible controls. One `/systemone` request picks an operation (CLICK, TYPE_TEXT, SELECT, SCROLL, WAIT, BLOCKED) and a compatible element; a chat helper turns the goal into a checklist and writes field text. `src/config.ts` reads `TYPESAFE_BASE_URL`, `TYPESAFE_API_KEY` and `TYPESAFE_MODEL`, with a local default and a TypeSafe cloud example. Integration evidence: [`src/config.ts`](https://github.com/ali-master/jev-browser-agent/blob/35df9bc7a27583c4f50962ac8dca48cdf529997c/src/config.ts).

## Get started

From the upstream README: clone, install with Bun, install the browser, copy `.env.example`, then start the inspector.

```sh
git clone https://github.com/ali-master/jev-browser-agent.git && cd jev-browser-agent
bun install --frozen-lockfile
bun run browser:install
cp .env.example .env && bun start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Local inspector on port 8766 after `bun start`
- [github.com/browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) (original project)

## Limits and data handling

Page content goes to the configured decision and chat endpoints. Browser actions run on live sites.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 35df9bc7a275](https://github.com/ali-master/jev-browser-agent/tree/35df9bc7a27583c4f50962ac8dca48cdf529997c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
