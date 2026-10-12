# ego-jev

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

CLI that lets Jev click through multi-step browser flows inside ego lite (your real Chromium browser on macOS) while your LLM agent keeps the goal; Jev decides which element to act on and which caller-supplied value goes where.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kimjisub/ego-jev) |
| Maintainer | [kimjisub](https://github.com/kimjisub). Independently curated. |
| Format | Node.js CLI (npm `ego-jev`) |
| Requirements | macOS with ego lite installed (`ego-browser`); Node.js 20+; `TYPESAFE_API_KEY` or an `ego-jev proxy`. |
| License | [MIT](https://github.com/kimjisub/ego-jev/blob/8d5f91acdf19534d2825716cfe73a1ac8adb2bed/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Hand repetitive form/checkout flows to Jev with `--require` page-state checks instead of spending an LLM turn per click.
- Ask yes/no (`check`) or relevance (`read`) questions about the current page.
- Mismatch: macOS + ego lite only; irreversible steps need `--allow-irreversible`. Speedups are the maintainer's own measurements.

## How it works

`ego-jev do` reads the page, asks Jev which element and which `key=value` to use next plus requirement probabilities, acts through ego, and stops when requirements look satisfied. Strings typed always come from the caller. Portions derive from jev-browser 0.1.2 (MIT). Jev integration: [`src/jev/jev.mjs`](https://github.com/kimjisub/ego-jev/blob/8d5f91acdf19534d2825716cfe73a1ac8adb2bed/src/jev/jev.mjs). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
npm install -g ego-jev
export TYPESAFE_API_KEY=...
ego-jev do "<goal>" key=value --url https://example.com --require "<page state>"
```

## Limits and data handling

Page text/elements are sent to TypeSafe; runs in a browser with your logins, so scope tasks carefully. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 8d5f91acdf19](https://github.com/kimjisub/ego-jev/tree/8d5f91acdf19534d2825716cfe73a1ac8adb2bed). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
