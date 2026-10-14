# @amatelic/jev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Node library and local server for one-line choice/noul/score decisions from small open models, with no API key or cloud call.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/amatelic/jev) |
| Maintainer | [amatelic](https://github.com/amatelic). Independently curated. |
| Format | Node.js library + HTTP server |
| Requirements | Node.js; ARM64 Mac or Linux; models auto-download. |
| License | [MIT](https://github.com/amatelic/jev/blob/bc1902e476bfc70969559acc9b79d497849d491c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/server.ts`](https://github.com/amatelic/jev/blob/bc1902e476bfc70969559acc9b79d497849d491c/src/server.ts) at the pinned commit. |

## When to use

- Prototype Jev-style typed decisions fully offline.
- Mismatch: open small models (not TypeSafe Jev); calibration is the author's claim.

## How it works

`createJev()` loads a local model; `decide()` takes typed questions and returns calibrated answers. The server exposes the same over HTTP. Integration evidence: [`src/server.ts`](https://github.com/amatelic/jev/blob/bc1902e476bfc70969559acc9b79d497849d491c/src/server.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install @amatelic/jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Bench and eval scripts: `bench.mjs`, `eval.mjs`.
- Docs: `docs/`.

## Limits and data handling

Runs locally; model downloads from the configured hub.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit bc1902e476bf](https://github.com/amatelic/jev/tree/bc1902e476bfc70969559acc9b79d497849d491c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
