# Atmosphere (animate a rigged 3D character from a plain-language action, with Jev judging each pose)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Web app built for the Devpost Build With AI: Basics hackathon: upload a rigged 3D character, describe an action, and an OpenAI model plans the timing, beats and poses while Jev judges and polishes each pose before the result plays back.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JackMerma/atmosphere) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/JackMerma/atmosphere#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. OpenAI and TypeSafe usage is billed to your own keys. Checked 2026-10-27. |
| Jev evidence | [`lib/jevClient.ts`](https://github.com/JackMerma/atmosphere/blob/c331775e14a2ec92e33a4b1d888e2bc91b742b8a/lib/jevClient.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [JackMerma](https://github.com/JackMerma). Independently curated. |
| Format | Next.js web app |
| Platform and availability | Run locally from source (Node.js). |
| Jev's role | Pose judge: scores and picks pose refinements during the animation pipeline. |
| Requirements | Node.js; an OpenAI API key and a TypeSafe API key. |
| License | [MIT](https://github.com/JackMerma/atmosphere/blob/c331775e14a2ec92e33a4b1d888e2bc91b742b8a/LICENSE) |

## When to use

- Prototype character animation from text prompts.
- Mismatch: hackathon project; run locally only.

## How it works

`lib/jevClient.ts` posts pose questions to `https://api.typesafe.ai/v1/systemone` with your `TYPESAFE_API_KEY`. Integration evidence: [`lib/jevClient.ts`](https://github.com/JackMerma/atmosphere/blob/c331775e14a2ec92e33a4b1d888e2bc91b742b8a/lib/jevClient.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/JackMerma/atmosphere && cd atmosphere
npm install
npm run dev   # http://localhost:3000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/JackMerma/atmosphere#readme](https://github.com/JackMerma/atmosphere#readme)

## Limits and data handling

Action descriptions and pose data go to OpenAI and TypeSafe. Uploaded characters are handled by the local app.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit c331775e14a2](https://github.com/JackMerma/atmosphere/tree/c331775e14a2ec92e33a4b1d888e2bc91b742b8a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
