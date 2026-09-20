# clear-head

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code Stop hook that checks factual claims in the assistant’s answer against what it actually read this session, using TypeSafe Jev as the judge.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VladyslavHontar/clear-head) |
| Maintainer | [VladyslavHontar](https://github.com/VladyslavHontar). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python Stop-hook script (`stop_verify.py`) plus `install.sh` / `uninstall.sh`. |
| Requirements | Python 3; Claude Code; `TYPESAFE_API_KEY` (installer can write a local `.env`). |
| License | [MIT](https://github.com/VladyslavHontar/clear-head/blob/4d21f7a8bb4a057bea3938ae72ec580b68ac272d/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live Stop hooks and live Jev were not run. |

## When to use

Use it when assistants invent codebase facts with high confidence and you want an automatic end-of-turn check against session tool outputs. Prefer [Canny](canny.md) for ledger-backed “done without checks” gates, [jev-preflight](jev-preflight.md) for multi-axis risk on a turn diff, or [jev-guard](jev-guard.md) for per-tool-call risk scoring.

## How it works

[`stop_verify.py`](https://github.com/VladyslavHontar/clear-head/blob/4d21f7a8bb4a057bea3938ae72ec580b68ac272d/stop_verify.py) posts to `https://api.typesafe.ai/v1/systemone` with model `jev-latest`. It first classifies sentences as factual claims, then judges each claim against keyword-overlapping tool-output lines (not whole files), logging payloads to `sent.jsonl`. Contradicted or unsupported claims (above configurable thresholds) block the turn with a bullet list; `JEV_HOOK=off` disables for one shell. Optional `JEV_FAIL_CLOSED` follows the fail-closed pattern borrowed from jev-guard.

## Get started

```sh
git clone https://github.com/VladyslavHontar/clear-head.git
cd clear-head
git checkout 4d21f7a8bb4a057bea3938ae72ec580b68ac272d
./install.sh              # or ./install.sh --project
```

Installer verifies the TypeSafe key with a tiny Jev probe. Live stops send claim text and selected tool-output excerpts to TypeSafe and can incur charges. This listing did not install the hook or call live Jev beyond reading the installer probe code.

## Examples and demos

- README block message format (`[CONTRADICTED]` / `[UNSUPPORTED]`).
- Env-var tuning table (`JEV_CONTRA`, `JEV_THRESH`, `JEV_FACT`, …).

## Limits and data handling

Excerpts of code and session tool output leave the host for TypeSafe. Upstream warns not to install on repos you would not send to a third-party API. Threshold defaults may need per-repo tuning via `log.jsonl`.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 4d21f7a](https://github.com/VladyslavHontar/clear-head/tree/4d21f7a8bb4a057bea3938ae72ec580b68ac272d). AI-assisted source review of README, LICENSE, `stop_verify.py`, and install scripts. No live TypeSafe or Claude Code hook runs.

Related: [Canny](canny.md), [jev-preflight](jev-preflight.md), [jev-guard](jev-guard.md).
