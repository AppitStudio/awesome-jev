# recalibench by Pankaj Daga (measure and fix how honest Jev's confidence is on your own labelled cases)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A plug-in Python framework that measures how far a decision model's stated confidence is from reality on your task, fits a post-hoc calibrator on a few thousand labelled cases (eight families, from temperature and Platt to isotonic and Dirichlet) and shows what that buys in automation at a fixed accuracy. It ships a live benchmark of `jev-1.14.0` on three public tasks, an HTML report and a Streamlit app.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dagap/recalibench) |
| Maintainer | [dagap](https://github.com/dagap). Independently curated. |
| Format | Python package + CLI (`recal`) + Streamlit app |
| Requirements | Python 3.13 and uv; a TypeSafe API key only for live mode (mock mode runs offline for free). |
| License | [MIT](https://github.com/dagap/recalibench/blob/9aa3cae0e80f0bb484bda62a074cf1b20462d55c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/recalibench/models/jev.py`](https://github.com/dagap/recalibench/blob/9aa3cae0e80f0bb484bda62a074cf1b20462d55c/src/recalibench/models/jev.py) at the pinned commit. |

## When to use

- Before acting on thresholds like "auto-approve above 95%", check and correct whether Jev's probabilities mean what they say on your data.
- Mismatch: tasks without a labelled sample; calibration has to be fitted per task.

## How it works

`src/recalibench/models/jev.py` calls `https://api.typesafe.ai/v1` with a pinned model version (configured in `conf/model/jev.yaml`), with bounded concurrency, retries, a response cache, question batching and a budget cap that estimates cost before spending. Integration evidence: [`src/recalibench/models/jev.py`](https://github.com/dagap/recalibench/blob/9aa3cae0e80f0bb484bda62a074cf1b20462d55c/src/recalibench/models/jev.py).

## Get started

Run the whole pipeline offline in mock mode, open the app, then estimate and run live against Jev with your key.

```sh
git clone https://github.com/dagap/recalibench && cd recalibench
uv sync
make all        # mock mode, offline
make demo       # Streamlit app
cp .env.example .env   # add TYPESAFE_API_KEY
make estimate MODE=live
make smoke
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Design notes: [github.com/dagap/recalibench/blob/9aa3cae0e80f0bb484bda62a074cf1b20462d55c/docs/DESIGN.md](https://github.com/dagap/recalibench/blob/9aa3cae0e80f0bb484bda62a074cf1b20462d55c/docs/DESIGN.md)
- Live report (download and open): [github.com/dagap/recalibench/blob/9aa3cae0e80f0bb484bda62a074cf1b20462d55c/reports/report.html](https://github.com/dagap/recalibench/blob/9aa3cae0e80f0bb484bda62a074cf1b20462d55c/reports/report.html)

## Limits and data handling

The reported numbers are the author's own (for example ECE 0.117 to 0.005 on a workers' comp task; the full live run of 15,000 requests cost $0.55). Live mode sends your cases to TypeSafe. One of the two datasets downloads from osha.gov, which may block automated downloads.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 9aa3cae0e80f](https://github.com/dagap/recalibench/tree/9aa3cae0e80f0bb484bda62a074cf1b20462d55c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
