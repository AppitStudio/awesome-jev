# decision-models-eval

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent, pre-registered evaluation of SubQ Snap against TypeSafe Jev 1.13 and 1.14 on Decision Index benchmarks, including a long-context fairness test (whole documents vs chunks), with figures and confidence intervals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sammy143/decision-models-eval) |
| Maintainer | [sammy143](https://github.com/sammy143). Independently curated. |
| Format | Python evaluation code + results |
| Requirements | Python; TypeSafe and SubQ keys to reproduce. |
| License | [MIT](https://github.com/sammy143/decision-models-eval/blob/78769cac4a5fa2ca0de16e941a03af6f037cee2c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`dme/exp1/score.py`](https://github.com/sammy143/decision-models-eval/blob/78769cac4a5fa2ca0de16e941a03af6f037cee2c/dme/exp1/score.py) at the pinned commit. |

## When to use

- Check vendor benchmark claims about Jev with independent numbers.
- Mismatch: research results; rerun before relying on them.

## How it works

Experiments call both providers on the same items and score them; `dme/exp1/score.py` builds the comparison tables (Board jev-1.13, Snap, Jev). Integration evidence: [`dme/exp1/score.py`](https://github.com/sammy143/decision-models-eval/blob/78769cac4a5fa2ca0de16e941a03af6f037cee2c/dme/exp1/score.py).

## Get started

From the upstream README: install, set provider keys, and run each experiment.

```sh
git clone https://github.com/sammy143/decision-models-eval
# see README for experiment commands
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- figures/
- README experiment table

## Limits and data handling

Benchmark items go to TypeSafe and SubQ. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 78769cac4a5f](https://github.com/sammy143/decision-models-eval/tree/78769cac4a5fa2ca0de16e941a03af6f037cee2c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
