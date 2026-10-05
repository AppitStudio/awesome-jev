# TensorSharp

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Native .NET GGUF inference engine and agent runtime that serves a Jev-compatible `POST /v1/systemone` with DiffusionGemma, answering typed questions over text, images, documents, video frames and transcripts; `jev-latest` is an alias for the local model, not hosted Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zhongkaifu/TensorSharp) |
| Product homepage | [tensorsharp.ai](https://tensorsharp.ai) |
| Maintainer | [zhongkaifu](https://github.com/zhongkaifu). Independently curated. |
| Format | Self-hosted inference server and libraries; Jev-compatible decision endpoint documented in `docs/models/jev.md` |
| Requirements | .NET SDK, the DiffusionGemma 26B-A4B Q4_K_M GGUF (downloaded by the config), and a 16 GiB CUDA GPU for the reference recipe, or a CPU backend; the vision tower (2.8 GB) only for image rows. No TypeSafe key. |
| License | [BSD-3-Clause](https://github.com/zhongkaifu/TensorSharp/blob/b72e393d449e02b7bc1b88323588db267d454738/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Serve Jev-format decisions on-premises from a .NET stack, including multimodal state (screenshots, PDFs, sampled video frames).
- Prototype against the Jev request shape without sending data to a hosted API.
- Mismatch: this is not TypeSafe's model and has no numerical parity claim; use hosted Jev where its calibration matters.

## How it works

The server builds an answer canvas with one token slot per question and reads the requested label logits after a single DiffusionGemma denoising step — no sampling or JSON generation — following the structured-read approach in vLLM PR #57250. Requests carry `state` and typed questions; responses give `noul` probabilities, choices and expected scores. Upstream states that `jev-latest`/`jev-preview` are aliases for the loaded model, not the proprietary hosted Jev ([docs/models/jev.md](https://github.com/zhongkaifu/TensorSharp/blob/b72e393d449e02b7bc1b88323588db267d454738/docs/models/jev.md)).

## Get started

From a checkout, start the server with the Jev DiffusionGemma configuration (local inference; downloads the model on first run):

```sh
git clone https://github.com/zhongkaifu/TensorSharp.git && cd TensorSharp
dotnet run --project TensorSharp.Server.Host -c Release -- --config config/jev-diffusiongemma-q4.json
# add --backend cpu for the pure-C# CPU path; then POST http://127.0.0.1:5000/v1/systemone
```

Local inference has no TypeSafe charge; hardware and model-download costs are yours.

## Examples and demos

- [docs/models/jev.md](https://github.com/zhongkaifu/TensorSharp/blob/b72e393d449e02b7bc1b88323588db267d454738/docs/models/jev.md): server recipe, attachments, CPU timings measured by the maintainer with `eng/JevProbe` (for example 0.92 s for a width-16 read on an i7-11800H), and the quality probe.
- `InferenceWeb.Tests/Fixtures/JevAttachments`: request fixtures for policy/review/outage states.

## Limits and data handling

Large model downloads and GPU memory tuning (`DIFFUSION_VRAM_HEADROOM_MB`) are required for the GPU recipe. Timings and probe results are upstream measurements; no build or inference ran on the review host. Not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit b72e393d449e](https://github.com/zhongkaifu/TensorSharp/tree/b72e393d449e02b7bc1b88323588db267d454738). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
