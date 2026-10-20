# Supply Chain Hunter

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted monitor for software supply-chain attacks: diffs each new release of the top npm and PyPI packages (and lookalike names) against the previous version, has Jev answer many narrow yes/no questions about the diff as the Scout stage, and escalates only suspicious releases to triage and analyst models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SecOps-AG/Supply-Chain-Hunter) |
| Maintainer | [SecOps-AG](https://github.com/SecOps-AG). Independently curated. |
| Format | Self-hosted service (Python, SQLite, local dashboard) |
| Requirements | Python 3.11+; `TYPESAFE_API_KEY` for the Scout stage; a Cursor Agent CLI key or another model API for triage and analyst. |
| License | [MIT](https://github.com/SecOps-AG/Supply-Chain-Hunter/blob/96bf498cf6f4465174892721c4ff8bcb57e9aae8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hunter/jev.py`](https://github.com/SecOps-AG/Supply-Chain-Hunter/blob/96bf498cf6f4465174892721c4ff8bcb57e9aae8/hunter/jev.py) at the pinned commit. |

## When to use

- Watch popular package releases for malicious changes before they reach your builds.
- Keep per-release cost low by running a decision model on every diff and a frontier model only on the few flagged ones.
- Mismatch: beta; the public instance is paused because it is expensive to run.

## How it works

Hunter polls the npm and PyPI feeds, diffs each watched release, optionally runs YARA and Python rules, then `hunter/jev.py` asks Jev (or Clef) narrow questions about the diff to band it; flagged releases go to triage, and only an analyst "malicious" verdict sends a webhook alert. Integration evidence: [`hunter/jev.py`](https://github.com/SecOps-AG/Supply-Chain-Hunter/blob/96bf498cf6f4465174892721c4ff8bcb57e9aae8/hunter/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
export TYPESAFE_API_KEY=...  CURSOR_API_KEY=...  HUNTER_ANALYST_MODEL=<model id>
python -m hunter serve
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Detection notes: [github.com/SecOps-AG/Supply-Chain-Hunter/blob/main/docs/detection.md](https://github.com/SecOps-AG/Supply-Chain-Hunter/blob/main/docs/detection.md)

## Limits and data handling

Package diffs (public code) are sent to TypeSafe and to the triage and analyst providers. Running it at full scale costs real money, per the README.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 96bf498cf6f4](https://github.com/SecOps-AG/Supply-Chain-Hunter/tree/96bf498cf6f4465174892721c4ff8bcb57e9aae8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
