# axonhub-jev-guard (AxonHub plugin that screens requests with TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

AxonHub gateway plugin that classifies each incoming request with TypeSafe Jev before quota, routing and upstream calls, and rejects requests over a configured threshold.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/looplj/axonhub-jev-guard) |
| Maintainer | [looplj](https://github.com/looplj). Independently curated. |
| Format | AxonHub plugin (JavaScript; no SPDX license file on the reviewed commit) |
| Requirements | An AxonHub instance and a TypeSafe API key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/screen.js`](https://github.com/looplj/axonhub-jev-guard/blob/5a55a891bb4e9cfdec5746d2022b5babcb22bba3/lib/screen.js) at the pinned commit. |

## When to use

- Block disallowed prompts at the gateway before they reach upstream models.
- Run per-category probability thresholds.
- Mismatch: no OSI license on the reviewed commit; Chinese-language docs.

## How it works

`lib/screen.js` builds one `POST https://api.typesafe.ai/v1/systemone` request answering each configured category in parallel; `manifest.json` declares the network scope and default `jev-latest`. Integration evidence: [`lib/screen.js`](https://github.com/looplj/axonhub-jev-guard/blob/5a55a891bb4e9cfdec5746d2022b5babcb22bba3/lib/screen.js).

## Get started

Install the plugin into AxonHub, set the TypeSafe key and categories in its config.

```sh
git clone https://github.com/looplj/axonhub-jev-guard.git && cd axonhub-jev-guard
export TYPESAFE_API_KEY=...
node --test screen.test.mjs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/looplj/axonhub-jev-guard/blob/5a55a891bb4e9cfdec5746d2022b5babcb22bba3/README.md](https://github.com/looplj/axonhub-jev-guard/blob/5a55a891bb4e9cfdec5746d2022b5babcb22bba3/README.md)

## Limits and data handling

Request text is sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 5a55a891bb4e](https://github.com/looplj/axonhub-jev-guard/tree/5a55a891bb4e9cfdec5746d2022b5babcb22bba3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
