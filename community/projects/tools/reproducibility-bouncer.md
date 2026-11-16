# reproducibility-bouncer (paper auditor that scores a publication's reproducibility with deterministic evidence, Jev judging and an optional re-run harness)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Audit a scientific paper (by DOI or PDF) for reproducibility, robustness and methodological and statistical soundness. Deterministic evidence gathering pulls the paper, data and code availability; Jev answers typed judging questions for each audit stage; an LLM drafts proposals; and the full mode uses an Orbit-backed harness that actually tries to re-run the analysis. Output is an audit record and a readiness report. Mock judge and generator modes run offline for development.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/d-callan/reproducibility-bouncer) |
| Maintainer | [d-callan](https://github.com/d-callan). Independently curated. |
| Format | Python CLI (`reprobouncer`, MIT), Dockerfile included |
| Requirements | Python; `TYPESAFE_API_KEY` for judged stages, an OpenAI-compatible LLM key, `UNPAYWALL_EMAIL`; Orbit/loom 0.9.x for the reproduction harness. |
| License | [MIT](https://github.com/d-callan/reproducibility-bouncer/blob/4136c2941f68c8b1dcf705183926299db8c6823d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/reproducibility_bouncer/jev.py`](https://github.com/d-callan/reproducibility-bouncer/blob/4136c2941f68c8b1dcf705183926299db8c6823d/src/reproducibility_bouncer/jev.py) at the pinned commit. |

## When to use

- Screen papers for reproducibility red flags before trusting or building on them.
- Mismatch: peer review; the verdicts are model-assisted screening, not expert judgement.

## How it works

`src/reproducibility_bouncer/jev.py` posts typed questions to `https://api.typesafe.ai/v1/systemone` with `jev-latest` by default (`JEV_BASE_URL` and `JEV_MODEL` override it) and returns typed answers with probabilities. Integration evidence: [`src/reproducibility_bouncer/jev.py`](https://github.com/d-callan/reproducibility-bouncer/blob/4136c2941f68c8b1dcf705183926299db8c6823d/src/reproducibility_bouncer/jev.py).

## Get started

Install, try the offline mock audit, then run a real audit with your keys.

```sh
git clone https://github.com/d-callan/reproducibility-bouncer && cd reproducibility-bouncer
pip install -e .
reprobouncer audit doi:10.1073/pnas.2409747121 --mock-jev --mock-llm
export TYPESAFE_API_KEY=... LLM_API_KEY=... UNPAYWALL_EMAIL=you@example.com
reprobouncer audit doi:10.1073/pnas.2409747121 --out audit.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/d-callan/reproducibility-bouncer/blob/4136c2941f68c8b1dcf705183926299db8c6823d/README.md](https://github.com/d-callan/reproducibility-bouncer/blob/4136c2941f68c8b1dcf705183926299db8c6823d/README.md)
- Design: [github.com/d-callan/reproducibility-bouncer/blob/4136c2941f68c8b1dcf705183926299db8c6823d/PLAN.md](https://github.com/d-callan/reproducibility-bouncer/blob/4136c2941f68c8b1dcf705183926299db8c6823d/PLAN.md)

## Limits and data handling

Paper text and evidence go to TypeSafe and your LLM provider on your keys. Early project (design in PLAN.md); verdict quality is not independently measured.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 4136c2941f68](https://github.com/d-callan/reproducibility-bouncer/tree/4136c2941f68c8b1dcf705183926299db8c6823d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
