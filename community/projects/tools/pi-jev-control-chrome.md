# pi-jev-control-chrome

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Pi Agent extension where the main model hands a browsing task to a bounded loop: pi-control-chrome reads the page DOM, Jev picks one action from a finite candidate list, and the loop clicks, types, scrolls until done or a limit.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JHXs/pi-jev-control-chrome) |
| Maintainer | [JHXs](https://github.com/JHXs). Independently curated. |
| Format | Pi Agent extension (Node.js) using pi-control-chrome |
| Requirements | Node.js 22+, Pi Agent with pi-control-chrome and its Chrome extension, a TypeSafe key (or a compatible gateway) in `~/.pi/agent/jev-browser.json`. |
| License | [MIT](https://github.com/JHXs/pi-jev-control-chrome/blob/106fdfb954af8b52f86c1a79cf8bfeb343ca9a58/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/config.mjs`](https://github.com/JHXs/pi-jev-control-chrome/blob/106fdfb954af8b52f86c1a79cf8bfeb343ca9a58/src/config.mjs) at the pinned commit. |

## When to use

- Let a Pi agent finish short browser tasks (search, fill, submit) without a large model choosing every click.
- Keep browsing bounded with step limits, a source allowlist and a safety policy.
- Mismatch: experimental; per-site DOM handling and long-task latency still need testing. README is in Chinese.

## How it works

The extension registers `jev_browser_task`. Each step reads the DOM through pi-control-chrome (no screenshots), asks the configured System One classifier (default `typesafe` / `jev-latest`) to choose among candidate actions, executes it, and repeats; the main Pi model reviews the result, and `done_unverified` is not treated as success. Integration evidence: [`src/config.mjs`](https://github.com/JHXs/pi-jev-control-chrome/blob/106fdfb954af8b52f86c1a79cf8bfeb343ca9a58/src/config.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
pi install npm:pi-control-chrome
mkdir -p ~/.pi/agent/extensions
git clone https://github.com/JHXs/pi-jev-control-chrome.git ~/.pi/agent/extensions/pi-jev-control-chrome
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Wikipedia search loop described in the README (3 steps, about 8 seconds).

## Limits and data handling

Page DOM text goes to TypeSafe or your configured gateway on your key. You install the Chrome extension yourself.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 106fdfb954af](https://github.com/JHXs/pi-jev-control-chrome/tree/106fdfb954af8b52f86c1a79cf8bfeb343ca9a58). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
