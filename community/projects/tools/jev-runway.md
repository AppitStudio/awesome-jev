# Jev Runway

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local proxy for Codex that asks TypeSafe Jev which old tool outputs the session still needs and trims the rest before each provider request.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/IPECTER/jev-runway) |
| Maintainer | [IPECTER](https://github.com/IPECTER). Independently curated. |
| Format | npm CLI / self-contained binary (`jev-runway`). |
| Requirements | macOS or Linux; Node once for `npx` install; Codex CLI/desktop; TypeSafe or Vercel AI Gateway Jev key. |
| License | [MIT](https://github.com/IPECTER/jev-runway/blob/bcd0a95c7e64070ba2faee05e6f38145f0212bf5/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Codex+Jev not run. |

## When to use

Use to **cut token spend** on long Codex sessions by trimming stale tool output under Jev judgments. Prefer [jev-pruner](jev-pruner.md) for Claude Code Bash stdout pruning.

## How it works

Between turns, Runway asks Jev which tool outputs still matter; on the next request it shortens the rest while keeping call metadata and saving trimmed bodies locally (per README). Fails open if Jev is unavailable.

## Get started

```sh
npx jev-runway install
jev-runway status
```

Pin tip `bcd0a95c7e64070ba2faee05e6f38145f0212bf5`.

## Examples and demos

- README replay claims on sample sessions; bilingual README.ko.md.

## Limits and data handling

Tool outputs and task context reach the Jev provider. Trimmed data stays on disk for recall.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit bcd0a95](https://github.com/IPECTER/jev-runway/tree/bcd0a95c7e64070ba2faee05e6f38145f0212bf5). AI-assisted README inspection; live provider path not run.

Related: [jev-pruner](jev-pruner.md).
