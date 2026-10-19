# agent-test-pruning

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Scripts and data for the paper "Which Tests to Keep When a Coding Agent Writes the Test Suite": replays of Claude Code writing tests, planted and real bugs, and pruning signals including four facet questions asked of Jev per test.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/olegpustovit/agent-test-pruning) |
| Maintainer | [olegpustovit](https://github.com/olegpustovit). Independently curated. |
| Format | Python scripts + datasets |
| Requirements | Python with uv; Claude Code for replays and grading; `JEV_API_KEY` for the Jev facets. |
| License | [MIT](https://github.com/olegpustovit/agent-test-pruning/blob/4e59ffec9791f5873fe01cc5f8855d78429148c0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`code/tool/jev.py`](https://github.com/olegpustovit/agent-test-pruning/blob/4e59ffec9791f5873fe01cc5f8855d78429148c0/code/tool/jev.py) at the pinned commit. |

## When to use

- Decide which agent-written tests to keep under a budget.
- Compare Jev typed judgments against coverage and CI signals.
- Mismatch: research artifact for a paper, not a drop-in CI tool.

## How it works

`code/tool/jev.py` is a Jev (TypeSafe System One) client and CLI for typed questions; `jev_typed.py` and `jev_facets.json` ask four facet questions per test. `testprune.py` orders tests by coverage, risk reach, judge and combined signals and scores them against mutant and real-bug kill sets. Integration evidence: [`code/tool/jev.py`](https://github.com/olegpustovit/agent-test-pruning/blob/4e59ffec9791f5873fe01cc5f8855d78429148c0/code/tool/jev.py).

## Get started

From the upstream README: run each script with `uv run <script>.py --help`.

```sh
git clone https://github.com/olegpustovit/agent-test-pruning && cd agent-test-pruning
uv run code/tool/testprune.py --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- SUBJECTS.md
- data/ (grades, jev-facets.jsonl, stats)

## Limits and data handling

Test code goes to TypeSafe when computing Jev facets. Findings come from a small set of subject projects.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 4e59ffec9791](https://github.com/olegpustovit/agent-test-pruning/tree/4e59ffec9791f5873fe01cc5f8855d78429148c0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
