# JevSlop

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hosted and source-built app that scores note articles for AI-slop writing patterns with TypeSafe Jev (multi-axis Score plus overall Choice). Bring your own TypeSafe key; the key stays session-side via a Cloudflare Pages Function.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TKY-27/JevSlop) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Live app](https://jevslop.pages.dev/) |
| Pricing and access | Free to use from source or the hosted Pages site with your own TypeSafe key; no app purchase fee. Inference usage can incur TypeSafe charges. Reviewed 2026-09-20. |
| Jev evidence | [`lib/jev.ts`](https://github.com/TKY-27/JevSlop/blob/9829750f072aaeaad42a1307c35eb9f52288bba0/lib/jev.ts) builds Score questions per axis plus overall Score/Choice and calls `client.systemOne` via `@typesafe-ai/sdk` (`jev-1.13.0`). Pages Function [`functions/api/evaluate.ts`](https://github.com/TKY-27/JevSlop/blob/9829750f072aaeaad42a1307c35eb9f52288bba0/functions/api/evaluate.ts) forwards `{ title, body }` with the user-supplied key. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Community project, not affiliated with TypeSafe. Listing is not an endorsement. Source and offline `npm test` inspected; hosted live evaluation with a TypeSafe key was not run on the review host. |
| Maintainer | [TKY-27](https://github.com/TKY-27). Independently curated. |
| Format | Next.js + Cloudflare Pages app **jevslop 0.1.0**. |
| Platform and availability | Web: [jevslop.pages.dev](https://jevslop.pages.dev/); local `npm run dev` (Pages Functions-compatible). |
| Jev's role | Judges writing-quality axes and an overall AI-slop label/score from title+body only. Does not claim to detect whether AI authored the text. |
| Requirements | Node.js 22.12+ to build from source; TypeSafe API key entered in Settings (BYOK). |
| License | [MIT](https://github.com/TKY-27/JevSlop/blob/9829750f072aaeaad42a1307c35eb9f52288bba0/LICENSE). |

## When to use

Use it when you want a browser workflow to score articles (especially note.host-style pages) for thin/generic/formulaic writing with calibrated Jev scores. Prefer [Sniff Test](../tools/snifftest.md) for local house-rule prose linting with optional Jev, or [PageGrade](pagegrade.md) for on-page section grading in Chrome. Do not treat scores as authorship forensics.

## How it works

1. You paste or load an article URL the Function is allowed to fetch.
2. The evaluate API extracts title/body, then `lib/jev.ts` asks TypeSafe Jev for per-axis scores and an overall AI-slop score/label.
3. Results stay in-tab; the Function does not persist the API key or include it in exports (per upstream SECURITY notes).

Only `{ title, body }` are sent as Jev state; URL/author/date and experiment labels are excluded from that payload per upstream docs.

## Get started

```sh
git clone https://github.com/TKY-27/JevSlop.git
cd JevSlop
git checkout 9829750f072aaeaad42a1307c35eb9f52288bba0
npm ci
npm test
# Optional local UI: npm run dev  # then enter TYPESAFE key in Settings
```

Or open [https://jevslop.pages.dev/](https://jevslop.pages.dev/) and supply your key. This listing did not call TypeSafe.

## Examples and demos

- Hosted app: [jevslop.pages.dev](https://jevslop.pages.dev/).
- Spec/experiment notes: `SPEC.md`, `EXPERIMENT.md`.
- Offline `npm test` on the review host (see Review).

## Limits and data handling

Title and body leave the browser to TypeSafe through the Pages Function when you evaluate. BYOK key is session-oriented per upstream security design—review `SECURITY.md` before shared machines. Scoring targets writing quality patterns, not author identity. Cloudflare and TypeSafe processing follow their respective policies.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 9829750](https://github.com/TKY-27/JevSlop/tree/9829750f072aaeaad42a1307c35eb9f52288bba0): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `lib/jev.ts`, `functions/api/evaluate.ts`, and SECURITY notes. Ran `npm ci` and `npm test`: **7** passed. Live hosted TypeSafe evaluation not executed.

Related: [Sniff Test](../tools/snifftest.md), [PageGrade](pagegrade.md), [Vibe Check for X](vibecheck.md).
