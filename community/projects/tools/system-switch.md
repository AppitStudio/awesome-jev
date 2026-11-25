# System Switch by Gianluca Bailo (paper and code: when should a fast System One decision model in Doom stop and ask a reasoning model?)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code and data for the arXiv paper *System Switch*. A fast System One actor plays Doom through doomLaya and takes every decision; a gate watches for low confidence, loops or no progress and then asks a vision reasoning model for a plan. It compares open Jev-style models (Laya, OpenJev, Clef and others) zero-shot and measures when deferring to the reasoner helps.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dexmac221/system-switch) |
| Maintainer | Gianluca Bailo ([dexmac221](https://github.com/dexmac221)). Independently curated. |
| Format | Python research code with patches for doomLaya |
| Requirements | doomLaya at commit b25edd3, a llama.cpp server with System One support for the actor models, and a chat model for the reasoner. |
| License | [Apache-2.0](https://github.com/dexmac221/system-switch/blob/ece62efe4995fbe1cc023b984919f65c7d8d3967/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/serve_systemone.py`](https://github.com/dexmac221/system-switch/blob/ece62efe4995fbe1cc023b984919f65c7d8d3967/src/serve_systemone.py) at the pinned commit. |

## When to use

- Study when a fast decision model should defer to a slower reasoner.
- Mismatch: if you want results for TypeSafe's hosted Jev; the paper tests open models.

## How it works

`src/serve_systemone.py` bridges doomLaya's `/predict` to any llama.cpp `/v1/systemone` server (TypeSafe-compatible request shape); `src/switch.py` implements the gate and plans. The paper evaluates open models; no TypeSafe Jev calls are made. Integration evidence: [`src/serve_systemone.py`](https://github.com/dexmac221/system-switch/blob/ece62efe4995fbe1cc023b984919f65c7d8d3967/src/serve_systemone.py).

## Get started

Patch doomLaya, copy the switch code in, then follow the reproducing steps.

```sh
git -C doomLaya apply ../system-switch/patches/doomLaya-agent.patch
(cd doomLaya && python ../system-switch/patches/apply_switch_patch.py)
# then see README 'Reproducing'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Paper: [arxiv.org/abs/2610.09683](https://arxiv.org/abs/2610.09683)

## Limits and data handling

Results are the author's own: deferring 30% of decisions to Qwen3.6-35B-A3B gains +0.13 accuracy with doomLaya's option order and +0.08 with shuffled options, and in closed-loop play no variant reached the exit.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit ece62efe4995](https://github.com/dexmac221/system-switch/tree/ece62efe4995fbe1cc023b984919f65c7d8d3967). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
