# jevrev by Andrew Rabert (code review CLI that asks Jev whether code breaks rules you write)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI that scans a directory, git diff or GitHub pull request against YAML rule sets (each rule a defect with good and bad examples), prints findings with Jev's probability, and offers a review workflow to confirm or reject findings and post them as a PR review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/andrewrabert/jevrev) |
| Maintainer | [andrewrabert](https://github.com/andrewrabert). Independently curated. |
| Format | Python CLI |
| Requirements | Python with uv; a `TYPESAFE_API_KEY`; a GitHub token to scan or post pull requests. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jevrev/jev/api.py`](https://github.com/andrewrabert/jevrev/blob/26cbacae4ccea0a0e25e908b2f1ecaf5a0c6dc1a/src/jevrev/jev/api.py) at the pinned commit. |

## When to use

- Check code against team-specific rules that linters cannot express, with a confirm/reject review loop.
- Mismatch: general-purpose AI code review; it only checks the rules you write, and there is no license file.

## How it works

`src/jevrev/jev/api.py` wraps the TypeSafe Python SDK and sends one `noul` per rule with the file, hunk or language range as state; exit codes (0 clean, 1 findings, 2 error) make it usable in CI or pre-commit. Integration evidence: [`src/jevrev/jev/api.py`](https://github.com/andrewrabert/jevrev/blob/26cbacae4ccea0a0e25e908b2f1ecaf5a0c6dc1a/src/jevrev/jev/api.py).

## Get started

Install the tool, point it at your rule sets and scan.

```sh
git clone https://github.com/andrewrabert/jevrev
cd jevrev
uv tool install .
export TYPESAFE_API_KEY=...
export JEV_RULES=$PWD/example_rules
jevrev scan src
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/andrewrabert/jevrev/blob/26cbacae4ccea0a0e25e908b2f1ecaf5a0c6dc1a/README.md](https://github.com/andrewrabert/jevrev/blob/26cbacae4ccea0a0e25e908b2f1ecaf5a0c6dc1a/README.md)
- Example rules: [github.com/andrewrabert/jevrev/tree/26cbacae4ccea0a0e25e908b2f1ecaf5a0c6dc1a/example_rules](https://github.com/andrewrabert/jevrev/tree/26cbacae4ccea0a0e25e908b2f1ecaf5a0c6dc1a/example_rules)

## Limits and data handling

Code under review is sent to TypeSafe. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) at [commit 26cbacae4cce](https://github.com/andrewrabert/jevrev/tree/26cbacae4ccea0a0e25e908b2f1ecaf5a0c6dc1a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
