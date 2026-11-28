# hook-contract by Hamza Ahmad Aslam (CLI and GitHub Action that flags WordPress hook changes that break other people's code)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Compares the WordPress actions and filters two versions of a plugin or theme fire, from two folders, two git revisions or a pull request, and reports breaking changes: removed or renamed hooks, fewer arguments, an action turned into a filter, hooks that became conditional. It reads the PHP without running it and uses Jev for the judgment calls code cannot settle, such as whether a hook was renamed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hamzaahmadaslam/hook-contract) |
| Maintainer | [Hamza Ahmad Aslam](https://github.com/hamzaahmadaslam) (hamzaahmadaslam). Independently curated. |
| Format | Node.js CLI + GitHub Action (`@hamzaahmadaslam/hook-contract`) |
| Requirements | Node.js 20+; a TypeSafe API key for the Jev judgments. |
| License | [MIT](https://github.com/hamzaahmadaslam/hook-contract/blob/1515bbe1e2697ee9d7c269a08922b7b6a7adfd07/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/hamzaahmadaslam/hook-contract/blob/1515bbe1e2697ee9d7c269a08922b7b6a7adfd07/src/jev.mjs) at the pinned commit. |

## When to use

- WordPress plugin and theme maintainers who want to catch hook-contract breaks before release.
- Mismatch: PHP function-signature checks; those are covered by existing tools.

## How it works

`src/jev.mjs` posts the hook evidence and questions to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`); `src/judge.mjs` turns the answers into findings next to the code-side comparison. Integration evidence: [`src/jev.mjs`](https://github.com/hamzaahmadaslam/hook-contract/blob/1515bbe1e2697ee9d7c269a08922b7b6a7adfd07/src/jev.mjs).

## Get started

Install from npm and compare two releases, or add the Action to a workflow.

```sh
npm install -g @hamzaahmadaslam/hook-contract
export TYPESAFE_API_KEY=...
hook-contract --git v2.3.0 v2.4.0
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- GitHub Action: [github.com/hamzaahmadaslam/hook-contract/blob/main/action.yml](https://github.com/hamzaahmadaslam/hook-contract/blob/main/action.yml)
- Examples: [github.com/hamzaahmadaslam/hook-contract/tree/main/examples](https://github.com/hamzaahmadaslam/hook-contract/tree/main/examples)

## Limits and data handling

Hook names, arguments and surrounding code excerpts go to TypeSafe for the Jev judgments. `vendor`, `node_modules` and test folders are skipped by default.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 1515bbe1e269](https://github.com/hamzaahmadaslam/hook-contract/tree/1515bbe1e2697ee9d7c269a08922b7b6a7adfd07). Inspected the README, LICENSE, `action.yml` and `src/jev.mjs` at the pinned commit and confirmed version 1.0.0 on npm; nothing was installed or run on the review host. Carried over from the 2026-11-28 00:36 run. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
