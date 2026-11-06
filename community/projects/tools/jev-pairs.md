# jev-pairs (deduplicate and link records with measurable blocking plus a low-cost Jev cascade)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Python toolkit for pair decisions—dedupe, cluster, link, contradiction—with blocking audits, a budget-bounded pair-plan selector, and TypeSafe Jev judgments only for pairs that survive cheaper stages.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/jev-pairs) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Python 3.11+ package (MIT) |
| Requirements | Python 3.11+ and `TYPESAFE_API_KEY` for live pair judgments (offline fixtures available). |
| License | [MIT](https://github.com/gbesse/jev-pairs/blob/12bfcc0f639293cda383227afabaa9cfe2a9e721/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_pairs/core.py`](https://github.com/gbesse/jev-pairs/blob/12bfcc0f639293cda383227afabaa9cfe2a9e721/src/jev_pairs/core.py) at the pinned commit. |

## When to use

- Deduplicate or link a corpus with an auditable blocking rule.
- Tune a pair plan on labeled data before spending on Jev.
- Mismatch: fixtures are synthetic; pick rules on your own labeled sample.

## How it works

`src/jev_pairs/core.py` pins `jev-1.13.0` and drives cascade judgments after deterministic blocking. Integration evidence: [`src/jev_pairs/core.py`](https://github.com/gbesse/jev-pairs/blob/12bfcc0f639293cda383227afabaa9cfe2a9e721/src/jev_pairs/core.py).

## Get started

Clone, install the offline demo deps, then run the blocking audit example.

```sh
git clone https://github.com/gbesse/jev-pairs.git && cd jev-pairs
python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-dev.txt
python -m examples.offline_demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/jev-pairs/blob/12bfcc0f639293cda383227afabaa9cfe2a9e721/README.md](https://github.com/gbesse/jev-pairs/blob/12bfcc0f639293cda383227afabaa9cfe2a9e721/README.md)

## Limits and data handling

Paired record text is sent to TypeSafe on your key when live. Public alpha.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 12bfcc0f6392](https://github.com/gbesse/jev-pairs/tree/12bfcc0f639293cda383227afabaa9cfe2a9e721). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
