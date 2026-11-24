# Jev Question Lab by alphastack (local browser demo for asking Jev Noul, Choice, Score and Box questions and inspecting the API request and response)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A small local web app with built-in cases for each Jev primitive (Noul, Choice, Score and Box). Edit the input or question, run it, and see the typed answer, probabilities and the exact request and response sent to TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alphastack1/TS-PRIMITIVES-DEMO) |
| Maintainer | [alphastack1](https://github.com/alphastack1). Independently curated. |
| Format | Node.js local web app (no dependencies) |
| Requirements | Node.js 22+ and a TypeSafe API key in `.env` (`TYPESAFE_API_KEY`). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server.cjs`](https://github.com/alphastack1/TS-PRIMITIVES-DEMO/blob/6dc0bb42619324a25e5ddea4db231a156deec3c9/server.cjs) at the pinned commit. |

## When to use

- Learn how Jev's four primitives behave and how wording changes the returned probabilities.
- Mismatch: production integrations; this is a teaching demo.

## How it works

`server.cjs` keeps the key server-side and forwards each request to `https://api.typesafe.ai/v1/systemone`; `lab.js` holds the cases, builds the requests and draws the four result types. Integration evidence: [`server.cjs`](https://github.com/alphastack1/TS-PRIMITIVES-DEMO/blob/6dc0bb42619324a25e5ddea4db231a156deec3c9/server.cjs).

## Get started

Clone, add your key to `.env`, and start the local server (on Windows, `Launch Question Lab.cmd`).

```sh
git clone https://github.com/alphastack1/TS-PRIMITIVES-DEMO.git && cd TS-PRIMITIVES-DEMO
echo 'TYPESAFE_API_KEY=your_key_here' > .env
node server.cjs   # http://127.0.0.1:48176
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with screenshot: [github.com/alphastack1/TS-PRIMITIVES-DEMO/blob/6dc0bb42619324a25e5ddea4db231a156deec3c9/README.md](https://github.com/alphastack1/TS-PRIMITIVES-DEMO/blob/6dc0bb42619324a25e5ddea4db231a156deec3c9/README.md)
- Cases: [github.com/alphastack1/TS-PRIMITIVES-DEMO/blob/6dc0bb42619324a25e5ddea4db231a156deec3c9/lab.js](https://github.com/alphastack1/TS-PRIMITIVES-DEMO/blob/6dc0bb42619324a25e5ddea4db231a156deec3c9/lab.js)

## Limits and data handling

Inputs, questions and images you run are sent to TypeSafe and billed to your key. No license file, so no reuse terms are granted.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 6dc0bb426193](https://github.com/alphastack1/TS-PRIMITIVES-DEMO/tree/6dc0bb42619324a25e5ddea4db231a156deec3c9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
