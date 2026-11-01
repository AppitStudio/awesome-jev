# Mimir (self-hosted news reader that ranks RSS feeds against your interests and groups stories with Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted news reader: collect any number of RSS and Atom feeds, describe your interests in plain words, and Mimir scores every article against them and groups articles about the same event into one story with a timeline. Jev does the scoring and story matching; on-demand sourced briefs are written by a MiniMax model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sp1r1t/mimir) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/sp1r1t/mimir#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (MIT); you supply TypeSafe and optional MiniMax keys. Checked 2026-11-01. |
| Jev evidence | [`src/classification/jev.ts`](https://github.com/sp1r1t/mimir/blob/60c65db891d7ae9e138be8796dd4b820b842f836/src/classification/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [sp1r1t](https://github.com/sp1r1t). Independently curated. |
| Format | Web app (Docker Compose) |
| Platform and availability | Self-hosted web app in the browser; no hosted instance verified. |
| Jev's role | Scores articles against your profile and matches articles into stories. |
| Requirements | Docker; a TypeSafe key for ranking and stories; optional MiniMax plan for briefs. |
| License | [MIT](https://github.com/sp1r1t/mimir/blob/60c65db891d7ae9e138be8796dd4b820b842f836/LICENSE) |

## When to use

- Read hundreds of articles a day ranked by your own profile without a per-article LLM bill.
- Mismatch: briefs need a separate MiniMax subscription.

## How it works

`src/classification/jev.ts` uses `@typesafe-ai/sdk` to score each article against your profile, and `src/stories/matcher.ts` asks Jev whether a new article reports the same event as an existing story. Integration evidence: [`src/classification/jev.ts`](https://github.com/sp1r1t/mimir/blob/60c65db891d7ae9e138be8796dd4b820b842f836/src/classification/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/sp1r1t/mimir.git && cd mimir
docker compose up -d --build
# add TYPESAFE_API_KEY to .env, then docker compose up -d
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/sp1r1t/mimir#readme](https://github.com/sp1r1t/mimir#readme)

## Limits and data handling

Article titles and text are sent to TypeSafe (and MiniMax for briefs). Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 60c65db891d7](https://github.com/sp1r1t/mimir/tree/60c65db891d7ae9e138be8796dd4b820b842f836). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
