# SiteClarity

[All projects](../README.md) · [Web apps](README.md#web-apps)

Evidence-backed AI answer-readiness page audit: structural and language checks plus TypeSafe Jev meaning judgments; every finding carries a verbatim quote from your page—no generative prose scores.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sanjuacodez/siteclarity) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://siteclarity.sanjay-shankar.workers.dev) |
| Pricing and access | Hosted demo appears free (checked 2026-09-23); self-host from MIT source with your own System One / Workers AI provider keys. Hosted rate limits and any account requirements were not verified. Provider inference billed separately when you supply keys. |
| Jev evidence | [`src/provider/systemone.ts`](https://github.com/sanjuacodez/siteclarity/blob/1ec2ffe13b2d3e7a63ff6bbdea6757f2384c3abc/src/provider/systemone.ts), [`src/semantic/`](https://github.com/sanjuacodez/siteclarity/tree/1ec2ffe13b2d3e7a63ff6bbdea6757f2384c3abc/src/semantic) — typed System One questions; findings assembled from templates + verified substrings. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; live hosted audit and self-host deploy were **not** executed on the review host. |
| Maintainer | [sanjuacodez](https://github.com/sanjuacodez). Independently curated. |
| Format | Cloudflare Workers web app + TypeScript source (**siteclarity 0.1.0**). |
| Platform and availability | Web (hosted Workers URL) · source build. Release: early public. |
| Jev's role | Meaning/quote-readiness judgments over extracted page sections; about half the checks are deterministic without a model. Optional Kev/Laya/Workers AI providers exist in source. |
| Requirements | For self-host: Node tooling per upstream; provider keys as configured. Hosted demo: browser only. |
| License | [MIT](https://github.com/sanjuacodez/siteclarity/blob/1ec2ffe13b2d3e7a63ff6bbdea6757f2384c3abc/LICENSE). |

## When to use

Use it when you want ordered, quote-backed fixes for how quotable/answer-ready a page is—not an SEO score. Prefer general SEO CLIs when you need SERP tooling instead of answer-readiness audits.

## How it works

Deterministic HTML extraction feeds templated findings; Jev (or compatible System One) answers narrow meaning questions; quotes are verified as substrings before display. `/checks` on the live app is generated from the check registry.

## Get started

- Hosted: open [siteclarity.sanjay-shankar.workers.dev](https://siteclarity.sanjay-shankar.workers.dev) and audit a URL.
- Source: clone [sanjuacodez/siteclarity](https://github.com/sanjuacodez/siteclarity) at [commit 1ec2ffe](https://github.com/sanjuacodez/siteclarity/tree/1ec2ffe13b2d3e7a63ff6bbdea6757f2384c3abc) and follow upstream deploy docs (not run here).

## Examples and demos

- [YouTube walkthrough](https://www.youtube.com/watch?v=Fd_TAiQClr0) (upstream).
- Live `/checks` catalog on the hosted app.

## Limits and data handling

Audited page content is fetched/processed by the host you use. Live Jev paths send section text to the configured provider. This listing did not run an audit or deploy Workers.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 1ec2ffe](https://github.com/sanjuacodez/siteclarity/tree/1ec2ffe13b2d3e7a63ff6bbdea6757f2384c3abc) (**0.1.0**, MIT). AI-assisted review of README, LICENSE, and provider/semantic paths. No live TypeSafe spend.

Related: [AnchorLint](../tools/anchorlint.md), [jev-seo](../tools/jev-seo.md), [PageGrade](pagegrade.md).
