# Claim Laundering (paper code: decision models trust an agent's record over reality)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Paper code from the University of Southern California showing that fast decision models, hosted Jev among them, follow an agent's own record of success when an action silently failed, across three domains, and that a linear probe on a middle layer (EviGate) can veto those decisions in open models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tinakhezresmaeilzadeh/claim-laundering) |
| Maintainer | [tinakhezresmaeilzadeh](https://github.com/tinakhezresmaeilzadeh). Independently curated. |
| Format | Python research code with paper |
| Requirements | Python 3.12; an OpenRouter key for hosted Jev; GPUs for the open models. |
| License | [MIT](https://github.com/tinakhezresmaeilzadeh/claim-laundering/blob/3cb0248dca2da2d82592ea6ce7d7c707387ce38b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/scoring/run_jev.py`](https://github.com/tinakhezresmaeilzadeh/claim-laundering/blob/3cb0248dca2da2d82592ea6ce7d7c707387ce38b/src/scoring/run_jev.py) at the pinned commit. |

## When to use

- Understand a failure mode before letting a decision model gate agent actions.
- Reproduce the hosted-Jev results.
- Mismatch: research code; EviGate applies to open models, not hosted Jev.

## How it works

`src/scoring/run_jev.py` sends the agent states to OpenRouter's System One route with `typesafe/jev-1.13`. Integration evidence: [`src/scoring/run_jev.py`](https://github.com/tinakhezresmaeilzadeh/claim-laundering/blob/3cb0248dca2da2d82592ea6ce7d7c707387ce38b/src/scoring/run_jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/tinakhezresmaeilzadeh/claim-laundering && cd claim-laundering
# see the README for setup; hosted Jev reads ~/.openrouter_key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Paper: [arxiv.org/abs/2610.25947](https://arxiv.org/abs/2610.25947)
- README: [github.com/tinakhezresmaeilzadeh/claim-laundering#readme](https://github.com/tinakhezresmaeilzadeh/claim-laundering#readme)

## Limits and data handling

Benchmark states go to OpenRouter and on to TypeSafe. Results are the authors'. Independent research; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 3cb0248dca2d](https://github.com/tinakhezresmaeilzadeh/claim-laundering/tree/3cb0248dca2da2d82592ea6ce7d7c707387ce38b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
