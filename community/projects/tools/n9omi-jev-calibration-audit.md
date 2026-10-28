# jev-calibration-audit (independent test of whether Jev's probabilities are calibrated, on US petroleum reports)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent audit of Jev's calibration on questions about EIA weekly petroleum inventory reports, where the right answer can be computed exactly: reliability diagrams, ECE, Murphy decomposition and a Spiegelhalter test, compared with an LLM classifier asked the same questions word for word, plus rules and climatology baselines.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/n9omi/jev-calibration-audit) |
| Maintainer | [n9omi](https://github.com/n9omi). Independently curated. |
| Format | Python package and CLI |
| Requirements | Python; EIA, TypeSafe and LLM-provider keys for a real run; the demo needs none. |
| License | [MIT](https://github.com/n9omi/jev-calibration-audit/blob/0b6d814bfd6ebd77ca776d2ca4a58a3055fafa30/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_audit/arms/jev.py`](https://github.com/n9omi/jev-calibration-audit/blob/0b6d814bfd6ebd77ca776d2ca4a58a3055fafa30/src/jev_audit/arms/jev.py) at the pinned commit. |

## When to use

- Decide whether to threshold or aggregate Jev probabilities in a forecasting setting.
- Mismatch: one domain; results are the author's.

## How it works

`src/jev_audit/arms/jev.py` calls Jev through `langchain-typesafe`'s `TypeSafeClassifier` (`jev-latest` by default) and caches each response. Integration evidence: [`src/jev_audit/arms/jev.py`](https://github.com/n9omi/jev-calibration-audit/blob/0b6d814bfd6ebd77ca776d2ca4a58a3055fafa30/src/jev_audit/arms/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/n9omi/jev-calibration-audit && cd jev-calibration-audit
pip install -e ".[jev,llm,dev]"
jev-audit demo   # offline, synthetic data
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/n9omi/jev-calibration-audit#readme](https://github.com/n9omi/jev-calibration-audit#readme)

## Limits and data handling

Public EIA-derived states go to TypeSafe and the LLM provider during real runs.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 0b6d814bfd6e](https://github.com/n9omi/jev-calibration-audit/tree/0b6d814bfd6ebd77ca776d2ca4a58a3055fafa30). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
