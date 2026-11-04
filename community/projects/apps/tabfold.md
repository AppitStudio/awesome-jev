# Tabfold (Chrome extension that groups and folds crowded tabs, with Jev classifying tabs when you add a key)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Manifest V3 Chrome extension that proposes tab groups, lets you review them, then applies and collapses them without merging windows. It works without AI using local title similarity; with an OpenRouter or TypeSafe key, Jev (1.13) classifies tabs into your categories and can suggest new ones. Pinned, audible, incognito and internal tabs are protected, and the last grouping can be undone.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JayYun98/tabfold) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/JayYun98/tabfold#readme) (source-built; no separate product site verified). |
| Pricing and access | Free to load from source; no account or paid plan was found. The AI preview needs your own TypeSafe or OpenRouter key and incurs provider charges. Checked 2026-11-04. |
| Jev evidence | [`extension/ai.js`](https://github.com/JayYun98/tabfold/blob/14202c60459a31e31fa9b02ec7b6c08a05aab3f4/extension/ai.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. The repository has no license file, so no open-source license is granted. Discovered via X ([post](https://x.com/Jayyun98_dev/status/2117757767394148515)). |
| Maintainer | [JayYun98](https://github.com/JayYun98). Independently curated. |
| Format | Chrome Manifest V3 extension (JavaScript, no build step), nine UI languages |
| Platform and availability | Desktop Chrome; load unpacked from the cloned repo (no Chrome Web Store listing verified). |
| Jev's role | Optionally classifies open tabs into your categories and suggests new groups; local similarity is the default. |
| Requirements | Chrome; load the `extension` folder unpacked. A TypeSafe or OpenRouter key only for the AI preview. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Tame a crowded browser with previewed, reversible grouping, using Jev only if you opt in.
- Mismatch: the repository has no license file, and the AI path sends tab titles and URLs to your chosen provider.

## How it works

`extension/ai.js` posts the tab state and typed questions to `https://api.typesafe.ai/v1/systemone` (`jev-1.13.0`) or to OpenRouter's decisions endpoint (`typesafe/jev-1.13`); both are optional host permissions you grant, and local clustering is the default. Integration evidence: [`extension/ai.js`](https://github.com/JayYun98/tabfold/blob/14202c60459a31e31fa9b02ec7b6c08a05aab3f4/extension/ai.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/JayYun98/tabfold
# chrome://extensions > Developer mode > Load unpacked > select the extension folder
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with preview, review and apply flow and privacy notes: [github.com/JayYun98/tabfold#readme](https://github.com/JayYun98/tabfold#readme)
- Announcement post on X: [x.com/Jayyun98_dev/status/2117757767394148515](https://x.com/Jayyun98_dev/status/2117757767394148515)

## Limits and data handling

With the AI preview on, eligible tabs' titles and URLs go to the provider you choose on your key. The README's demo video is labelled illustrative. No Chrome Web Store listing was verified. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 14202c60459a](https://github.com/JayYun98/tabfold/tree/14202c60459a31e31fa9b02ec7b6c08a05aab3f4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
