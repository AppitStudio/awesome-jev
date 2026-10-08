# 2048: Jev vs Laya

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Experiment where two System One decision models — hosted TypeSafe Jev and open-weight Laya (plus a LoRA fine-tune) — play 2048 on the same seeds against random and greedy baselines, each move asking a `move` choice and a `danger` yes/no from a board description, with every move logged and reports comparing win likelihood, choices and latency.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Devikrishna545/2048GameDecision) |
| Maintainer | [Devikrishna545](https://github.com/Devikrishna545). Independently curated. |
| Format | Python scripts (`python -m runner.simulate`, `runner.report`) |
| Requirements | Python; `TYPESAFE_API_KEY` for Jev; PyTorch and an ~843 MB Laya checkpoint for Laya. |
| License | [MIT](https://github.com/Devikrishna545/2048GameDecision/blob/47a04bb7dd964b3f9c8b803acbbad91b40133968/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Compare hosted vs open System One models on a simple, seeded game.
- Mismatch: small game counts; results are the author's runs.

## How it works

[`agents/jev_agent.py`](https://github.com/Devikrishna545/2048GameDecision/blob/47a04bb7dd964b3f9c8b803acbbad91b40133968/agents/jev_agent.py) and [`agents/laya_agent.py`](https://github.com/Devikrishna545/2048GameDecision/blob/47a04bb7dd964b3f9c8b803acbbad91b40133968/agents/laya_agent.py) share a request builder in [`agents/base.py`](https://github.com/Devikrishna545/2048GameDecision/blob/47a04bb7dd964b3f9c8b803acbbad91b40133968/agents/base.py); fine-tuning notes in [`finetuning/RESULTS.md`](https://github.com/Devikrishna545/2048GameDecision/blob/47a04bb7dd964b3f9c8b803acbbad91b40133968/finetuning/RESULTS.md).

## Get started

Run games (README):

```sh
git clone https://github.com/Devikrishna545/2048GameDecision.git && cd 2048GameDecision
pip install -r requirements.txt
export TYPESAFE_API_KEY=...   # Jev only
python -m runner.simulate --agents laya jev greedy random --games 10 --run-id main
```

Jev moves bill your key; Laya runs locally.

## Examples and demos

- Held-out report: [`results/heldout/report.md`](https://github.com/Devikrishna545/2048GameDecision/blob/47a04bb7dd964b3f9c8b803acbbad91b40133968/results/heldout/report.md).

## Limits and data handling

Board states go to TypeSafe for Jev. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 47a04bb7dd96](https://github.com/Devikrishna545/2048GameDecision/tree/47a04bb7dd964b3f9c8b803acbbad91b40133968). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
