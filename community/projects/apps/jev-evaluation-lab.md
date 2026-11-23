# Jev Evaluation Lab by march (research workspace that classifies AI-system descriptions with Jev and compares results with human reviews)

[All projects](../README.md) · [Web apps](README.md#web-apps)

An independent research workspace: analyze AI-system descriptions with five governance questions (Choice, Noul and Score), read exact passages on human oversight in a synthetic document corpus, compare text and graph search, and compare predictions with reviewer labels. An assessments workspace runs documentary checks for a Claude Code adoption or an internal assistant against eight regulatory excerpts and exports an evidence-linked report. English and German UI; it makes no legal compliance decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/marchexe/jev-evaluation-lab) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/marchexe/jev-evaluation-lab#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; live Jev runs use your own TypeSafe key and are off by default. A hosted deployment is linked from the repository ([jev-evaluation-lab-lovat.vercel.app](https://jev-evaluation-lab-lovat.vercel.app)) but was not checked. No license file (package.json says UNLICENSED), so reuse terms are not granted. Checked 2026-11-23. |
| Jev evidence | [`src/system-one.js`](https://github.com/marchexe/jev-evaluation-lab/blob/1ab300fa042b6128172170eec6f81290091048ab/src/system-one.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [marchexe](https://github.com/marchexe). Independently curated. |
| Format | Next.js web app + CLI scripts |
| Platform and availability | Local web app (Next.js); browser storage for history and reviews. |
| Jev's role | Jev answers the governance questions about a description and, only on an explicit action, judges whether a single synthetic passage is relevant evidence. Search, rules and assessments are deterministic code. |
| Requirements | Node.js 24.x; a TypeSafe API key and `JEV_LIVE_INFERENCE_ENABLED=true` for live web runs (CLI needs `--live`). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Study how Jev classifies AI-system descriptions and compare it with human reviewers, with evidence and limits kept visible.
- Mismatch: legal compliance; the author says it is not an exhaustive legal assessment or approval.

## How it works

`src/system-one.js` uses the official `@typesafe-ai/sdk` (`TypeSafeClient` against `https://api.typesafe.ai`) with no automatic retries; live inference is disabled until you set the key server-side and enable it. Recorded runs can be imported and replayed offline. Integration evidence: [`src/system-one.js`](https://github.com/marchexe/jev-evaluation-lab/blob/1ab300fa042b6128172170eec6f81290091048ab/src/system-one.js).

## Get started

Install from the lockfile and start the dev server; browse, search and review offline, then enable live inference if you want new Jev runs.

```sh
git clone https://github.com/marchexe/jev-evaluation-lab && cd jev-evaluation-lab
npm ci
cp .env.example .env   # TYPESAFE_API_KEY, JEV_LIVE_INFERENCE_ENABLED=true for live runs
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Assessment guide: [github.com/marchexe/jev-evaluation-lab/blob/1ab300fa042b6128172170eec6f81290091048ab/docs/assessments.md](https://github.com/marchexe/jev-evaluation-lab/blob/1ab300fa042b6128172170eec6f81290091048ab/docs/assessments.md)
- Offline evidence walkthrough: [github.com/marchexe/jev-evaluation-lab/blob/1ab300fa042b6128172170eec6f81290091048ab/docs/evidence-demo.md](https://github.com/marchexe/jev-evaluation-lab/blob/1ab300fa042b6128172170eec6f81290091048ab/docs/evidence-demo.md)

## Limits and data handling

Live runs send descriptions and passages to TypeSafe. The regulatory PDFs are local inputs not included in Git; the app runs from extracted excerpts. Not an official TypeSafe product. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 1ab300fa042b](https://github.com/marchexe/jev-evaluation-lab/tree/1ab300fa042b6128172170eec6f81290091048ab). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
