# Bulma by ruverd (software factory for coding agents that asks Jev at its judgment calls)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Software factory that runs inside Claude Code, Codex, Cursor or Grok: one `/bulma` command picks the next piece of work and takes a ticket from plan to a tested pull request (spec, TDD, CI, browser QA with recorded evidence), then waits for you to merge. Most steps follow fixed rules; at a few forks (which stage fits a free-text request, whether a change is risky, whether a QA failure is clear) it asks Jev, uses the answer only above a confidence you set, and logs it next to what the fixed rule would have done so `/bulma report` shows where Jev deserves more say. Shadow mode lets you watch before trusting it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ruverd/bulma) |
| Maintainer | [ruverd](https://github.com/ruverd). Independently curated. |
| Format | Agent skills and Python scripts with an installer (MIT) |
| Requirements | macOS, Linux or WSL; git, curl, Python 3.9+, GitHub CLI (or glab), agent-browser, a supported coding agent, and `TYPESAFE_API_KEY` for `/bulma` itself. |
| License | [MIT](https://github.com/ruverd/bulma/blob/f9fc009fe22face91bb74a714e022150a14a842d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/bulma/scripts/bulma.py`](https://github.com/ruverd/bulma/blob/f9fc009fe22face91bb74a714e022150a14a842d/skills/bulma/scripts/bulma.py) at the pinned commit. |

## When to use

- Run tickets through a fixed delivery process where Jev only arbitrates the judgment calls, with an audit trail.
- Mismatch: a hands-off autonomous merger; Bulma stops at the pull request for you to merge.

## How it works

`skills/bulma/scripts/bulma.py` posts each hook's state and the node's options to `https://api.typesafe.ai/v1/systemone` (default model `jev-1.14.0`); `skills/bulma/HOOKS.md` and `skills/bulma/decisions.json` list every point where it asks. Integration evidence: [`skills/bulma/scripts/bulma.py`](https://github.com/ruverd/bulma/blob/f9fc009fe22face91bb74a714e022150a14a842d/skills/bulma/scripts/bulma.py).

## Get started

Run the installer, add your TypeSafe key, restart your coding agent and start in shadow mode.

```sh
curl -fsSL https://raw.githubusercontent.com/ruverd/bulma/main/install.sh | bash
export TYPESAFE_API_KEY=...
# in your coding agent:
/bulma doctor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ruverd/bulma/blob/f9fc009fe22face91bb74a714e022150a14a842d/README.md](https://github.com/ruverd/bulma/blob/f9fc009fe22face91bb74a714e022150a14a842d/README.md)
- How it works: [github.com/ruverd/bulma/blob/f9fc009fe22face91bb74a714e022150a14a842d/docs/how-it-works.md](https://github.com/ruverd/bulma/blob/f9fc009fe22face91bb74a714e022150a14a842d/docs/how-it-works.md)

## Limits and data handling

Ticket text, file paths, review comments, CI log tails and QA findings are sent to TypeSafe at Jev hooks (REQUIREMENTS.md lists what is removed first). Without the key `/bulma` stops, though the underlying graphs still run.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit f9fc009fe22f](https://github.com/ruverd/bulma/tree/f9fc009fe22face91bb74a714e022150a14a842d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
