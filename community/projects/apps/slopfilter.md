# SlopFilter (Chrome extension that folds or hides AI-generated slop on X, judged by Jev and local rules)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension for X: local rules scan each post, then Jev answers three questions (is it AI slop, what kind, does it show a human touch) and posts above your threshold are folded to one line or hidden. A floating counter shows how many were caught, you can pick lenient, balanced or strict, and marking a false positive restores the post and stops filtering that author. Without a key it runs on local rules only. Interface in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HerrysYu/SlopFilter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/HerrysYu/SlopFilter#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; bring your own TypeSafe key (optional). Checked 2026-10-30. |
| Jev evidence | [`src/background.js`](https://github.com/HerrysYu/SlopFilter/blob/0d40917086441b4e724dee785df998c92a9dd585/src/background.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [HerrysYu](https://github.com/HerrysYu). Independently curated. |
| Format | Chrome extension (unpacked) |
| Platform and availability | Desktop Chrome; load unpacked from the cloned repo (no Chrome Web Store listing verified). |
| Jev's role | Judges each X post for AI slop so the extension can fold or hide it. |
| Requirements | Desktop Chrome and a TypeSafe API key (optional; local rules only without it). |
| License | [MIT](https://github.com/HerrysYu/SlopFilter/blob/0d40917086441b4e724dee785df998c92a9dd585/LICENSE) |

## When to use

- Clean AI-written filler out of your X timeline.
- Mismatch: Chinese interface; judgments are probabilistic, so expect some false positives.

## How it works

`src/prompt.js` builds the three-question request and `src/background.js` sends it to `https://api.typesafe.ai/v1/systemone`, then blends the scores with the local rule score. Integration evidence: [`src/background.js`](https://github.com/HerrysYu/SlopFilter/blob/0d40917086441b4e724dee785df998c92a9dd585/src/background.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/HerrysYu/SlopFilter.git
# chrome://extensions -> Developer mode -> Load unpacked -> select the folder
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with screenshots: [github.com/HerrysYu/SlopFilter#readme](https://github.com/HerrysYu/SlopFilter#readme)

## Limits and data handling

Post text from your timeline is sent to TypeSafe when a key is set.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 0d4091708644](https://github.com/HerrysYu/SlopFilter/tree/0d40917086441b4e724dee785df998c92a9dd585). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
