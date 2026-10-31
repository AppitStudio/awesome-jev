# uCable (your YouTube subscriptions as an early-2000s satellite TV guide, with Jev tagging every video)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Web app that takes the last 14 days of videos from your YouTube subscriptions and schedules them into numbered themed channels with a two-screen TV guide; type 1-0-5 to change channel. Jev labels each video with its channel theme, while a plain-code scheduler decides order and remembers where you stopped. Italian UI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hiitsmax/ucable) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/hiitsmax/ucable#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (MIT); you supply Google Cloud credentials and a TypeSafe key. Checked 2026-10-31. |
| Jev evidence | [`lib/jev.ts`](https://github.com/hiitsmax/ucable/blob/b890933a68812fd058eed91b6f330c006d4cc5d1/lib/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [hiitsmax](https://github.com/hiitsmax). Independently curated. |
| Format | Web app (Node 22) |
| Platform and availability | Self-hosted web app in the browser; no hosted instance verified. |
| Jev's role | Tags every recent subscription video with the themed channel it belongs to. |
| Requirements | Node 22.18+, a Google Cloud project with YouTube Data API v3 and OAuth, and a TypeSafe key. |
| License | [MIT](https://github.com/hiitsmax/ucable/blob/b890933a68812fd058eed91b6f330c006d4cc5d1/LICENSE) |

## When to use

- Turn a subscription feed into lean-back themed channels.
- Mismatch: Jev only tags videos; scheduling is deterministic code.

## How it works

`lib/jev.ts` posts video metadata to `api.typesafe.ai/v1/systemone` with the question prompts from `prompts.json` and maps the answers to channel tags. Integration evidence: [`lib/jev.ts`](https://github.com/hiitsmax/ucable/blob/b890933a68812fd058eed91b6f330c006d4cc5d1/lib/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/hiitsmax/ucable.git && cd ucable
npm install
npm start   # after filling .env.local (Google OAuth + TYPESAFE_API_KEY)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Italian): [github.com/hiitsmax/ucable#readme](https://github.com/hiitsmax/ucable#readme)

## Limits and data handling

Video titles and descriptions from your subscriptions go to TypeSafe; Google OAuth grants read access to your subscriptions. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit b890933a6881](https://github.com/hiitsmax/ucable/tree/b890933a68812fd058eed91b6f330c006d4cc5d1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
