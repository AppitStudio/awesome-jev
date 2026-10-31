# safe-to-merge (GitHub Action and CLI where Jev judges whether a pull request is safe to merge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action and Bun CLI that answers one question about a pull request: can it merge right now? Hard facts such as conflicts, failing checks and approvals are enforced in code; judgment calls such as risk, test adequacy, breaking changes, blocking comments and flaky CI go to Jev. Jev can raise concerns but never turn a hard-rule block into a pass.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Hiccup-za/safe-to-merge) |
| Maintainer | [Hiccup-za](https://github.com/Hiccup-za). Independently curated. |
| Format | GitHub Action + CLI (JavaScript, Bun) |
| Requirements | Bun; a GitHub token; a TypeSafe key. |
| License | [MIT](https://github.com/Hiccup-za/safe-to-merge/blob/4e3f846a84fb93cd5a0342f7338b773d573d5527/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.js`](https://github.com/Hiccup-za/safe-to-merge/blob/4e3f846a84fb93cd5a0342f7338b773d573d5527/src/jev.js) at the pinned commit. |

## When to use

- Add a 'safe / needs review / block' verdict to PRs as a comment or status check.
- Mismatch: advisory judgment; it does not replace code review or tests.

## How it works

`src/jev.js` sends a redacted, size-budgeted diff plus PR metadata to TypeSafe as typed questions (verdict, risk, tests, breaking change, security, description match), and `src/cli.js` combines the answers with code-enforced rules into a final verdict. Integration evidence: [`src/jev.js`](https://github.com/Hiccup-za/safe-to-merge/blob/4e3f846a84fb93cd5a0342f7338b773d573d5527/src/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=... GITHUB_TOKEN=...
bun src/cli.js acme/shop#123
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Workflow example: [github.com/Hiccup-za/safe-to-merge/blob/main/examples/safe-to-merge.yml](https://github.com/Hiccup-za/safe-to-merge/blob/main/examples/safe-to-merge.yml)

## Limits and data handling

A redacted diff and PR metadata are sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 4e3f846a84fb](https://github.com/Hiccup-za/safe-to-merge/tree/4e3f846a84fb93cd5a0342f7338b773d573d5527). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
