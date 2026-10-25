# jev-open-calibration (Jev's calibrated-decision interface rebuilt on scikit-learn and tested against Jev)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code, data and figures for the Towards Data Science article "Jev Is API-Only. Its Best Idea Is Open.": rebuilds Jev's typed Choice, Score and Noul interface on scikit-learn with temperature scaling, then compares calibration, cascades and a none-of-the-above trap with live Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ankur287/jev-open-calibration) |
| Maintainer | [ankur287](https://github.com/ankur287). Independently curated. |
| Format | Python experiments with data and figures |
| Requirements | Python with scikit-learn; a TypeSafe API key only for the live Jev experiments. |
| License | [MIT](https://github.com/ankur287/jev-open-calibration/blob/f95875ffd859e729603cbbca149b52b6dd1fcbd9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`code/exp04_jev_live.py`](https://github.com/ankur287/jev-open-calibration/blob/f95875ffd859e729603cbbca149b52b6dd1fcbd9/code/exp04_jev_live.py) at the pinned commit. |

## When to use

- Compare an open, calibrated classifier with Jev on intent routing.
- Reuse the ECE, reliability and cascade code for your own decision tasks.
- Mismatch: results are the author's own on banking intents and were not reproduced.

## How it works

`code/exp04_jev_live.py` and the 77-intent scripts post Choice and Noul questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); the open experiments run offline. Integration evidence: [`code/exp04_jev_live.py`](https://github.com/ankur287/jev-open-calibration/blob/f95875ffd859e729603cbbca149b52b6dd1fcbd9/code/exp04_jev_live.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ankur287/jev-open-calibration && cd jev-open-calibration
TYPESAFE_API_KEY=... python code/exp04_jev_live.py --probe   # one live call
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results: [github.com/ankur287/jev-open-calibration#readme](https://github.com/ankur287/jev-open-calibration#readme)

## Limits and data handling

Live experiments send intent texts to TypeSafe. Distinct from the listed jev-calibration and jev-ood-calibration.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit f95875ffd859](https://github.com/ankur287/jev-open-calibration/tree/f95875ffd859e729603cbbca149b52b6dd1fcbd9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
