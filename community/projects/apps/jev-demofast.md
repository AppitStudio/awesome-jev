# jev-demofast

[All projects](../README.md) · [Web apps](README.md#web-apps)

One sentence in, a narrated product demo video out: TypeSafe Jev drives your real product in a browser, guided by an optional index built from your source code.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/q3learners/jev-demofast) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [onecentdemo.com](https://onecentdemo.com) |
| Pricing and access | MIT source build; Cloudflare Workers AI / AI Gateway credits for Jev (`typesafe/jev`); optional Deepgram voice ~$0.03/1k chars. Hosted replay demos on the product site. Checked 2026-09-25. |
| Jev evidence | [README](https://github.com/q3learners/jev-demofast/blob/f771b87383ee6a728c3c46b0014fdb2b84941979/README.md) documents Jev step decisions; [LinkedIn write-up](https://www.linkedin.com/pulse/jev-couldnt-find-password-reset-form-we-gave-map-venkat-podugu-p23fe/). |
| Disclosure | Open source MIT source build (no app purchase fee). Provider AI Gateway / Deepgram costs are separate (BYOK). Independently curated; no affiliation. Listing is not an endorsement. Live Cloudflare/Deepgram demos not run on the review host. |
| Maintainer | [q3learners](https://github.com/q3learners). Independently curated. |
| Format | Application (CLI + browser driver). |
| Platform and availability | Python 3.12+, uv, ffmpeg, Google Chrome; [Try demos](https://onecentdemo.com) or source build. |
| Jev's role | Jev chooses each browser step (and uses a source-built screen map when provided); optional LLM plans a route only when no index; narration is separate. |
| Requirements | `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_API_TOKEN` (Workers AI); optional Deepgram for `--voice`. |
| License | [MIT](https://github.com/q3learners/jev-demofast/blob/f771b87383ee6a728c3c46b0014fdb2b84941979/LICENSE). |

## When to use

Use to **regenerate product demos from a sentence** after UI changes. Prefer manual recording tools when you need human-directed click paths without a decision model.

## How it works

`jev-demofast` opens an isolated Chrome profile, optionally indexes a Next.js app router into a screen map, then asks Jev which element/action to take until the goal is done. Runs write `replay.json` with questions, probabilities, and timing (per README).

## Get started

```sh
git clone https://github.com/q3learners/jev-demofast.git
cd jev-demofast
git checkout f771b87383ee6a728c3c46b0014fdb2b84941979
uv sync
export CLOUDFLARE_ACCOUNT_ID=... CLOUDFLARE_API_TOKEN=...
uv run jev-demofast chrome
uv run jev-demofast demo "Show how to find hot trending projects on GitHub this week" \
  --url https://github.com/ --gif --out github.mp4
```

## Examples and demos

- Hosted replays at [onecentdemo.com](https://onecentdemo.com).
- README GIF of an unedited GitHub trending demo.

## Limits and data handling

The tool clicks real buttons and submits forms—use staging/test accounts. `--dry-run` stops before mutating actions. Browser traffic and credentials stay in the tool Chrome profile; Jev calls go through Cloudflare Workers AI.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit f771b87](https://github.com/q3learners/jev-demofast/tree/f771b87383ee6a728c3c46b0014fdb2b84941979). AI-assisted README and license inspection; live Cloudflare/Deepgram demo path not run.
