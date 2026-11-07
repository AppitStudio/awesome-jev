# uzh-demo-library (UZH talk demos: WhichRide/WhichFlight ranked with TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small University of Zurich talk demos: WhichRide ranks real Swiss transport connections with TypeSafe Jev preference questions, and WhichFlight applies similar typed rankings to flight options.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/48Nauts-Operator/UZH-Demo-Library) |
| Maintainer | [48Nauts-Operator](https://github.com/48Nauts-Operator). Independently curated. |
| Format | Node demos (MIT) |
| Requirements | Node.js and a TypeSafe API key for Jev ranking (timetables work without a key). |
| License | [MIT](https://github.com/48Nauts-Operator/UZH-Demo-Library/blob/d901ad1a56b30c33b2a65e5b11508952b34be904/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`WhichRide/server.mjs`](https://github.com/48Nauts-Operator/UZH-Demo-Library/blob/d901ad1a56b30c33b2a65e5b11508952b34be904/WhichRide/server.mjs) at the pinned commit. |

## When to use

- Try classroom demos of Jev preference ranking on real travel data.
- Separate free timetable fetch from keyed Jev ranking.
- Mismatch: teaching demos; not a full travel product.

## How it works

`WhichRide/server.mjs` POSTs to `https://api.typesafe.ai/v1/systemone` with model `jev-1.13.0` and `TYPESAFE_API_KEY` to rank journey options. Integration evidence: [`WhichRide/server.mjs`](https://github.com/48Nauts-Operator/UZH-Demo-Library/blob/d901ad1a56b30c33b2a65e5b11508952b34be904/WhichRide/server.mjs).

## Get started

Clone a demo folder, copy `.env.example`, set TYPESAFE_API_KEY, and start the local server per that folder's README.

```sh
git clone https://github.com/48Nauts-Operator/UZH-Demo-Library.git && cd UZH-Demo-Library/WhichRide
export TYPESAFE_API_KEY=...
# follow WhichRide/README.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/48Nauts-Operator/UZH-Demo-Library/blob/d901ad1a56b30c33b2a65e5b11508952b34be904/README.md](https://github.com/48Nauts-Operator/UZH-Demo-Library/blob/d901ad1a56b30c33b2a65e5b11508952b34be904/README.md)

## Limits and data handling

Journey/flight option text is sent to TypeSafe on your key when ranking is enabled.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit d901ad1a56b3](https://github.com/48Nauts-Operator/UZH-Demo-Library/tree/d901ad1a56b30c33b2a65e5b11508952b34be904). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
