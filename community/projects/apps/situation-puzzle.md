# Jev Situation Puzzle

[All projects](../README.md) · [Web apps](README.md#web-apps)

Lateral-thinking puzzle game where TypeSafe Jev answers yes / no / irrelevant and judges story reconstructs (English and Chinese).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ZeroTang05/Situation-Puzzle) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [puzzle.xiaobaozi.cn](https://puzzle.xiaobaozi.cn/?lang=en) |
| Pricing and access | Free public demo and GPL-3.0 source; Jev calls billed to the operator's TypeSafe key. Checked 2026-10-13. |
| Jev evidence | [`lib/jev.ts`](https://github.com/ZeroTang05/Situation-Puzzle/blob/ce27da4429185d0babf492af7d46456edc297622/lib/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [ZeroTang05](https://github.com/ZeroTang05). Independently curated. |
| Format | Web app (TypeScript) |
| Platform and availability | Hosted demo or self-host from source |
| Jev's role | Jev answers yes/no/irrelevant and judges reconstructed stories; UGC puzzles supported. |
| Requirements | TypeSafe API key for self-host; none to try the public demo. |
| License | [GPL-3.0](https://github.com/ZeroTang05/Situation-Puzzle/blob/ce27da4429185d0babf492af7d46456edc297622/LICENSE) |

## When to use

- Play or host a 海龟汤 / situation puzzle where the referee is Jev, not a script.
- Mismatch: Hosted demo availability and keys are operator-controlled.

## How it works

Questions and reconstructs go to Jev typed decisions; the UI presents the host answers. (Summarized from the upstream [README](https://github.com/ZeroTang05/Situation-Puzzle/blob/ce27da4429185d0babf492af7d46456edc297622/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): open the hosted demo, or clone, set a TypeSafe key, and run the web app.

## Limits and data handling

Puzzle questions and guesses go to TypeSafe on the host that holds the key. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit ce27da442918](https://github.com/ZeroTang05/Situation-Puzzle/tree/ce27da4429185d0babf492af7d46456edc297622). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
