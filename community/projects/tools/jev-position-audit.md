# Same Answer, Different Verdict by Suraj Phanindra (registered audit of order and format sensitivity in Jev 1.13)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code, aggregate results and figures for a pre-registered (OSF) audit of position bias in `jev-1.13.0` on pairwise judgments from MT-Bench, HANNA and SummEval. It measures order effects on identical copies, how they shrink as the human-rated quality gap grows, question order and format envelopes, with Claude Haiku 4.5 and DeepSeek V4 Flash as reference judges.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/suraj-phanindra/jev-position-audit) |
| Maintainer | [suraj-phanindra](https://github.com/suraj-phanindra). Independently curated. |
| Format | Python research code + aggregate results |
| Requirements | Python 3 with the listed requirements; a TypeSafe key only to collect new data (figures rebuild from the committed aggregates). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`harness/audit.py`](https://github.com/suraj-phanindra/jev-position-audit/blob/df92208204a671814672e4d393fe03b4e157bf15/harness/audit.py) at the pinned commit. |

## When to use

- Before using Jev Choice as a pairwise judge, see how much candidate order moves its verdicts and at what confidence that matters.
- Mismatch: a reusable library; this is a study's code.

## How it works

`harness/audit.py` builds requests and posts them to `https://api.typesafe.ai/v1/systemone` with `TYPESAFE_API_KEY`, keeping an audit trail; `preflight/` holds registration-time checks and amendment adapters, and `inference/` the registered analysis. Integration evidence: [`harness/audit.py`](https://github.com/suraj-phanindra/jev-position-audit/blob/df92208204a671814672e4d393fe03b4e157bf15/harness/audit.py).

## Get started

Run the unit tests and rebuild the figures from the committed results.

```sh
git clone https://github.com/suraj-phanindra/jev-position-audit && cd jev-position-audit
python -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m unittest discover tests
.venv/bin/python figures/make_figures.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- OSF registration: [osf.io/4nme3/](https://osf.io/4nme3/)
- Figures: [github.com/suraj-phanindra/jev-position-audit/tree/df92208204a671814672e4d393fe03b4e157bf15/figures](https://github.com/suraj-phanindra/jev-position-audit/tree/df92208204a671814672e4d393fe03b4e157bf15/figures)

## Limits and data handling

Findings are the author's (for example a +0.127 first-slot gain on identical copies, with 47.5% of decisions under 0.6 confidence flipping on order reversal) and apply to Jev 1.13. Raw API responses (about 6.6 GB) and corpus text are not included. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit df92208204a6](https://github.com/suraj-phanindra/jev-position-audit/tree/df92208204a671814672e4d393fe03b4e157bf15). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
