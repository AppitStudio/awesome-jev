# REPLAY

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

macOS computer- and browser-use toolkit (Chinese docs, English summary) splitting work fast and slow: a slow model such as Opus plans, handles exceptions and approves risky actions, TypeSafe Jev (~0.5–1 s per judgment) decides each screen — what to look at, click or fill, and whether it's done — and code acts through Ego Lite for web, cua-driver and Peekaboo for apps and native dialogs, with Apple Vision OCR as fallback; recorded demonstrations become reusable task chains.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/balue8246-maker/replay) |
| Maintainer | [balue8246-maker](https://github.com/balue8246-maker). Independently curated. |
| Format | Node CLI `replay` (`node bin/replay.mjs`) + agent skill |
| Requirements | macOS; Node; Ego browser skills; TypeSafe API key; optional cua-driver and Peekaboo for desktop control. |
| License | [MIT](https://github.com/balue8246-maker/replay/blob/3e85f7564fcc7c9aee1a80cd45a77ca02c0c2cba/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Automate repetitive back-office web and desktop chores after one demonstration.
- Mismatch: v0.2, macOS only; timings in the README are author-measured on one machine.

## How it works

[`src/jev.mjs`](https://github.com/balue8246-maker/replay/blob/3e85f7564fcc7c9aee1a80cd45a77ca02c0c2cba/src/jev.mjs) and [`src/judge.mjs`](https://github.com/balue8246-maker/replay/blob/3e85f7564fcc7c9aee1a80cd45a77ca02c0c2cba/src/judge.mjs) score candidate elements and page state; [`src/loop.mjs`](https://github.com/balue8246-maker/replay/blob/3e85f7564fcc7c9aee1a80cd45a77ca02c0c2cba/src/loop.mjs) acts when Jev is confident and escalates otherwise. Design: [`docs/DESIGN.md`](https://github.com/balue8246-maker/replay/blob/3e85f7564fcc7c9aee1a80cd45a77ca02c0c2cba/docs/DESIGN.md).

## Get started

Set up (README):

```sh
git clone https://github.com/balue8246-maker/replay.git && cd replay
node bin/replay.mjs setup
replay look
```

Each screen judgment is a Jev request on your key; the slow model bills separately.

## Examples and demos

- Example plan: [`examples/httpbin-pizza.plan.json`](https://github.com/balue8246-maker/replay/blob/3e85f7564fcc7c9aee1a80cd45a77ca02c0c2cba/examples/httpbin-pizza.plan.json).

## Limits and data handling

Element lists and page state go to TypeSafe. Grants desktop control. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 3e85f7564fcc](https://github.com/balue8246-maker/replay/tree/3e85f7564fcc7c9aee1a80cd45a77ca02c0c2cba). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
