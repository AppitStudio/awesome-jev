# TypeSafe Use Case Lab by chaitanya-y (local app with 32 small runnable Jev workflows adapted from TypeSafe's use case map)

[All projects](../README.md) · [Web apps](README.md#web-apps)

A local web app with 32 compact adaptations of TypeSafe's use case map, from invoice inboxes and support triage to OCR field checks, vaccination records and bird frames. Each example has editable inputs, a JSON view, the workflow code, its source link and a scope statement; you can preview with clearly labelled illustrative answers for free, or run it live on Jev and download the exact run JSON.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chaitanya-y/typesafe-jev-workflows) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/chaitanya-y/typesafe-jev-workflows#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build with no packages to install; live runs use your own TypeSafe key. No license file, so reuse terms are not granted. Checked 2026-11-23. |
| Jev evidence | [`engine.mjs`](https://github.com/chaitanya-y/typesafe-jev-workflows/blob/d0d321ad8a6670c88e4e98bcc9cc8b0c7fbb0eaf/engine.mjs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [chaitanya-y](https://github.com/chaitanya-y). Independently curated. |
| Format | Node.js app (no dependencies, no build step) |
| Platform and availability | Local web app (Node.js server + browser UI); macOS double-click launcher included. |
| Jev's role | Each workflow sends typed questions to Jev and applies plain decision rules to the answers; image examples use Box and crop-then-recheck. |
| Requirements | Node.js 20.11+; a TypeSafe API key for live runs. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Explore many Jev patterns quickly with editable inputs and the actual workflow code side by side.
- Mismatch: production integrations; examples use small editable datasets and do not connect to banks, Google Sheets or other services.

## How it works

`engine.mjs` posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest` (or `TYPESAFE_MODEL`), records the returned model version, tokens and timing, and surfaces HTTP errors instead of turning them into judgments. Live runs are capped at 16 calls and 320 questions per click, with no automatic retries. Integration evidence: [`engine.mjs`](https://github.com/chaitanya-y/typesafe-jev-workflows/blob/d0d321ad8a6670c88e4e98bcc9cc8b0c7fbb0eaf/engine.mjs).

## Get started

Start the server, try a sample preview, then add your key to `.env` and use Run with Jev.

```sh
git clone https://github.com/chaitanya-y/typesafe-jev-workflows.git && cd typesafe-jev-workflows
npm start   # http://127.0.0.1:4317
cp .env.example .env   # add TYPESAFE_API_KEY, then restart
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Coverage map: [github.com/chaitanya-y/typesafe-jev-workflows/blob/d0d321ad8a6670c88e4e98bcc9cc8b0c7fbb0eaf/docs/coverage.md](https://github.com/chaitanya-y/typesafe-jev-workflows/blob/d0d321ad8a6670c88e4e98bcc9cc8b0c7fbb0eaf/docs/coverage.md)
- App preview: [github.com/chaitanya-y/typesafe-jev-workflows/blob/d0d321ad8a6670c88e4e98bcc9cc8b0c7fbb0eaf/docs/app-preview.jpg](https://github.com/chaitanya-y/typesafe-jev-workflows/blob/d0d321ad8a6670c88e4e98bcc9cc8b0c7fbb0eaf/docs/app-preview.jpg)

## Limits and data handling

Live runs send the displayed input (and uploaded images, scaled to at most 1,800 px) to TypeSafe. Vaccination output is only a reading aid. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit d0d321ad8a66](https://github.com/chaitanya-y/typesafe-jev-workflows/tree/d0d321ad8a6670c88e4e98bcc9cc8b0c7fbb0eaf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
