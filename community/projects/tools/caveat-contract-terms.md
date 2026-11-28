# Caveat by Ololadestephen (Fly.io Sprites agent where Jev reads contract payment terms and a cash-flow model stress-tests them)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hacksgiving 2026 agent for consultants: it reads contract documents from Box, has Jev make typed decisions about payment terms (net days, milestones, monthly fees), and stress-tests those readings against a deterministic cash-flow model on two isolated worker Sprites. Every run ends in a receipt a human must approve; the only export is a draft counteroffer note, never sent and not legal advice. Demo uses public SEC EDGAR exhibits.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ololadestephen/caveat) |
| Maintainer | [Ololadestephen](https://github.com/Ololadestephen). Independently curated. |
| Format | TypeScript (Node.js 24) agent on Fly.io Sprites |
| Requirements | Node.js 24, npm 11 and, for live runs, Fly.io Sprites with Box, TypeSafeAI and OpenRouter connectors. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/interpret/jev.ts`](https://github.com/Ololadestephen/caveat/blob/ef6f2baf4e17869c25fcda54902c31a931e1ffb2/src/interpret/jev.ts) at the pinned commit. |

## When to use

- Freelancers and small firms who want a second look at payment terms before signing.
- Mismatch: legal advice; the output is a draft note for a human.

## How it works

`src/interpret/jev.ts` sends contract clauses and typed questions to Jev (`jev-1.14.0`) through the TypeSafeAI Sprites connector; the cash runner and review pages show which decisions came from Jev. Integration evidence: [`src/interpret/jev.ts`](https://github.com/Ololadestephen/caveat/blob/ef6f2baf4e17869c25fcda54902c31a931e1ffb2/src/interpret/jev.ts).

## Get started

Install and run the local checks and a cash-runner fixture.

```sh
git clone https://github.com/Ololadestephen/caveat && cd caveat
npm install
npm run check
npm run fixture -- fixtures/runner/<name>.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo video: [youtu.be/tmyJL_PotMQ](https://youtu.be/tmyJL_PotMQ)

## Limits and data handling

Contract text goes to TypeSafe and OpenRouter (a free, sometimes slow model for extraction). Read-only towards Box. No licence file, so no reuse rights are granted.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit ef6f2baf4e17](https://github.com/Ololadestephen/caveat/tree/ef6f2baf4e17869c25fcda54902c31a931e1ffb2). Inspected the README and `src/interpret/jev.ts` at the pinned commit; no licence file present. Not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
