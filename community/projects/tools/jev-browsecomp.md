# jev-browsecomp

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research harness comparing cheap TypeSafe Jev typed decisions (Choice/Noul act|review|abstain over stable doc ids) to full-LLM and Recursive Language Model pipelines on BrowseComp-Plus–style must-cite QA.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jjd-lab/jev-browsecomp) |
| Maintainer | [jjd-lab](https://github.com/jjd-lab). Independently curated; not affiliated with TypeSafe. |
| Format | Python research harness + scoreboards. |
| Requirements | Python 3; offline pytest needs no keys. Live arms need TYPESAFE_API_KEY and ANTHROPIC_API_KEY; corpus builds need substantial disk/Docker. |
| License | [Apache-2.0](https://github.com/jjd-lab/jev-browsecomp/blob/24e488ae02bea93d77179f4059be83e893842a90/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Upstream FINDINGS not independently reproduced. |

## When to use

Use to **reproduce or extend** BrowseComp-Plus experiments where Jev screens candidate docs before a single reader call. Not a production search product.

## How it works

Code owns corpus indexing, arm orchestration, and mechanical citation checks. Jev answers typed questions in [`must_cite_rlm/rlm_jev.py`](https://github.com/jjd-lab/jev-browsecomp/blob/24e488ae02bea93d77179f4059be83e893842a90/must_cite_rlm/rlm_jev.py). Results under `results/` and `wiki/`.

## Get started

```sh
git clone https://github.com/jjd-lab/jev-browsecomp.git
cd jev-browsecomp
git checkout 24e488ae02bea93d77179f4059be83e893842a90
pip install pytest && python3 -m pytest
# live corpus/RLM arms: see upstream wiki (not run here)
```

## Examples and demos

- [`results/FINDINGS.md`](https://github.com/jjd-lab/jev-browsecomp/blob/24e488ae02bea93d77179f4059be83e893842a90/results/FINDINGS.md)
- [https://jjd-lab.github.io/jev-browsecomp/](https://jjd-lab.github.io/jev-browsecomp/)

## Limits and data handling

Live questions/doc text go to TypeSafe and Anthropic when arms run. Upstream accuracy/cost claims are author-reported. Do not install typesafe-sdk into the venv per upstream.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 24e488a](https://github.com/jjd-lab/jev-browsecomp/tree/24e488ae02bea93d77179f4059be83e893842a90). AI-assisted README and LICENSE inspection of harness layout; install/live paths not executed.
