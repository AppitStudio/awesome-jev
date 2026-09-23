# Paper Radar

[All projects](../README.md) · [Web apps](README.md#web-apps)

Daily arXiv paper radar: TypeSafe Jev judges every new paper against plain-English interests; publish a GitHub Pages digest, RSS, and optional chat/email digests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Eliot5566/JEV-Paper-Radar) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/Eliot5566/JEV-Paper-Radar#readme) — fork + GitHub Actions/Pages; optional local CLI. |
| Pricing and access | MIT source; no app purchase fee, checked **2026-09-23**. Needs `TYPESAFE_API_KEY` or OpenRouter (`typesafe/jev-1.13`) in Actions secrets / `.env`. Provider usage billed separately. Upstream cites ≈$0.06/day for full weekday arXiv as an author-measured estimate—not independently verified here. |
| Jev evidence | Inspected [`paper_radar/jev.py`](https://github.com/Eliot5566/JEV-Paper-Radar/blob/d55299b911ea4ada60912648158bf5258d99ccfa/paper_radar/jev.py) and HTTP tests [`tests/test_jev_http.py`](https://github.com/Eliot5566/JEV-Paper-Radar/blob/d55299b911ea4ada60912648158bf5258d99ccfa/tests/test_jev_http.py). Live arXiv/Jev runs were **not** executed on the review host. Distinct from [Jev Radar](jev-radar.md) (multi-step research workspace) and [jev-issue-radar](../tools/jev-issue-radar.md). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; `pip install`, Actions, and live Jev were **not** executed here. Cost/throughput figures are upstream-reported. |
| Maintainer | [Eliot5566](https://github.com/Eliot5566). |
| Format | Python package/CLI (`paper-radar`) + GitHub Actions workflow publishing Pages/`feed.xml`. |
| Platform and availability | Fork-and-run on GitHub; local CLI on Python with `pip install git+https://github.com/Eliot5566/JEV-Paper-Radar`. |
| Jev's role | Per-paper interest match probabilities (calibrated System One judgments). Optional separate LLM TL;DRs only for top papers. Code owns thresholds, digests, and site build. |
| Requirements | TypeSafe or OpenRouter key; GitHub Actions + Pages for the hosted digest path. |
| License | [MIT](https://github.com/Eliot5566/JEV-Paper-Radar/blob/d55299b911ea4ada60912648158bf5258d99ccfa/LICENSE). |

## When to use

Use it to **shortlist new arXiv papers** against interests you wrote in plain English, with tunable thresholds and an audit trail. Prefer [Jev Radar](jev-radar.md) for interactive multi-step web research, not daily arXiv firehose triage.

## How it works

`radar.toml` interests become Jev questions; each new paper is judged without generating labels. Results become a Pages site, RSS, and optional Slack/Discord/Telegram/email digests. `paper-radar demo` uses fictional papers and a keyword heuristic offline (no key).

## Get started

```sh
pip install git+https://github.com/Eliot5566/JEV-Paper-Radar
paper-radar demo          # offline fictional digest; no key
# Live (charges): configure .env / secrets, then
# paper-radar check
# paper-radar run --limit 50
```

Pin for review: [commit d55299b](https://github.com/Eliot5566/JEV-Paper-Radar/tree/d55299b911ea4ada60912648158bf5258d99ccfa). Fork + Actions enablement steps are in the upstream README.

## Examples and demos

- Upstream `docs/demo.png` and `paper-radar demo` offline site.
- `calibrate` / `check` commands for threshold and cost estimates (not run here).

## Limits and data handling

Paper titles/abstracts (and interest text) leave the host on live Jev calls. Optional TL;DR LLMs are separate. Author cost claims were not re-measured. Live arXiv pull not run here.

## Review and maintenance

Reviewed on **2026-09-23** at [commit d55299b](https://github.com/Eliot5566/JEV-Paper-Radar/tree/d55299b911ea4ada60912648158bf5258d99ccfa) (MIT). AI-assisted review of README, LICENSE, `paper_radar/jev.py`. No live TypeSafe/arXiv spend.

Related: [Jev Radar](jev-radar.md), [jev-issue-radar](../tools/jev-issue-radar.md).
