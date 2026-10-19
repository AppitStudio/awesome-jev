# Job Matcher (MCP server)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local MCP server and JSON CLI that gives Claude Code, Claude Desktop, Cursor or Codex a memory and judgment for your job search: it finds postings on public job boards for companies you add and has Jev evaluate and rank them against your profile, with blockers and concerns spelled out.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/thefotes/job-matcher) |
| Maintainer | [thefotes](https://github.com/thefotes). Independently curated. |
| Format | MCP server + CLI (Python 3.12, uv, SQLite) |
| Requirements | Python 3.12+, uv and a TypeSafe API key (about 5,000 input tokens per job evaluated). |
| License | [MIT](https://github.com/thefotes/job-matcher/blob/1b5d76bd1aba4c1fb206849c3c403d487dd39300/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/job_matcher/provider.py`](https://github.com/thefotes/job-matcher/blob/1b5d76bd1aba4c1fb206849c3c403d487dd39300/src/job_matcher/provider.py) at the pinned commit. |

## When to use

- Run a daily ranked report of new postings that fit your profile and dealbreakers.
- Keep track of jobs seen, saved, applied to or dismissed.
- Mismatch: interview topics and weights currently assume engineering roles.

## How it works

Your resume, targets and dealbreakers are stored locally in SQLite. Postings come from Greenhouse, Ashby, Lever, SmartRecruiters, Recruitee and Workday boards. `src/job_matcher/provider.py` sends each posting with your profile to Jev under a strictness setting you choose; evaluation is the only step that sends data off your machine. Integration evidence: [`src/job_matcher/provider.py`](https://github.com/thefotes/job-matcher/blob/1b5d76bd1aba4c1fb206849c3c403d487dd39300/src/job_matcher/provider.py).

## Get started

From the upstream README: clone, set your TypeSafe key, then initialise a profile from your resume.

```sh
git clone https://github.com/thefotes/job-matcher.git && cd job-matcher
uv run --no-sync job-matcher init --resume /absolute/path/to/resume.txt
uv run --no-sync job-matcher batch --input examples/jobs.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- examples/jobs.json
- docs/open-source-readiness.md

## Limits and data handling

Profile and posting text go to TypeSafe during evaluation (see the README Consent section). Rankings are model judgments; applying stays with you.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 1b5d76bd1aba](https://github.com/thefotes/job-matcher/tree/1b5d76bd1aba4c1fb206849c3c403d487dd39300). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
