# capability-diff by Hamza Ahmad Aslam (CLI and GitHub Action that flags WordPress permission changes, with optional Jev review)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Compares two versions of a WordPress plugin or theme and reports changes that let more users run an operation: AJAX and admin-post actions, REST routes and admin pages that lost or lowered a capability check, dropped an object ID, moved a check after the write, became public or stopped checking a nonce. It reads the PHP without running it, works on two folders, two git revisions or a pull request, and can ask Jev to judge the cases code cannot rank.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hamzaahmadaslam/capability-diff) |
| Maintainer | [Hamza Ahmad Aslam](https://github.com/hamzaahmadaslam) (hamzaahmadaslam). Independently curated. |
| Format | Node.js CLI + GitHub Action (npm `@hamzaahmadaslam/capability-diff`) |
| Requirements | Node 20+; a TypeSafe key only with `--jev`. |
| License | [MIT](https://github.com/hamzaahmadaslam/capability-diff/blob/3931aeaafe265867a85a4c9b46ce99e2dd4566c1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/hamzaahmadaslam/capability-diff/blob/3931aeaafe265867a85a4c9b46ce99e2dd4566c1/src/jev.mjs) at the pinned commit. |

## When to use

- WordPress plugin and theme maintainers who want permission regressions caught in review or CI.
- Mismatch: a full security audit; custom permission callbacks and hook-only code paths are not ranked.

## How it works

Most findings come from static analysis alone. With `--jev`, `src/jev.mjs` sends each finding marked Check as one `noul` question (up to 25 per request) to `https://api.typesafe.ai/v1/systemone` (`jev-latest`). A confident yes raises it to Wider, a confident no lowers it, and anything in between stays for review; findings already marked Wider are never sent. Integration evidence: [`src/jev.mjs`](https://github.com/hamzaahmadaslam/capability-diff/blob/3931aeaafe265867a85a4c9b46ce99e2dd4566c1/src/jev.mjs).

## Get started

Install from npm and compare two releases.

```sh
npm install -g @hamzaahmadaslam/capability-diff
capability-diff --git v2.3.0 v2.4.0
export TYPESAFE_API_KEY=...
capability-diff --git v2.3.0 v2.4.0 --jev --dry-run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example report: [github.com/hamzaahmadaslam/capability-diff#example](https://github.com/hamzaahmadaslam/capability-diff#example)
- GitHub Action: [github.com/hamzaahmadaslam/capability-diff/blob/main/action.yml](https://github.com/hamzaahmadaslam/capability-diff/blob/main/action.yml)

## Limits and data handling

Without `--jev` nothing leaves the machine. With it, only operation names, handler names and up to a few short check snippets (240 characters each) per finding are sent. Ranks assume WordPress's default roles.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 3931aeaafe26](https://github.com/hamzaahmadaslam/capability-diff/tree/3931aeaafe265867a85a4c9b46ce99e2dd4566c1). Inspected the README, LICENSE, `src/jev.mjs` and `src/judge.mjs` at the pinned commit and confirmed `@hamzaahmadaslam/capability-diff` 1.0.0 on npm; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
