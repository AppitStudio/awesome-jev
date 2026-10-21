# Y!News Filter Plus (Yahoo! News filter)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Unofficial Chrome extension that hides Yahoo! News Japan article cards by keyword and, optionally, uses Jev to highlight articles related to your interests and hide ones related to topics you don't want, with a details table of each verdict.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/doraTeX/YNewsFilterPlus) |
| Maintainer | [doraTeX](https://github.com/doraTeX). Independently curated. |
| Format | Chrome extension (TypeScript); README in Japanese |
| Requirements | Chrome; optional TypeSafe API key for the Jev feature (off by default). |
| License | [MIT](https://github.com/doraTeX/YNewsFilterPlus/blob/bee45529b7eae81db1705bc9b3156aa57a36364e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/content/engine.js`](https://github.com/doraTeX/YNewsFilterPlus/blob/bee45529b7eae81db1705bc9b3156aa57a36364e/src/content/engine.js) at the pinned commit. |

## When to use

- Filter a Japanese news feed by meaning rather than exact keywords.
- Check why an article was hidden in the Jev details table and copy it as TSV.
- Mismatch: only works on Yahoo! News Japan; not affiliated with Yahoo! JAPAN.

## How it works

Keyword rules run locally; when Jev is enabled, headlines (and optionally the start of the article body) plus your conditions are sent to `https://api.typesafe.ai/v1/systemone` (model `jev-1.13.0`, see `src/content/engine.js`) and results are cached for 7 days. Integration evidence: [`src/content/engine.js`](https://github.com/doraTeX/YNewsFilterPlus/blob/bee45529b7eae81db1705bc9b3156aa57a36364e/src/content/engine.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/doraTeX/YNewsFilterPlus.git && cd YNewsFilterPlus
npm ci && npm run build
# or install from the Chrome Web Store link in the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Feature list and privacy policy link in the README: [github.com/doraTeX/YNewsFilterPlus#readme](https://github.com/doraTeX/YNewsFilterPlus#readme)

## Limits and data handling

Jev is off by default; when on, headlines and conditions go to TypeSafe and API charges are between you and TypeSafe. The API key stays in local extension storage.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit bee45529b7ea](https://github.com/doraTeX/YNewsFilterPlus/tree/bee45529b7eae81db1705bc9b3156aa57a36364e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
