# Nature Lens

[All projects](../README.md) · [Web apps](README.md#web-apps)

Upload a nature photo and Jev ranks which landscape categories are visible, picks the main subject and draws a box around any person (Jev 1.14 Box), all in one request.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JonesSteven/jevnatureimage) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/JonesSteven/jevnatureimage#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-15. |
| Jev evidence | [`server/jev.ts`](https://github.com/JonesSteven/jevnatureimage/blob/bfde53e89686042212faa228a4c464d09d7a1329/server/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [JonesSteven](https://github.com/JonesSteven). Independently curated. |
| Format | Web app (Vite + TypeScript, Node server; Docker) |
| Platform and availability | Web (local source build or Docker) |
| Jev's role | Jev classifies each photo (visible categories, main subject, person + box). |
| Requirements | Node.js or Docker; your TypeSafe API key in `.env`. |
| License | [MIT](https://github.com/JonesSteven/jevnatureimage/blob/bfde53e89686042212faa228a4c464d09d7a1329/LICENSE) |

## When to use

- Try Jev's image input, Noul, Choice and experimental Box questions on your own photos.
- Use as a reference for normalizing images to Jev's size limits before sending.
- Mismatch: a demo classifier, not a photo-management app.

## How it works

The server normalizes each upload (EXIF rotation, 256–1568 px, baseline JPEG), then sends 13 questions in a single Jev request with the image placed once in `state`; answers are normalized and shown next to the exact JPEG sent. Integration evidence: [`server/jev.ts`](https://github.com/JonesSteven/jevnatureimage/blob/bfde53e89686042212faa228a4c464d09d7a1329/server/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env   # set TYPESAFE_API_KEY
npm install
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- `npm run probe -- photo.jpg` prints raw and normalized answers for one photo (one live request).

## Limits and data handling

Photos are sent to TypeSafe with the experimental images header and billed to your key; the key stays server-side.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit bfde53e89686](https://github.com/JonesSteven/jevnatureimage/tree/bfde53e89686042212faa228a4c464d09d7a1329). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
