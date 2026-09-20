# PageGrade

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

WXT Chrome extension that grades readable page sections for clarity, writing, and on-page SEO. TypeSafe Jev Score rubrics run through the Vercel AI Gateway evaluation endpoint; the page gets an A–E summary you can inspect.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kitze/pagegrade) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/kitze/pagegrade#pagegrade) |
| Pricing and access | [Load unpacked from a Bun build](https://github.com/kitze/pagegrade#install-locally); no app purchase fee. Bring a **Vercel AI Gateway** API key (Gateway credits and Jev access may be required). Reviewed 2026-09-20. |
| Jev evidence | [`lib/jev.ts`](https://github.com/kitze/pagegrade/blob/65b275005e513f580cc89a11c1ca708cd81732f6/lib/jev.ts) posts Score questions to `https://ai-gateway.vercel.sh/v4/ai/evaluation-model` with `ai-model-id: typesafe-ai/jev` and parses fractional 0–4 rubric positions. |
| Disclosure | AI-assisted catalog review; no affiliation or commercial relationship with the maintainer was supplied. Listing is not an endorsement. Source inspected; Chrome install and live grading were not tested. Do not use upstream README referral (`?ref=`) links from this catalog. |
| Maintainer | [kitze](https://github.com/kitze). Independently curated. |
| Format | WXT Manifest V3 Chrome extension **pagegrade 0.2.0** (Bun build). |
| Platform and availability | Chrome 120+ Developer mode → Load unpacked `.output/chrome-mv3`. No store listing verified. |
| Jev's role | Scores section and page metrics on ordered rubrics; application code aggregates into letter grades. Page content is treated as untrusted data in question instructions. |
| Requirements | Bun; Chromium; Vercel AI Gateway API key entered in the extension Connection settings. |
| License | [MIT](https://github.com/kitze/pagegrade/blob/65b275005e513f580cc89a11c1ca708cd81732f6/LICENSE). |

## When to use

Use it for personal, local grading of public page sections you already view. Prefer [jev-seo](../tools/jev-seo.md) for a CLI/MCP SEO workflow rather than an in-browser side panel. Grades are rubric judgments, not SEO ranking guarantees.

## How it works

1. The extension extracts readable sections from the active tab.
2. [`lib/jev.ts`](https://github.com/kitze/pagegrade/blob/65b275005e513f580cc89a11c1ca708cd81732f6/lib/jev.ts) builds Score questions from shipped metrics and calls the Vercel AI Gateway evaluation API targeting TypeSafe Jev.
3. Incomplete answer sets throw; no grade is assigned from partial responses.
4. Results render in Chrome's side panel.

## Get started

```sh
git clone https://github.com/kitze/pagegrade.git
cd pagegrade
git checkout 65b275005e513f580cc89a11c1ca708cd81732f6
bun install --frozen-lockfile
bun run build
# Chrome → chrome://extensions → Developer mode → Load unpacked → .output/chrome-mv3
```

**Analyze sections** sends extracted page content through the Gateway to Jev and can incur Gateway/TypeSafe charges. This listing did not build, load, or analyze live pages.

## Examples and demos

- README local install and Connection key steps.
- `tests/core.test.ts` and `scripts/smoke-jev.ts` (live smoke needs credentials—not run here).

## Limits and data handling

Extracted page text leaves the browser for Vercel AI Gateway / TypeSafe. Keys are stored in extension settings. Upstream marketing blocks with referral query params are omitted from this listing. Rubric quality and SEO outcomes were not measured on the review host.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 65b27500](https://github.com/kitze/pagegrade/tree/65b275005e513f580cc89a11c1ca708cd81732f6): **0.2.0**, MIT. AI-assisted source review of README, `lib/jev.ts`, `package.json`, tests inventory, and license. Bun build, Chrome load, and live Gateway/Jev calls were not executed on the review host.

Related: [jev-seo](../tools/jev-seo.md), [Vibe Check for X](vibecheck.md), [Unclutter](unclutter.md).
