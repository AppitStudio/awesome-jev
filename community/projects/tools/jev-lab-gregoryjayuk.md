# jev-lab (gregoryjayuk)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Two standard-library Python experiments with Jev: a feed sieve that judges a week of posts from 500+ RSS, Atom, and YouTube feeds against a reader profile and writes a reading list, and a bookmark re-filing eval of agreement, calibration, and cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gregoryjayuk/jev-lab) |
| Maintainer | [gregoryjayuk](https://github.com/gregoryjayuk). Independently curated. |
| Format | Python scripts (stdlib only) |
| Requirements | Python 3; `TYPESAFE_API_KEY` (or macOS Keychain). |
| License | [MIT](https://github.com/gregoryjayuk/jev-lab/blob/25af2f64b840ed3115d1e81d5716099ee38b6379/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bookmark_eval.py`](https://github.com/gregoryjayuk/jev-lab/blob/25af2f64b840ed3115d1e81d5716099ee38b6379/bookmark_eval.py) at the pinned commit. |

## When to use

- See real cost and calibration numbers for Jev on feed filtering.
- Mismatch: experiments, not a packaged tool.

## How it works

The sieve asks Jev four questions per item in one call (a Score for worth plus three yes/no checks); `bookmark_eval.py` hides labels and measures agreement and confidence. README reports 1,096 calls for about $0.04 on the example profile. Integration evidence: [`bookmark_eval.py`](https://github.com/gregoryjayuk/jev-lab/blob/25af2f64b840ed3115d1e81d5716099ee38b6379/bookmark_eval.py).

## Get started

From the upstream README: copy the example profile, set your key, and run the sieve.

```sh
git clone https://github.com/gregoryjayuk/jev-lab && cd jev-lab
export TYPESAFE_API_KEY=...
# see README for sieve and bookmark_eval commands
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- docs/screenshots

## Limits and data handling

Feed item text goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 25af2f64b840](https://github.com/gregoryjayuk/jev-lab/tree/25af2f64b840ed3115d1e81d5716099ee38b6379). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
