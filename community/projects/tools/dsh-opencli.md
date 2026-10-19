# dsh-opencli

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

DeepSeek Harness (dsh) plugin that drives your own logged-in Chrome or Edge through OpenCLI: 180+ site commands, generic browser primitives, approval gates on writes, watch jobs, and a System One decision layer (Jev or local Laya) for fast checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/IKEASven69/dsh-opencli) |
| Maintainer | [IKEASven69](https://github.com/IKEASven69). Independently curated. |
| Format | dsh plugin (Node.js) |
| Requirements | dsh, OpenCLI daemon + BrowserBridge extension; optional TypeSafe key in `~/.dsh/typesafe-key` for Jev decisions. |
| License | [MIT](https://github.com/IKEASven69/dsh-opencli/blob/1448a724bc9c904d8e412426677920058f8762f3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/index.js`](https://github.com/IKEASven69/dsh-opencli/blob/1448a724bc9c904d8e412426677920058f8762f3/lib/index.js) at the pinned commit. |

## When to use

- Let a dsh agent read and act on sites with your real login state.
- Want write actions behind an approval prompt.
- Mismatch: Chinese-first docs; acts in your real browser session, so review permissions carefully.

## How it works

The plugin talks to the OpenCLI daemon and its browser extension to run structured site commands or open, click and fill pages in your normal browser. Its bundled `SystemOne` class in `lib/index.js` posts to `https://api.typesafe.ai/v1/systemone` (or a local Laya engine) for quick yes/no and verification judgments. Integration evidence: [`lib/index.js`](https://github.com/IKEASven69/dsh-opencli/blob/1448a724bc9c904d8e412426677920058f8762f3/lib/index.js).

## Get started

From the upstream README: install OpenCLI and its BrowserBridge extension, then `dsh plugin add IKEASven69/dsh-opencli`.

```sh
npm i -g @jackwener/opencli && opencli daemon restart
dsh plugin add IKEASven69/dsh-opencli
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [github.com/IKEASven69/dsh-opencli/blob/opencli-release/AGENT_INSTALL.md](https://github.com/IKEASven69/dsh-opencli/blob/opencli-release/AGENT_INSTALL.md)

## Limits and data handling

Runs with your real browser cookies and accounts. Page text sent for decisions goes to TypeSafe when Jev is selected.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 1448a724bc9c](https://github.com/IKEASven69/dsh-opencli/tree/1448a724bc9c904d8e412426677920058f8762f3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
