# WhatsApp Inbox (local WhatsApp conversation inbox classified by TypeSafe Jev)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Lightweight local inbox for managing WhatsApp conversations by status and label, with the main label suggested by TypeSafe Jev via `@typesafe-ai/sdk`; runs on your PC without Docker.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Betinhos-Executive-Service/whatsapp-inbox) |
| Maintainer | [Betinhos-Executive-Service](https://github.com/Betinhos-Executive-Service). Independently curated. |
| Format | Node.js local app (no SPDX license file on the reviewed commit) |
| Requirements | Node.js, pnpm, a WhatsApp account, and a TypeSafe API key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/jev.ts`](https://github.com/Betinhos-Executive-Service/whatsapp-inbox/blob/8eec8ddc86f085f672bf7a75340d188129a3928b/server/jev.ts) at the pinned commit. |

## When to use

- Triage business WhatsApp conversations by label and status.
- Keep the inbox local without external databases.
- Mismatch: Portuguese docs; unofficial WhatsApp client; no OSI license on the reviewed commit.

## How it works

`server/jev.ts` uses `TypeSafeClient` with `choice`/`noul` to classify conversations into editable labels. Integration evidence: [`server/jev.ts`](https://github.com/Betinhos-Executive-Service/whatsapp-inbox/blob/8eec8ddc86f085f672bf7a75340d188129a3928b/server/jev.ts).

## Get started

Clone, install with pnpm, set the TypeSafe key, and pair WhatsApp per README.

```sh
git clone https://github.com/Betinhos-Executive-Service/whatsapp-inbox.git && cd whatsapp-inbox
export TYPESAFE_API_KEY=...
pnpm i && pnpm dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Betinhos-Executive-Service/whatsapp-inbox/blob/8eec8ddc86f085f672bf7a75340d188129a3928b/README.md](https://github.com/Betinhos-Executive-Service/whatsapp-inbox/blob/8eec8ddc86f085f672bf7a75340d188129a3928b/README.md)

## Limits and data handling

Message text is sent to TypeSafe on your key; follow WhatsApp terms.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 8eec8ddc86f0](https://github.com/Betinhos-Executive-Service/whatsapp-inbox/tree/8eec8ddc86f085f672bf7a75340d188129a3928b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
