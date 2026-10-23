# jevtool (test Jev judgments against labeled cases)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Node.js CLI that runs a suite of Jev questions and expected answers to report accuracy, misses and how much you could automate at a target accuracy, compares model versions, checks agent deliveries against real test results and filters records by meaning, with TypeSafe or OpenRouter as the provider.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jevtool/jevtool) |
| Maintainer | [jevtool](https://github.com/jevtool). Independently curated. |
| Format | Node.js CLI (npm: jevtool) |
| Requirements | Node.js 20+; a TypeSafe or OpenRouter API key; Git only for `verify`. |
| License | [MIT](https://github.com/jevtool/jevtool/blob/bd605a1c93ff6a713b59c471fb9f983002cc0d18/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/client.mjs`](https://github.com/jevtool/jevtool/blob/bd605a1c93ff6a713b59c471fb9f983002cc0d18/src/client.mjs) at the pinned commit. |

## When to use

- Check a Jev judgment on your own cases before you ship it.
- See which answers change when you move to a new Jev version.
- Mismatch: an evaluation harness, not a runtime gateway.

## How it works

`src/client.mjs` calls `https://api.typesafe.ai/v1/systemone` (default `jev-1.13.0`) with `TYPESAFE_API_KEY`, or OpenRouter's decisions endpoint with `typesafe/jev-1.13`; suites are plain JSON files of questions and cases. Integration evidence: [`src/client.mjs`](https://github.com/jevtool/jevtool/blob/bd605a1c93ff6a713b59c471fb9f983002cc0d18/src/client.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
npm install -g jevtool
export TYPESAFE_API_KEY=...
jevtool eval --examples
jevtool eval example:support-triage
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project site: [jevtool.dev](https://jevtool.dev)
- Weekly benchmark built on jevtool: [github.com/jevtool/benchmarks](https://github.com/jevtool/benchmarks)

## Limits and data handling

Case states are sent to the chosen provider. Independent project, not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit bd605a1c93ff](https://github.com/jevtool/jevtool/tree/bd605a1c93ff6a713b59c471fb9f983002cc0d18). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
