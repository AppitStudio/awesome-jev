# claude-jev-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin (Indonesian README) that asks Jev three questions per prompt to pick the cheapest sufficient Claude tier and thinking effort, with a prompt-cache guard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sutan13/claude-jev-router) |
| Maintainer | [sutan13](https://github.com/sutan13). Independently curated. |
| Format | Claude Code plugin (TypeScript hooks) |
| Requirements | Claude Code, TypeSafe API key. |
| License | [MIT](https://github.com/sutan13/claude-jev-router/blob/ca76882a18d97fc87d2ae6a334b092896f9c3e55/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/router.ts`](https://github.com/sutan13/claude-jev-router/blob/ca76882a18d97fc87d2ae6a334b092896f9c3e55/hooks/router.ts) at the pinned commit. |

## When to use

- Cut Claude Code cost by routing simple prompts to cheaper tiers.
- Mismatch: installs from a local marketplace path; README in Indonesian.

## How it works

Jev answers `tier` (choice), `effort` (score) and `continuation` (noul). Code picks the cheapest tier within a risk tolerance, clamps effort, reuses the previous decision for follow-ups, and refuses to downgrade on long conversations to keep the prompt cache. Integration evidence: [`hooks/router.ts`](https://github.com/sutan13/claude-jev-router/blob/ca76882a18d97fc87d2ae6a334b092896f9c3e55/hooks/router.ts).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin marketplace add ~/claude-plugins/jev-router
claude plugin install jev-router@jev-local --scope user
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Status-line output example in the upstream README.
- Tests: `hooks/router.test.ts`.

## Limits and data handling

Prompt plus a short context excerpt go to TypeSafe. If Jev fails or no key is set, the session model is used.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit ca76882a18d9](https://github.com/sutan13/claude-jev-router/tree/ca76882a18d97fc87d2ae6a334b092896f9c3e55). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
