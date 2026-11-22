# jev-gate by Akkshar (Claude Code hook that risk-scores every shell command, with snapshots so approving is reversible)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A Claude Code `PreToolUse` hook for Bash and PowerShell: regex layers allow read-only commands and deny or ask on known destructive ones, and a pluggable model scores everything else for destructiveness, category, changes outside the working folder and secret exposure. Before an `ask` it snapshots the folder with unrun so a yes can be undone, and it learns from what you approve. It never returns `allow` by default.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Akkshar/jev-gate) |
| Maintainer | [Akkshar](https://github.com/Akkshar). Independently curated. |
| Format | Python hook script (Claude Code PreToolUse/PostToolUse) |
| Requirements | Claude Code and Python (run through uv); a model backend: a local distilled classifier (offline), Groq's free tier (default) or Jev with `TYPESAFE_API_KEY`; unrun is optional. |
| License | [MIT](https://github.com/Akkshar/jev-gate/blob/6c059de8da44ad33b2a3a48f3720c2ca25ce623f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`gate.py`](https://github.com/Akkshar/jev-gate/blob/6c059de8da44ad33b2a3a48f3720c2ca25ce623f/gate.py) at the pinned commit. |

## When to use

- An extra, explainable risk check on the shell commands an AI agent runs, with undo for approved changes.
- Mismatch: a hard security boundary; failures fail open unless `strict` is set, and Claude Code's own permissions still apply.

## How it works

With the `jev` backend, `gate.py` sends the redacted command to `https://api.typesafe.ai/v1/systemone` and asks a `score` for destructiveness (0–3), a `choice` for category and `noul` questions for outside-cwd and secret exposure; every backend returns the same shape, so the decision policy and log do not change. Integration evidence: [`gate.py`](https://github.com/Akkshar/jev-gate/blob/6c059de8da44ad33b2a3a48f3720c2ca25ce623f/gate.py).

## Get started

Clone it, choose a backend in `config.json` (set `"backend": "jev"` and `TYPESAFE_API_KEY` for Jev), and register the hooks in `~/.claude/settings.json`; dry-run a command first.

```sh
git clone https://github.com/Akkshar/jev-gate && cd jev-gate
export TYPESAFE_API_KEY=...
python gate.py --check "rm -rf build" --backend jev   # dry-run one command
python gate.py --tail 20
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Unrun (snapshots): [github.com/Akkshar/unrun](https://github.com/Akkshar/unrun)
- README backends table: [github.com/Akkshar/jev-gate/blob/6c059de8da44ad33b2a3a48f3720c2ca25ce623f/README.md](https://github.com/Akkshar/jev-gate/blob/6c059de8da44ad33b2a3a48f3720c2ca25ce623f/README.md)

## Limits and data handling

Secrets are redacted and commands capped at 6,000 characters before anything is sent to the chosen backend. Jev is one of three model backends and not the default (Groq is). Decisions and feedback are logged locally.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 6c059de8da44](https://github.com/Akkshar/jev-gate/tree/6c059de8da44ad33b2a3a48f3720c2ca25ce623f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
