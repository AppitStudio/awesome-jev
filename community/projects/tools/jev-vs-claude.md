# Jev vs Claude by Abdullah Abdel-Khalek (study and code comparing Jev with Claude Sonnet on confidence, cost and speed)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Paper and replication code for "Can a Decision Model Beat an LLM at Its Own Game?". Study 1 asks whether 300 AI-agent logs (ASSEBench-Safety) show unsafe behaviour; Study 2 asks narrow document questions on SummEdits claims and SEntFiN headlines. Each record goes to Jev and to Claude with the same wording, and the scripts measure calibration, confidence gates, accuracy at matched coverage and a Jev-then-Claude cascade with bootstrap intervals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AbdullahAbdelKhalek/jev-vs-claude) |
| Maintainer | [AbdullahAbdelKhalek](https://github.com/AbdullahAbdelKhalek). Independently curated. |
| Format | Python research scripts + PDF paper |
| Requirements | Python 3.13; an OpenRouter key for Jev and an Anthropic key for Claude (the author puts all model runs at about $8.50). |
| License | [MIT](https://github.com/AbdullahAbdelKhalek/jev-vs-claude/blob/546d031b7623e2d982380f420b32503b15718317/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/run_models.py`](https://github.com/AbdullahAbdelKhalek/jev-vs-claude/blob/546d031b7623e2d982380f420b32503b15718317/src/run_models.py) at the pinned commit. |

## When to use

- Decide whether a cheap decision model can take over yes/no judgments from an LLM, and where to hand unsure answers to the LLM.
- Mismatch: a reusable library; these are one study's scripts.

## How it works

`src/run_models.py` and `src/run_study2.py` send all questions about one text in one request as `typesafe/jev-1.14` to OpenRouter's `/api/v1/systemone` endpoint and save each call with its cost and latency; the analysis scripts redraw the figures and check every quoted example against the saved answers. Integration evidence: [`src/run_models.py`](https://github.com/AbdullahAbdelKhalek/jev-vs-claude/blob/546d031b7623e2d982380f420b32503b15718317/src/run_models.py).

## Get started

Install the pinned packages, prepare the datasets (downloaded at pinned commits and hash-checked), then run the dev splits before the test splits.

```sh
git clone https://github.com/AbdullahAbdelKhalek/jev-vs-claude && cd jev-vs-claude
pip install -r requirements.txt
export OPENROUTER_API_KEY=... ANTHROPIC_API_KEY=...
python src/prepare_benchmark.py
python src/run_models.py jev dev
python src/analyze.py dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Paper (PDF): [github.com/AbdullahAbdelKhalek/jev-vs-claude/blob/546d031b7623e2d982380f420b32503b15718317/paper/jev-vs-claude.pdf](https://github.com/AbdullahAbdelKhalek/jev-vs-claude/blob/546d031b7623e2d982380f420b32503b15718317/paper/jev-vs-claude.pdf)
- Reliability figure: [github.com/AbdullahAbdelKhalek/jev-vs-claude/blob/546d031b7623e2d982380f420b32503b15718317/paper/figures/reliability_3panel.png](https://github.com/AbdullahAbdelKhalek/jev-vs-claude/blob/546d031b7623e2d982380f420b32503b15718317/paper/figures/reliability_3panel.png)

## Limits and data handling

Results are the author's own: for example Jev tied Claude on agent safety (68.7% vs 67.3%) at 80 to 250 times lower cost, but its confidence on the broad safety question could not be trusted. No data is included; records are sent to OpenRouter and Anthropic when you run it.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 546d031b7623](https://github.com/AbdullahAbdelKhalek/jev-vs-claude/tree/546d031b7623e2d982380f420b32503b15718317). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
