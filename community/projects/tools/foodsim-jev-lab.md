# FoodSim Jev Lab (browser benchmark of Jev on simulated support-ticket sorting)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Plain-HTML simulation project whose Jev Lab page benchmarks Jev deciding ticket category, urgency and escalation against hand-written gold labels, via a small server-side proxy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nomarcus/FoodSim) |
| Maintainer | [Nomarcus](https://github.com/Nomarcus). Independently curated. |
| Format | Static HTML/JS pages plus a serverless proxy (source only) |
| Requirements | A browser, and a deployment with `TYPESAFE_API_KEY` set for the `api/typesafe.js` proxy. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`api/typesafe.js`](https://github.com/Nomarcus/FoodSim/blob/cf55af7d837b90f62ed2f807e98efde587298455/api/typesafe.js) at the pinned commit. |

## When to use

- Watch Jev classify simulated support tickets against known answers.
- Borrow the proxy pattern for calling Jev from a static site.
- Mismatch: hobby project with no license file (source-available, not open source); the rest of the repo is unrelated browser games.

## How it works

`api/typesafe.js` forwards System One request bodies to `api.typesafe.ai/v1/systemone` (`jev-latest` default) so the key stays server-side; `typesafe-tickets.js` keeps gold, predicted and displayed categories apart so the classifier is scored honestly in `jev-lab.html`. Integration evidence: [`api/typesafe.js`](https://github.com/Nomarcus/FoodSim/blob/cf55af7d837b90f62ed2f807e98efde587298455/api/typesafe.js).

## Get started

Deploy the repo with `TYPESAFE_API_KEY` set, then open `jev-lab.html`.

```sh
git clone https://github.com/Nomarcus/FoodSim.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev Lab page: [github.com/Nomarcus/FoodSim/blob/cf55af7d837b90f62ed2f807e98efde587298455/jev-lab.html](https://github.com/Nomarcus/FoodSim/blob/cf55af7d837b90f62ed2f807e98efde587298455/jev-lab.html)

## Limits and data handling

Ticket text goes to TypeSafe on the deployer's key; redeploy after changing the key.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit cf55af7d837b](https://github.com/Nomarcus/FoodSim/tree/cf55af7d837b90f62ed2f807e98efde587298455). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
