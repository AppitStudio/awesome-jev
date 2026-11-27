# MiniCPM receipt agent by Doğukan Ürker (local receipt-to-ledger agent where MiniCPM-OCR Jev scores every OCR read on one RTX 3060)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local agent that turns a receipt photo into a ledger entry plus a list of fields a person should check. MiniCPM-V 4.7 plans and checks the arithmetic, MiniCPM-OCR reads regions, and the System One model MiniCPM-OCR Jev scores each read; low-scoring reads are resampled and the best-scored one is kept. Reports results on CORD-v2, a degraded CORD set and SROIE, including where Jev did not make a significant difference. Everything runs on one 12 GB GPU and no receipt leaves the machine.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DogukanUrker/minicpm-receipt-agent) |
| Maintainer | [Doğukan Ürker](https://github.com/DogukanUrker) (DogukanUrker). Independently curated. |
| Format | Python agent + llama.cpp servers and eval scripts |
| Requirements | NVIDIA GPU with about 12 GB VRAM, 16 GB RAM, llama.cpp and the three OpenBMB GGUF models downloaded by `setup.sh`; no cloud key. |
| License | [Apache-2.0](https://github.com/DogukanUrker/minicpm-receipt-agent/blob/718e9441edfff49a3d1be935d8655738bf6587ad/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`agent/clients.py`](https://github.com/DogukanUrker/minicpm-receipt-agent/blob/718e9441edfff49a3d1be935d8655738bf6587ad/agent/clients.py) at the pinned commit. |

## When to use

- People building local document agents who want a self-check score on OCR reads and a review queue instead of silent errors.
- Mismatch: TypeSafe's hosted Jev; this uses OpenBMB's open MiniCPM-OCR Jev model locally.

## How it works

`agent/clients.py` posts each crop and its OCR text to a local llama.cpp `/v1/systemone` endpoint serving MiniCPM-OCR Jev and uses the returned score; below 0.5 the agent samples three more reads and keeps the one Jev scores highest. Integration evidence: [`agent/clients.py`](https://github.com/DogukanUrker/minicpm-receipt-agent/blob/718e9441edfff49a3d1be935d8655738bf6587ad/agent/clients.py).

## Get started

Download the models, start the three local servers, then run the evaluation.

```sh
git clone https://github.com/DogukanUrker/minicpm-receipt-agent && cd minicpm-receipt-agent
bash setup.sh   # downloads OpenBMB GGUF models
bash serve.sh
bash run_all.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example cards: [github.com/DogukanUrker/minicpm-receipt-agent/tree/main/visuals](https://github.com/DogukanUrker/minicpm-receipt-agent/tree/main/visuals)
- OpenBMB post: [x.com/OpenBMB/status/2126304982093947118](https://x.com/OpenBMB/status/2126304982093947118)

## Limits and data handling

Author's own evaluation on 100 receipts per set; the author reports the agent does not significantly beat OCR plus MiniCPM-V in one shot and takes about 3x longer. Built for the OpenBMB MiniCPM Spark Program. Model downloads are large.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 718e9441edff](https://github.com/DogukanUrker/minicpm-receipt-agent/tree/718e9441edfff49a3d1be935d8655738bf6587ad). Inspected the README, LICENSE, `agent/agent.py`, `agent/clients.py` and `setup.sh` at the pinned commit; models were not downloaded or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
