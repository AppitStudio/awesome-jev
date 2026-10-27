# Finclaude (personal investment-research agent in Claude Code, with Jev probabilities logged and scored)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Personal investment-research assistant built on Claude Code: Claude fetches official sources (SEC EDGAR, Fed, BLS, BEA, investor-relations pages) and computes with Python, while probabilities come only from data and models including Jev; every probability is logged before the outcome and scored by Brier score against a coin-flip baseline. Weekly News, Decision and Lesson pages; read-only broker access, no buy or sell orders. Educational, not investment advice. Chinese docs with English summary.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/seanyi0104/Finclaude) |
| Maintainer | [seanyi0104](https://github.com/seanyi0104). Independently curated. |
| Format | Claude Code project (Python) |
| Requirements | Claude Code, uv and Python; a Vercel AI Gateway key for Jev. |
| License | [MIT](https://github.com/seanyi0104/Finclaude/blob/7ab4d25c5da12cba0d798ec91c09c5b0f8ad2e59/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`finclaude/jev.py`](https://github.com/seanyi0104/Finclaude/blob/7ab4d25c5da12cba0d798ec91c09c5b0f8ad2e59/finclaude/jev.py) at the pinned commit. |

## When to use

- Keep sourced research and checkable forecasts for your own investing.
- Mismatch: educational, not investment advice; never places orders.

## How it works

`finclaude/jev.py` calls `typesafe-ai/jev` through Vercel AI Gateway with Choice questions over given options; if no probability comes back the workflow stops instead of letting Claude guess. Integration evidence: [`finclaude/jev.py`](https://github.com/seanyi0104/Finclaude/blob/7ab4d25c5da12cba0d798ec91c09c5b0f8ad2e59/finclaude/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/seanyi0104/Finclaude && cd Finclaude
# install uv, then follow the README's quick start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/seanyi0104/Finclaude#readme](https://github.com/seanyi0104/Finclaude#readme)

## Limits and data handling

Question context goes to Vercel AI Gateway and TypeSafe. Not investment advice; forecast scores are the user's own log.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 7ab4d25c5da1](https://github.com/seanyi0104/Finclaude/tree/7ab4d25c5da12cba0d798ec91c09c5b0f8ad2e59). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
