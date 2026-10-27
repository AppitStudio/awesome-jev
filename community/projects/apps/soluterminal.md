# SoluTerminal (Windows workspace for Claude Code and Codex, with Jev smart approvals)

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Windows workspace that runs Claude Code and Codex side by side in PowerShell and WSL panes, keeps them running when the window closes, lets one agent ask another for a second opinion, and stops agents approving their own requests; Jev classifies each task into a tier and answers cautious permission prompts as smart approvals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/soluterminal/soluterminal) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://soluterminal.com/) |
| Pricing and access | Open source (Apache-2.0); the Windows app is free during beta per soluterminal.com (future pricing not published). With your own key, Jev calls are billed to your TypeSafe account. Checked 2026-10-27. |
| Jev evidence | [`daemon/jev/jev.go`](https://github.com/soluterminal/soluterminal/blob/354f51b1d6d0f041da9fd61458933cbf8aa92fb1/daemon/jev/jev.go) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [soluterminal](https://github.com/soluterminal). Independently curated. |
| Format | Windows desktop app (Go daemon with web UI) |
| Platform and availability | Windows; installer from soluterminal.com (free during beta) or build from source. |
| Jev's role | Tier classification and smart approvals: one Choice for the task tier and one Noul risk question, gated on confidence. |
| Requirements | Windows with Claude Code or Codex; a free SoluTerminal sign-in or your own TypeSafe API key for smart approvals. |
| License | [Apache-2.0](https://github.com/soluterminal/soluterminal/blob/354f51b1d6d0f041da9fd61458933cbf8aa92fb1/LICENSE) |

## When to use

- Run several coding agents on Windows with approvals you stay in charge of.
- Mismatch: Windows only; beta.

## How it works

`daemon/jev/jev.go` turns a task into a TypeSafe System One evaluation (`shared/typesafe/typesafe.go` posts to `https://api.typesafe.ai/v1/systemone`) and returns a tier verdict; low-confidence results fall back to you. Integration evidence: [`daemon/jev/jev.go`](https://github.com/soluterminal/soluterminal/blob/354f51b1d6d0f041da9fd61458933cbf8aa92fb1/daemon/jev/jev.go).

## Get started

From the upstream README (not run on the review host):

```sh
# Windows: download from https://soluterminal.com/download/
# from source:
cd web && npm ci && npm run build && cd ..
cd daemon && go build -o solud . && ./solud
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Help: [soluterminal.com/help/](https://soluterminal.com/help/)
- README: [github.com/soluterminal/soluterminal#readme](https://github.com/soluterminal/soluterminal#readme)

## Limits and data handling

Task and permission context goes to TypeSafe (directly or via the signed-in service) for smart approvals. See the project's [privacy page](https://soluterminal.com/privacy/).

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 354f51b1d6d0](https://github.com/soluterminal/soluterminal/tree/354f51b1d6d0f041da9fd61458933cbf8aa92fb1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
