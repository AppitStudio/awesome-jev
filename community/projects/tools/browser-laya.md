# browser-laya

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Runs the open Laya System One decision model entirely in a browser tab (ONNX on WebGPU or WASM): an npm library `@wexare/laya-web` and a hosted playground answer typed choice / score / noul questions in the Jev request shape with no server or API key once the ~900 MB weights are cached.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wexare-ai/browser-laya) |
| Maintainer | [wexare-ai](https://github.com/wexare-ai). Independently curated. |
| Format | npm library (`@wexare/laya-web`) and a static web playground |
| Requirements | A WebGPU-capable browser recommended (WASM fallback); ~900 MB first download. Python + uv only to regenerate fixtures or export ONNX. |
| License | [MIT](https://github.com/wexare-ai/browser-laya/blob/c156ac60cd35b1f228e61b129d4715e28972b051/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run cheap typed decisions privately in a web app without a backend.
- Prototype Jev-style questions before paying for hosted calls.
- Mismatch: large first download; Laya accuracy differs from hosted Jev.

## How it works

[`packages/laya-web/src/laya.ts`](https://github.com/wexare-ai/browser-laya/blob/c156ac60cd35b1f228e61b129d4715e28972b051/packages/laya-web/src/laya.ts) tokenizes the state and questions and scores every option in one forward pass inside a worker ([`worker.ts`](https://github.com/wexare-ai/browser-laya/blob/c156ac60cd35b1f228e61b129d4715e28972b051/packages/laya-web/src/worker.ts)); [`tools/export_onnx.py`](https://github.com/wexare-ai/browser-laya/blob/c156ac60cd35b1f228e61b129d4715e28972b051/tools/export_onnx.py) produces the fp16 ONNX weights and `tools/eval_agreement.py` checks agreement with Python Laya.

## Get started

Try the hosted playground, or add the library (README *Use the library*):

```sh
npm install @wexare/laya-web
# or run the playground locally
git clone https://github.com/wexare-ai/browser-laya.git && cd browser-laya
pnpm install && pnpm dev
```

No inference charges; runs on the user's device.

## Examples and demos

- [Live playground](https://wexare-ai.github.io/browser-laya/) (reachable 2026-10-08).
- npm package: [`@wexare/laya-web`](https://www.npmjs.com/package/@wexare/laya-web) (0.1.1).
- README *Measured behaviour* and *Accuracy* (author-measured).

## Limits and data handling

Runs open Laya, not TypeSafe Jev; data stays in the page after weights download. Measurements are the author's. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit c156ac60cd35](https://github.com/wexare-ai/browser-laya/tree/c156ac60cd35b1f228e61b129d4715e28972b051). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
