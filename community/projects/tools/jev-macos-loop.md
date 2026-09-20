# jev-macos-loop

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Native Apple silicon macOS computer-use agent: local OmniParser CoreML + Vision OCR + Accessibility identify controls; Jev chooses the next guarded GUI action. Screenshots stay on-device.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jcpsimmons/jev-macos-loop) |
| Maintainer | [jcpsimmons](https://github.com/jcpsimmons). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js (≥22) CLI and loop (`jev-macos-loop` **0.1.0**); CoreML model export via `uv`/Python 3.12. |
| Requirements | Apple silicon, macOS 14.2+, Xcode CLT, Node.js 22+, `uv` for one-time OmniParser conversion. BYOK for Vercel AI Gateway, OpenRouter, or TypesafeAI (`JEV_PROVIDER`). |
| License | [AGPL-3.0](https://github.com/jcpsimmons/jev-macos-loop/blob/1aadc01ef262c3b01460909c5dd102f0d9616ba5/LICENSE). |

## When to use

Use it to automate native Mac apps (Finder demos included) when you want local perception and text-only Jev decisions. Prefer [typesafe-computer-use](typesafe-computer-use.md) for a Python OCR/Accessibility study path, or browser agents such as [Jev Ultrafast](jev-ultrafast.md) when the target is the web.

## How it works

Local ScreenCaptureKit / OmniParser / Vision / Accessibility build a control inventory. [`src/providers.mjs`](https://github.com/jcpsimmons/jev-macos-loop/blob/1aadc01ef262c3b01460909c5dd102f0d9616ba5/src/providers.mjs) routes typed evaluation to Vercel (`typesafe-ai/jev`), OpenRouter Decisions (`~typesafe/jev-latest`), or TypesafeAI `https://api.typesafe.ai/v1/systemone` (`jev-latest`). Only observed text, the goal, and finite choices leave the machine. Input is guarded (focus, occlusion, confidence) before clicks or scoped Finder drags. A separate verifier checks outcomes independently of Jev's DONE decision.

## Get started

Requires a local Apple silicon Mac (not runnable on this Linux review host):

```sh
git clone https://github.com/jcpsimmons/jev-macos-loop.git
cd jev-macos-loop
git checkout 1aadc01ef262c3b01460909c5dd102f0d9616ba5
npm ci
uv venv --python 3.12
uv pip install --python .venv/bin/python -r scripts/model-requirements.txt
.venv/bin/python scripts/export_model.py
npm run build
cp .env.example .env.local   # set JEV_PROVIDER and the matching token
npm start -- --doctor
```

Live runs send decision text to the selected provider and can incur charges. This listing did not install CoreML models or call TypeSafe.

## Examples and demos

- Finder batch demo media and notes under [`docs/media/`](https://github.com/jcpsimmons/jev-macos-loop/tree/1aadc01ef262c3b01460909c5dd102f0d9616ba5/docs/media) and [`docs/recording.md`](https://github.com/jcpsimmons/jev-macos-loop/blob/1aadc01ef262c3b01460909c5dd102f0d9616ba5/docs/recording.md).
- [`docs/providers.md`](https://github.com/jcpsimmons/jev-macos-loop/blob/1aadc01ef262c3b01460909c5dd102f0d9616ba5/docs/providers.md) and `npm run check:provider` (three small decision requests; no screen access).
- [`test/providers.test.mjs`](https://github.com/jcpsimmons/jev-macos-loop/blob/1aadc01ef262c3b01460909c5dd102f0d9616ba5/test/providers.test.mjs): offline provider contract tests.

## Limits and data handling

AGPL-3.0 applies to the agent code. Model weights and credentials are gitignored. Tokens go only to the selected provider; the runner does not silently switch providers. Direct TypesafeAI adapter has offline contract tests; upstream notes live Typesafe verification still needs your console token. Accessibility and screen-recording permissions are required on macOS.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 1aadc01](https://github.com/jcpsimmons/jev-macos-loop/tree/1aadc01ef262c3b01460909c5dd102f0d9616ba5): **0.1.0**, AGPL-3.0. AI-assisted source review of `providers.mjs`, README, LICENSE, and provider docs. No macOS install, CoreML export, GUI automation, or live provider calls were run on the Linux review host.

Related: [typesafe-computer-use](typesafe-computer-use.md), [Jev-cu](jev-cu.md), [Cua jev-use](cua-jev-use.md).
