# paperless-jev (Paperless-ngx inbox classifier with TypeSafe Jev or local Ollama)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Docker service with a web UI that classifies new Paperless-ngx inbox documents (type, correspondent, storage path, issue date, tags) using TypeSafe Jev, Cloudflare Workers AI, or a local Ollama model such as clef.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PenDraga/paperless-jev) |
| Maintainer | [PenDraga](https://github.com/PenDraga). Independently curated. |
| Format | Python Docker service + web UI (AGPL-3.0) |
| Requirements | Docker, a Paperless-ngx instance, and a TypeSafe key (or Cloudflare/Ollama) for classification. |
| License | [AGPL-3.0](https://github.com/PenDraga/paperless-jev/blob/5b7eb30038ea376c52649ef3d4edd775e8ac02fe/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/paperless_jev/jev.py`](https://github.com/PenDraga/paperless-jev/blob/5b7eb30038ea376c52649ef3d4edd775e8ac02fe/src/paperless_jev/jev.py) at the pinned commit. |

## When to use

- Classify Paperless-ngx inbox documents with calibrated choices.
- Prefer a review UI before writing tags back.
- Mismatch: needs Paperless and a classifier endpoint; not a general DMS.

## How it works

`src/paperless_jev/jev.py` POSTs System One choice/noul questions to `https://api.typesafe.ai` (or Cloudflare `typesafe/jev` / Ollama) over HTTP without the SDK, with 429-aware retries. Integration evidence: [`src/paperless_jev/jev.py`](https://github.com/PenDraga/paperless-jev/blob/5b7eb30038ea376c52649ef3d4edd775e8ac02fe/src/paperless_jev/jev.py).

## Get started

Follow the README Docker quick start, point it at Paperless, and pick TypeSafe Jev in the setup UI with your key.

```sh
git clone https://github.com/PenDraga/paperless-jev.git && cd paperless-jev
# follow README Docker compose
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/PenDraga/paperless-jev/blob/5b7eb30038ea376c52649ef3d4edd775e8ac02fe/README.md](https://github.com/PenDraga/paperless-jev/blob/5b7eb30038ea376c52649ef3d4edd775e8ac02fe/README.md)

## Limits and data handling

Document text and candidate labels under review are sent to the configured classifier on your key. Review before writing back to Paperless.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 5b7eb30038ea](https://github.com/PenDraga/paperless-jev/tree/5b7eb30038ea376c52649ef3d4edd775e8ac02fe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
