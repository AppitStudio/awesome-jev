# JevClaude by Yusuf (mobile app testing for Claude Code where a local runner drives the phone and Jev makes the per-step calls)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP server and CLI: Claude Code writes a test flow once, a local runner drives an Android device (iOS simulator experimental), and Jev decides which element to tap, whether a step passed, whether an error shows and whether an action is risky. A replay cache makes reruns model-free; Claude hears back only on failure or when Jev is unsure.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Yupol02/jevclaude) |
| Maintainer | [Yusuf](https://github.com/Yupol02). Independently curated. |
| Format | Node.js CLI and MCP server (npm `jevclaude`) |
| Requirements | Node.js, adb (Android) or Xcode simulator with WebDriverAgent (iOS), and a TypeSafe or Cloudflare Workers AI key. |
| License | [MIT](https://github.com/Yupol02/jevclaude/blob/eb3ceb5071cbd403ca9054b54efa82452936f2ec/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/providers.ts`](https://github.com/Yupol02/jevclaude/blob/eb3ceb5071cbd403ca9054b54efa82452936f2ec/src/jev/providers.ts) at the pinned commit. |

## When to use

- Run cheap repeatable UI flows on a real Android phone from Claude Code.
- Mismatch: for canvas, game or Flutter screens without accessibility semantics; those produce empty trees.

## How it works

`src/jev/providers.ts` calls TypeSafe's `POST /v1/systemone` (default `jev-1.14.0`) or Cloudflare Workers AI's `typesafe/jev`. Risky taps (money, installs, deletion, messaging) are blocked when Jev's risk probability is 0.5 or more. Integration evidence: [`src/jev/providers.ts`](https://github.com/Yupol02/jevclaude/blob/eb3ceb5071cbd403ca9054b54efa82452936f2ec/src/jev/providers.ts).

## Get started

Initialise a config, set up Android, then register the MCP server with Claude Code.

```sh
npx jevclaude init
npx jevclaude setup android && npx jevclaude doctor
claude mcp add jevclaude -- npx -y jevclaude mcp
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmark: [github.com/Yupol02/jevclaude/tree/eb3ceb5071cbd403ca9054b54efa82452936f2ec/bench](https://github.com/Yupol02/jevclaude/tree/eb3ceb5071cbd403ca9054b54efa82452936f2ec/bench)

## Limits and data handling

Verified by the author on one Samsung Galaxy S22 Ultra; iOS is simulator-only and unverified live. Screen text and labels go to TypeSafe or Cloudflare (a third-party host) with each call. Benchmark numbers are the author's own.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit eb3ceb5071cb](https://github.com/Yupol02/jevclaude/tree/eb3ceb5071cbd403ca9054b54efa82452936f2ec). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
