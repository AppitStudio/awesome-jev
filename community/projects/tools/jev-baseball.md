# jev-baseball by Yasunori Morishima (pre-registered studies of Jev on MLB and NPB judgement tasks against simple baselines)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Pre-registered experiments that test Jev on baseball questions before the first call: forecasting next-season wOBA from an anonymised batting line (Jev has skill but is worse than a textbook Marcel-lite rule), adding Jev readings of pre-arrival Wikipedia text to predict foreign players' first NPB season (no gain against a shuffled-feature floor), and ABS challenge overturns. Each study reports its result against its pre-declared reading, with raw answers committed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yasumorishima/jev-baseball) |
| Maintainer | [yasumorishima](https://github.com/yasumorishima). Independently curated. |
| Format | Python scripts, pre-registrations and results |
| Requirements | Python 3 with the packages in `requirements.txt`; an OpenRouter key to re-run the Jev calls (analysis runs on the committed answers). |
| License | [MIT](https://github.com/yasumorishima/jev-baseball/blob/6170d5f0af0af074cb94fc370fc8f073219e8dd2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`study2-projection/run_jev.py`](https://github.com/yasumorishima/jev-baseball/blob/6170d5f0af0af074cb94fc370fc8f073219e8dd2/study2-projection/run_jev.py) at the pinned commit. |

## When to use

- See how to test Jev honestly on a numeric forecasting task, with pre-registration and baselines.
- Mismatch: betting or scouting tools; these are small research studies with mostly negative results.

## How it works

`study2-projection/run_jev.py` posts to OpenRouter's `https://openrouter.ai/api/alpha/decisions` with model `typesafe/jev-1.13`, is resumable and stops on the first refusal; answers are saved to `results/jev_answers.jsonl`. Integration evidence: [`study2-projection/run_jev.py`](https://github.com/yasumorishima/jev-baseball/blob/6170d5f0af0af074cb94fc370fc8f073219e8dd2/study2-projection/run_jev.py).

## Get started

Read a study's PREREG.md and results, then re-run the analysis on the committed answers.

```sh
git clone https://github.com/yasumorishima/jev-baseball && cd jev-baseball
pip install -r requirements.txt
cat study2-projection/PREREG.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- English write-up (DEV.to): [dev.to/yasumorishima/asking-a-decision-only-ai-typesafe-jev-to-forecast-next-seasons-hitting-worth-about-20-to-50-360k](https://dev.to/yasumorishima/asking-a-decision-only-ai-typesafe-jev-to-forecast-next-seasons-hitting-worth-about-20-to-50-360k)
- Japanese write-up (Qiita): [qiita.com/ussu_ussu_ussu/items/cc28f711396515c1fb31](https://qiita.com/ussu_ussu_ussu/items/cc28f711396515c1fb31)

## Limits and data handling

Sample sizes are small (for example 51 batters and 69 pitchers in Study 4), so only large effects are detectable; Wikipedia text is CC BY-SA and not committed. Results are the author's, not catalog-verified.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 6170d5f0af0a](https://github.com/yasumorishima/jev-baseball/tree/6170d5f0af0af074cb94fc370fc8f073219e8dd2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
