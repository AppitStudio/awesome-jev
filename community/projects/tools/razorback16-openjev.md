# OpenJev by razorback16 (open Jev-compatible System One server on DiffusionGemma 26B-A4B, plus other open decision models)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open-source System One decision server that speaks the same `/v1/systemone` wire API as TypeSafe's Jev, so TypeSafe SDKs work unchanged, and also answers OpenAI's Decisions API. It reads typed `noul`, `choice` and `score` answers directly from DiffusionGemma 26B-A4B's probabilities (images supported) through vLLM on NVIDIA or MLX on Apple silicon, and serves other open models (Laya, Verdict, CLM, JevK5, Clef) from separate images. About 800 GitHub stars.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/razorback16/openjev) |
| Maintainer | [razorback16](https://github.com/razorback16). Independently curated. |
| Format | Python server + Docker images |
| Requirements | NVIDIA GPU with 24 GB+ (Docker) or Apple silicon with about 16 GB free (MLX). |
| License | [Apache-2.0](https://github.com/razorback16/openjev/blob/b4339c640f5331ef75098637d1be2c787715ee88/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`openjev/api.py`](https://github.com/razorback16/openjev/blob/b4339c640f5331ef75098637d1be2c787715ee88/openjev/api.py) at the pinned commit. |

## When to use

- Teams who want Jev-style typed decisions on their own hardware with existing TypeSafe client code.
- Mismatch: TypeSafe's hosted Jev quality; answers reflect the open model, so evaluate on your own tasks.

## How it works

`openjev/api.py` implements `POST /v1/systemone` and `GET /v1/models` and translates OpenAI `/v1/decisions` requests; answers are read from label probabilities with no text parsing. It does not call TypeSafe; point `TYPESAFE_BASE_URL` at it to reuse Jev client code. Integration evidence: [`openjev/api.py`](https://github.com/razorback16/openjev/blob/b4339c640f5331ef75098637d1be2c787715ee88/openjev/api.py).

## Get started

Run the Docker image locally and point the TypeSafe SDK at it.

```sh
git clone https://github.com/razorback16/openjev && cd openjev
docker compose up -d          # 127.0.0.1:8080
export TYPESAFE_BASE_URL=http://127.0.0.1:8080
curl localhost:8080/v1/models
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Models: [github.com/razorback16/openjev#models](https://github.com/razorback16/openjev#models)
- Run your own: [github.com/razorback16/openjev#run-your-own](https://github.com/razorback16/openjev#run-your-own)

## Limits and data handling

Independent project, not affiliated with TypeSafe. The README also advertises a hosted endpoint on Codiv with a free token allowance; that service and its terms were not reviewed. The image patches upstream vLLM.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit b4339c640f53](https://github.com/razorback16/openjev/tree/b4339c640f5331ef75098637d1be2c787715ee88). Inspected the README, LICENSE, CHANGELOG and `openjev/api.py` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
