# jev-auto-mode (OpenCode plugin where Jev judges permission requests)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode V2 plugin that adds an auto mode: edits are approved, and Jev judges other permission requests for task relevance, data destruction, secret exposure, data transmission and unauthorized remote or system changes, denying anything uncertain.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ttyobiwan/jev-auto-mode) |
| Maintainer | [ttyobiwan](https://github.com/ttyobiwan). Independently curated. |
| Format | OpenCode plugin (TypeScript) |
| Requirements | OpenCode V2; a TypeSafe API key (without it, non-edit requests go to you). |
| License | [MIT](https://github.com/ttyobiwan/jev-auto-mode/blob/f4006253741936d79dde4808b20fdbf41bcd9198/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev/judge.ts`](https://github.com/ttyobiwan/jev-auto-mode/blob/f4006253741936d79dde4808b20fdbf41bcd9198/jev/judge.ts) at the pinned commit. |

## When to use

- Let a coding agent work with fewer permission prompts but keep risky actions blocked.
- Get a denial reason that tells the agent to pick a narrower action.
- Mismatch: OpenCode's explicit allow and deny rules still win.

## How it works

`jev/judge.ts` uses `@typesafe-ai/sdk` with yes/no rubric questions from `rubric.ts`; all harm scores must reach 0.80 and relevance 0.35 to allow a request. Integration evidence: [`jev/judge.ts`](https://github.com/ttyobiwan/jev-auto-mode/blob/f4006253741936d79dde4808b20fdbf41bcd9198/jev/judge.ts).

## Get started

From the upstream README (not run on the review host):

```sh
opencode plugin add github:ttyobiwan/jev-auto-mode
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ttyobiwan/jev-auto-mode#readme](https://github.com/ttyobiwan/jev-auto-mode#readme)

## Limits and data handling

Tool calls, diffs (up to 4,000 characters per string) and project paths are sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit f40062537419](https://github.com/ttyobiwan/jev-auto-mode/tree/f4006253741936d79dde4808b20fdbf41bcd9198). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
