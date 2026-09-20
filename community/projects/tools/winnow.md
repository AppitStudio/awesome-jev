# winnow

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Calibrated context sieve for Claude Code: every large tool result is judged by TypeSafe Jev (or a System One adapter) before it enters context; confident-no blocks become recallable stubs. Distinct from any Chrome read/skim “Winnow” tools.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/GhalebDweikat/winnow) |
| Maintainer | [GhalebDweikat](https://github.com/GhalebDweikat). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Claude Code function-hook plugin plus Python sidecar CLI **winnow 0.5.0** (`winnow serve` / `winnow doctor`). |
| Requirements | Python ≥ 3.10; [uv](https://docs.astral.sh/uv/); Claude Code with function hooks enabled; `TYPESAFE_API_KEY` for judge `typesafe`, or Anthropic credentials for judge `adapter`. |
| License | [MIT](https://github.com/GhalebDweikat/winnow/blob/51d80b945c74c8384bc47fa817179f668289afd8/LICENSE). TypeSafe or Anthropic usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; offline `pytest` run in the sidecar. Live Claude Code hooks and live TypeSafe/Anthropic judge calls were not run. |

## When to use

Use it when Claude Code sessions drown in large `Read` / `Bash` / `Grep` output and you want block-level keep/hide judgments with on-demand recall. Prefer [fast-jev-compaction](fast-jev-compaction.md) or [jev-pruner](jev-pruner.md) when you need different compaction or Bash-stdout pruning shapes. Do not treat measured calibration notes as a guarantee for your workload.

## How it works

A tool-call hook splits large results into ~25-line blocks and asks a yes/no relevance Noul per block. Default judge is TypeSafe Jev via [`sidecar/src/winnow/judge.py`](https://github.com/GhalebDweikat/winnow/blob/51d80b945c74c8384bc47fa817179f668289afd8/sidecar/src/winnow/judge.py) (`typesafe_sdk`); `WINNOW_JUDGE=adapter` uses TypeSafe’s `system-one-adapter` against Claude Haiku instead. Confident-no blocks are cached and replaced with a stub plus optional summary; error-looking output and uncertain probabilities stay verbatim. A prompt-time hook can inject ranked project memory files. Disk files and Claude’s transcript are not rewritten.

## Get started

```sh
git clone https://github.com/GhalebDweikat/winnow.git
cd winnow
git checkout 51d80b945c74c8384bc47fa817179f668289afd8
# Enable Claude Code function hooks, then follow upstream README install / winnow doctor
cd sidecar && uv sync && uv run pytest -q
```

Live judging needs a TypeSafe or Anthropic path as configured. This listing did not enable hooks in Claude Code or call TypeSafe.

## Examples and demos

- Upstream README quick start and measured replay notes under `docs/DESIGN.md` / `docs/results/` (not re-run here).
- Offline sidecar tests on the review host (see Review).
- `winnow demo --fake` for a judge-free local demo path (not executed on the review host).

## Limits and data handling

Judged tool output and short task context leave the host on every live TypeSafe or adapter call. Thresholds (`WINNOW_DROP` / `WINNOW_KEEP`) are tunable; defaults come from upstream labeling, not your data. Early-access Claude Code function hooks are required. Do not ship API keys in shared settings without review.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 51d80b9](https://github.com/GhalebDweikat/winnow/tree/51d80b945c74c8384bc47fa817179f668289afd8): **winnow 0.5.0**, MIT. AI-assisted source review of README, LICENSE, `judge.py`, hooks, and config. Ran `uv sync` and `uv run pytest -q` in `sidecar/`: **80 passed**. Live Claude Code / TypeSafe paths not executed.

Related: [jev-pruner](jev-pruner.md), [fast-jev-compaction](fast-jev-compaction.md), [Jev Sift](jev-sift.md), [clear-head](clear-head.md).
