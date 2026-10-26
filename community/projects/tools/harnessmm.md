# HarnessMM (paper code: reuse of agent decisions for harness token efficiency, with Jev runs)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research code for an arXiv paper on making agent harnesses cheaper by reusing decisions: a slow model writes future tool actions into an executable decision graph, guarded reuse checks each tool result before replaying a stored action, and recursive self-improvement tunes the setup; ALFWorld runs include a Jev decision runtime.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/YuhuaJiang2002/HarnessMM) |
| Maintainer | [YuhuaJiang2002](https://github.com/YuhuaJiang2002). Independently curated. |
| Format | Python research code |
| Requirements | Python; keys for the models you run; a TypeSafe API key for the Jev ALFWorld runtime. |
| License | [Apache-2.0](https://github.com/YuhuaJiang2002/HarnessMM/blob/9c2ed7b38aec25b137106c7d1276ed589efb0661/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/alfworld_jev_runtime.py`](https://github.com/YuhuaJiang2002/HarnessMM/blob/9c2ed7b38aec25b137106c7d1276ed589efb0661/scripts/alfworld_jev_runtime.py) at the pinned commit. |

## When to use

- Study decision reuse as a way to cut agent tokens.
- Reproduce the paper's ALFWorld experiments with Jev.
- Mismatch: research code; Jev is one runtime among several.

## How it works

`scripts/alfworld_jev_runtime.py` posts ALFWorld states with action questions to `https://api.typesafe.ai/v1/systemone`, pinned to `jev-1.13.0` in `phiagent/learning/alfworld_jev.py`. Integration evidence: [`scripts/alfworld_jev_runtime.py`](https://github.com/YuhuaJiang2002/HarnessMM/blob/9c2ed7b38aec25b137106c7d1276ed589efb0661/scripts/alfworld_jev_runtime.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/YuhuaJiang2002/HarnessMM && cd HarnessMM
# see the README for setup and experiment scripts
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Paper: [arxiv.org/abs/2610.32813](https://arxiv.org/abs/2610.32813)
- README: [github.com/YuhuaJiang2002/HarnessMM#readme](https://github.com/YuhuaJiang2002/HarnessMM#readme)

## Limits and data handling

Jev runs send environment states to TypeSafe. Results are the authors'. Independent research; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 9c2ed7b38aec](https://github.com/YuhuaJiang2002/HarnessMM/tree/9c2ed7b38aec25b137106c7d1276ed589efb0661). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
