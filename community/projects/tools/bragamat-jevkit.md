# jevkit (bragamat)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unofficial `jev` CLI (Homebrew, Scoop, install script) that puts TypeSafe Jev in a coding agent's toolbox: `find`/`check` to read less, `decide`/`yesno`/`score` with ACT/CONFIRM/REPHRASE verdicts tuned to risk, and a local gateway that predicts the next tool for Claude Code or Codex; distinct from the other jevkit listing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bragamat/jevkit) |
| Maintainer | [bragamat](https://github.com/bragamat). Independently curated. |
| Format | CLI binary (Linux, macOS, Windows; amd64/arm64), Agent Skill, Claude Code plugin |
| Requirements | `TYPESAFE_API_KEY` (default model pinned to `jev-1.13.0`). |
| License | [MIT](https://github.com/bragamat/jevkit/blob/3162889b2f160799a80c76865abedad541691e99/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Cut context spend: ask Jev where an answer is in a large file and read only those lines.
- Make agent judgment calls explicit with risk-tuned thresholds (`--risk high` needs 0.90 to ACT).
- Mismatch: unofficial community tool; the gateway rewrites requests to your LLM, so review it before routing production agent traffic.

## How it works

`decide`, `pick` and `find` ask each choice in two option orders in one request and average them (upstream notes jev-1.13 leans to the first option); inconsistent orders demote ACT to CONFIRM. Bands follow TypeSafe's confidence guidance. `jev gateway` (ports 8789/8790) asks Jev which tool the next step needs and steers only when confident; any Jev error, timeout or low confidence passes the request through unchanged. Usage and decisions are logged to `$XDG_STATE_HOME/jev/`.

## Get started

Install, export the key, and try a decision (live TypeSafe calls):

```sh
brew install --cask bragamat/tap/jev
export TYPESAFE_API_KEY=...
jev decide "Is this failure caused by the change under review?" yes no=pre-existing \
  --ctx failing-test.log --risk high
claude plugin marketplace add bragamat/jevkit && claude plugin install jevkit@jevkit
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README *Deciding* and *Gateway* sections with sample output.
- [Agent Skill](https://github.com/bragamat/jevkit/blob/3162889b2f160799a80c76865abedad541691e99/skills/jev-cli/SKILL.md) teaching agents when to use `find`, `check` and `decide` (release v0.3.2).

## Limits and data handling

Unofficial; not affiliated with TypeSafe. Evidence passed with `--ctx` (capped at 60,000 characters) and gateway conversation context are sent to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 3162889b2f16](https://github.com/bragamat/jevkit/tree/3162889b2f160799a80c76865abedad541691e99). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
