# voicevox-jev-proxy

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Corrects VOICEVOX Japanese readings (optional intonation) with TypeSafe Jev; CLI WAV export or VOICEVOX-compatible API proxy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nemalabs/voicevox-jev-proxy) |
| Maintainer | [nemalabs](https://github.com/nemalabs). Independently curated. |
| Format | Python CLI and VOICEVOX-compatible API proxy. |
| Requirements | Python; VOICEVOX engine; TypeSafe API key; Sudachi/UniDic per upstream. |
| License | [MIT](https://github.com/nemalabs/voicevox-jev-proxy/blob/16c9aebaf64fb09fc465dc7a3023d028849985a5/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use when VOICEVOX **misreads** Japanese text and you want calibrated Jev choices over reading/segmentation candidates. Prefer plain VOICEVOX when defaults are good enough.

## How it works

Tokenizes with Sudachi/UniDic, asks Jev Choice questions about segmentation, readings, and optional intonation, then synthesizes corrected audio or proxies the VOICEVOX API.

## Get started

```sh
git clone https://github.com/nemalabs/voicevox-jev-proxy.git
cd voicevox-jev-proxy
git checkout 16c9aebaf64fb09fc465dc7a3023d028849985a5
# Needs VOICEVOX + TYPESAFE_API_KEY; see README for CLI vs proxy modes
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 16c9aeb](https://github.com/nemalabs/voicevox-jev-proxy/tree/16c9aebaf64fb09fc465dc7a3023d028849985a5). AI-assisted README and license inspection; install/live paths not executed.
