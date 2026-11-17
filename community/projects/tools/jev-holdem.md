# Jev Hold'em by lawsirlawsir-png (heads-up no-limit Texas hold'em against Jev, answering typed questions that code turns into bets)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Browser game of heads-up no-limit Texas hold'em against Jev. A local engine deals, ranks hands, computes pot odds and enforces legal actions; on Jev's turn the page sends one request with the table state and nine typed questions (made-hand strength, draw equity, board danger, fold to price, value bet, bluff, trap, line, bet size). A policy layer uses the Choice answer when it is confident and otherwise composes the Score and Noul answers into fold, check, call, bet, raise or all-in. If the API is unavailable, a heuristic keeps the hand going. Mobile-first table; English and Chinese READMEs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lawsirlawsir-png/jev-holdem) |
| Maintainer | [lawsirlawsir-png](https://github.com/lawsirlawsir-png). Independently curated. |
| Format | Static web game with an edge function for EdgeOne Pages (JavaScript; no license file) |
| Requirements | An EdgeOne Pages deployment with EdgeOne Makers Models, which supplies the `@makers/jev` model. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`edge-functions/typesafe/holdem.js`](https://github.com/lawsirlawsir-png/jev-holdem/blob/26c96590035130c1da6f6f58d62e3ded7df16914/edge-functions/typesafe/holdem.js) at the pinned commit. |

## When to use

- Play poker against Jev and see how typed answers become a betting line.
- Mismatch: poker training with solver-grade strategy; it is a demo of Jev as an opponent.

## How it works

`edge-functions/typesafe/holdem.js` defines the questions and sends the System One request with model `@makers/jev`, served by EdgeOne Makers Models; the frontend's only model call is `POST /typesafe/v1/systemone`, and `src/jev/policy.js` maps the answers onto legal actions. Integration evidence: [`edge-functions/typesafe/holdem.js`](https://github.com/lawsirlawsir-png/jev-holdem/blob/26c96590035130c1da6f6f58d62e3ded7df16914/edge-functions/typesafe/holdem.js).

## Get started

Deploy the template to EdgeOne Pages and open the page to start a match.

```sh
git clone https://github.com/lawsirlawsir-png/jev-holdem && cd jev-holdem
# deploy with EdgeOne Pages (README 'Deploy' button); EdgeOne Makers Models provides @makers/jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/lawsirlawsir-png/jev-holdem/blob/26c96590035130c1da6f6f58d62e3ded7df16914/README.md](https://github.com/lawsirlawsir-png/jev-holdem/blob/26c96590035130c1da6f6f58d62e3ded7df16914/README.md)

## Limits and data handling

Table state goes to the Jev model served through EdgeOne Makers Models on the deployer's account; pricing and terms are EdgeOne's. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 26c965900351](https://github.com/lawsirlawsir-png/jev-holdem/tree/26c96590035130c1da6f6f58d62e3ded7df16914). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
