# monitor-calibration (how well Jev and other models report confidence when flagging harmful chatbot prompts)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Study of confidence quality on a safety-monitor task: a TF-IDF baseline, local open-weight models, commercial APIs, Claude and Jev each give P(harmful) for prompts from ToxicChat and WildGuardTest, compared on AUROC, Brier, ECE, risk-coverage and catch rate at a fixed audit budget. Jev is read natively through the TypeSafe SDK.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sampan501/monitor-calibration) |
| Maintainer | [sampan501](https://github.com/sampan501). Independently curated. |
| Format | Python scripts with results |
| Requirements | Python; API keys for the models you rerun (TypeSafe for Jev). |
| License | [MIT](https://github.com/sampan501/monitor-calibration/blob/db565fe4151f98b6272f16c5786c491df7c53499/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scorers.py`](https://github.com/sampan501/monitor-calibration/blob/db565fe4151f98b6272f16c5786c491df7c53499/scorers.py) at the pinned commit. |

## When to use

- Choose a monitor model by how trustworthy its probabilities are, not only accuracy.
- Mismatch: one task and two datasets; results are the author's.

## How it works

`scorers.py` uses `typesafe_sdk` (`TypeSafeClient`, `Noul`) with `jev-latest` to get P(harmful) per prompt; `run.py` selects scorers. Integration evidence: [`scorers.py`](https://github.com/sampan501/monitor-calibration/blob/db565fe4151f98b6272f16c5786c491df7c53499/scorers.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/sampan501/monitor-calibration && cd monitor-calibration
# see the README for run.py scorer options
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results: [github.com/sampan501/monitor-calibration#readme](https://github.com/sampan501/monitor-calibration#readme)

## Limits and data handling

Benchmark prompts (some harmful) go to each provider you run.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit db565fe4151f](https://github.com/sampan501/monitor-calibration/tree/db565fe4151f98b6272f16c5786c491df7c53499). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
