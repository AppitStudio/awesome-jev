# commit-changelog by Hamza Ahmad Aslam (CLI that sorts plain commit messages into Keep a Changelog sections with Jev, unchanged, and lists unsure ones for review)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Turns the commits since your last tag into a Keep a Changelog section without needing conventional-commit prefixes. Prefixed commits are placed in code; for the rest, Jev answers which section each commit belongs to and whether users would notice it, and code copies each first line unchanged into Added, Changed, Deprecated, Removed, Fixed or Security, or onto a review list.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hamzaahmadaslam/commit-changelog) |
| Maintainer | [Hamza Ahmad Aslam](https://github.com/hamzaahmadaslam). Independently curated. |
| Format | Node.js CLI (npm, no dependencies) |
| Requirements | Node.js 20+ and a TypeSafe API key (not needed for `--dry-run`). Git and a repository with tags. |
| License | [MIT](https://github.com/hamzaahmadaslam/commit-changelog/blob/b34ab58410aeb70e6bd987bc657d44ee1455e3ec/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/hamzaahmadaslam/commit-changelog/blob/b34ab58410aeb70e6bd987bc657d44ee1455e3ec/src/jev.mjs) at the pinned commit. |

## When to use

- Maintainers whose commit messages do not follow a convention and who write changelogs by hand.
- Mismatch: polished release notes; entries are copied as written, not rewritten.

## How it works

`src/jev.mjs` posts batches to `https://api.typesafe.ai/v1/systemone` with typed `choice`, `noul` and `score` questions, and code applies one `--threshold` (default 0.8) to place each item or send it to review. Integration evidence: [`src/jev.mjs`](https://github.com/hamzaahmadaslam/commit-changelog/blob/b34ab58410aeb70e6bd987bc657d44ee1455e3ec/src/jev.mjs).

## Get started

Install from npm and run it in a repository; `--dry-run` shows what would be sent.

```sh
npm install -g @hamzaahmadaslam/commit-changelog
export TYPESAFE_API_KEY=...
commit-changelog --dry-run   # nothing sent
commit-changelog
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Worked example in the README: [github.com/hamzaahmadaslam/commit-changelog#example](https://github.com/hamzaahmadaslam/commit-changelog#example)

## Limits and data handling

Commit subjects, bodies and file names go to TypeSafe; diffs do not. Vague messages usually land in review, a commit that does two things gets one section, and merge commits are skipped. English works best, and text in a commit message can move Jev's answers; read the section before you release.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit b34ab58410ae](https://github.com/hamzaahmadaslam/commit-changelog/tree/b34ab58410aeb70e6bd987bc657d44ee1455e3ec). Inspected the README, LICENSE and `src/jev.mjs` at the pinned commit; npm package version 1.0.0 confirmed. The CLI was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
