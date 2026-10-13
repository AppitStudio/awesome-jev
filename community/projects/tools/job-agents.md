# job-agents

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Three spec-driven agents that collect job postings, score resumes against them, and email a daily digest; TypeSafe Jev gates new postings on location, role fit and resume variant.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/senthilsweb/job-agents) |
| Maintainer | [senthilsweb](https://github.com/senthilsweb). Independently curated. |
| Format | Python services (six Docker images) |
| Requirements | Docker; TypeSafe key; email credentials for digests. |
| License | [Apache-2.0](https://github.com/senthilsweb/job-agents/blob/43044dbdb3b9fcd7bc8715cff1952733378dfae0/LICENSE) |
| Jev evidence | [`job-pilot/pipeline/jev.py`](https://github.com/senthilsweb/job-agents/blob/43044dbdb3b9fcd7bc8715cff1952733378dfae0/job-pilot/pipeline/jev.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Automate a personal daily job digest with a cheap typed pre-filter.
- Mismatch: opinionated pipeline; scoring in job-matcher is deterministic, Jev only gates.

## How it works

job-scout publishes daily postings; job-pilot asks Jev typed questions per new job, sends survivors to job-matcher for scoring, and emails a digest with cover letters. (Summarized from the upstream [README](https://github.com/senthilsweb/job-agents/blob/43044dbdb3b9fcd7bc8715cff1952733378dfae0/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow the docs site / README to run the images with your config.

## Limits and data handling

Posting text and resume variant choices go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 43044dbdb3b9](https://github.com/senthilsweb/job-agents/tree/43044dbdb3b9fcd7bc8715cff1952733378dfae0). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
