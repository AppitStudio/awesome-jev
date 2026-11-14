# jev-skillbench (benchmark of Jev as a malicious agent-skill detector on MalSkillBench, with a verify-and-escalate cascade to an LLM)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Measures whether Jev catches malicious agent skills on the public MalSkillBench corpus (about 3,900 malicious and 4,000 benign skills): Jev reads each skill's code and instructions together, and only uncertain cases go to an LLM. The maintainer reports Jev settling 83% of skills alone and the cascade reaching 95% recall at 0.8% false positives, compared with an LLM-on-everything baseline; per-sample results and costs are committed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MohibShaikh/jev-skillbench) |
| Maintainer | [MohibShaikh](https://github.com/MohibShaikh). Independently curated. |
| Format | Python CLI and committed results (MIT) |
| Requirements | Python 3 and uv; a `TYPESAFE_API_KEY` (or an OpenRouter key) for the Jev arm and an LLM key for the escalation arm. |
| License | [MIT](https://github.com/MohibShaikh/jev-skillbench/blob/650c9956b28686c4b47c4b5d3f56a46befd42b35/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_skillbench/detect.py`](https://github.com/MohibShaikh/jev-skillbench/blob/650c9956b28686c4b47c4b5d3f56a46befd42b35/src/jev_skillbench/detect.py) at the pinned commit. |

## When to use

- Judge whether Jev is a fit as a first-pass scanner for third-party agent skills.
- Mismatch: a ready-made skill scanner for production; it is a measurement harness.

## How it works

`src/jev_skillbench/detect.py` calls Jev through the TypeSafe Python SDK (default `jev-1.13.0`) or OpenRouter (`~typesafe/jev-latest`); `questions.py` defines the Choice, Noul and Score questions about each skill. Integration evidence: [`src/jev_skillbench/detect.py`](https://github.com/MohibShaikh/jev-skillbench/blob/650c9956b28686c4b47c4b5d3f56a46befd42b35/src/jev_skillbench/detect.py).

## Get started

Install, fetch the benchmark, then run the Jev arm.

```sh
git clone https://github.com/MohibShaikh/jev-skillbench && cd jev-skillbench
uv venv .venv && uv pip install -e ".[dev]"
cp .env.example .env    # add a key
.venv/bin/jev-skillbench fetch
.venv/bin/jev-skillbench run --arm jev --per-class 50
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results: [github.com/MohibShaikh/jev-skillbench/blob/650c9956b28686c4b47c4b5d3f56a46befd42b35/README.md](https://github.com/MohibShaikh/jev-skillbench/blob/650c9956b28686c4b47c4b5d3f56a46befd42b35/README.md)
- Results: [github.com/MohibShaikh/jev-skillbench/tree/650c9956b28686c4b47c4b5d3f56a46befd42b35/results](https://github.com/MohibShaikh/jev-skillbench/tree/650c9956b28686c4b47c4b5d3f56a46befd42b35/results)

## Limits and data handling

Skill contents from the benchmark are sent to TypeSafe (and the LLM for escalations) on your keys. Results are the maintainer's own runs on one benchmark; MalSkillBench baselines are cited, not rerun.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 650c9956b286](https://github.com/MohibShaikh/jev-skillbench/tree/650c9956b28686c4b47c4b5d3f56a46befd42b35). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
