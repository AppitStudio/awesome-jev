# spendcoder (GL-code corporate card spend from your own policy; models judge, code decides)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Turns a corporate-card export into GL-coded transactions using your categories, rule matrix and vendor overrides: code handles arithmetic, eligibility, amount ranges and row preservation, while small bounded questions (category, which matching rule, review flags) go to a decision model, Jev by default via OpenRouter Decisions. Every row gets an audit trail and uncertain rows go to a review queue.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ansh-shah/spendcoder) |
| Maintainer | [ansh-shah](https://github.com/ansh-shah). Independently curated. |
| Format | Python CLI |
| Requirements | Python; OpenRouter (Decisions and chat) and Parallel Search keys for live runs; a mock backend runs offline. |
| License | [MIT](https://github.com/ansh-shah/spendcoder/blob/0734e950e6748bdb6a02131368ec0ddfc64fd458/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/spendcoder/config.py`](https://github.com/ansh-shah/spendcoder/blob/0734e950e6748bdb6a02131368ec0ddfc64fd458/src/spendcoder/config.py) at the pinned commit. |

## When to use

- Speed up month-end card coding while keeping an audit trail.
- Mismatch: built around Airbase exports (other exports need column mapping).

## How it works

`src/spendcoder/config.py` sets `decision_model = "typesafe/jev-1.13"` for OpenRouter's Decisions API; the categorize, rule-select and review stages send Choice and Noul questions there. Integration evidence: [`src/spendcoder/config.py`](https://github.com/ansh-shah/spendcoder/blob/0734e950e6748bdb6a02131368ec0ddfc64fd458/src/spendcoder/config.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ansh-shah/spendcoder && cd spendcoder
pip install -e ".[tune]"
spendcoder init demo --template acme && cd demo
spendcoder run --backend mock
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ansh-shah/spendcoder#readme](https://github.com/ansh-shah/spendcoder#readme)

## Limits and data handling

Merchant descriptions and memos go to OpenRouter (and on to TypeSafe) in live runs. The mock backend sends nothing.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 0734e950e674](https://github.com/ansh-shah/spendcoder/tree/0734e950e6748bdb6a02131368ec0ddfc64fd458). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
