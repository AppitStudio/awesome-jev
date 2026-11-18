# Jev SEO Dashboard by MBN4 (local web dashboard for the jev-seo audit engine and its Jev content judgments)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Local Next.js dashboard for the [jev-seo](https://github.com/AgriciDaniel/jev-seo) audit engine, which it runs unchanged as a subprocess. Start audits from the browser with every engine option (including the Jev page judgments), watch live progress, and explore findings, pages, Core Web Vitals and an AI Content tab that shows only the engine's real Jev answers. Tracks fixes, keeps an audit history and serves the engine's own PDF, Excel and Markdown reports. Keys are stored write-only.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MBN4/jev-seo-dashboard) |
| Maintainer | [MBN4](https://github.com/MBN4). Independently curated. |
| Format | Next.js web app (TypeScript) (no license file) |
| Requirements | Ubuntu 20.04+ (or similar), Node.js, the jev-seo engine with its Python venv, and `TYPESAFE_API_KEY` for the Jev judgments (audits are marked partial without it); PageSpeed and DataForSEO keys optional. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`types/engine.ts`](https://github.com/MBN4/jev-seo-dashboard/blob/26956edae774bea75ae7223996656d1d214d9acd/types/engine.ts) at the pinned commit. |

## When to use

- Run and review jev-seo audits, including Jev's content judgments, from a browser instead of the CLI.
- Mismatch: a standalone SEO tool; it needs the jev-seo engine.

## How it works

`types/engine.ts` mirrors the engine's `audit.json`, including its Jev questions and answers (`EngineJev`, `JevAnswer`); the dashboard spawns `python -m jevseo run` with the Jev flag and renders those answers. The Jev calls are made by the engine. Integration evidence: [`types/engine.ts`](https://github.com/MBN4/jev-seo-dashboard/blob/26956edae774bea75ae7223996656d1d214d9acd/types/engine.ts).

## Get started

Install the jev-seo engine, point the dashboard at it, and run the start script.

```sh
git clone https://github.com/MBN4/jev-seo-dashboard ~/jev-seo-dashboard && cd ~/jev-seo-dashboard
echo "JEVSEO_DIR=$HOME/jev-seo" > .env.local
./start.sh    # http://localhost:3000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/MBN4/jev-seo-dashboard/blob/26956edae774bea75ae7223996656d1d214d9acd/README.md](https://github.com/MBN4/jev-seo-dashboard/blob/26956edae774bea75ae7223996656d1d214d9acd/README.md)
- Engine listing: [jevlist.ai/projects/agrici-jev-seo](https://jevlist.ai/projects/agrici-jev-seo)

## Limits and data handling

No license file on the reviewed commit, so reuse terms are not granted. Page content is sent to TypeSafe by the engine when Jev is on; paid DataForSEO mode needs explicit confirmation. Listen on localhost only by default.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 26956edae774](https://github.com/MBN4/jev-seo-dashboard/tree/26956edae774bea75ae7223996656d1d214d9acd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
