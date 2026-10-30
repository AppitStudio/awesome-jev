# s1flow (choose, ship and fix decision models such as Jev on your own labelled data, driven from your coding agent)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI and agent skill for picking a decision model by measuring it: describe the decision in plain words, let your coding agent collect labelled cases, compare models such as Jev, D1, Clef and OpenAI Decisions on accuracy and coverage at a confidence threshold, and save the winner as a policy file your app loads with a small client. Includes a benchmark app with reports across 13 to 21 models and an optional CI check.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gotalab/s1flow) |
| Maintainer | [gotalab](https://github.com/gotalab). Independently curated. |
| Format | Python CLI, library and Claude Code / Codex skill |
| Requirements | Python 3.13+; an OpenRouter key for the default line-up (or provider keys); the gh CLI for the GitHub-issues example. |
| License | [Apache-2.0](https://github.com/gotalab/s1flow/blob/81a305383e63c85d707e294d478016480d170248/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/s1flow/client/providers/openrouter.py`](https://github.com/gotalab/s1flow/blob/81a305383e63c85d707e294d478016480d170248/src/s1flow/client/providers/openrouter.py) at the pinned commit. |

## When to use

- Decide which decision model and threshold to use for one task with your own data instead of a leaderboard.
- Mismatch: needs labelled examples to be meaningful; results are snapshots, not rankings.

## How it works

`src/s1flow/client/providers/openrouter.py` sends typed questions to each model, including TypeSafe Jev, and `src/s1flow/client/_client.py` applies the saved policy's threshold at run time. Integration evidence: [`src/s1flow/client/providers/openrouter.py`](https://github.com/gotalab/s1flow/blob/81a305383e63c85d707e294d478016480d170248/src/s1flow/client/providers/openrouter.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv tool install "s1flow[eval]"
# in Claude Code:
/plugin marketplace add gotalab/s1flow
/plugin install s1flow@s1flow
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmark reports: [github.com/gotalab/s1flow/tree/main/apps/bench/reports](https://github.com/gotalab/s1flow/tree/main/apps/bench/reports)

## Limits and data handling

Your labelled cases are sent to every model you compare, through OpenRouter or the providers you configure.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 81a305383e63](https://github.com/gotalab/s1flow/tree/81a305383e63c85d707e294d478016480d170248). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
