# OCR Gateway

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Self-hosted document parsing gateway for TypeScript, Python, React and agent tools that routes PDFs, scans, images and office files across hosted OCR and vision providers or local parsers, using Jev to choose providers from metadata and returning location citations and embedding-ready chunks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alvarovillalbaa/ocr-gateway) |
| Maintainer | [alvarovillalbaa](https://github.com/alvarovillalbaa). Independently curated. |
| Format | TypeScript core, Python client, React components and agent tools (release tarball and wheel) |
| Requirements | Node.js 22+ and Python 3.11+; your own OCR/vision provider keys; a TypeSafe key for Jev routing (optional). |
| License | [MIT](https://github.com/alvarovillalbaa/ocr-gateway/blob/117d8694b23922061a79b987af390b8f1f36cd07/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/routing.ts`](https://github.com/alvarovillalbaa/ocr-gateway/blob/117d8694b23922061a79b987af390b8f1f36cd07/src/routing.ts) at the pinned commit. |

## When to use

- Put several OCR providers behind one parse interface and let routing pick by document type and needed features.
- Get chunked output with citations ready for retrieval.
- Mismatch: provider accounts and credits are separate; no managed universal key is sold.

## How it works

In `auto` mode, custom functions and matching rules run first; then `src/routing.ts` asks Jev at `/v1/systemone` which providers fit. Low confidence, invalid answers or failure fall back to OpenAI `/v1/decisions`, then to deterministic capability ranking. Per the README, the decision services receive metadata and desired features, never document contents, filenames or URLs. Integration evidence: [`src/routing.ts`](https://github.com/alvarovillalbaa/ocr-gateway/blob/117d8694b23922061a79b987af390b8f1f36cd07/src/routing.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/alvarovillalbaa/ocr-gateway.git && cd ocr-gateway
npm ci && npm run build
python3 -m pip install ./python
# set provider keys and TYPESAFE_API_KEY on the server (see .env.example)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- PROVIDERS.md (provider capabilities and credentials)
- [github.com/alvarovillalbaa/ocr-gateway/releases](https://github.com/alvarovillalbaa/ocr-gateway/releases)

## Limits and data handling

Documents go to whichever OCR providers are selected. Only routing metadata goes to TypeSafe, per the README; not verified here.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 117d8694b239](https://github.com/alvarovillalbaa/ocr-gateway/tree/117d8694b23922061a79b987af390b8f1f36cd07). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
