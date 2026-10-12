# Reddit Pain

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that labels Reddit posts and comments as you scroll and boxes the ones asking for a product or describing a pain (with intensity 0–3), using TypeSafe Jev with your own key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Tribespencer/reddit-pain) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [github.com/Tribespencer/reddit-pain#readme](https://github.com/Tribespencer/reddit-pain#readme) |
| Pricing and access | Free MIT extension; every labelled item is one TypeSafe API call billed to your key. Checked 2026-10-13. |
| Jev evidence | [`src/jev.ts`](https://github.com/Tribespencer/reddit-pain/blob/c35f97c240025b298e0ef3f89bde08ce267e5496/src/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [Tribespencer](https://github.com/Tribespencer). Independently curated. |
| Format | Chrome extension (TypeScript) |
| Platform and availability | Chrome (unpacked extension from release zip) |
| Jev's role | Jev labels each post/comment that scrolls into view (product request, pain, intensity); the extension draws boxes and caches labels. |
| Requirements | Chrome; TypeSafe API key with Jev access. |
| License | [MIT](https://github.com/Tribespencer/reddit-pain/blob/c35f97c240025b298e0ef3f89bde08ce267e5496/LICENSE) |

## When to use

- Spot product demand and pain points while browsing Reddit.
- Mismatch: sends what you read to TypeSafe; costs scale with scrolling.

## How it works

Visible post/comment text (no usernames or links) is sent once per item; labels are stored locally and reused. (Summarized from the upstream [README](https://github.com/Tribespencer/reddit-pain/blob/c35f97c240025b298e0ef3f89bde08ce267e5496/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): download `reddit-pain.zip` from the latest release, load it unpacked, paste your key and click Test Jev connection.

## Limits and data handling

Text you scroll past goes to api.typesafe.ai; the key is stored in plain text in extension storage. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit c35f97c24002](https://github.com/Tribespencer/reddit-pain/tree/c35f97c240025b298e0ef3f89bde08ce267e5496). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
