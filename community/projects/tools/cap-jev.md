# cap-jev (SAP CAP plugin)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Plugin for SAP CAP Node.js applications that adds an internal `system-one` service for choice, score and yes/no questions against one text or JSON state, defaulting to TypeSafe Jev and working with other Jev-compatible System One endpoints.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hendrik77/cap-jev) |
| Maintainer | [hendrik77](https://github.com/hendrik77). Independently curated. |
| Format | SAP CAP plugin (TypeScript, Node.js 22+) |
| Requirements | SAP CAP Node.js 10 on Node.js 22 or newer; a Jev API token (or another System One endpoint). Not on npm yet; install from a packed tarball. |
| License | [MIT](https://github.com/hendrik77/cap-jev/blob/1ca4d34b4b0b3ddc3121fe9f692da920b2cc43c2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/transport.ts`](https://github.com/hendrik77/cap-jev/blob/1ca4d34b4b0b3ddc3121fe9f692da920b2cc43c2/src/transport.ts) at the pinned commit. |

## When to use

- Add routing, urgency scoring or yes/no checks to a CAP service handler.
- Keep the decision endpoint configurable per environment.
- Mismatch: CAP Node.js only; package not yet published to npm.

## How it works

CAP loads `cds-plugin.js` and registers the `system-one` required service. Handlers call `systemOne.decide({state, questions})`, and `src/transport.ts` posts the request to the configured endpoint, with built-in defaults of `https://api.typesafe.ai/v1/systemone`, `jev-latest` and a 10-second timeout. Integration evidence: [`src/transport.ts`](https://github.com/hendrik77/cap-jev/blob/1ca4d34b4b0b3ddc3121fe9f692da920b2cc43c2/src/transport.ts).

## Get started

From the upstream README: pack the plugin, install the tarball in your CAP app, then configure `cds.requires.system-one.credentials`.

```sh
git clone https://github.com/hendrik77/cap-jev && cd cap-jev
npm install && npm pack
# in your CAP application:
npm install /path/to/cap-jev/cap-jev-0.1.0.tgz
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- examples/cap-app (TypeScript action handler)

## Limits and data handling

State text goes to the configured endpoint. Store the token in a runtime binding, not source control.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 1ca4d34b4b0b](https://github.com/hendrik77/cap-jev/tree/1ca4d34b4b0b3ddc3121fe9f692da920b2cc43c2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
