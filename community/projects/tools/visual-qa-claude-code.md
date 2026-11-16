# Visual QA by dontdothatapp (Claude Code plugin that runs plain-language QA checklists in your Chrome, with Jev navigating and Claude judging)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Paste a QA checklist (bullets, check boxes, sections, notes, plus the site's address) into Claude Code and Visual QA tests every check in your own Chrome, then hands you an HTML report with a verdict and a screenshot for each one. Jev is the fast navigator that clicks through the pages; Claude takes over when Jev gets stuck and judges every result. A guided `/visual-qa:setup` handles Node.js, the TypeSafe key file and Chrome's remote-debugging switch.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dontdothatapp/qa-no-qa) |
| Maintainer | [dontdothatapp](https://github.com/dontdothatapp). Independently curated. |
| Format | Claude Code plugin (TypeScript, MIT) |
| Requirements | macOS, Claude Code, Google Chrome 144+, Node.js 22.18+ and a TypeSafe key (stored in a local key file). |
| License | [MIT](https://github.com/dontdothatapp/qa-no-qa/blob/7960f44bb9d40d909fe3d0b6cebb7f8724e5b00f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`visual-qa/src/jev-client.ts`](https://github.com/dontdothatapp/qa-no-qa/blob/7960f44bb9d40d909fe3d0b6cebb7f8724e5b00f/visual-qa/src/jev-client.ts) at the pinned commit. |

## When to use

- Turn a written QA checklist into a screenshot-backed test report without writing test code.
- Mismatch: CI test suites on Linux; it drives your own Chrome on a Mac.

## How it works

`visual-qa/src/jev-client.ts` calls `systemOne` through the official `@typesafe-ai/sdk` with `jev-latest` (set in `src/config.ts`); `src/decide.ts` builds each navigation request from a page snapshot and the scenario goal, and `src/setup.ts` manages the `TYPESAFE_API_KEY` key file. Integration evidence: [`visual-qa/src/jev-client.ts`](https://github.com/dontdothatapp/qa-no-qa/blob/7960f44bb9d40d909fe3d0b6cebb7f8724e5b00f/visual-qa/src/jev-client.ts).

## Get started

Install the plugin from its marketplace inside Claude Code, then run setup.

```sh
claude plugin marketplace add dontdothatapp/qa-no-qa
claude plugin install visual-qa@qa-no-qa
# in Claude Code: /reload-plugins, then /visual-qa:setup, then /visual-qa:test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/dontdothatapp/qa-no-qa/blob/7960f44bb9d40d909fe3d0b6cebb7f8724e5b00f/README.md](https://github.com/dontdothatapp/qa-no-qa/blob/7960f44bb9d40d909fe3d0b6cebb7f8724e5b00f/README.md)

## Limits and data handling

Page content goes to TypeSafe for navigation (billed on your key) and to Claude on your subscription. Tests run in your real Chrome profile with remote debugging on.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 7960f44bb9d4](https://github.com/dontdothatapp/qa-no-qa/tree/7960f44bb9d40d909fe3d0b6cebb7f8724e5b00f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
