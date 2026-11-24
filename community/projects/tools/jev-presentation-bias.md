# Does answer presentation sway Jev as a judge? by Cole Torres (experiment on whether Jev judges what an answer says or how it is written)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Small study that rewrites one correct and one wrong answer per question in seven styles with the facts fixed, then measures how Jev's verdicts and probabilities move on TruthfulQA (80 questions) and MMLU-Pro (40). Jev picked the correct plain answer 96.5% and 90.5% of the time; confident wording lowered its P(correct) by several points.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/coltranetorres/jev-presentation-bias) |
| Maintainer | [coltranetorres](https://github.com/coltranetorres). Independently curated. |
| Format | Python experiment (uv) with cached results |
| Requirements | Python with uv and an OpenRouter key (Jev is called as `typesafe/jev-1.14` through OpenRouter's decisions API; chat models write the rewrites). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/itscoleeee/status/2125231416715960550)). |
| Jev evidence | [`src/jev_bias/client.py`](https://github.com/coltranetorres/jev-presentation-bias/blob/5fdfb1bf2d14bcaecfda219757cbec7ed9661e88/src/jev_bias/client.py) at the pinned commit. |

## When to use

- Check how much answer style can sway Jev before using it as an LLM judge.
- Mismatch: a general judge benchmark; this is one run per setting on two small sets.

## How it works

`src/jev_bias/client.py` posts noul and pairwise choice questions to `https://openrouter.ai/api/alpha/decisions` with `typesafe/jev-1.14` and caches every response on disk; `analyze.py` computes shifts, flip rates and bootstrap intervals. Integration evidence: [`src/jev_bias/client.py`](https://github.com/coltranetorres/jev-presentation-bias/blob/5fdfb1bf2d14bcaecfda219757cbec7ed9661e88/src/jev_bias/client.py).

## Get started

Add your OpenRouter key, sync, run the offline tests, then run the pipeline.

```sh
git clone https://github.com/coltranetorres/jev-presentation-bias.git && cd jev-presentation-bias
echo "OPENROUTER_API_KEY=sk-or-..." > .env
uv sync && uv run pytest
uv run python run_all.py tr
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results summaries: [github.com/coltranetorres/jev-presentation-bias/tree/5fdfb1bf2d14bcaecfda219757cbec7ed9661e88/results](https://github.com/coltranetorres/jev-presentation-bias/tree/5fdfb1bf2d14bcaecfda219757cbec7ed9661e88/results)
- Draft write-up: [github.com/coltranetorres/jev-presentation-bias/blob/5fdfb1bf2d14bcaecfda219757cbec7ed9661e88/WRITEUP.md](https://github.com/coltranetorres/jev-presentation-bias/blob/5fdfb1bf2d14bcaecfda219757cbec7ed9661e88/WRITEUP.md)

## Limits and data handling

The author's caveats: one run per setting, only 37 usable MMLU-Pro pairs, high baselines and LLM-written rewrites; the decisions endpoint used is OpenRouter's alpha. Reaches Jev through OpenRouter, not TypeSafe directly. No license file, so no reuse terms are granted.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 5fdfb1bf2d14](https://github.com/coltranetorres/jev-presentation-bias/tree/5fdfb1bf2d14bcaecfda219757cbec7ed9661e88). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
