# JEV City

[All projects](../README.md) · [Web apps](README.md#web-apps)

Illustrated isometric city simulation where every citizen decision (routine, shelter, help, restore power…) comes from TypeSafe Jev, with the full choice distribution shown on click.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/WilliamJones/JEV-City) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/WilliamJones/JEV-City#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-15. |
| Jev evidence | [`src/jev/client.ts`](https://github.com/WilliamJones/JEV-City/blob/b5c7ddfee26e6f004314a545ddf7f85acd9fc76d/src/jev/client.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [WilliamJones](https://github.com/WilliamJones). Independently curated. |
| Format | Web app (TypeScript, Vite) |
| Platform and availability | Web (local source build) |
| Jev's role | Jev chooses each citizen's next action; the simulation executes it. |
| Requirements | Node.js; TypeSafe API key for live mode (recorded mode without one). |
| License | [MIT](https://github.com/WilliamJones/JEV-City/blob/b5c7ddfee26e6f004314a545ddf7f85acd9fc76d/LICENSE) |

## When to use

- Watch a decision model drive many agents through scenarios like blackouts, fires and floods.
- Inspect each Jev response: choice distribution, rubric scores, yes/no probability and latency.
- Mismatch: a demo simulation, not a planning tool.

## How it works

For each citizen decision the app sends their state to Jev (`jev-1.13.0`) with a choice question plus scores; deterministic simulation code applies the chosen action. Recorded responses allow offline replay. Integration evidence: [`src/jev/client.ts`](https://github.com/WilliamJones/JEV-City/blob/b5c7ddfee26e6f004314a545ddf7f85acd9fc76d/src/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
cp .env.example .env.local
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Eight scenarios described in the upstream README.

## Limits and data handling

In live mode citizen states go to TypeSafe and are billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit b5c7ddfee26e](https://github.com/WilliamJones/JEV-City/tree/b5c7ddfee26e6f004314a545ddf7f85acd9fc76d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
