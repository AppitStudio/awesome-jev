# openrouter-spend-jev (Jev model router for Hermes)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Desktop setup for a Hermes agent on Linux: a local OpenAI-compatible proxy asks Jev on OpenRouter which of three model tiers (GLM Flash, DeepSeek V4 Flash, DeepSeek V4 Pro) should take each request, next to an OpenRouter spend widget for the Omarchy and KDE bars and Android.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/adymitruk/openrouter-spend-jev) |
| Maintainer | [adymitruk](https://github.com/adymitruk). Independently curated. |
| Format | Python FastAPI proxy (systemd user service) plus QML bar widgets and deploy scripts |
| Requirements | Linux with systemd (Omarchy or CachyOS/KDE for the widgets), Python with FastAPI and httpx, an OpenRouter key used for both Jev and the routed models. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/adymitruk/status/2111676628032167984)). |
| Jev evidence | [`jev-proxy/jev-proxy.py`](https://github.com/adymitruk/openrouter-spend-jev/blob/811ae3f0524488e07ed9a9a589908b628df24e9b/jev-proxy/jev-proxy.py) at the pinned commit. |

## When to use

- Send cheap, routine agent turns to a small model and only escalate hard ones, without changing the agent's OpenAI-style endpoint.
- Copy the two fixes the author documents: keep one model across a tool-call loop, and map reasoning effort per lane.
- Mismatch: personal dotfiles-style setup for Hermes on the author's machines; paths and tiers need editing.

## How it works

`jev-proxy.py` accepts OpenAI chat requests locally, asks `typesafe/jev-1.13` through OpenRouter's Decisions endpoint which lane fits the request, then forwards it to the chosen model's chat endpoint. Lanes are pinned across assistant and tool turns so a conversation is not split between models mid-turn. Integration evidence: [`jev-proxy/jev-proxy.py`](https://github.com/adymitruk/openrouter-spend-jev/blob/811ae3f0524488e07ed9a9a589908b628df24e9b/jev-proxy/jev-proxy.py).

## Get started

From the upstream README (not run on the review host):

```sh
./deploy.sh   # copy files into place and enable the services
./config.sh   # wire up bar placement and Hermes aliases
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Author's X post with the widget on KDE: [x.com/adymitruk/status/2111676628032167984](https://x.com/adymitruk/status/2111676628032167984)
- `jev-proxy/README.md` describes the three lanes.

## Limits and data handling

Prompts go to OpenRouter (Jev for the routing call, then the chosen model) on your key. No LICENSE file on the reviewed commit, so the code is source-available only; ask the author before reusing it.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 811ae3f05244](https://github.com/adymitruk/openrouter-spend-jev/tree/811ae3f0524488e07ed9a9a589908b628df24e9b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
