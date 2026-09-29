# jev-subtitle-translator

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Translate SRT subtitles with structured LLM output and TypeSafe Jev QC checks on every source–translation pair

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/GeekLinkDev/jev-subtitle-translator) |
| Maintainer | [GeekLinkDev](https://github.com/GeekLinkDev). Independently curated; this entry is not an upstream submission or endorsement. Related commercial workflow: [geeklink.dev/subtitle-translator](https://geeklink.dev/subtitle-translator/). |
| Format | Python · local web UI + CLI (GPL-3.0). |
| Requirements | Python 3.10+; OpenRouter API key for translation/QC path documented upstream. |
| License | [GPL-3.0](https://github.com/GeekLinkDev/jev-subtitle-translator/blob/475d6dc91e7c9822dce8eeb2a0864440e60e63c9/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; live OpenRouter/Jev paths not run on the review host. |

## When to use

Use when translating existing SRT files with ID-stable structured LLM batches and automatic Jev review flags before publish.

## How it works

Parse SRT locally (IDs/timestamps preserved) → translate ID-tagged batches via OpenRouter → retry missing IDs → deterministic checks + Jev QC → rebuild SRT from original cue list.

## Get started

```sh
git clone https://github.com/GeekLinkDev/jev-subtitle-translator.git
cd jev-subtitle-translator
git checkout 475d6dc91e7c9822dce8eeb2a0864440e60e63c9
bash run_web.sh
# open http://127.0.0.1:8000
```

## Examples and demos

Upstream demo GIF and QC report download. No live translation/QC on the review host.

## Limits and data handling

Subtitle text is sent to OpenRouter/Jev providers when live. Hosted GeekLink product is separate from this OSS repo.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 475d6dc](https://github.com/GeekLinkDev/jev-subtitle-translator/tree/475d6dc91e7c9822dce8eeb2a0864440e60e63c9). AI-assisted README + LICENSE inspection; live paths not executed.
