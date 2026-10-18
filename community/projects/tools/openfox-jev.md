# openfox-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenFox plugin: deterministic policy plus a System One approval reviewer (TypeSafe Jev or a local Jev-style `/v1/systemone` server) for tool/approval decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/adriy-be/openfox-jev) |
| Maintainer | [adriy-be](https://github.com/adriy-be). Independently curated. |
| Format | JavaScript OpenFox plugin |
| Requirements | OpenFox; TypeSafe key or local System One endpoint. |
| License | [MIT](https://github.com/adriy-be/openfox-jev/blob/4bd10768909e3619e3145baca7e3d117577b53f6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/providers.js`](https://github.com/adriy-be/openfox-jev/blob/4bd10768909e3619e3145baca7e3d117577b53f6/src/providers.js) at the pinned commit. |

## When to use

- Add a Jev approval reviewer beside deterministic OpenFox policy.
- Need to point at either TypeSafe or a loopback System One server.
- Mismatch: OpenFox plugin; not a standalone app.

## How it works

`src/providers.js` resolves endpoints to `/v1/systemone` (including local `127.0.0.1:8765`) and routes approval questions through that wire format. Integration evidence: [`src/providers.js`](https://github.com/adriy-be/openfox-jev/blob/4bd10768909e3619e3145baca7e3d117577b53f6/src/providers.js).

## Get started

Install the plugin into OpenFox and configure the provider endpoint and key.

```sh
git clone https://github.com/adriy-be/openfox-jev && cd openfox-jev
# wire into OpenFox per README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README plugin description
- src/providers.js endpoint resolution

## Limits and data handling

Depends on OpenFox. Local servers are only as trustworthy as their host.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 4bd10768909e](https://github.com/adriy-be/openfox-jev/tree/4bd10768909e3619e3145baca7e3d117577b53f6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
