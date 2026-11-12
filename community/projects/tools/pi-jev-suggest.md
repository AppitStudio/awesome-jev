# pi-jev-suggest (Pi extension that suggests your next request, with Jev choosing the intent)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension that, when a run ends, asks Jev which kind of request you are likely to type next (one of twelve built-in tags such as continue, plan, verify or simplify, plus your own) and offers a reply from that tag's pool under the editor; nothing is sent for you.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/luw2007/pi-jev-suggest) |
| Maintainer | [luw2007](https://github.com/luw2007). Independently curated. |
| Format | Pi extension installed from GitHub (TypeScript, MIT; README in English and Chinese) |
| Requirements | Pi and `TYPESAFE_API_KEY` (endpoint and model configurable in `jev-suggest.json`). |
| License | [MIT](https://github.com/luw2007/pi-jev-suggest/blob/11e3981d3f1d4427fdbab766cb5b3e1b2dd5478f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/config.ts`](https://github.com/luw2007/pi-jev-suggest/blob/11e3981d3f1d4427fdbab766cb5b3e1b2dd5478f/src/config.ts) at the pinned commit. |

## When to use

- Get a one-key suggestion for the next prompt in a Pi session.
- Mismatch: Pi only; suggestions come from fixed reply pools.

## How it works

`src/config.ts` defaults to `https://api.typesafe.ai/v1/systemone` with model `jev-1.13.0`; Jev makes one closed-set choice of tag and never writes the reply text. Integration evidence: [`src/config.ts`](https://github.com/luw2007/pi-jev-suggest/blob/11e3981d3f1d4427fdbab766cb5b3e1b2dd5478f/src/config.ts).

## Get started

Install the extension in Pi and set your TypeSafe key; optionally add tags and replies in `jev-suggest.json`.

```sh
pi install git:github.com/luw2007/pi-jev-suggest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/luw2007/pi-jev-suggest/blob/11e3981d3f1d4427fdbab766cb5b3e1b2dd5478f/README.md](https://github.com/luw2007/pi-jev-suggest/blob/11e3981d3f1d4427fdbab766cb5b3e1b2dd5478f/README.md)

## Limits and data handling

Recent run state is sent to TypeSafe on your key after each run.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 11e3981d3f1d](https://github.com/luw2007/pi-jev-suggest/tree/11e3981d3f1d4427fdbab766cb5b3e1b2dd5478f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
