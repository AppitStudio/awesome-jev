# Jevfill

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome Manifest V3 extension that autofills web forms from unstructured personal notes using TypeSafe Jev field-to-line matching—no structured profile required.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/imohitmayank/jevfill) |
| Tags | Open source · Free source build · BYOK |
| Product homepage | [Project homepage](https://github.com/imohitmayank/jevfill#readme) |
| Pricing and access | Build and load unpacked from MIT source (Chrome Developer mode). No app purchase fee. Bring a TypeSafe API key in extension options. TypeSafe usage can incur charges. Checked 2026-09-21. |
| Jev evidence | [`src/jev/client.ts`](https://github.com/imohitmayank/jevfill/blob/12246f784a49f5e48be9aca8c2dd7588f1d1fa9f/src/jev/client.ts) posts to `https://api.typesafe.ai/v1/systemone` with model `jev-1.13.0` (`JEV_MODEL` in `src/types.ts`). Build-request / parse-response unit tests mock answers. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; Chrome install and live TypeSafe calls were not run. Offline `vitest`: **7 passed**. Distinct from [Smart Paste](smart-paste.md) (exact source-passage paste/verify vs unstructured notes → field fill). |
| Maintainer | [imohitmayank](https://github.com/imohitmayank). Independently curated. |
| Format | TypeScript Manifest V3 extension **0.1.0** (Vite / `@crxjs/vite-plugin`). |
| Platform and availability | Chromium load-unpacked via `npm run build` → `dist/`. Not Chrome Web Store listed in the reviewed tree. |
| Jev's role | Matches each visible form field to the best line from the user's saved notes; extension code fills values and highlights them. Password and payment fields are never sent or filled. |
| Requirements | Chrome/Chromium; TypeSafe API key in options; Node.js for build/test. |
| License | [MIT](https://github.com/imohitmayank/jevfill/blob/12246f784a49f5e48be9aca8c2dd7588f1d1fa9f/LICENSE). |

## When to use

Use it when you keep free-form personal notes and want on-demand form autofill with calibrated Jev matching and a confidence threshold. Prefer [Smart Paste](smart-paste.md) when you already have a clipboard block and need exact substring paste plus undo. Do not use it for passwords, cards, or other secrets—those fields are skipped by design.

## How it works

Notes and field labels/context go to TypeSafe System One; Jev returns per-field line choices. The service worker (`src/background/service-worker.ts`) calls `classifyFields`, and `field-filler.ts` writes matching values with a temporary highlight. Threshold tuning lives in extension settings.

## Get started

```sh
git clone https://github.com/imohitmayank/jevfill.git
cd jevfill
git checkout 12246f784a49f5e48be9aca8c2dd7588f1d1fa9f
npm ci --ignore-scripts
npm test
npm run build
```

Load `dist/` unpacked at `chrome://extensions`, open Options, paste notes, add a TypeSafe key, save, then **Autofill page** on a form. Live runs send note lines and field context to TypeSafe and can incur charges.

## Examples and demos

- Upstream README demo GIF under `assets/jevfill_demo.gif`.
- Sample form: `test/sample-form.html` (manual).
- This listing: `npm test` (vitest) → **7 passed**. No Chrome load; no live TypeSafe call.

## Limits and data handling

Notes and form field metadata leave the host on live classifications; the key stays in extension storage. Password/payment fields are excluded. Matching quality depends on note phrasing and threshold—review highlighted fills before submit. Confirm TypeSafe account terms separately.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 12246f7](https://github.com/imohitmayank/jevfill/tree/12246f784a49f5e48be9aca8c2dd7588f1d1fa9f): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `src/jev/*`, and offline vitest. No browser install; no live provider call.

Related: [Smart Paste](smart-paste.md), [Jev for Chrome](jev-for-chrome.md), [Focus](focus.md).
