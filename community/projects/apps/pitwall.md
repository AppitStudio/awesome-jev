# pitwall

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Native terminal multiplexer for coding agents (live status, persistent sessions, tabs/panes) that can connect TypeSafe Jev (`pitwall jev login`) to answer quick questions about your agents: is this permission request safe, how urgent is this pane, has a hook-less agent finished, does this turn need review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/quanticstudios/pitwall) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/quanticstudios/pitwall#readme); binaries on [GitHub Releases](https://github.com/quanticstudios/pitwall/releases). |
| Pricing and access | Free MIT binaries (alpha releases) via install script. Jev decisions need your own TypeSafe key; usage billed by TypeSafe. Checked 2026-10-06. |
| Jev evidence | README [*Decisions (Jev)*](https://github.com/quanticstudios/pitwall/blob/b82196c1c4a3dda2f80b878948453033211ac5e1/README.md#decisions-jev) documents login/status/logout, the four features, what each sends and the redaction applied first; source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [quanticstudios](https://github.com/quanticstudios). Independently curated. |
| Format | Terminal app (TUI) with agent hooks |
| Platform and availability | Linux, macOS and Windows (PowerShell installer). |
| Jev's role | Optional decision provider for approvals (suggest by default), attention triage (fyi/later/soon/now), screen-reading state for agents without hooks, and turn checks; everything else works without it. |
| Requirements | Claude Code, Codex or other terminal agents; your own TypeSafe key for decisions. |
| License | [MIT](https://github.com/quanticstudios/pitwall/blob/b82196c1c4a3dda2f80b878948453033211ac5e1/LICENSE). |

## When to use

- Supervise several coding agents in one terminal and jump to the pane that needs you most urgently.
- Get a calibrated safety suggestion on agent permission prompts before you approve them.
- Mismatch: alpha releases; approvals default to suggestions, so you still decide.

## How it works

`pitwall jev login` stores the key (0600, private folder) and sets `provider = "jev"` under `[decisions]`; triage is on and approvals suggest, while screen reading and turn checks stay off until enabled. Before anything leaves the machine pitwall strips secret-looking content (keys, auth headers, tokens, passwords in URLs, your TypeSafe key) and trims text, then asks Jev typed questions; answers set pills, switcher order and notifications when confidence reaches the configured thresholds.

## Get started

Install, connect Jev, and check the connection (`status` makes one small real call):

```sh
curl -fsSL https://raw.githubusercontent.com/quanticstudios/pitwall/main/scripts/get.sh | sh
pitwall jev login     # key without echo
pitwall jev status    # one small live call
pitwall hooks install
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README feature table: approvals, attention triage, agents without hooks, turn check — with what each sends and when.
- `pitwall logs -f` to follow decision and app logs.

## Limits and data handling

Redaction is pattern matching, not a guarantee (upstream statement); pane text and agent context are sent to TypeSafe when features are on. Windows credentials inherit AppData permissions. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit b82196c1c4a3](https://github.com/quanticstudios/pitwall/tree/b82196c1c4a3dda2f80b878948453033211ac5e1). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
