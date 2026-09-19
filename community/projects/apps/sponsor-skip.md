# Sponsor Skip

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

A Chrome extension and local web interface that use Jev to locate YouTube sponsor reads, with optional automatic skipping and live audio analysis.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/trungdq88/youtube-sponsor-detection) |
| Tags | `Source unverified` · `Pricing unverified` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/trungdq88/youtube-sponsor-detection#readme) |
| Pricing and access | [Source setup](https://github.com/trungdq88/youtube-sponsor-detection#chrome-extension) requires a TypeSafe key; Smart and Listen modes also require Deepgram. Provider charges apply. App licensing/pricing terms were not established on 2026-09-19. |
| Jev evidence | [Transcript pipeline](https://github.com/trungdq88/youtube-sponsor-detection/blob/de01f0568d043035889a296a61ce21e0accc8b16/src/jev.js) and [live decision loop](https://github.com/trungdq88/youtube-sponsor-detection/blob/de01f0568d043035889a296a61ce21e0accc8b16/src/live.js). |
| Disclosure | Public code was inspected, but no license was found. AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. |
| Maintainer | [trungdq88](https://github.com/trungdq88) |
| Format | JavaScript Chrome MV3 extension plus Node.js/Express local web app; version 0.1.0 |
| Platform and availability | Load-unpacked Chrome extension; local web interface. Store distribution was not verified. |
| Jev's role | Judges sponsor presence, selects transcript line/phrase boundaries, and checks whether playback is still inside a sponsor read. |
| Requirements | Chrome and TypeSafe account/key for the extension; Deepgram key for audio modes. Node.js and npm dependencies for the local web app. |
| License | No license file or package license declaration found at the reviewed commit; public source is not established as open source. |

## When to use

Use the extension to inspect and skip detected sponsor reads while watching YouTube,
or use the local web app to inspect proposed timestamps and surrounding transcript text.
The transcript-only mode is the default. The extension enables auto-skip by default;
turn it off in settings when you want to review boundaries before moving playback.

## How it works

Code converts timestamped captions to labeled lines and scans overlapping 80-line windows.
Jev answers Noul presence questions and Choice questions over actual line IDs. Later passes
confirm the sponsor, trace its lead-in and judge boundary phrases. Code maps selected
IDs back to timestamps and limits the search to six detected reads.

The extension calls TypeSafe `/v1/systemone` with `jev-latest` by default; the web app
uses `@typesafe-ai/sdk`. The model does not generate timestamps or execute seeks.
The audio loop asks Jev about recent transcribed speech and decides whether to jump again.
Default skip threshold is `0.7`; phrase-boundary policy uses `0.8`. Neither establishes
calibrated accuracy or guarantees that normal content will remain untouched.

## Get started

The [extension setup](https://github.com/trungdq88/youtube-sponsor-detection#chrome-extension)
requires no repository build step:

```sh
git clone https://github.com/trungdq88/youtube-sponsor-detection.git
```

Open `chrome://extensions`, enable Developer mode and load the checkout's `extension/`
directory. Open the extension popup, privately enter a TypeSafe key and inspect the
mode/auto-skip settings. Loading a YouTube video can trigger paid transcript analysis;
video titles and transcript excerpts reach TypeSafe. The page panel shows detected reads,
manual **Skip**, auto-skip controls, estimated cost and **Re-analyze**.

Smart and Listen modes also need a Deepgram key and stream video audio to Deepgram.
Smart mode uses transcript boundaries plus audio confirmation, with a transcript fallback
after 12 seconds; Listen mode jumps in fixed steps. **Stop** ends listening for that video.

For the optional web app, install dependencies in the checkout and configure
`TYPESAFE_API_KEY` privately before `npm start`. The README's start script uses
`--env-file-if-exists`; use a current Node release supporting that flag rather than
assuming every Node version allowed by the package's `>=20` range supports it.

## Examples and demos

- [Screenshots](https://github.com/trungdq88/youtube-sponsor-detection/tree/de01f0568d043035889a296a61ce21e0accc8b16/docs) show the popup, playback panel and local web app.
- [Synthetic transcript fixtures](https://github.com/trungdq88/youtube-sponsor-detection/tree/de01f0568d043035889a296a61ce21e0accc8b16/fixtures) and [stub tests](https://github.com/trungdq88/youtube-sponsor-detection/tree/de01f0568d043035889a296a61ce21e0accc8b16/test) demonstrate the pipeline without model-quality evidence.
- [Mock API instructions](https://github.com/trungdq88/youtube-sponsor-detection#web-app) run the web app against a local stand-in. Use its demo transcript to avoid live YouTube retrieval; ordinary URL inputs still contact YouTube.

## Limits and data handling

YouTube transcript retrieval uses an unofficial API and may fail or change, particularly
from cloud IPs. A pasted transcript is available in the local web interface. Listen mode
supports one tab at a time, hears the first part of a read, and can overshoot its end by
one configured step. Speech recognition and classification errors can skip useful content.

Extension settings/keys, results and usage totals use `chrome.storage.local`. TypeSafe
receives titles/transcript excerpts or recent speech text; Deepgram receives audio in
Smart/Listen modes. The source's background `get-state` returns merged settings including
keys, and sender validation is not a comprehensive privilege boundary. This review did
not perform a browser security audit; do not treat the README's key-isolation claim as
independently established.

Transcript processing accesses expected answer fields directly rather than applying a
complete response schema. The live loop coerces a Noul value to a number without a strict
finite-range check. Missing/malformed responses can fail analysis, and inferred confidence
is not a correctness guarantee. Extension HTTP 429/5xx requests retry up to three attempts;
no explicit fetch timeout appears in that request helper.

The local Express app has no authentication layer and uses `app.listen(port)` without an
explicit loopback host; keep it in a trusted local environment. Cost displays use configured
rates rather than verified billing. The bundled SponsorBlock evaluation workflow makes
external requests and was not reproduced.

## Review and maintenance

Reviewed **2026-09-19** at
[`de01f0568d043035889a296a61ce21e0accc8b16`](https://github.com/trungdq88/youtube-sponsor-detection/tree/de01f0568d043035889a296a61ce21e0accc8b16).
Inspected README, package metadata, extension manifest, Jev pipeline, live loop,
background request/settings handling, speech socket, server and representative stub tests.
No license was found. No install, test execution, browser session, provider request or
accuracy evaluation was performed; screenshots and performance claims remain upstream evidence.
