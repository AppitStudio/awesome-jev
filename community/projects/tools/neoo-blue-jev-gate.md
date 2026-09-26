# jev-gate (Neoo-Blue)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plan/result gate—Jev verifies scope before build and before stop.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Neoo-Blue/jev-gate) |
| Maintainer | [Neoo-Blue](https://github.com/Neoo-Blue). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Claude Code marketplace plugin with PreToolUse/Stop hooks. |
| Requirements | Python 3 on PATH; `TYPESAFE_API_KEY`; Claude Code plugin install. |
| License | [MIT](https://github.com/Neoo-Blue/jev-gate/blob/b58cfac01bd6edde523835dc6dc8df5a2a6aeb0a/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when you want Claude Code kept honest about delivering the full requested scope.

## How it works

Cuts request/plan/summary into items; one batched Jev request per check; failed items quoted back for fix rounds (fail-open on API errors). Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
claude plugin marketplace add Neoo-Blue/jev-gate
claude plugin install jev-gate@jev-gate
export TYPESAFE_API_KEY=…
python3 scripts/test_jev_gate.py
```

Pin revision `b58cfac01bd6edde523835dc6dc8df5a2a6aeb0a` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Judges summaries, not code correctness. Bash edits not blocked by PreToolUse. Live Claude/TypeSafe path not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit b58cfac](https://github.com/Neoo-Blue/jev-gate/tree/b58cfac01bd6edde523835dc6dc8df5a2a6aeb0a). AI-assisted README and LICENSE inspection; install/live paths not executed.
