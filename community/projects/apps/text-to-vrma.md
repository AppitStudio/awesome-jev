# Text-To-VRMA

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Text-to-motion app for VRM avatars: type a line such as "jump for joy" and it generates a `.vrma` animation with facial expressions, previews it on your VRM model, and exports VRMA, GIF or video. Since v1.1.9 an optional Jev pass analyses the text's emotion, gaze, energy and tempo and feeds those typed results into motion generation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Kirakun0328/text-to-vrma) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Project README](https://github.com/Kirakun0328/text-to-vrma#readme) |
| Pricing and access | Free MIT source (browser version via `npm run dev`, Electron desktop build) and a free Windows portable zip on [Releases](https://github.com/Kirakun0328/text-to-vrma/releases/latest). Motion generation uses local NVIDIA ARDY (no key) or your own OpenAI / Claude / OpenAI-compatible key or Codex plan; the optional Jev analysis needs your own TypeSafe key (billed by TypeSafe). Checked 2026-10-12. |
| Jev evidence | [`src/jevAnalyzer.js`](https://github.com/Kirakun0328/text-to-vrma/blob/53c50504d1dc5137d4414b27ae8afaff89a62943/src/jevAnalyzer.js) builds independent Choice/Score/Noul questions (emotion, intensity, energy, amplitude, tempo, social attitude, loop, gaze, facial scores) for `https://api.typesafe.ai`; `test/jev-analyzer.test.cjs` covers it. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Not commercial (GitHub Sponsors link only). Listing is not an endorsement. App not run on the review host. |
| Maintainer | [Kiratchi (Kirakun0328)](https://github.com/Kirakun0328). Independently curated. |
| Format | Browser app (Vite) + Electron desktop app; optional local HTTP API |
| Platform and availability | Windows 10/11 (maintainer-tested, portable zip); macOS and Linux reported by contributors; browser version on any OS. Active development (v1.1.x). |
| Jev's role | Optional: Jev only analyses the input text (emotion, per-emotion affect scores, energy, amplitude, tempo, attitude, gaze) as auxiliary conditioning; ARDY or an LLM still generates every motion. Without a key, errors or timeouts it continues without Jev. Japanese input is machine-translated to English before Jev by default. |
| Requirements | Node.js (see README); for ARDY a supported GPU/CPU setup; optional OpenAI/Claude key or Codex plan; optional TypeSafe key (`JEV_API_KEY` for the local HTTP API, or entered in Settings). |
| License | [MIT](https://github.com/Kirakun0328/text-to-vrma/blob/53c50504d1dc5137d4414b27ae8afaff89a62943/LICENSE). |

## When to use

- Generate short VRM avatar motions and expressions from plain-language prompts for VTubing, streaming clips or VRM apps.
- Let typed emotion/tempo cues steer expression and pacing without hand-tuning prompts.
- Mismatch: Jev does not generate motion; it is an optional analysis step. Japanese text is translated first because Jev targets English.

## How it works

The app sends the prompt to the chosen motion engine (ARDY or an LLM keyframe planner). In parallel, when a TypeSafe key is configured, Jev answers typed questions about the text; the results are passed as hints into the generation prompt and used for an opening facial expression, while existing expression tracks are kept.

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Kirakun0328/text-to-vrma.git
cd text-to-vrma
npm install
npm run dev
```

## Limits and data handling

Keys are stored in browser `localStorage` (or passed via Electron IPC / the local server) and sent only to the chosen providers; the input text goes to TypeSafe when Jev is enabled. Analysis logs keep only emotions/confidences, not keys or full input (per README). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 53c50504d1dc](https://github.com/Kirakun0328/text-to-vrma/tree/53c50504d1dc5137d4414b27ae8afaff89a62943). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
