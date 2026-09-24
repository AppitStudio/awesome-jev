# jev-omni.js

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Browser WebGPU runner for the independent [Jev-Omni](jev-omni.md) multimodal decision classifier via onnxruntime-web (text + images; video/audio not done yet).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ai-ecoverse/jev-omni.js) |
| Maintainer | [ai-ecoverse](https://github.com/ai-ecoverse). Independently curated. |
| Format | JavaScript/TypeScript library + GitHub Pages demo. |
| Requirements | Chrome with WebGPU; large memory (upstream tested on M4 Max 128 GB); ~13.6 GB first download from Hugging Face. |
| License | [Apache-2.0](https://github.com/ai-ecoverse/jev-omni.js/blob/58aa8d3caadba7b973655b33ab07b910cdf1544f/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement or parity claim with official Jev. Distinct from the [Jev-Omni HF weights](jev-omni.md) listing. Live WebGPU demo not run on the review host. |

## When to use

Use to **run Jev-Omni in-browser** on WebGPU without a CUDA server. Prefer the HF Python loader when you have a large GPU and want the reference stack.

## How it works

`loadJevOmni` downloads a SHA-256-checked ONNX bundle into Cache Storage, then `predict` returns option probabilities for a state/question (optional RGBA image). Work-in-progress: text and image paths documented; video/audio pending (per README).

## Get started

```js
import * as ort from "onnxruntime-web/webgpu";
import { loadJevOmni } from "@ai-ecoverse/jev-omni.js";

const jev = await loadJevOmni(
  "https://huggingface.co/ai-ecoverse/jev-omni.js/resolve/main/jev-omni",
  { ort }
);
const res = await jev.predict({
  state: "The meeting starts at 10 AM. It is now 9 AM.",
  question: "Has the meeting started?",
  options: ["Yes", "No"],
});
```

Pin review tip: `58aa8d3caadba7b973655b33ab07b910cdf1544f`. Demo: [ai-ecoverse.github.io/jev-omni.js](https://ai-ecoverse.github.io/jev-omni.js/).

## Examples and demos

- Public demo site (large download).
- Phase docs under `docs/phase1-text.md` and `docs/phase2-images.md`.

## Limits and data handling

Weights stay in the browser cache after download. Independent of TypeSafe hosted Jev; Jev-Omni states it is independent of TypeSafe AI's Jev.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 58aa8d3](https://github.com/ai-ecoverse/jev-omni.js/tree/58aa8d3caadba7b973655b33ab07b910cdf1544f). AI-assisted README and LICENSE inspection; WebGPU load not executed.

Related: [Jev-Omni](jev-omni.md), [kevala](kevala.md).
