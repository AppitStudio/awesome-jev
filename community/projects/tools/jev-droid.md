# jev-droid (Android UI automation on a free emulator, with DeepSeek planning and Jev triaging screens)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Android UI automation agent (README in Portuguese) built on Google's free emulator, WHPX on Windows and local ADB. The agent reads the accessibility tree, DeepSeek V4.1 Flash picks one action per turn, and Jev 1.13 via OpenRouter triages screens and acts as a guardrail before actions run.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/frederico-kluser/jev-droid) |
| Maintainer | [frederico-kluser](https://github.com/frederico-kluser). Independently curated. |
| Format | Node.js CLI (TypeScript) |
| Requirements | Windows with WHPX, Android SDK command-line tools, Node.js; an OpenRouter key. |
| License | [MIT](https://github.com/frederico-kluser/jev-droid/blob/bc4c6228ebbd783adea726959768bf5e6c366ae6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/frederico-kluser/jev-droid/blob/bc4c6228ebbd783adea726959768bf5e6c366ae6/src/jev.ts) at the pinned commit. |

## When to use

- Automate Android settings or app flows cheaply without Android Studio.
- Mismatch: Windows-focused setup; README in Portuguese.

## How it works

`src/jev.ts` sends typed questions to `typesafe/jev-1.13` on OpenRouter for screen triage and guardrail checks; `examples/jev-guard.json` shows a request. The planner LLM proposes, Jev screens, and ADB executes. Integration evidence: [`src/jev.ts`](https://github.com/frederico-kluser/jev-droid/blob/bc4c6228ebbd783adea726959768bf5e6c366ae6/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/frederico-kluser/jev-droid.git && cd jev-droid
npm install
npm run setup:android
npm run doctor -- --live
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Portuguese): [github.com/frederico-kluser/jev-droid#readme](https://github.com/frederico-kluser/jev-droid#readme)

## Limits and data handling

Accessibility-tree text is sent to OpenRouter. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit bc4c6228ebbd](https://github.com/frederico-kluser/jev-droid/tree/bc4c6228ebbd783adea726959768bf5e6c366ae6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
