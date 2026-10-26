# System Analyzer (terminal tool that rates your machine and answers "can I run this?" with a decision model)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Terminal tool that detects CPU, RAM, GPU, VRAM, disks and OS, then asks a System One decision model to rate the machine out of 100 and answer questions such as whether it can run a given task; it can use TypeSafe Jev, OpenRouter's Jev route, OpenCode Zen's free Jev tier or a local model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sadra-hatami/System-Analyzer) |
| Maintainer | [sadra-hatami](https://github.com/sadra-hatami). Independently curated. |
| Format | Python command-line tool |
| Requirements | Python 3.10+ and psutil; a key for the provider you choose (TypeSafe, OpenRouter or OpenCode Zen), or a local model. |
| License | [MIT](https://github.com/sadra-hatami/System-Analyzer/blob/ce03f871dca41ae146097b7c00dac8c2b3af2d1c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`providers.py`](https://github.com/sadra-hatami/System-Analyzer/blob/ce03f871dca41ae146097b7c00dac8c2b3af2d1c/providers.py) at the pinned commit. |

## When to use

- Get a quick yes or no on whether a machine can handle a workload.
- Compare decision-model providers on the same hardware summary.
- Mismatch: the default chain uses OpenCode Zen's free Jev tier, a third-party route, not TypeSafe directly.

## How it works

`providers.py` lists TypeSafe (`https://api.typesafe.ai`), OpenRouter (`/api/v1/systemone`, `~typesafe/jev-latest`) and OpenCode Zen's `jev-1.13-free` as providers; the hardware summary and your question go to the first configured one, sent with the tool's own user agent. Integration evidence: [`providers.py`](https://github.com/sadra-hatami/System-Analyzer/blob/ce03f871dca41ae146097b7c00dac8c2b3af2d1c/providers.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/sadra-hatami/System-Analyzer && cd System-Analyzer
pip install -r requirements.txt
python main.py   # set TYPESAFE_API_KEY in settings for direct Jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/sadra-hatami/System-Analyzer#readme](https://github.com/sadra-hatami/System-Analyzer#readme)

## Limits and data handling

A hardware summary and your question go to the selected provider. OpenCode Zen and OpenRouter are third-party routes to Jev.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit ce03f871dca4](https://github.com/sadra-hatami/System-Analyzer/tree/ce03f871dca41ae146097b7c00dac8c2b3af2d1c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
