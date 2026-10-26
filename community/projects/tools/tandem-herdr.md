# tandem (paired planner and builder agents under Herdr, with an optional Jev judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Herdr harness where Claude Code plans, a builder agent (Codex, Claude, Copilot or OpenCode) implements in the same checkout, and a separate reviewer checks every plan and task; an optional Jev judge, pinned to `jev-1.13.0`, gives typed verdicts on handoffs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/emsnoel/tandem) |
| Maintainer | [emsnoel](https://github.com/emsnoel). Independently curated. |
| Format | Go binary and shell commands for Herdr |
| Requirements | Herdr, the agent CLIs you use, curl, tar, jq and shasum; a TypeSafe key only for the optional judge. |
| License | [MIT](https://github.com/emsnoel/tandem/blob/64a1c10b9bcdedaa387e4d180610929ea6fc3fb5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/decision/jev/client.go`](https://github.com/emsnoel/tandem/blob/64a1c10b9bcdedaa387e4d180610929ea6fc3fb5/internal/decision/jev/client.go) at the pinned commit. |

## When to use

- Run a planner, builder and reviewer on one branch without merging worktrees.
- Add a cheap typed check to agent handoffs when you want one.
- Mismatch: Jev is off unless you enable the judge (`HERDR_JUDGE=1`).

## How it works

`internal/decision/jev/client.go` posts handoff state and questions to `https://api.typesafe.ai/v1/systemone` with the model pinned in `internal/decision/contract.go`; the judge runs only when enabled and a key is set. Integration evidence: [`internal/decision/jev/client.go`](https://github.com/emsnoel/tandem/blob/64a1c10b9bcdedaa387e4d180610929ea6fc3fb5/internal/decision/jev/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/emsnoel/tandem/main/install.sh | bash
# optional: export TYPESAFE_API_KEY=... and HERDR_JUDGE=1
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/emsnoel/tandem#readme](https://github.com/emsnoel/tandem#readme)
- Release v0.1.0: [github.com/emsnoel/tandem/releases/tag/v0.1.0](https://github.com/emsnoel/tandem/releases/tag/v0.1.0)

## Limits and data handling

With the judge on, handoff summaries go to TypeSafe. Agent CLIs send code to their own providers.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 64a1c10b9bcd](https://github.com/emsnoel/tandem/tree/64a1c10b9bcdedaa387e4d180610929ea6fc3fb5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
