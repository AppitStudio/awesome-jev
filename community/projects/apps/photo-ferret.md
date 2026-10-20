# Photo Ferret

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted photo gallery where Jev's image questions rate every photo on dozens of scales (how much sky, water or snow, sky drama, wildness, close-up or vista, quality), so visitors filter a static Cloudflare site with sliders, chips, a colour picker and an experimental 3D map.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JonesSteven/photo-ferret) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://stevenjonesphotography.ca) |
| Pricing and access | Free MIT source; you pay for your own Jev image calls and Cloudflare hosting (free plan fits about 10,000 photos, per the README). Checked 2026-10-20. |
| Jev evidence | [`server/jev.ts`](https://github.com/JonesSteven/photo-ferret/blob/bddd12bfdda219feff09e5de411419f95611eb66/server/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [JonesSteven](https://github.com/JonesSteven). Independently curated. |
| Format | Local authoring tool (Node.js, SQLite) plus an exported static site for Cloudflare |
| Platform and availability | Self-hosted: local Node.js tool; published gallery runs in any browser. |
| Jev's role | Jev looks at each photo and answers the tagging questions; the gallery filters on those stored answers. |
| Requirements | Node.js 24+; a TypeSafe key with image access (box questions need Jev 1.14); Cloudflare Workers to publish. |
| License | [MIT](https://github.com/JonesSteven/photo-ferret/blob/bddd12bfdda219feff09e5de411419f95611eb66/LICENSE) |

## When to use

- Make a large personal photo archive browsable by look and mood instead of folders.
- Tag photos once locally and publish a static site with no model calls at view time.
- Mismatch: single-owner tool; the deploy config points at the author's domain until you change it.

## How it works

Photos uploaded in the admin are resized and `server/jev.ts` sends one JPEG per photo to Jev through the TypeSafe SDK with noul, score and image questions; answers become per-photo tags you can override. `npm run export-site` writes the gallery, thumbnails and a `data.json` of tags (without raw answers or confidences) for Cloudflare. Integration evidence: [`server/jev.ts`](https://github.com/JonesSteven/photo-ferret/blob/bddd12bfdda219feff09e5de411419f95611eb66/server/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env   # TYPESAFE_API_KEY, ADMIN_USER, ADMIN_PASSWORD, SESSION_SECRET
npm install
npm run dev            # gallery on :5173, admin at /admin/
npm run export-site && npm run deploy
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [stevenjonesphotography.ca](https://stevenjonesphotography.ca) (about 2,800 nature photos)
- `npm run probe -- photo.jpg` prints one raw Jev answer

## Limits and data handling

Each new photo is sent to TypeSafe (several requests per photo). Originals stay local; the exported site has no private data, per the README.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit bddd12bfdda2](https://github.com/JonesSteven/photo-ferret/tree/bddd12bfdda219feff09e5de411419f95611eb66). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
