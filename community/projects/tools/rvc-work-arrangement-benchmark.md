# RVC work-arrangement benchmark by RVC.global (Jev vs Claude Haiku vs GPT-6 Luna on labelling 200 job postings as remote, hybrid or on-site)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Pre-registered test on 200 job postings from the RVC remote-work job board: Jev 1.14 with the board's own question set reached 97.1% weighted accuracy (95% CI 94.3–99.3) versus 94.5% for Claude Haiku 5.5 with reasoning and 87.5% for GPT-6 Luna at medium effort; generic options dropped Jev to 88.6%. Ships gold labels, frozen manifests (OpenTimestamps) and the scorer. The data behind one of the listed Eventum Jev builds.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/maketeamake/rvc-work-arrangement-benchmark) |
| Maintainer | [RVC.global](https://github.com/maketeamake). Independently curated. |
| Format | Python scoring script with run data and gold labels |
| Requirements | Python with numpy to re-score; a TypeSafe key only to re-run the Jev arms. |
| License | [MIT](https://github.com/maketeamake/rvc-work-arrangement-benchmark/blob/08397b473065f9f4d378501e31b7ad101dbda6c2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`arms/run_arm.py`](https://github.com/maketeamake/rvc-work-arrangement-benchmark/blob/08397b473065f9f4d378501e31b7ad101dbda6c2/arms/run_arm.py) at the pinned commit. |

## When to use

- See how much a task-specific question set changes Jev accuracy on a real labelling job.
- Mismatch: a general model ranking; it is one task on 200 postings.

## How it works

`arms/run_arm.py` posts each posting with the arm's question set to `https://api.typesafe.ai/v1/systemone`; `score.py` scores all arms against the gold labels. Integration evidence: [`arms/run_arm.py`](https://github.com/maketeamake/rvc-work-arrangement-benchmark/blob/08397b473065f9f4d378501e31b7ad101dbda6c2/arms/run_arm.py).

## Get started

Re-score the recorded runs offline.

```sh
git clone https://github.com/maketeamake/rvc-work-arrangement-benchmark.git && cd rvc-work-arrangement-benchmark
pip install numpy
python3 score.py runs gold/gold-owner.jsonl
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Report: [github.com/maketeamake/rvc-work-arrangement-benchmark/blob/08397b473065f9f4d378501e31b7ad101dbda6c2/report.txt](https://github.com/maketeamake/rvc-work-arrangement-benchmark/blob/08397b473065f9f4d378501e31b7ad101dbda6c2/report.txt)
- Write-up: [www.eventum.ai/preview/jev-builds/remote-job-labels](https://www.eventum.ai/preview/jev-builds/remote-job-labels)

## Limits and data handling

Gold labels are the job board's own; the board published the write-up with Eventum, a TypeSafe partner. Deviations from the pre-registration are listed in DEVIATIONS.md.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 08397b473065](https://github.com/maketeamake/rvc-work-arrangement-benchmark/tree/08397b473065f9f4d378501e31b7ad101dbda6c2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
