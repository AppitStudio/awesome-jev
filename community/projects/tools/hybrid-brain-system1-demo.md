# Hybrid Brain (classroom demo: Jev routes, an LLM answers)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Live classroom demo of System 1 decision models: you type a task and two routers pick which GWDG supercomputer model should answer, Jev (via OpenRouter) or a free local CLM-8B answering typed Choice, Noul and Score questions with probabilities versus an LLM generating its routing decision as JSON, showing decision time, probability bars, cost and whether the JSON was usable; a gatekeeper trusts Jev only above a confidence slider.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sina-778/system1-demo) |
| Maintainer | [sina-778](https://github.com/sina-778). Independently curated. |
| Format | Streamlit app (Python) |
| Requirements | Python; an OpenRouter key for Jev and GWDG access for the answering models (or the local CLM-8B). |
| License | [MIT](https://github.com/sina-778/system1-demo/blob/235d2099489a6f9d9d1eaf14ba0c608892e87cb1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`brains.py`](https://github.com/sina-778/system1-demo/blob/235d2099489a6f9d9d1eaf14ba0c608892e87cb1/brains.py) at the pinned commit. |

## When to use

- Show students the difference between typed decisions and LLM-as-router.
- Mismatch: built around GWDG academic models; a teaching demo, not a production router.

## How it works

`brains.py` calls the real `/v1/systemone` route for Jev (`~typesafe/jev-latest` via OpenRouter) and for a local CLM server, and reads the probabilities back. Integration evidence: [`brains.py`](https://github.com/sina-778/system1-demo/blob/235d2099489a6f9d9d1eaf14ba0c608892e87cb1/brains.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/sina-778/system1-demo && cd system1-demo
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/sina-778/system1-demo#readme](https://github.com/sina-778/system1-demo#readme)

## Limits and data handling

Tasks go to OpenRouter/TypeSafe and to GWDG. Timings and costs shown are live measurements in your session.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 235d2099489a](https://github.com/sina-778/system1-demo/tree/235d2099489a6f9d9d1eaf14ba0c608892e87cb1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
