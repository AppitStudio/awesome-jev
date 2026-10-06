# Skipto

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that answers a question about a YouTube video by asking TypeSafe Jev a Choice over ~30-second transcript windows plus a yes/no “is it covered at all?” check, then highlights the progress bar and jumps to the best moment.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jinukuntlaakhilakumargoud-web/skipto) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/jinukuntlaakhilakumargoud-web/skipto#readme) (source-built app; no separate website verified). |
| Pricing and access | No extension fee (load unpacked from source). Requires a TypeSafe key, or a Vercel AI Gateway key / any `/v1/systemone`-compatible server; usage billed by that provider (README estimates about a twentieth of a cent per question on a one-hour transcript). Checked 2026-10-07. |
| Jev evidence | Inspected [`src/core.js`](https://github.com/jinukuntlaakhilakumargoud-web/skipto/blob/b814810417d47e8de81dae33ca0a0d25319d0e39/src/core.js) and the README *How it works* section (one request: Choice over window ids + Noul). |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [jinukuntlaakhilakumargoud-web](https://github.com/jinukuntlaakhilakumargoud-web). Independently curated. |
| Format | Manifest V3 Chrome extension (plain JS) |
| Platform and availability | Chrome desktop, load unpacked; YouTube videos with a transcript only; early open-source project. |
| Jev's role | Jev chooses which transcript window answers the question and estimates whether any window does; code splits long videos into several requests (≤255 options each), merges results and drives the player. |
| Requirements | Chrome; a TypeSafe API key (or Vercel AI Gateway key with base URL `https://ai-gateway.vercel.sh/typesafe`). |
| License | [MIT](https://github.com/jinukuntlaakhilakumargoud-web/skipto/blob/b814810417d47e8de81dae33ca0a0d25319d0e39/LICENSE). |

## When to use

- Jump to the moment in a long talk or tutorial that answers your question.
- Get a clear “this video doesn't cover that” instead of the least-bad moment.
- Mismatch: videos without transcripts are not supported.

## How it works

[`src/content.js`](https://github.com/jinukuntlaakhilakumargoud-web/skipto/blob/b814810417d47e8de81dae33ca0a0d25319d0e39/src/content.js) reads YouTube's transcript and tags ~30 s windows (`W000`, `W001`, …); [`src/core.js`](https://github.com/jinukuntlaakhilakumargoud-web/skipto/blob/b814810417d47e8de81dae33ca0a0d25319d0e39/src/core.js) builds the Choice + Noul request; the top three moments are listed and the video seeks when the answer is confident.

## Get started

Load the extension and paste a key:

```sh
git clone https://github.com/jinukuntlaakhilakumargoud-web/skipto.git
# chrome://extensions → Developer mode → Load unpacked → select skipto/
# click the Skipto icon → paste TypeSafe key → open a YouTube video with a transcript
```

Each question is one or more Jev requests billed to your key.

## Examples and demos

- README *How it works* and *Cost* sections.
- Settings for alternative `/v1/systemone` endpoints (Vercel AI Gateway).

## Limits and data handling

Transcript text and your question go to the configured API; the key stays in extension storage. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit b814810417d4](https://github.com/jinukuntlaakhilakumargoud-web/skipto/tree/b814810417d47e8de81dae33ca0a0d25319d0e39). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
