# JevSense (self-hosted site personalization where Jev judges a visitor's browsing against your Yes/No questions to show the right offer; Japanese)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted app for marketers: describe what you want to say and who it is for, build a node-based audience rule from URL, Jev, AND and OR conditions, and the site SDK asks Jev, once per page at most, whether the visitor's browsing so far fits before showing a registered offer (modal, banner, notice bar or custom script). It includes drafts and previews, passkey sign-in, per-site roles, encrypted site keys and a call log. The interface and guides are in Japanese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/manji6/jev-personalization) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://manji6.github.io/jev-personalization/) |
| Pricing and access | Free source build under MIT; you pay TypeSafe per site key and any Cloudflare charges. Checked 2026-11-03. |
| Jev evidence | [`src/jev.js`](https://github.com/manji6/jev-personalization/blob/bd984438612208063f970a454cc8a2fbd4b5e04b/src/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [manji6](https://github.com/manji6). Independently curated. |
| Format | Cloudflare Workers app (Node 24+; D1 and Durable Objects) with a site SDK |
| Platform and availability | Self-hosted on Cloudflare Workers (browser admin UI; site SDK). |
| Jev's role | Judges a visitor's browsing against your Yes/No audience questions to choose an offer. |
| Requirements | Node.js 24+, a Cloudflare account for the documented deployment, and a TypeSafe key per site. |
| License | [MIT](https://github.com/manji6/jev-personalization/blob/bd984438612208063f970a454cc8a2fbd4b5e04b/LICENSE) |

## When to use

- Show an offer only to visitors whose browsing history fits an audience you describe, judged by independent Yes/No questions.
- Mismatch: Japanese documentation, and Jev scores are not purchase probabilities or measured campaign effect.

## How it works

`src/jev.js` posts the page names, descriptions, types and browsing order to `https://api.typesafe.ai/v1/systemone` (`jev-1.14.0`, 1.2 s timeout) with the questions built from your rule, after recording the dispatch so a failed log write blocks the call, and the result drives which offer shows. Integration evidence: [`src/jev.js`](https://github.com/manji6/jev-personalization/blob/bd984438612208063f970a454cc8a2fbd4b5e04b/src/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/manji6/jev-personalization.git
cd jev-personalization
npm ci
npm run review      # local checks
npm run cf:preview  # Cloudflare preview
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Help and setup guide (Japanese): [manji6.github.io/jev-personalization/](https://manji6.github.io/jev-personalization/)
- Repository README: [github.com/manji6/jev-personalization#readme](https://github.com/manji6/jev-personalization#readme)

## Limits and data handling

Page titles, descriptions, types and a short history go to TypeSafe on each site's key (no form input, full page text or whole JSON-LD); visitor history stays in the browser's sessionStorage, but the README warns page information can contain personal data, so design consent. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit bd9844386122](https://github.com/manji6/jev-personalization/tree/bd984438612208063f970a454cc8a2fbd4b5e04b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
