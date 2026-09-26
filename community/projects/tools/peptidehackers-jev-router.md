# jev-router (peptidehackers)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local numpy System One heads with statistically certified act-or-escalate routing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/peptidehackers/jev-router) |
| Maintainer | [peptidehackers](https://github.com/peptidehackers). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | From-scratch numpy implementation of Choice/Score/Noul heads + Wilson router. |
| Requirements | Python 3; numpy. No TypeSafe key for core path. |
| License | [MIT](https://github.com/peptidehackers/jev-router/blob/19f292a7a4afd71927ed1ad8c5358314356c53e1/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use to study or reproduce System One routing with local heads—not as a drop-in TypeSafe client.

## How it works

Embedding → parallel typed heads → calibrated confidence → Wilson gate ACT vs ESCALATE; fail-closed on corrupt artifacts. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/peptidehackers/jev-router.git
cd jev-router
git checkout 19f292a7a4afd71927ed1ad8c5358314356c53e1
python3 -m venv .venv && .venv/bin/pip install numpy
.venv/bin/python tests.py
```

Pin revision `19f292a7a4afd71927ed1ad8c5358314356c53e1` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Independent research/prior-art demo; synthetic dataset metrics are not production proof. Distinct from hosted-Jev routers in the catalog.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 19f292a](https://github.com/peptidehackers/jev-router/tree/19f292a7a4afd71927ed1ad8c5358314356c53e1). AI-assisted README and LICENSE inspection; install/live paths not executed.
