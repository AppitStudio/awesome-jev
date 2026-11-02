# Permission Approver for Herdr (approves reversible agent permission requests with Jev and leaves irreversible ones to you)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Herdr plugin that handles Claude Code and Codex permission prompts one request at a time: Jev scores whether the exact action is clear and reversible, low scores get a second review from the Pi CLI, and catastrophic or irreversible actions are left for a human. It never grants permanent or session-wide permissions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sagwaco/herdr-permissions) |
| Maintainer | [sagwaco](https://github.com/sagwaco). Independently curated. |
| Format | Herdr plugin (Node.js, no dependencies) |
| Requirements | macOS, Node.js 22+, Herdr 0.9.3+, a TypeSafe key in the Keychain, an authenticated Pi CLI. |
| License | [MIT](https://github.com/sagwaco/herdr-permissions/blob/dd7fe600a05b9c53391973f6663318f185b33c45/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`policy.mjs`](https://github.com/sagwaco/herdr-permissions/blob/dd7fe600a05b9c53391973f6663318f185b33c45/policy.mjs) at the pinned commit. |

## When to use

- Cut down on approving routine agent commands by hand.
- Mismatch: macOS only; approvals are automated judgments, so review the policy first.

## How it works

`policy.mjs` posts each request to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) with an `approve` noul question whose criteria describe reversible vs catastrophic actions; if TypeSafe is unavailable it does not approve. Integration evidence: [`policy.mjs`](https://github.com/sagwaco/herdr-permissions/blob/dd7fe600a05b9c53391973f6663318f185b33c45/policy.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/sagwaco/herdr-permissions.git && cd herdr-permissions
npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Herdr: [herdr.dev](https://herdr.dev)

## Limits and data handling

Each permission request is sent to TypeSafe, and low-score ones to the Pi CLI's model. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit dd7fe600a05b](https://github.com/sagwaco/herdr-permissions/tree/dd7fe600a05b9c53391973f6663318f185b33c45). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
