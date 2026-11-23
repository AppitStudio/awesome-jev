# Jev Code Review by zavaii (offline-first, budget-bounded Python CLI that screens committed code with Jev as a first-pass reviewer)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Prepare review requests from a Git commit offline, inspect them, then send them to Jev only when you pass `--live`, with a per-preparation budget and request cap. Each rubric item (input validation, path boundaries, command injection, secret exposure, duplicate side effects, hidden failures, races, value-flow errors) returns violation, no_violation or insufficient with a probability, as review candidates rather than confirmed bugs. Korean README.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zavaii/jev-code-review) |
| Maintainer | [zavaii](https://github.com/zavaii). Independently curated. |
| Format | Python CLI (standard library only) |
| Requirements | Python 3.10+ and Git on macOS or Linux (WSL on Windows); a TypeSafe API key and credits for live runs. |
| License | [MIT](https://github.com/zavaii/jev-code-review/blob/14d9a24517cd60294d4a43bc84a67b58936a664a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`review.py`](https://github.com/zavaii/jev-code-review/blob/14d9a24517cd60294d4a43bc84a67b58936a664a/review.py) at the pinned commit. |

## When to use

- Get a cheap, budget-capped first pass over committed code that a person or agent then verifies.
- Mismatch: proof that code is safe; results are candidates, and only committed files are read.

## How it works

`review.py` sends requests only to the fixed `https://api.typesafe.ai/v1/systemone` (redirects refused) with model `jev-1.14.0` pinned, reserves a worst-case cost before each request, records completed requests so they are not re-sent, and never retries failures automatically. Integration evidence: [`review.py`](https://github.com/zavaii/jev-code-review/blob/14d9a24517cd60294d4a43bc84a67b58936a664a/review.py).

## Get started

Prepare requests offline, check them, then make a small live run with a budget cap.

```sh
git clone https://github.com/zavaii/jev-code-review.git && cd jev-code-review
cp .env.example .env && chmod 600 .env   # TYPESAFE_API_KEY=...
python3 review.py prepare --repo ../your-project --ref HEAD
python3 review.py run runs/<preparation> --live --budget-usd 0.05 --max-requests 5
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Default rubric: [github.com/zavaii/jev-code-review/blob/14d9a24517cd60294d4a43bc84a67b58936a664a/rubric.json](https://github.com/zavaii/jev-code-review/blob/14d9a24517cd60294d4a43bc84a67b58936a664a/rubric.json)

## Limits and data handling

With `--live`, code excerpts are sent to TypeSafe. The secret filter is pattern-based and can miss secrets; check the prepared requests first. The budget is per preparation, not an account hard cap.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 14d9a24517cd](https://github.com/zavaii/jev-code-review/tree/14d9a24517cd60294d4a43bc84a67b58936a664a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
