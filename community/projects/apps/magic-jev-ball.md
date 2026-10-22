# Magic Jev Ball

[All projects](../README.md) · [Web apps](README.md#web-apps)

Magic 8 Ball in the browser that doesn't pick at random: hold it, shake it, let go, and Jev picks which of the 20 classic answers fits your question, with a probability for every answer shown under the ball.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mikecann/magic-jev-ball) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://magic-jev.mikecann.app) |
| Pricing and access | Free to use on the live site; self-hosting needs a paid Convex plan for the AI Gateway. Checked 2026-10-22. |
| Jev evidence | [`convex/jev.ts`](https://github.com/mikecann/magic-jev-ball/blob/36e311432fc63d6c4dd51b46d9205d150c8e4b4f/convex/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [mikecann](https://github.com/mikecann). Independently curated. |
| Format | Web app (three.js, Convex) |
| Platform and availability | Web, live at magic-jev.mikecann.app. |
| Jev's role | Jev chooses the answer among the 20 classic options and returns their probabilities. |
| Requirements | A browser for the live site; to self-host, a Convex project on a paid plan (the AI Gateway is a paid feature). |
| License | [MIT](https://github.com/mikecann/magic-jev-ball/blob/36e311432fc63d6c4dd51b46d9205d150c8e4b4f/LICENSE) |

## When to use

- Show Jev's choice probabilities in a playful, visual demo.
- Use as a small reference for calling Jev through the Convex AI Gateway.
- Mismatch: a toy; answers are for fun.

## How it works

`convex/jev.ts` is one Convex action that sends your question with the 20 answers to `typesafe/jev-1.13` through the Convex AI Gateway, so no model keys are managed in the app. Integration evidence: [`convex/jev.ts`](https://github.com/mikecann/magic-jev-ball/blob/36e311432fc63d6c4dd51b46d9205d150c8e4b4f/convex/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npx convex dev
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live site: [magic-jev.mikecann.app](https://magic-jev.mikecann.app)

## Limits and data handling

Questions are sent to Convex and TypeSafe.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 36e311432fc6](https://github.com/mikecann/magic-jev-ball/tree/36e311432fc63d6c4dd51b46d9205d150c8e4b4f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
