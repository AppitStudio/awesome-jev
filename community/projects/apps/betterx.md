# betterx

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome/Brave extension that classifies posts and replies on x.com with TypeSafe Jev as you browse — seven questions per post in one ~150–250 ms request (tone, post type, argument quality, racist, contempt for a nationality or immigrants, antisemitic, sexually explicit) — and labels, dims, blurs or hides them by your rules.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kalowery/betterx) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/kalowery/betterx#readme) (unpacked extension). |
| Pricing and access | No fee; load unpacked. Requires your own TypeSafe API key (billed by TypeSafe). Checked 2026-10-08. |
| Jev evidence | [`background.js`](https://github.com/kalowery/betterx/blob/94b9356d6ca3b94cd860f932c51ff05efdaa4380/background.js) posts each post's text to `/v1/systemone` with a cache and up to six concurrent requests; [`content.js`](https://github.com/kalowery/betterx/blob/94b9356d6ca3b94cd860f932c51ff05efdaa4380/content.js) applies your rules. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [kalowery](https://github.com/kalowery). Independently curated. |
| Format | Chrome/Brave MV3 extension (load unpacked) |
| Platform and availability | Chrome or Brave on desktop. |
| Jev's role | Classifies every visible post; your settings decide whether to label, dim, blur or hide. |
| Requirements | Chrome or Brave (developer-mode unpacked install) and a TypeSafe API key. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |

## When to use

- Tune your x.com timeline by tone or argument quality instead of keywords.
- Hide hateful or explicit replies before you read them.
- Mismatch: classifier likelihoods are probabilistic and can mislabel posts.

## How it works

The content script finds posts in the page and sends their text to the background worker, which asks Jev seven questions per post and caches answers; your thresholds map answers to actions.

## Get started

Clone and load unpacked (README *Install*):

```sh
git clone https://github.com/kalowery/betterx.git
# chrome://extensions → Developer mode → Load unpacked → betterx
# extension icon → Settings… → paste key → Save → Test, then reload x.com
```

One Jev request per post viewed (cached), billed to your TypeSafe key.

## Examples and demos

- README *What you see* and *Settings*.

## Limits and data handling

Text of posts you view goes to TypeSafe. No LICENSE file. Not affiliated with X. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 94b9356d6ca3](https://github.com/kalowery/betterx/tree/94b9356d6ca3b94cd860f932c51ff05efdaa4380). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
