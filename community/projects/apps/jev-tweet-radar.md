# Jev Tweet Radar

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome Manifest V3 extension (plus optional iOS Safari Web Extension) that scores each X timeline post with one TypeSafe Jev call.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DDnim/jev-tweet-radar) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/DDnim/jev-tweet-radar#readme) |
| Pricing and access | Load unpacked from MIT source; TypeSafe API key in options. No app purchase fee; ~300 input tokens per judgment billed by TypeSafe. Checked **2026-09-26**. |
| Jev evidence | [`background.js`](https://github.com/DDnim/jev-tweet-radar/blob/0c877728449409a78fe836077aa3e32b147db2b0/background.js) posts Noul batches from [`questions.js`](https://github.com/DDnim/jev-tweet-radar/blob/0c877728449409a78fe836077aa3e32b147db2b0/questions.js) to `https://api.typesafe.ai/v1/systemone`. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; live install/provider paths not run on the review host. Distinct from Jev Slop Guard and jev-x-filter. |
| Maintainer | [DDnim](https://github.com/DDnim). Independently curated. |
| Format | JavaScript MV3 extension; optional Safari/iOS wrapper. |
| Platform and availability | Chromium load-unpacked; iOS via Xcode project under `safari/`. No Chrome Web Store listing verified. |
| Jev's role | One batched System One call per post for engage/buzz/spam/AI-ish (and selected tags); UI fades/folds/long-press actions are local code. |
| Requirements | Chromium (or Safari iOS build); TypeSafe API key. |
| License | [MIT](https://github.com/DDnim/jev-tweet-radar/blob/0c877728449409a78fe836077aa3e32b147db2b0/LICENSE). |

## When to use

Use to **triage an X timeline** with cheap typed scores and optional opacity filters. Distinct from [Jev Slop Guard](jev-slop-guard.md).

## How it works

[`content.js`](https://github.com/DDnim/jev-tweet-radar/blob/0c877728449409a78fe836077aa3e32b147db2b0/content.js) observes tweets; background calls Jev; results cache in chrome.storage.local.

## Get started

```sh
git clone https://github.com/DDnim/jev-tweet-radar.git
cd jev-tweet-radar
git checkout 0c877728449409a78fe836077aa3e32b147db2b0
# chrome://extensions → Developer mode → Load unpacked → this folder
# Options → paste TypeSafe API key → open x.com
```

## Examples and demos

- Upstream README (EN/JP/中文) documents filters, long-press actions, and draft scoring.

## Limits and data handling

Post text goes to TypeSafe. Extension can bookmark/repost/like or block on long-press—review those behaviors before enabling.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 0c87772](https://github.com/DDnim/jev-tweet-radar/tree/0c877728449409a78fe836077aa3e32b147db2b0). AI-assisted source inspection; live paths not executed.
