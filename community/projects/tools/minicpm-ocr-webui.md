# MiniCPM-OCR WebUI by Mark20240805 (unofficial Windows one-click bundle: MiniCPM-OCR plus MiniCPM-OCR Jev quality scores, offline)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Unofficial Windows all-in-one (Chinese UI) for OpenBMB's MiniCPM-OCR 1.0 and the Jev-style MiniCPM-OCR Jev scorer: images, PDFs and Word files go through OCR, and the scorer gives each result a 0-1 consistency score against the source image so doubtful reads are flagged, with batch checks, preprocessing and exports. The installer downloads a portable Python, llama.cpp and the models from official sources with pinned checksums; everything then runs on 127.0.0.1.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Mark20240805/MiniCPM-OCR-WebUI) |
| Maintainer | [Mark20240805](https://github.com/Mark20240805). Independently curated. |
| Format | Windows installer scripts + Python server + local WebUI |
| Requirements | Windows 10/11 64-bit, an NVIDIA GPU (6 GB+ VRAM recommended) and about 8 GB of disk. |
| License | [GPL-3.0](https://github.com/Mark20240805/MiniCPM-OCR-WebUI/blob/a46f31c21e3189b784cb0651095284fdada8c78b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/server.py`](https://github.com/Mark20240805/MiniCPM-OCR-WebUI/blob/a46f31c21e3189b784cb0651095284fdada8c78b/app/server.py) at the pinned commit. |

## When to use

- Windows users who want local OCR with an automatic check on which results need a human look.
- Mismatch: hosted Jev; this uses OpenBMB's open Jev-style model locally.

## How it works

`app/server.py` starts llama.cpp with the MiniCPM-OCR Jev GGUF and posts the candidate text and image to its local `/v1/systemone` decision endpoint, reading the probability as the quality score. No hosted TypeSafe call is involved. Integration evidence: [`app/server.py`](https://github.com/Mark20240805/MiniCPM-OCR-WebUI/blob/a46f31c21e3189b784cb0651095284fdada8c78b/app/server.py).

## Get started

Download the repo, run the installer, then start the WebUI.

```sh
git clone https://github.com/Mark20240805/MiniCPM-OCR-WebUI && cd MiniCPM-OCR-WebUI
install.bat
启动MiniCPM-OCR.bat
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Install notes: [github.com/Mark20240805/MiniCPM-OCR-WebUI/blob/main/docs/install.md](https://github.com/Mark20240805/MiniCPM-OCR-WebUI/blob/main/docs/install.md)

## Limits and data handling

Not affiliated with OpenBMB. Model weights (Apache-2.0) and llama.cpp (MIT) keep their own terms. The installer downloads 3-7 GB.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit a46f31c21e31](https://github.com/Mark20240805/MiniCPM-OCR-WebUI/tree/a46f31c21e3189b784cb0651095284fdada8c78b). Inspected the README, LICENSE, `setup_download.py` and `app/server.py` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
