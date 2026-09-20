# JEV Document Classification

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local-first Vite/Express app that files root-folder documents into configured category folders using TypeSafe Jev (via Vercel AI Gateway) for category, confidentiality, prompt-injection risk, and subject choices.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Charlyhno-eng/jev-document-classification) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/Charlyhno-eng/jev-document-classification#readme) — source-built local web app; no separate hosted product required. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-20**. Classification needs a Vercel AI Gateway API key. Provider usage can incur charges. Preview/undo stay local to the selected folder. |
| Jev evidence | Inspected [`server/classification.ts`](https://github.com/Charlyhno-eng/jev-document-classification/blob/17cdc20acb407e7cfb623ef47d32e1b8568a5c86/server/classification.ts): `createGateway` + `experimental_evaluate` with model `typesafe-ai/jev`; typed Choice questions for category, confidentiality, injection risk, and subject. Live classification not run. |
| Disclosure | Free source access does not include Gateway usage. AI-assisted, independently curated listing; no commercial relationship was declared. Inclusion is not endorsement. Implementation reviewed from public source. |
| Maintainer | [Charlyhno-eng](https://github.com/Charlyhno-eng). |
| Format | Vite + React front end with Express local server (`jev-document-classification` 0.1.0). |
| Platform and availability | Source build with Node.js and npm; `npm run dev` opens `http://localhost:5173`. Experimental personal tool. |
| Jev's role | Supplies typed filing decisions over locally extracted document profiles; application code owns extraction, folder moves, audit, preview, undo, and reserved folders (`Need review`, `Not processable`, `Suspected prompt injection`). |
| Requirements | Node.js + npm; Vercel AI Gateway key for live classification. |
| License | [MIT](https://github.com/Charlyhno-eng/jev-document-classification/blob/17cdc20acb407e7cfb623ef47d32e1b8568a5c86/LICENSE). |

## When to use

Use it to sort a messy local document folder into named categories with an audit trail and undo. Prefer [tax-doc-classifier](../tools/tax-doc-classifier.md) when the problem is IRS form/page identity from PDF page text. Prefer [doc-router](../tools/doc-router.md) when routing PDF pages between local extraction and OCR rather than filing into folders.

## How it works

The local server extracts readable text and builds a bounded document profile (headings, subject candidates, excerpts). [`server/classification.ts`](https://github.com/Charlyhno-eng/jev-document-classification/blob/17cdc20acb407e7cfb623ef47d32e1b8568a5c86/server/classification.ts) asks Jev through the Gateway; low category confidence routes to `Need review`, injection flags to `Suspected prompt injection`, and unreadable files to `Not processable` without a Jev call. Short documents can batch; files move only after a successful decision and are never overwritten.

## Get started

```sh
git clone https://github.com/Charlyhno-eng/jev-document-classification.git
cd jev-document-classification
git checkout 17cdc20acb407e7cfb623ef47d32e1b8568a5c86
npm install
npm run dev
```

Open <http://localhost:5173>, enter a Gateway key, choose a folder, and start classification. Live runs send document profiles to Vercel AI Gateway / Jev and can incur charges. This listing did not run `npm test` or live classification.

## Examples and demos

- README screenshots of the audit UI and filing run.
- Offline tests under `tests/server/` (local moves without Jev) — not executed on the review host.

## Limits and data handling

Bounded profiles (not full originals beyond the profile cap) leave the host for the Gateway when classifying. Keys live in local config; do not expose a public deploy with a shared key. Upstream cost/speed claims were not independently measured.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 17cdc20](https://github.com/Charlyhno-eng/jev-document-classification/tree/17cdc20acb407e7cfb623ef47d32e1b8568a5c86): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `server/classification.ts`, and `package.json`. No live Gateway calls.

Related: [tax-doc-classifier](../tools/tax-doc-classifier.md), [doc-router](../tools/doc-router.md).
