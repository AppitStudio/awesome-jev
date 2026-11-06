# routr (hand coding work across your existing AI CLI subscriptions with Jev triage questions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Terminal orchestrator that lets a lead coding agent farm tasks to Claude Code, Codex, Cursor, Antigravity or Kiro workers you already pay for (via herdr panes or headless CLIs). Before and after each handoff, TypeSafe Jev (or Cloudflare Clef) answers fixed yes/no triage questions; code adds live subscription usage.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sirkirby/routr) |
| Maintainer | [sirkirby](https://github.com/sirkirby). Independently curated. |
| Format | Node.js TUI/orchestrator (MIT) |
| Requirements | Installed coding CLIs you already use, optional herdr, and a TypeSafe or Clef decision path. |
| License | [MIT](https://github.com/sirkirby/routr/blob/4ea3c8dd0fa3ef7ff041a4dd23705984035b7bf7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lib/systemone.mjs`](https://github.com/sirkirby/routr/blob/4ea3c8dd0fa3ef7ff041a4dd23705984035b7bf7/src/lib/systemone.mjs) at the pinned commit. |

## When to use

- Spread work across multiple coding subscriptions without a new proxy account.
- Triage brief difficulty and report quality with calibrated questions.
- Mismatch: workers are your local CLIs; decision keys are separate and optional if you self-host Clef.

## How it works

`src/lib/systemone.mjs` calls TypeSafe Jev (default) or Clef with a fixed question set tuned on real briefs and worker reports. Integration evidence: [`src/lib/systemone.mjs`](https://github.com/sirkirby/routr/blob/4ea3c8dd0fa3ef7ff041a4dd23705984035b7bf7/src/lib/systemone.mjs).

## Get started

Install per the README, point at your CLIs, and optionally set a TypeSafe key.

```sh
git clone https://github.com/sirkirby/routr.git && cd routr
# follow README install
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/sirkirby/routr/blob/4ea3c8dd0fa3ef7ff041a4dd23705984035b7bf7/README.md](https://github.com/sirkirby/routr/blob/4ea3c8dd0fa3ef7ff041a4dd23705984035b7bf7/README.md)

## Limits and data handling

Brief and report text used in triage questions are sent to the decision provider on your key.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 4ea3c8dd0fa3](https://github.com/sirkirby/routr/tree/4ea3c8dd0fa3ef7ff041a4dd23705984035b7bf7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
