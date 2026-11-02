# Jev for cc-cockpit (plugin service that lets other cc-cockpit plugins ask Jev typed questions, with usage caps)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

cc-cockpit plugin that wraps Jev as a shared `jev` service: other plugins ask yes/no, choice and score questions about text, singly or over a grid of items, and it keeps per-plugin usage counts and monthly request, token and spending caps.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BronOS/cc-cockpit-jev) |
| Maintainer | [BronOS](https://github.com/BronOS). Independently curated. |
| Format | cc-cockpit plugin (plain JavaScript) |
| Requirements | cc-cockpit; a TypeSafe or OpenRouter API key set in Settings > Plugins. |
| License | [MIT](https://github.com/BronOS/cc-cockpit-jev/blob/e7eff62bcc0f574043e19d16f5502643ee33d585/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`dist/lib/client.js`](https://github.com/BronOS/cc-cockpit-jev/blob/e7eff62bcc0f574043e19d16f5502643ee33d585/dist/lib/client.js) at the pinned commit. |

## When to use

- Give several cc-cockpit plugins one capped, logged way to call Jev.
- Mismatch: only useful inside cc-cockpit; the dollar cap works on OpenRouter only.

## How it works

`dist/lib/client.js` validates each request, posts it to `<base>/v1/systemone` on TypeSafe, OpenRouter or a custom base URL (`typesafe/jev-1.13` by default) with retries on 429 and 5xx, and counts usage against app-wide caps before answering the calling plugin. Integration evidence: [`dist/lib/client.js`](https://github.com/BronOS/cc-cockpit-jev/blob/e7eff62bcc0f574043e19d16f5502643ee33d585/dist/lib/client.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/BronOS/cc-cockpit-jev
cd cc-cockpit-jev
npm test
ccc jev help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Service API and settings: [github.com/BronOS/cc-cockpit-jev#readme](https://github.com/BronOS/cc-cockpit-jev#readme)

## Limits and data handling

The text other plugins pass is sent to TypeSafe or OpenRouter on your key; the per-project usage log keeps the first 160 characters of each question. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit e7eff62bcc0f](https://github.com/BronOS/cc-cockpit-jev/tree/e7eff62bcc0f574043e19d16f5502643ee33d585). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
