# JADE (decision-governance runtime that journals and gates Claude Code's TypeSafe Jev calls)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Design plus a small Python runtime for agents that ask Jev "is this right?": every call is journaled, probabilities map to accept/abstain/reject per task family, and risky side effects need a human-approved permit.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vahidkaargar/jade-decision-governance) |
| Maintainer | [vahidkaargar](https://github.com/vahidkaargar). Independently curated. |
| Format | Python CLI + Claude Code hooks (MIT; advisory/soak stage) |
| Requirements | Python/uv, Claude Code, and a Jev route (OpenRouter or TypeSafe key) for the `jev` shim. |
| License | [MIT](https://github.com/vahidkaargar/jade-decision-governance/blob/f95427bd43b364bbceb8c3ed8a3c24e0332f04e5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jade/adapter.py`](https://github.com/vahidkaargar/jade-decision-governance/blob/f95427bd43b364bbceb8c3ed8a3c24e0332f04e5/jade/adapter.py) at the pinned commit. |

## When to use

- Stop an agent from treating a Jev 'yes' as permission.
- Journal and calibrate Jev decisions per task family.
- Mismatch: status is advisory (soak); not yet validated or production-approved.

## How it works

`jade/adapter.py` is the decision-model adapter behind the `jev` shim; `ask.py`, `thresholds.py` and `permits.py` turn Jev probabilities into accept/abstain/reject plus single-use execution permits, all written to a SQLite ledger. Integration evidence: [`jade/adapter.py`](https://github.com/vahidkaargar/jade-decision-governance/blob/f95427bd43b364bbceb8c3ed8a3c24e0332f04e5/jade/adapter.py).

## Get started

Install with `uv tool install git+https://github.com/vahidkaargar/jade-decision-governance@v0.3.3`, then run `jade hooks install` and `jade check` yourself.

```sh
uv tool install git+https://github.com/vahidkaargar/jade-decision-governance@v0.3.3
jade hooks install && jade check
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/vahidkaargar/jade-decision-governance/blob/f95427bd43b364bbceb8c3ed8a3c24e0332f04e5/README.md](https://github.com/vahidkaargar/jade-decision-governance/blob/f95427bd43b364bbceb8c3ed8a3c24e0332f04e5/README.md)

## Limits and data handling

Redacted decision questions go to the configured Jev route; the ledger stays local.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit f95427bd43b3](https://github.com/vahidkaargar/jade-decision-governance/tree/f95427bd43b364bbceb8c3ed8a3c24e0332f04e5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
