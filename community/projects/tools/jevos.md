# jevos

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Self-hosted, Jev-compatible `/v1/systemone` server that answers yes/no (Noul) questions from a CPU-only 1B GGUF model, fully offline.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/feder-cr/jev) |
| Maintainer | [Federico Elia](https://github.com/feder-cr) and [Loris Salsi](https://github.com/LosaLosSantos); self-submission. |
| Format | Python/FastAPI decision-model API server; llama.cpp GGUF weights, CPU-only. |
| Requirements | Python runtime and llama.cpp for local inference; no TypeSafe cloud key or GPU required. |
| License | [MIT](https://github.com/feder-cr/jev/blob/eb74cf78e5377e85fcaa76f6ebc9f82e8b517250/LICENSE). |
| Disclosure | Submitted by one of the project's maintainers (self-submission); independent of hosted TypeSafe Jev; listing is not an endorsement. |

## When to use

- You want code written against the official TypeSafe Jev SDK to keep working for yes/no questions, but need a fully offline, CPU-only, self-hosted engine instead of the hosted API.
- You can accept a small distilled model in place of Jev's own weights: on 2,000 held-out yes/no rule questions from policies not seen in training, the authors report jevos at 0.815 accuracy against Jev's 0.927 (Laya: 0.489) — a real accuracy gap, not a drop-in substitute where correctness matters most.
- Choice and Score questions are out of scope; the server returns HTTP 422 for anything other than a Noul (yes/no) question.

## How it works

The authors cut a MiniCPM5-1B checkpoint down to 17 layers, added a single-logit output head, and exported it to GGUF (q4_k_m and q8_0 builds) served locally through llama.cpp on CPU only — one forward pass per request, no text generation. The FastAPI layer implements the same `/v1/systemone` wire format as hosted Jev, so the official TypeSafe SDK works unchanged for yes/no questions; the [`/v1/systemone` handler](https://github.com/feder-cr/jev/blob/eb74cf78e5377e85fcaa76f6ebc9f82e8b517250/src/jev/api/app.py) rejects Choice/Score payloads with a 422 rather than emulating them. Application policy, parsing, and downstream actions stay in the caller's code, as with Jev itself.

## Get started

```sh
git clone https://github.com/feder-cr/jev.git
cd jev
git checkout eb74cf78e5377e85fcaa76f6ebc9f82e8b517250
```

Download `jevos-q4_k_m.gguf` (619 MB) or `jevos-q8_0.gguf` from the [jevos release](https://github.com/feder-cr/jev/releases/tag/jevos), then follow the upstream README to sync the Python environment, fetch the matching llama.cpp runtime, and start the FastAPI server pointed at the downloaded weights. Commands were not executed on the review host.

## Examples and demos

- [jevos release](https://github.com/feder-cr/jev/releases/tag/jevos) — `jevos-q4_k_m.gguf` and `jevos-q8_0.gguf` weights with a `SHA256SUMS.txt` checksum file.
- [`/v1/systemone` handler](https://github.com/feder-cr/jev/blob/eb74cf78e5377e85fcaa76f6ebc9f82e8b517250/src/jev/api/app.py) — request handling and the 422 response for non-Noul questions.
- Upstream README benchmark chart — latency and accuracy figures reproduced under Limits below.

## Limits and data handling

Noul-only: Choice and Score requests return HTTP 422 rather than a best-effort answer. Inference is local and offline (llama.cpp on CPU), so request text does not leave the host. The authors' own benchmark on an Intel Core Ultra 7 255H (16 threads) reports 54 ms / 220 ms (short/long request) for jevos versus 344 ms / 345 ms for the hosted Jev API and 104 ms / 449 ms for Laya on the same CPU. Accuracy on 2,000 yes/no questions drawn from policies not seen in training is 0.815 for jevos, 0.927 for Jev, and 0.489 for Laya — Jev remains the more accurate option of the three. These are the authors' reported figures, not independently reproduced for this catalog entry.

## Review and maintenance

Reviewed **2026-09-27** at [commit eb74cf7](https://github.com/feder-cr/jev/tree/eb74cf78e5377e85fcaa76f6ebc9f82e8b517250) and the [jevos release](https://github.com/feder-cr/jev/releases/tag/jevos). The README, LICENSE, release assets, and the `/v1/systemone` handler were inspected; install and live-serving paths were not executed on the review host. Benchmark and accuracy figures are the authors' own reported results, not rerun independently.

Related: [Decis](chaitin-decis.md) for another self-hosted `/v1/systemone` server; [TinyJev](tinyjev.md) for a similarly sized offline System One–compatible model.
