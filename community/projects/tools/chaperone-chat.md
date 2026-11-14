# chaperone-chat (anonymous in-app chat that keeps phone numbers and emails out: deterministic rules first, then Jev reads every message)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

npm package for platforms where buyers and sellers, matches, recruiters or renters should talk anonymously until something is agreed: participants see only aliases, and every message passes deterministic contact-detail rules and then a Jev check in context (including details spelled out or split across messages, English and Spanish) before anyone sees it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HypnoLabs-io/chaperone-chat) |
| Maintainer | [HypnoLabs-io](https://github.com/HypnoLabs-io). Independently curated. |
| Format | TypeScript npm package with React components, CLI and demo server (MIT) |
| Requirements | Node.js and npm; a store (Postgres supported); `TYPESAFE_API_KEY` turns Jev on, otherwise only the rules run. |
| License | [MIT](https://github.com/HypnoLabs-io/chaperone-chat/blob/ca9f3d0ad76781a2b0464f3be296016f6d4350d5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/client.ts`](https://github.com/HypnoLabs-io/chaperone-chat/blob/ca9f3d0ad76781a2b0464f3be296016f6d4350d5/src/jev/client.ts) at the pinned commit. |

## When to use

- Keep marketplace or matching conversations on-platform by screening contact details before delivery.
- Mismatch: end-to-end encrypted chat; the server must read every message to screen it.

## How it works

`src/jev/client.ts` posts to `https://api.typesafe.ai/v1/systemone` with `jev-1.13.0` as the default model; the demo server only enables Jev when `TYPESAFE_API_KEY` is set. A `calibrate` CLI scores the shipped labelled corpus. Integration evidence: [`src/jev/client.ts`](https://github.com/HypnoLabs-io/chaperone-chat/blob/ca9f3d0ad76781a2b0464f3be296016f6d4350d5/src/jev/client.ts).

## Get started

Install the package, then follow the install guide or run the demo server.

```sh
npm install chaperone-chat
# demo from a checkout:
git clone https://github.com/HypnoLabs-io/chaperone-chat && cd chaperone-chat && npm ci
TYPESAFE_API_KEY=... node examples/demo/server.mjs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/HypnoLabs-io/chaperone-chat/blob/ca9f3d0ad76781a2b0464f3be296016f6d4350d5/README.md](https://github.com/HypnoLabs-io/chaperone-chat/blob/ca9f3d0ad76781a2b0464f3be296016f6d4350d5/README.md)
- Install guide: [github.com/HypnoLabs-io/chaperone-chat/blob/ca9f3d0ad76781a2b0464f3be296016f6d4350d5/docs/install.md](https://github.com/HypnoLabs-io/chaperone-chat/blob/ca9f3d0ad76781a2b0464f3be296016f6d4350d5/docs/install.md)

## Limits and data handling

With Jev enabled, every message text is sent to TypeSafe on your key. The maintainers report results on 595 bundled labelled messages; that corpus is their own test set, not an independent benchmark. Version 0.1.0.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit ca9f3d0ad767](https://github.com/HypnoLabs-io/chaperone-chat/tree/ca9f3d0ad76781a2b0464f3be296016f6d4350d5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
