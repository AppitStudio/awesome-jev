# systemone-qwen (self-hosted Jev-compatible decision API backed by a Qwen model on llama-server)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Small server that answers the same `/v1/systemone` wire format as Jev from a Qwen model on llama-server: each option gets a letter and its probability is the model's first-token logprob, so a Jev client switches by changing only the base URL. The author reports 0.827 on JevBench's 231 public tasks for Qwen3.5-9B against Jev's 0.857. Not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dohr-michael/systemone-qwen) |
| Maintainer | [dohr-michael](https://github.com/dohr-michael). Independently curated. |
| Format | Python API server (container image) |
| Requirements | A llama-server serving a Qwen GGUF; no TypeSafe key. |
| License | [MIT](https://github.com/dohr-michael/systemone-qwen/blob/44f1083802fce121f92fb6c62c3533f3e8e05c8d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/systemone_qwen/app.py`](https://github.com/dohr-michael/systemone-qwen/blob/44f1083802fce121f92fb6c62c3533f3e8e05c8d/src/systemone_qwen/app.py) at the pinned commit. |

## When to use

- Run Jev-shaped decisions on your own hardware.
- Mismatch: an independent re-implementation of the format, not TypeSafe's model; benchmarks are the author's.

## How it works

`src/systemone_qwen/app.py` serves `POST /v1/systemone` (and OpenRouter's alpha path), maps `jev-latest` to the local model if configured, and converts letter logprobs into option probabilities. Integration evidence: [`src/systemone_qwen/app.py`](https://github.com/dohr-michael/systemone-qwen/blob/44f1083802fce121f92fb6c62c3533f3e8e05c8d/src/systemone_qwen/app.py).

## Get started

From the upstream README (not run on the review host):

```sh
podman run --rm -p 127.0.0.1:8000:8000 \
  -e SYSTEMONE_BACKEND_URL=http://host.containers.internal:8080 \
  ghcr.io/dohr-michael/systemone-qwen:latest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmarks: [github.com/dohr-michael/systemone-qwen/blob/main/docs/benchmarks.md](https://github.com/dohr-michael/systemone-qwen/blob/main/docs/benchmarks.md)
- README: [github.com/dohr-michael/systemone-qwen#readme](https://github.com/dohr-michael/systemone-qwen#readme)

## Limits and data handling

Runs locally; nothing is sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 44f1083802fc](https://github.com/dohr-michael/systemone-qwen/tree/44f1083802fce121f92fb6c62c3533f3e8e05c8d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
