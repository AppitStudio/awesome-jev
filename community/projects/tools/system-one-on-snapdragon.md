# System One on Snapdragon

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Pinned snapshot of setup scripts, Jev-compatible servers and a benchmark harness for running open System One models on Snapdragon X Elite NPU/GPU/CPU and comparing them with Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/esterhuizen/system-one-on-snapdragon) |
| Maintainer | [esterhuizen](https://github.com/esterhuizen). Independently curated. |
| Format | Research harness and scripts (Python, PowerShell) |
| Requirements | Snapdragon X Elite Windows laptop (WSL), model downloads; TypeSafe key only for Jev comparisons. |
| License | [Apache-2.0](https://github.com/esterhuizen/system-one-on-snapdragon/blob/9d2dc083d0e5b8c4a94dd4587e18b75ea899784b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`harness/jevcmp.py`](https://github.com/esterhuizen/system-one-on-snapdragon/blob/9d2dc083d0e5b8c4a94dd4587e18b75ea899784b/harness/jevcmp.py) at the pinned commit. |

## When to use

- Run Laya, Decider, imajev or Winnow-12B locally on Windows-on-Arm hardware behind a Jev-compatible API.
- Compare local System One models with the hosted Jev API on the same items.
- Mismatch: dated snapshot, not a maintained fork; hardware-specific.

## How it works

Servers expose the Jev request shape locally; the harness sends identical typed questions to local models and to Jev and reports metrics. Integration evidence: [`harness/jevcmp.py`](https://github.com/esterhuizen/system-one-on-snapdragon/blob/9d2dc083d0e5b8c4a94dd4587e18b75ea899784b/harness/jevcmp.py).

## Get started

From the upstream README (not run on the review host):

```sh
laya/bin/winrun npu -m laya_snapdragon --models <models\npu> build --seq 128 256 512
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- NPU build notes: `docs/WINNOW-NPU.md`.
- Fine-tuning recipe: `docs/LAYA-FINETUNE.md`.

## Limits and data handling

Benchmark numbers are the maintainer's; not reproduced. Jev comparisons send items to TypeSafe.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 9d2dc083d0e5](https://github.com/esterhuizen/system-one-on-snapdragon/tree/9d2dc083d0e5b8c4a94dd4587e18b75ea899784b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
