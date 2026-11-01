# ljos (shared memory, tickets and ballots for coding agents, with Jev as an optional judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Machine-wide tool for Claude Code, Codex, Cursor and other coding agents: a git-backed ticket tracker, rules you tell it once that come back when relevant, ballots between agents, and a policy check for ruled-out shell commands. Jev is optional and off by default; when enabled it answers which memories, ballots and claims apply.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/leidarljos/ljos) |
| Maintainer | [leidarljos](https://github.com/leidarljos). Independently curated. |
| Format | Rust CLI and daemons (release installer or `cargo binstall`) |
| Requirements | macOS or Linux; optional TypeSafe or OpenRouter key in `~/.config/ljos/jev.toml`. |
| License | [MIT](https://github.com/leidarljos/ljos/blob/03d1b067059b7daec5abe6e0f12eacb6f9e83854/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/ljos-cli/src/jev.rs`](https://github.com/leidarljos/ljos/blob/03d1b067059b7daec5abe6e0f12eacb6f9e83854/crates/ljos-cli/src/jev.rs) at the pinned commit. |

## When to use

- Give several coding agents shared rules and memory on one machine.
- Mismatch: Jev is optional; without the config file ljos calls no model.

## How it works

`crates/ljos-cli/src/jev.rs` sends the prompt hook's judgments (which candidate memory or claim is relevant, which statement is true) to Jev over TypeSafe's API or OpenRouter's Decisions API; ballots Jev casts are recorded as `judge:MODEL`. Integration evidence: [`crates/ljos-cli/src/jev.rs`](https://github.com/leidarljos/ljos/blob/03d1b067059b7daec5abe6e0f12eacb6f9e83854/crates/ljos-cli/src/jev.rs).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSLO https://github.com/leidarljos/ljos/releases/latest/download/install.sh && sh install.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project site: [leidarljos.github.io/](https://leidarljos.github.io/)

## Limits and data handling

With Jev enabled, judged text is sent to TypeSafe or OpenRouter. The policy check is not a sandbox, as the README states. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 03d1b067059b](https://github.com/leidarljos/ljos/tree/03d1b067059b7daec5abe6e0f12eacb6f9e83854). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
