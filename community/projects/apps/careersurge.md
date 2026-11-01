# CareerSurge (free desktop app that finds job postings and applies for you locally, with Jev only picking among values it already found)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Local desktop app that searches Greenhouse, Lever and Ashby listings through your own Apify account, shows a batch to approve, and fills and submits each form in a headless Chromium. It does no captcha solving or made-up answers; Jev, if you add a key, only picks among values the app already found (resume parsing, label mapping, question classification), and anything unresolved waits in 'Needs you'.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ben19001/applypulse-public) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Ben19001/applypulse-public#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (Apache-2.0); Apify runs bill your own Apify account and Jev uses your own TypeSafe key. Checked 2026-11-01. |
| Jev evidence | [`backend/app/services/jev.py`](https://github.com/Ben19001/applypulse-public/blob/bf2166b9e6bea6686dffe4572252bcb51f16b933/backend/app/services/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Ben19001](https://github.com/Ben19001). Independently curated. |
| Format | Desktop app (local Python server + desktop window) |
| Platform and availability | Desktop (macOS, Windows, Linux) via a local server and window. |
| Jev's role | Optional chooser among already-found values for resume parsing and form answers. |
| Requirements | An Apify account (billed to you); optional TypeSafe key for Jev. |
| License | [Apache-2.0](https://github.com/Ben19001/applypulse-public/blob/bf2166b9e6bea6686dffe4572252bcb51f16b933/LICENSE) |

## When to use

- Apply to many ATS job postings from your own machine with every value traceable to your profile.
- Mismatch: only Greenhouse, Lever and Ashby; Jev is optional.

## How it works

`backend/app/services/jev.py` posts to `https://api.typesafe.ai/v1/systemone` with the key stored in your OS keychain; `local_profile.parse_resume` and `local_answers` use it to choose between candidate values, and the app falls back to its own matching when no key is set or TypeSafe refuses it. Integration evidence: [`backend/app/services/jev.py`](https://github.com/Ben19001/applypulse-public/blob/bf2166b9e6bea6686dffe4572252bcb51f16b933/backend/app/services/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Ben19001/applypulse-public && cd applypulse-public
# follow the README setup; add Apify and (optional) Jev keys in onboarding
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Ben19001/applypulse-public#readme](https://github.com/Ben19001/applypulse-public#readme)

## Limits and data handling

Resume fields and form questions are sent to TypeSafe when Jev is enabled; search filters go to Apify. Not affiliated with Greenhouse, Lever, Ashby, Apify or TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit bf2166b9e6be](https://github.com/Ben19001/applypulse-public/tree/bf2166b9e6bea6686dffe4572252bcb51f16b933). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
