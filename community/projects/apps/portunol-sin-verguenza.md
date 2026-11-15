# Portuñol Sin Vergüenza (Tucumán Spanish ⇄ Brazilian Portuguese chat translator whose web app has Jev check each candidate translation and slang sense)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Translator for real WhatsApp-style chat between Argentine (Tucumán) Spanish with voseo and Brazilian Portuguese, with slang, no accents and *jajaja*/*kkkk*. The self-hosted web app (also a PWA) runs a cascade: your own corrections, ready phrases, real subtitle phrases and DeepL's free tier first; Jev checks whether each candidate keeps meaning and tone and picks the sense of each ambiguous slang word in context; a paid GLM model is called only when nothing passes. The Android app works offline without Jev. README is in Portuguese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/straviosbr/portunol-sin-verguenza) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/straviosbr/portunol-sin-verguenza#readme) (source-built; no separate product site verified). |
| Pricing and access | Public source with no license file (all rights reserved by default); no purchase fee; DeepL API Free plus TypeSafe and optional OpenRouter usage on your keys, and your own server. Checked 2026-11-15. |
| Jev evidence | [`servidor/jev.py`](https://github.com/straviosbr/portunol-sin-verguenza/blob/2155e2e0654e25fae7de571b7410b0e27ac1fbea/servidor/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [straviosbr](https://github.com/straviosbr). Independently curated. |
| Format | Self-hosted Python web app (PWA) plus an Android app (Kotlin) |
| Platform and availability | Self-hosted web app / PWA (Jev path) and an Android APK built by the repo's GitHub Actions (offline, no Jev) |
| Jev's role | Jev checks each candidate translation for meaning and tone and picks the sense of ambiguous slang, so the paid translator runs only when nothing passes. |
| Requirements | For the web app: a server, a DeepL API Free key, `JEV_API_KEY` for Jev checks, and optionally an `OPENROUTER_API_KEY` for GLM. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Translate informal Argentine–Brazilian chat where generic translators miss slang and tone.
- Mismatch: European Spanish or Portugal Portuguese, which it deliberately avoids.

## How it works

`servidor/jev.py` sends one request per message to `https://api.typesafe.ai/v1/systemone` (model `jev-latest`) with a Noul per candidate translation and a Choice per ambiguous slang word; `servidor/motor.py` uses the first approved candidate. Integration evidence: [`servidor/jev.py`](https://github.com/straviosbr/portunol-sin-verguenza/blob/2155e2e0654e25fae7de571b7410b0e27ac1fbea/servidor/jev.py).

## Get started

Follow `servidor/README.md` to deploy the web app, then add your keys to `tradutor.env`.

```sh
git clone https://github.com/straviosbr/portunol-sin-verguenza && cd portunol-sin-verguenza
# see servidor/README.md to deploy; then in servidor/tradutor.env:
# JEV_API_KEY=...  (and optionally OPENROUTER_API_KEY=...)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/straviosbr/portunol-sin-verguenza/blob/2155e2e0654e25fae7de571b7410b0e27ac1fbea/README.md](https://github.com/straviosbr/portunol-sin-verguenza/blob/2155e2e0654e25fae7de571b7410b0e27ac1fbea/README.md)

## Limits and data handling

Messages are sent to DeepL, TypeSafe and (when needed) OpenRouter on your keys. The offline NLLB fallback is licensed for non-commercial use only; subtitle phrase databases are not included. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 2155e2e0654e](https://github.com/straviosbr/portunol-sin-verguenza/tree/2155e2e0654e25fae7de571b7410b0e27ac1fbea). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
