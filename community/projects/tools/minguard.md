# MinGuard (paper artifacts for data-minimization guards on LLM text-to-SQL agents, with Jev as a guard)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code, workloads, guard scores and human labels for the MinGuard paper (ICDE 2027 submission) on calibrated checks that stop an LLM database agent from returning more personal data than a request needs. Guards combine a deterministic SQL fact layer with single-fact questions answered by hosted Jev 1.13, the open JEV-27B, LLM judges and small classifiers, under conformal risk control. All scores are stored, so tables and figures rebuild without API keys. Code comments partly in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tusu-code/Minguard) |
| Maintainer | [tusu-code](https://github.com/tusu-code). Independently curated. |
| Format | Python research artifacts |
| Requirements | Python 3 and the requirements; the BIRD dev set download; `OPENROUTER_API_KEY` only to re-run the guards. |
| License | [MIT](https://github.com/tusu-code/Minguard/blob/74c15a43cb573a7d51af43091d081ce870e19f7d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_client.py`](https://github.com/tusu-code/Minguard/blob/74c15a43cb573a7d51af43091d081ce870e19f7d/src/jev_client.py) at the pinned commit. |

## When to use

- Study how typed decision models compare with LLM judges for privacy guardrails on SQL agents.
- Mismatch: research artifacts for a paper, not a drop-in guard library.

## How it works

`jev_client.py` calls System One over OpenRouter, TypeSafe or Vercel's decisions API with a disk cache, rate limiting and spend tracking; `run_guards.py` pins `jev-1.13-20260917` for the reported runs. Integration evidence: [`src/jev_client.py`](https://github.com/tusu-code/Minguard/blob/74c15a43cb573a7d51af43091d081ce870e19f7d/src/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install -r requirements.txt
bash reproduce.sh   # rebuilds tables and figures from stored scores; no API key needed
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Guards and baselines: [github.com/tusu-code/Minguard/blob/74c15a43cb573a7d51af43091d081ce870e19f7d/src/guards.py](https://github.com/tusu-code/Minguard/blob/74c15a43cb573a7d51af43091d081ce870e19f7d/src/guards.py)

## Limits and data handling

Re-running guards sends SQL requests and schema facts to the chosen provider. BIRD data is downloaded separately under its own terms. Not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 74c15a43cb57](https://github.com/tusu-code/Minguard/tree/74c15a43cb573a7d51af43091d081ce870e19f7d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
