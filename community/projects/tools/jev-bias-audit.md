# Jev bias audit (134,772 paired answers testing how one identity word shifts Jev's decisions)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Counterfactual bias audit of `jev-1.13.0` and `jev-1.14.0`: prompts that differ only in one identity sentence (82 identities across nine attributes, 50 names, placebos) over hiring, lending, trust and other templates, with bootstrap intervals, Benjamini-Hochberg correction and a birth-month placebo floor. The author finds explicit labels move decisions by 3 to 15 points while names barely do.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/isaacbitran/jev-bias-audit) |
| Maintainer | [isaacbitran](https://github.com/isaacbitran). Independently curated. |
| Format | Python scripts, cached answers and report |
| Requirements | Python; a TypeSafe API key only to collect new answers. |
| License | [MIT](https://github.com/isaacbitran/jev-bias-audit/blob/c97efba13a9f04d9c248c3d2b318a45e4298f4e6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev.py`](https://github.com/isaacbitran/jev-bias-audit/blob/c97efba13a9f04d9c248c3d2b318a45e4298f4e6/jev.py) at the pinned commit. |

## When to use

- Check fairness risks before using a decision model on people.
- Mismatch: findings are the author's for two model versions.

## How it works

`jev.py` posts each paired prompt to `https://api.typesafe.ai/v1/systemone`; `analyze.py` computes the contrasts from the cached answers. Integration evidence: [`jev.py`](https://github.com/isaacbitran/jev-bias-audit/blob/c97efba13a9f04d9c248c3d2b318a45e4298f4e6/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/isaacbitran/jev-bias-audit && cd jev-bias-audit
python3 -I run.py --dry   # rebuilds items, no API calls
python3 -I analyze.py     # reuses cache.jsonl, no key needed
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Report: [github.com/isaacbitran/jev-bias-audit/blob/main/REPORT.md](https://github.com/isaacbitran/jev-bias-audit/blob/main/REPORT.md)
- Summary: [github.com/isaacbitran/jev-bias-audit/blob/main/SUMMARY.md](https://github.com/isaacbitran/jev-bias-audit/blob/main/SUMMARY.md)

## Limits and data handling

Synthetic prompts only; new collection sends them to TypeSafe.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit c97efba13a9f](https://github.com/isaacbitran/jev-bias-audit/tree/c97efba13a9f04d9c248c3d2b318a45e4298f4e6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
