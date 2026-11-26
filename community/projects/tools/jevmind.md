# Jevmind by hi3wle (harness for Claude Code and Codex where Jev picks each task's workflow and risk, and the agent must show passing checks before it says done)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Outer harness for Claude Code and Codex (formerly Jodex). Jev reads each prompt and decides whether it changes files, which workflow fits (solo, reviewed, or plan → challenge → implement → test → review) and how risky it is; critical paths always need your approval, and the agent can only finish with checks bound to the exact source it ran on. Without a TypeSafe key, deterministic rules and thresholds decide.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hi3wle/jevmind) |
| Maintainer | [hi3wle](https://github.com/hi3wle) (hieventure). Independently curated. |
| Format | Node.js CLI and Claude Code / Codex plugin (version 0.1.0) |
| Requirements | Node.js 22.18+, git, Claude Code and/or Codex; a TypeSafe key only for Jev decisions (`jevmind init --jev` per project). |
| License | [MIT](https://github.com/hi3wle/jevmind/blob/81f3a8ba0cb38568f117cc2eb74d401cba2d73d6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/hi3wle/jevmind/blob/81f3a8ba0cb38568f117cc2eb74d401cba2d73d6/src/jev.ts) at the pinned commit. |

## When to use

- Developers who run Claude Code or Codex and want risk-based review steps and a stop gate that needs real check results.
- Mismatch: fully unattended runs; critical paths always wait for a human answer.

## How it works

`src/jev.ts` uses the official `@typesafe-ai/sdk` to send a redacted prompt and repository metadata (languages, test commands, protected-path matches), never source, with `noul`, `choice` and `score` questions; code applies thresholds and `jevmind calibrate` compares Jev's probabilities with how runs actually ended. Integration evidence: [`src/jev.ts`](https://github.com/hi3wle/jevmind/blob/81f3a8ba0cb38568f117cc2eb74d401cba2d73d6/src/jev.ts).

## Get started

The README installs with `npx jevmind@latest setup`, but no `jevmind` package was on npm when checked (2026-11-26), so build from source.

```sh
git clone https://github.com/hi3wle/jevmind
cd jevmind
npm ci && npm run build
node plugin/dist/jevmind.mjs setup   # README: npx jevmind@latest setup
pbpaste | node plugin/dist/jevmind.mjs key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Full specification: [github.com/hi3wle/jevmind/blob/81f3a8ba0cb38568f117cc2eb74d401cba2d73d6/coding-harness-v4.md](https://github.com/hi3wle/jevmind/blob/81f3a8ba0cb38568f117cc2eb74d401cba2d73d6/coding-harness-v4.md)

## Limits and data handling

Jev is off until enabled per project; with it on, each prompt is redacted with best-effort patterns and sent to TypeSafe with project metadata. Cross-provider review sends the change to the other agent you use. Tested by the author on Claude Code 2.1.311 and Codex 0.171.0; version 0.1.0.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 81f3a8ba0cb3](https://github.com/hi3wle/jevmind/tree/81f3a8ba0cb38568f117cc2eb74d401cba2d73d6). Inspected the README, LICENSE, `package.json` and `src/jev.ts` at the pinned commit; the npm package named in the README was not found on npm (2026-11-26). Nothing was built or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
