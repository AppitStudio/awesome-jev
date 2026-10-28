# openvons (open-Jev: an open decision layer for text, images and Japanese voice commands, with a Jev-compatible API)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open project that makes LLMs, vision encoders and speech models answer a finite set of options with a probability each (always including "none of the above"), then splits the calibrated result into execute, confirm or reject. Covers intent and tool choice (frozen LLM plus a trained head), image attributes and Japanese voice commands, and serves a TypeSafe Jev-compatible `POST /v1/systemone` endpoint. Measurements are the author's.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/genai-craft/openvons) |
| Maintainer | [genai-craft](https://github.com/genai-craft). Independently curated. |
| Format | Python package with model heads and an API server |
| Requirements | Python 3.12, PyTorch with a GPU; no TypeSafe key needed. |
| License | [Apache-2.0](https://github.com/genai-craft/openvons/blob/7a2cbf48070dcd38b21f7ca9aaa4ee9c0d1ba953/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. GitHub reports the license as NOASSERTION; the LICENSE file is Apache-2.0 text. |
| Jev evidence | [`openvons/lm/api/systemone.py`](https://github.com/genai-craft/openvons/blob/7a2cbf48070dcd38b21f7ca9aaa4ee9c0d1ba953/openvons/lm/api/systemone.py) at the pinned commit. |

## When to use

- Run a local, Jev-shaped decision endpoint on your own hardware.
- Mismatch: an independent re-implementation of the request format, not TypeSafe's model.

## How it works

`openvons/lm/api/systemone.py` maps the public Jev request and response format onto openvons' own Noul, Choice and Score questions; `import jev` remains as an alias. Integration evidence: [`openvons/lm/api/systemone.py`](https://github.com/genai-craft/openvons/blob/7a2cbf48070dcd38b21f7ca9aaa4ee9c0d1ba953/openvons/lm/api/systemone.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv venv --python 3.12 .venv && uv pip install --python .venv/bin/python -e ".[dev]"
.venv/bin/python -m pytest -q tests/test_voice_core.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/genai-craft/openvons#readme](https://github.com/genai-craft/openvons#readme)
- Japanese README: [github.com/genai-craft/openvons/blob/main/README_ja.md](https://github.com/genai-craft/openvons/blob/main/README_ja.md)

## Limits and data handling

Runs locally; nothing is sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 7a2cbf48070d](https://github.com/genai-craft/openvons/tree/7a2cbf48070dcd38b21f7ca9aaa4ee9c0d1ba953). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
