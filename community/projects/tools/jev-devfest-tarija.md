# Taller Jev DevFest Tarija by Kevin Guzman (Spanish workshop: spam filter, message triage and incident prioritiser with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Starter project for a DevFest Tarija workshop (Spanish): the NestJS backend and React UI are done, and attendees write only the Jev questions and decision logic in three services: a spam detector (`noul` plus threshold), message triage (`choice` plus two `score` questions in one call) and an incident prioritiser (`choice`, `score` and `noul`). Reference solutions are included.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Kevinho71/Jev-Devfest-Tarija) |
| Maintainer | [Kevin Guzman](https://github.com/Kevinho71) (Kevinho71). Independently curated. |
| Format | NestJS + React workshop repo |
| Requirements | Node.js 22+ and a TypeSafe API key. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`soluciones/spam.service.ts`](https://github.com/Kevinho71/Jev-Devfest-Tarija/blob/82bf1e9681735441023ce9e618152fd168698db4/soluciones/spam.service.ts) at the pinned commit. |

## When to use

- Spanish-speaking developers or meetup hosts looking for a hands-on first Jev session.
- Mismatch: production spam or ticket handling.

## How it works

`backend/src/jev/jev.service.ts` holds an `@typesafe-ai/sdk` client; the exercises call `client.systemOne` with typed questions, and `soluciones/spam.service.ts` and the other solution files show the finished versions. Integration evidence: [`soluciones/spam.service.ts`](https://github.com/Kevinho71/Jev-Devfest-Tarija/blob/82bf1e9681735441023ce9e618152fd168698db4/soluciones/spam.service.ts).

## Get started

Install, add your key and start both apps; unfinished exercises show "Ejercicio pendiente".

```sh
git clone https://github.com/Kevinho71/Jev-Devfest-Tarija && cd Jev-Devfest-Tarija
npm install && cp backend/.env.example backend/.env   # TYPESAFE_API_KEY=...
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Reference solutions: [github.com/Kevinho71/Jev-Devfest-Tarija/tree/main/soluciones](https://github.com/Kevinho71/Jev-Devfest-Tarija/tree/main/soluciones)

## Limits and data handling

Workshop material; message text from the exercises goes to TypeSafe. No licence file, so no reuse rights are granted.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 82bf1e968173](https://github.com/Kevinho71/Jev-Devfest-Tarija/tree/82bf1e9681735441023ce9e618152fd168698db4). Inspected the README, `jev.service.ts` and the solution files at the pinned commit; no licence file present. Not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
