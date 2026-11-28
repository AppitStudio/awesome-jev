# jev-local by Robert DiBiano (Jev-style typed decisions from real token probabilities on stock llama-server)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Python client that gives Jev-style typed answers (Noul, Score, Choice, plus bounded integers and numbers) with probabilities from your own GPU on unmodified llama-server. The model only computes decision tokens; all shared JSON is injected, and the prompt wording is imported from TypeSafe's own `system-one-adapter` so it cannot drift. The README is explicit that the probabilities are real but not Jev-calibrated.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DiBianoR/jev_local) |
| Maintainer | [Robert DiBiano](https://github.com/DiBianoR) (DiBianoR). Independently curated. |
| Format | Python library + PowerShell server script |
| Requirements | Prebuilt llama.cpp (2026-09-23 or later) with CUDA on Windows, a GGUF model, Python 3.12. |
| License | [MIT](https://github.com/DiBianoR/jev_local/blob/81766ff67fe82a119ee9f4a1bf7efa06f91f7016/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_local.py`](https://github.com/DiBianoR/jev_local/blob/81766ff67fe82a119ee9f4a1bf7efa06f91f7016/jev_local.py) at the pinned commit. |

## When to use

- Developers who want Jev-shaped decisions from a local model without forking llama.cpp.
- Mismatch: calibrated, hosted-Jev-equivalent answers; expect over-confidence without temperature scaling.

## How it works

`jev_local.py` builds prompts from `system-one-adapter` 0.2.1 (MIT), drives llama-server's completion API token by token, restricts each step's logits to legal answer tokens and renormalises them into per-option probabilities. It does not call hosted Jev. Integration evidence: [`jev_local.py`](https://github.com/DiBianoR/jev_local/blob/81766ff67fe82a119ee9f4a1bf7efa06f91f7016/jev_local.py).

## Get started

Start llama-server with the bundled script, then run the self-test.

```sh
git clone https://github.com/DiBianoR/jev_local && cd jev_local
# edit and run start-llama-server.ps1
pip install -r requirements.txt
python jev_local.py test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Plan and design notes: [github.com/DiBianoR/jev_local/blob/main/PLAN.md](https://github.com/DiBianoR/jev_local/blob/main/PLAN.md)

## Limits and data handling

Independent of TypeSafe; accuracy depends on the local model. Tested on Windows + CUDA.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 81766ff67fe8](https://github.com/DiBianoR/jev_local/tree/81766ff67fe82a119ee9f4a1bf7efa06f91f7016). Inspected the README, LICENSE and `jev_local.py` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
