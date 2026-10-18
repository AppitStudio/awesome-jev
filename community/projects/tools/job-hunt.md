# job-hunt

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Local job-search pipeline that fetches LinkedIn and Greenhouse, Ashby, and Personio postings, scores each against your plain-text profile with Jev through OpenRouter (fit 0 to 100, verdict, five typed reasons), and appends new openings to a CSV.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rdbeltrao/job-hunt) |
| Maintainer | [rdbeltrao](https://github.com/rdbeltrao). Independently curated. |
| Format | Python CLI (uv) |
| Requirements | Python, uv, an OpenRouter key with the TypeSafe provider; a browser session for LinkedIn. |
| License | [MIT](https://github.com/rdbeltrao/job-hunt/blob/a281e4a57fcb52ca5876661655f25d9cb2a167de/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jobs/scoring/jev.py`](https://github.com/rdbeltrao/job-hunt/blob/a281e4a57fcb52ca5876661655f25d9cb2a167de/jobs/scoring/jev.py) at the pinned commit. |

## When to use

- Score job postings with typed reasons instead of keyword filters.
- Mismatch: LinkedIn fetching runs as you in a real browser; check site terms.

## How it works

`jobs/scoring/jev.py` sends a posting and your profile to `typesafe/jev-1.13` and stores the fit score, verdict, and reasons; it falls back to an LLM scorer if the provider is unreachable. Integration evidence: [`jobs/scoring/jev.py`](https://github.com/rdbeltrao/job-hunt/blob/a281e4a57fcb52ca5876661655f25d9cb2a167de/jobs/scoring/jev.py).

## Get started

From the upstream README: copy the example profile and search files, set your key, then run the pipeline.

```sh
cp profile.example.md profile.md
uv run python -m jobs run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README output fields

## Limits and data handling

Posting text and your profile go to OpenRouter and TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit a281e4a57fcb](https://github.com/rdbeltrao/job-hunt/tree/a281e4a57fcb52ca5876661655f25d9cb2a167de). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
