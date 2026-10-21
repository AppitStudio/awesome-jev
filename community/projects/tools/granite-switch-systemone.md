# granite-switch-systemone (vLLM System One endpoint)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

vLLM endpoint plugin that serves a Granite Switch checkpoint's decision adapter through both OpenAI's Decisions API and Jev's System One API on the same server and GPU cache as chat completions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/generative-computing/granite-switch-systemone) |
| Maintainer | [generative-computing](https://github.com/generative-computing). Independently curated. |
| Format | vLLM plugin (Python) and container |
| Requirements | Linux with an NVIDIA GPU (8b fits one 80 GB H100), Python 3.11+, vLLM 0.30.0 (tested), granite-switch 0.1.1. |
| License | [Apache-2.0](https://github.com/generative-computing/granite-switch-systemone/blob/267f649848fdfac4bdbe565d7fc425dc29be0ac5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/granite_switch_systemone/plugin.py`](https://github.com/generative-computing/granite-switch-systemone/blob/267f649848fdfac4bdbe565d7fc425dc29be0ac5/src/granite_switch_systemone/plugin.py) at the pinned commit. |

## When to use

- Self-host a Jev-compatible `/v1/systemone` endpoint for clients written against the TypeSafe API.
- Serve decisions and chat from one vLLM process.
- Mismatch: this is a Jev-compatible runtime with Granite models, not TypeSafe's Jev.

## How it works

The plugin mounts `POST /v1/systemone` and `POST /v1/decisions` in vLLM (`plugin.py`); each question is one engine read of single-token option labels, returned as softmax probabilities. Integration evidence: [`src/granite_switch_systemone/plugin.py`](https://github.com/generative-computing/granite-switch-systemone/blob/267f649848fdfac4bdbe565d7fc425dc29be0ac5/src/granite_switch_systemone/plugin.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install "granite-switch[vllm]==0.1.1" "transformers>=5.16"
pip install "git+https://github.com/generative-computing/granite-switch-systemone@v0.1.0"
export VLLM_PLUGINS=register_granite_switch,granite_switch_systemone
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- What is and isn't tested: [github.com/generative-computing/granite-switch-systemone/blob/main/docs/STATUS.md](https://github.com/generative-computing/granite-switch-systemone/blob/main/docs/STATUS.md)
- Testing guide: [github.com/generative-computing/granite-switch-systemone/blob/main/docs/TESTING.md](https://github.com/generative-computing/granite-switch-systemone/blob/main/docs/TESTING.md)

## Limits and data handling

Runs locally; answers come from Granite Switch, not TypeSafe's Jev, so quality differs. Container path is lightly tested per the README.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 267f649848fd](https://github.com/generative-computing/granite-switch-systemone/tree/267f649848fdfac4bdbe565d7fc425dc29be0ac5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
