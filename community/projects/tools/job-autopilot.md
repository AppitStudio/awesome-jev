# job-autopilot (job-application agent that fills forms from your own data, with Jev mapping fields)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Application agent pulled out of Arkoo: it picks postings worth applying to, finds the application form, fills it from your profile and CV, and checks the result with 13 gates; Jev maps unrecognised questions to known fields, matches answer options and decides whether a free-text answer is needed, acting only at 0.9 confidence. Rehearse mode by default; automatic submission is off.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jordan-ae/job-autopilot) |
| Maintainer | [jordan-ae](https://github.com/jordan-ae). Independently curated. |
| Format | TypeScript CLI |
| Requirements | Node.js; a TypeSafe API key for the Jev pass and a DeepSeek key for drafts. |
| License | [MIT](https://github.com/jordan-ae/job-autopilot/blob/142fdbf86fa8e236ba14937c374952f5239c8b7c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/ai/decide.ts`](https://github.com/jordan-ae/job-autopilot/blob/142fdbf86fa8e236ba14937c374952f5239c8b7c/src/ai/decide.ts) at the pinned commit. |

## When to use

- Fill repetitive job applications from facts you have on file, and review them before sending.
- Mismatch: automatic submission is off by default; check every application yourself.

## How it works

`src/ai/decide.ts` posts field and option questions to TypeSafe's `/v1/systemone` and acts only above 0.9; answers are cached per ATS field. Integration evidence: [`src/ai/decide.ts`](https://github.com/jordan-ae/job-autopilot/blob/142fdbf86fa8e236ba14937c374952f5239c8b7c/src/ai/decide.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jordan-ae/job-autopilot && cd job-autopilot
npm install
npm run demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jordan-ae/job-autopilot#readme](https://github.com/jordan-ae/job-autopilot#readme)

## Limits and data handling

Form questions and your stored answers go to TypeSafe and DeepSeek. Follow each job site's terms.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 142fdbf86fa8](https://github.com/jordan-ae/job-autopilot/tree/142fdbf86fa8e236ba14937c374952f5239c8b7c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
