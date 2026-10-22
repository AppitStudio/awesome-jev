# Jev Talks (chat built one Jev choice at a time)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Chat experiment where a decision model writes the reply: on every step Jev picks the next character (English and Turkish letters, digits, punctuation, SPACE or STOP) or the next word from 250 common words, with an optional recheck pass.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bariskisir/JevTalks) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://jev-talks.vercel.app) |
| Pricing and access | Open source (MIT); see the live site for how keys are handled. Checked 2026-10-23. |
| Jev evidence | [`src/lib/jevProtocol.ts`](https://github.com/bariskisir/JevTalks/blob/db4e68930c60c0495e6b309f2c16f1b4c1f68a3e/src/lib/jevProtocol.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [bariskisir](https://github.com/bariskisir). Independently curated. |
| Format | Web app (TypeScript) |
| Platform and availability | Web, live at jev-talks.vercel.app. |
| Jev's role | Jev chooses every character or word of the reply and when to stop. |
| Requirements | A browser for the live site; Node.js and a TypeSafe API key to run it yourself. |
| License | [MIT](https://github.com/bariskisir/JevTalks/blob/db4e68930c60c0495e6b309f2c16f1b4c1f68a3e/LICENSE) |

## When to use

- See how far a pure choice model can get at writing text.
- Use as a reference for long chains of choice calls.
- Mismatch: an experiment; replies are slow and short by design.

## How it works

`src/lib/jevProtocol.ts` posts the full conversation and the reply so far to `https://api.typesafe.ai/v1/systemone` with model `jev-latest` and one choice question per step. Integration evidence: [`src/lib/jevProtocol.ts`](https://github.com/bariskisir/JevTalks/blob/db4e68930c60c0495e6b309f2c16f1b4c1f68a3e/src/lib/jevProtocol.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live site: [jev-talks.vercel.app](https://jev-talks.vercel.app)

## Limits and data handling

Conversations are sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit db4e68930c60](https://github.com/bariskisir/JevTalks/tree/db4e68930c60c0495e6b309f2c16f1b4c1f68a3e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
