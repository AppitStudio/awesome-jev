# jevb

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Browser and phone use for AI agents in plain English: the agent says what it wants (`jevb act mark "Buy oat milk" as done`, `jevb check …`) and TypeSafe Jev picks the element or judges the screen in about 150–300 ms, driving headless Chromium, your own Chrome, or real iOS and Android phones and returning short JSON instead of page snapshots.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mitya777/jevb) |
| Maintainer | [mitya777](https://github.com/mitya777). Independently curated. |
| Format | Node CLI `jevb` installed from the GitHub release tarball; `.jevb` scripts |
| Requirements | Node 22+, a TypeSafe key (`TYPESAFEAI_API_KEY` or `TYPESAFE_API_KEY`); Appium for phones. |
| License | [MIT](https://github.com/mitya777/jevb/blob/4903c3e2108ae4416e492de2dd0853c1f96017a2/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give a coding agent browser control without feeding it full accessibility snapshots.
- Write plain-English smoke tests (`jevb check`) that exit 0 or non-zero.
- Mismatch: Jev picks among elements found by code; it does not plan multi-step tasks.

## How it works

[`src/browser.mjs`](https://github.com/mitya777/jevb/blob/4903c3e2108ae4416e492de2dd0853c1f96017a2/src/browser.mjs) drives Chromium over CDP and collects candidate elements; Jev answers which element was meant, whether the screen shows something, or which text answers a question. Example scripts are in [`examples/`](https://github.com/mitya777/jevb/tree/4903c3e2108ae4416e492de2dd0853c1f96017a2/examples).

## Get started

Install from the latest release (README):

```sh
npm install -g https://github.com/mitya777/jevb/releases/latest/download/jevb.tgz
export TYPESAFEAI_API_KEY=...
jevb open https://demo.playwright.dev/todomvc/
```

Each `act` / `check` / lookup is a Jev request billed to your TypeSafe key.

## Examples and demos

- README TodoMVC walkthrough.
- [`examples/todomvc.jevb`](https://github.com/mitya777/jevb/blob/4903c3e2108ae4416e492de2dd0853c1f96017a2/examples/todomvc.jevb).

## Limits and data handling

Element descriptions and page text needed for each decision go to TypeSafe; the browser runs locally. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 4903c3e2108a](https://github.com/mitya777/jevb/tree/4903c3e2108ae4416e492de2dd0853c1f96017a2). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
