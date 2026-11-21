# docfriction by Cyrus Pastelero (friction logs for documentation pages, scored section by section with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A CLI (on PyPI) that walks a docs page or Markdown file one heading at a time and asks Jev a fixed set of typed questions per step (friction type, severity, missing prerequisites, undefined terms, code/prose mismatch), adds deterministic checks such as dead links, and writes a developer-advocate style friction log. It can gate CI on a severity threshold.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cyruspastelero/docfriction) |
| Maintainer | [cyruspastelero](https://github.com/cyruspastelero). Independently curated. |
| Format | Python CLI (PyPI `docfriction`) |
| Requirements | Python 3.10+ (`uv tool install docfriction` or pipx) and a TypeSafe API key; `--dry-run` needs no key. |
| License | [MIT](https://github.com/cyruspastelero/docfriction/blob/7c356d5f3a177243d31ba50e00e808b3f2a30db6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/docfriction/jev.py`](https://github.com/cyruspastelero/docfriction/blob/7c356d5f3a177243d31ba50e00e808b3f2a30db6/src/docfriction/jev.py) at the pinned commit. |

## When to use

- Get a quick first-pass friction log for a quickstart or API docs page, or fail CI when a docs change makes it worse.
- Mismatch: a replacement for real user testing; the author says the rubric has not been checked against human-written friction logs.

## How it works

`src/docfriction/jev.py` posts one `/v1/systemone` request per step to `https://api.typesafe.ai` with `TYPESAFE_API_KEY`; answers are mapped to sentiment and a 0–3 severity, and `--fail-on-severity` exits 2 for CI. Integration evidence: [`src/docfriction/jev.py`](https://github.com/cyruspastelero/docfriction/blob/7c356d5f3a177243d31ba50e00e808b3f2a30db6/src/docfriction/jev.py).

## Get started

Install from PyPI, preview the steps without a key, then run with your key.

```sh
uv tool install docfriction
docfriction https://docs.example.com/quickstart --dry-run
export TYPESAFE_API_KEY=...
docfriction https://docs.example.com/quickstart --check-links
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Sample friction log: [github.com/cyruspastelero/docfriction/blob/7c356d5f3a177243d31ba50e00e808b3f2a30db6/examples/sample-friction-log.md](https://github.com/cyruspastelero/docfriction/blob/7c356d5f3a177243d31ba50e00e808b3f2a30db6/examples/sample-friction-log.md)
- GitHub Action example: [github.com/cyruspastelero/docfriction/blob/7c356d5f3a177243d31ba50e00e808b3f2a30db6/examples/github-action.yml](https://github.com/cyruspastelero/docfriction/blob/7c356d5f3a177243d31ba50e00e808b3f2a30db6/examples/github-action.yml)
- PyPI: [pypi.org/project/docfriction/](https://pypi.org/project/docfriction/)

## Limits and data handling

Alpha software; the CLI may change before 1.0. Page text is sent to TypeSafe, one call per section.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 7c356d5f3a17](https://github.com/cyruspastelero/docfriction/tree/7c356d5f3a177243d31ba50e00e808b3f2a30db6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
