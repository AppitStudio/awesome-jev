# Same bet? (Jev decides whether a Polymarket and a Kalshi market pay out on the same outcome, benchmarked against title matching)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Small benchmark that pulls open Polymarket and Kalshi markets, finds look-alike pairs by title, and asks Jev in one request per pair whether they are the same bet, a variant or different, plus three yes/no checks on subject, terms and deadline. On 197 hand-labeled pairs the author reports 98% accuracy with tuned instructions (85% first draft) against 83% for the best title-match cutoff.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/siddhanttiwary25-eng/same-bet-jev) |
| Maintainer | [siddhanttiwary25-eng](https://github.com/siddhanttiwary25-eng). Independently curated. |
| Format | Python scripts, labeled data and a static results page (no license file) |
| Requirements | Python 3 with `certifi` and `rapidfuzz`, and a TypeSafe key (market data needs no key). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_match.py`](https://github.com/siddhanttiwary25-eng/same-bet-jev/blob/5ace29f34c726eb2603ebd158449cd5e6a4dbe65/src/jev_match.py) at the pinned commit. |

## When to use

- Match equivalent markets or listings across two venues where titles look alike but terms differ.
- Mismatch: trading decisions; this is a matching benchmark, not financial advice.

## How it works

`src/jev_match.py` sends one Choice plus three Noul questions per pair to `https://api.typesafe.ai/v1/systemone` and records the model id from each response. Instructions were tuned on a separate 40-pair practice set and the test set was run once with the locked version. Integration evidence: [`src/jev_match.py`](https://github.com/siddhanttiwary25-eng/same-bet-jev/blob/5ace29f34c726eb2603ebd158449cd5e6a4dbe65/src/jev_match.py).

## Get started

Create a venv, add your key, then fetch markets and run the benchmark.

```sh
git clone https://github.com/siddhanttiwary25-eng/same-bet-jev && cd same-bet-jev
python3 -m venv .venv && .venv/bin/pip install certifi rapidfuzz
echo 'TYPESAFE_API_KEY=...' > .env
.venv/bin/python src/fetch_markets.py && .venv/bin/python src/candidates.py
.venv/bin/python src/benchmark.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/siddhanttiwary25-eng/same-bet-jev/blob/5ace29f34c726eb2603ebd158449cd5e6a4dbe65/README.md](https://github.com/siddhanttiwary25-eng/same-bet-jev/blob/5ace29f34c726eb2603ebd158449cd5e6a4dbe65/README.md)
- Results page source: [github.com/siddhanttiwary25-eng/same-bet-jev/blob/5ace29f34c726eb2603ebd158449cd5e6a4dbe65/site/index.html](https://github.com/siddhanttiwary25-eng/same-bet-jev/blob/5ace29f34c726eb2603ebd158449cd5e6a4dbe65/site/index.html)

## Limits and data handling

Public market titles and rules go to TypeSafe on your key. Labels were made with AI help and reviewed by hand (10 corrected); the title-match row is an upper bound.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 5ace29f34c72](https://github.com/siddhanttiwary25-eng/same-bet-jev/tree/5ace29f34c726eb2603ebd158449cd5e6a4dbe65). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
