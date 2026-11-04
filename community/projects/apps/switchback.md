# Switchback (Expo mobile app with a browser demo that gives career switchers one technical lesson a day, with Jev choosing and grading each step)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Mobile app (Expo and Supabase) for people moving from business roles into go-to-market engineering, forward deployed and applied AI roles. All lesson content is written in advance, so every AI job in it is a Jev decision: which lesson comes next, which encouragement note fits the day, how well an answer scores against a three-level rubric, how well each synced job fits you, and which expert posts are worth reading. Confidence is shown in the app, and low-confidence grades ask you to compare with a sample answer. Without a key it falls back to simple rules.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/valerievanvu-dev/switchback) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://switchback.valerievu.com) |
| Pricing and access | The browser demo is described as needing no sign-up; the source is MIT and a self-hosted build needs your own Supabase project and TypeSafe key. No app-store or paid plan was verified. Checked 2026-11-04. |
| Jev evidence | [`supabase/functions/_shared/jev.ts`](https://github.com/valerievanvu-dev/switchback/blob/ef544e84f35ce76ad21b8b811c4d765d49b17a90/supabase/functions/_shared/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [valerievanvu-dev](https://github.com/valerievanvu-dev). Independently curated. |
| Format | Expo / React Native app with Supabase edge functions (TypeScript, Deno) |
| Platform and availability | Mobile app built with Expo, plus a browser demo; self-hosting needs your own Supabase project. |
| Jev's role | Chooses the next lesson and note, scores answers against a rubric and ranks jobs and expert posts. |
| Requirements | Node and Expo to run the app; a Supabase project and a `TYPESAFE_API_KEY` stored as a function secret for the Jev decisions. |
| License | [MIT](https://github.com/valerievanvu-dev/switchback/blob/ef544e84f35ce76ad21b8b811c4d765d49b17a90/LICENSE) |

## When to use

- See a complete app where every AI step is a typed decision (choice, score or probability) with visible confidence.
- Mismatch: the daily lessons, job feed and expert library are specific to GTM and applied-AI careers, and the job tracker covers 22 San Francisco companies.

## How it works

`supabase/functions/_shared/jev.ts` posts to `https://api.typesafe.ai/v1/systemone` from edge functions only (the key never ships in the app); the `today`, `grade`, `personalize`, `sync-jobs` and `sync-experts` functions ask choice, score and probability questions and use rules when Jev is unavailable. Integration evidence: [`supabase/functions/_shared/jev.ts`](https://github.com/valerievanvu-dev/switchback/blob/ef544e84f35ce76ad21b8b811c4d765d49b17a90/supabase/functions/_shared/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npx expo start
# backend: create a Supabase project, run the migrations and seed, set TYPESAFE_API_KEY as a function secret
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Browser demo (no sign-up; progress stays on your device): [switchback.valerievu.com](https://switchback.valerievu.com)
- README with the Jev decision table and architecture: [github.com/valerievanvu-dev/switchback#readme](https://github.com/valerievanvu-dev/switchback#readme)

## Limits and data handling

With a key, learner answers and job and post text go to TypeSafe from your Supabase functions. The demo is the maintainer's hosted copy; the review did not test sign-in, sync or grading quality. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit ef544e84f35c](https://github.com/valerievanvu-dev/switchback/tree/ef544e84f35ce76ad21b8b811c4d765d49b17a90). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
