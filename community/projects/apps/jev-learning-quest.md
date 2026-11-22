# Jev Learning Quest (Japanese study app where Jev picks today's quest and judges whether you need a review)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Choose how much time you have and your mood, and Jev picks one study quest; after you answer and self-assess, Jev judges your understanding and whether the item needs review. Content covers the Japanese Network Specialist and Registered Information Security Specialist exams plus AWS and GCP certification flashcards. UI and most docs are in Japanese, with an English README.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/moruku36/jev-learning-quest) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/moruku36/jev-learning-quest#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build: run locally with `npm start` or self-deploy to Vercel and Supabase with your own Jev key. The author's live deployment needs a GitHub login on an allowlist, so it is not open to the public. No license file, so reuse terms are not granted. Checked 2026-11-22. |
| Jev evidence | [`lib/quest-engine.js`](https://github.com/moruku36/jev-learning-quest/blob/5032bb3bddff1f5a04425174f0373b314b4adfa4/lib/quest-engine.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [moruku36](https://github.com/moruku36). Independently curated. |
| Format | Node.js web app |
| Platform and availability | Web: local Node server on 127.0.0.1, or self-hosted on Vercel + Supabase. |
| Jev's role | Picks one quest from your time and mood, then judges understanding and the need for review after each answer. |
| Requirements | Node.js and a Jev API key (`JEV_API_KEY`); Vercel and Supabase only for the cloud version. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Japanese-language exam prep where an AI chooses one short task per session and schedules reviews.
- Mismatch: non-Japanese learners; most content and the full guide are in Japanese.

## How it works

`lib/quest-engine.js` posts to `https://api.typesafe.ai/v1/systemone` (overridable with `JEV_API_URL`) with model `jev-latest` for quest selection and understanding checks; the local version stores progress in `data/store.json`. Integration evidence: [`lib/quest-engine.js`](https://github.com/moruku36/jev-learning-quest/blob/5032bb3bddff1f5a04425174f0373b314b4adfa4/lib/quest-engine.js).

## Get started

Run the local version, which listens only on 127.0.0.1; the Japanese README covers cloud setup.

```sh
git clone https://github.com/moruku36/jev-learning-quest && cd jev-learning-quest
export JEV_API_KEY=...
npm install
npm start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Architecture diagrams: [github.com/moruku36/jev-learning-quest/blob/5032bb3bddff1f5a04425174f0373b314b4adfa4/docs/architecture.md](https://github.com/moruku36/jev-learning-quest/blob/5032bb3bddff1f5a04425174f0373b314b4adfa4/docs/architecture.md)
- Japanese README: [github.com/moruku36/jev-learning-quest/blob/5032bb3bddff1f5a04425174f0373b314b4adfa4/README.ja.md](https://github.com/moruku36/jev-learning-quest/blob/5032bb3bddff1f5a04425174f0373b314b4adfa4/README.ja.md)

## Limits and data handling

Your choices, answers and self-assessments are sent to TypeSafe for each decision. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 5032bb3bddff](https://github.com/moruku36/jev-learning-quest/tree/5032bb3bddff1f5a04425174f0373b314b4adfa4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
