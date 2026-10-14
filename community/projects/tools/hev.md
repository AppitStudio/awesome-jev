# Hev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Working Jev-compatible Decisions API answered by human visitors on a live page; swap the Jev base URL to test an integration against human answers (not for production).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/luisrudge/hev) |
| Maintainer | [luisrudge](https://github.com/luisrudge). Independently curated. |
| Format | Hosted API + Cloudflare Worker source (TypeScript) |
| Requirements | None for the hosted endpoint; Cloudflare account with Workers AI to self-host. |
| License | [MIT](https://github.com/luisrudge/hev/blob/8faa5faa176c5bbfb8d2e7ca2121d2d25e1266cd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/luisrudge/status/2110071251255656754)). |
| Jev evidence | [`worker/index.ts`](https://github.com/luisrudge/hev/blob/8faa5faa176c5bbfb8d2e7ca2121d2d25e1266cd/worker/index.ts) at the pinned commit. |

## When to use

- Smoke-test a Jev client end-to-end with a human answering, or demo typed decisions live.
- Mismatch: explicitly not for production; latency is however long a stranger takes; no accounts.

## How it works

`POST /v1/systemone` puts the question in a live feed; a visitor clicks an answer and the request returns in Clef's response format. Cloudflare `clef-flash` screens questions before they reach the feed. Integration evidence: [`worker/index.ts`](https://github.com/luisrudge/hev/blob/8faa5faa176c5bbfb8d2e7ca2121d2d25e1266cd/worker/index.ts).

## Get started

From the upstream README (not run on the review host):

```sh
curl https://usehev.com/v1/systemone -d '{"model":"hev","state":"…","questions":{"q":{"type":"noul","instructions":"…"}}}'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live site: [usehev.com/](https://usehev.com/) (checked 2026-10-14).
- Worker: `worker/index.ts`.

## Limits and data handling

Questions you send are shown publicly to strangers — never send private data. Decided questions are deleted after 24h (per README).

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 8faa5faa176c](https://github.com/luisrudge/hev/tree/8faa5faa176c5bbfb8d2e7ca2121d2d25e1266cd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
