# Theseus by Joe Harris (pull-request reviewer that blocks merges until the exact commit passed review, with Jev sizing each PR)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python pull-request reviewer (`theseus-reviewer`) that runs AI reviews inside the OMP coding-agent CLI in a read-only session and blocks merging until a review of the exact commit being merged has passed. Jev is the classifier: it sizes each PR (trivial to max), picks routine or deep capability and the review template (standard, deep or gate), and decides whether to retry, escalate or stop when a reviewer fails. Runs as GitHub workflows or locally, with key rotation helpers and an eval suite.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/joeharris76/theseus) |
| Maintainer | [joeharris76](https://github.com/joeharris76). Independently curated. |
| Format | Python package and CLI (`theseus`) |
| Requirements | Python 3.11+, the OMP coding-agent CLI with model access for the reviews, a GitHub App and repository policy for gating, and `TYPESAFE_API_KEY` for the classifier (OpenAI Decisions can be set as a fallback). |
| License | [MIT](https://github.com/joeharris76/theseus/blob/976917576298553a818d48d1bcbbf8628c81c248/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/joeharris76/status/2123207119453262038)). |
| Jev evidence | [`src/theseus_reviewer/jev.py`](https://github.com/joeharris76/theseus/blob/976917576298553a818d48d1bcbbf8628c81c248/src/theseus_reviewer/jev.py) at the pinned commit. |

## When to use

- Gate merges on an AI review of the exact commit, with a cheap Jev call deciding how deep each review should go.
- Mismatch: a drop-in GitHub bot; it needs OMP, a GitHub App and per-repository policy.

## How it works

`src/theseus_reviewer/jev.py` wraps calls to `https://api.typesafe.ai` in a `JevSession` with timeouts and outage detection; the size, capability and template calls feed the review plan, and `recovery.py` uses Jev to choose retry, escalate or stop. Integration evidence: [`src/theseus_reviewer/jev.py`](https://github.com/joeharris76/theseus/blob/976917576298553a818d48d1bcbbf8628c81c248/src/theseus_reviewer/jev.py).

## Get started

Install the package, add a consumer policy to your repository and set the classifier key; the docs cover hosted workflows and local review.

```sh
pip install 'git+https://github.com/joeharris76/theseus'
export TYPESAFE_API_KEY=...   # classifier key
theseus --help   # see docs/local-review.md and docs/hosted-workflows.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/joeharris76/theseus/blob/976917576298553a818d48d1bcbbf8628c81c248/README.md](https://github.com/joeharris76/theseus/blob/976917576298553a818d48d1bcbbf8628c81c248/README.md)
- Review templates: [github.com/joeharris76/theseus/blob/976917576298553a818d48d1bcbbf8628c81c248/src/theseus_reviewer/templates/README.md](https://github.com/joeharris76/theseus/blob/976917576298553a818d48d1bcbbf8628c81c248/src/theseus_reviewer/templates/README.md)
- Example review on a PR: [github.com/joeharris76/theseus/pull/98](https://github.com/joeharris76/theseus/pull/98)

## Limits and data handling

PR metadata and diffs reach TypeSafe for classification and your configured model providers for the reviews. Setup is involved (GitHub App, secrets, policy). The author's statement that thousands of PRs cost a few dollars of Jev is his own, not measured here.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 976917576298](https://github.com/joeharris76/theseus/tree/976917576298553a818d48d1bcbbf8628c81c248). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
