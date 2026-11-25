# tapcheck by Ashish Jain (end-to-end and UI audit for any web app, with Jev judging screenshots for visual QA and usability)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI and GitHub Action that drives your running web app in a real browser: crawl, API contract, security headers, accessibility (axe-core), safe interaction and your own flows are checked by code, while Jev answers typed questions about screenshots for UI consistency, visual QA, usability heuristics and a simulated first-time user. A clear answer passes or fails; an unsure one is a warning.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ashishjain15491/tapcheck) |
| Maintainer | [Ashish Jain](https://github.com/ashishjain15491). Independently curated. |
| Format | Node.js CLI and GitHub Action (npm `@ashishjain15491/tapcheck`) |
| Requirements | Node.js, Playwright Chromium, your app running locally or reachable, and a TypeSafe API key for the Jev suites (they are skipped without one). |
| License | [MIT](https://github.com/ashishjain15491/tapcheck/blob/1b9ec12d9d0f3fa0873a49a0dadbbdb2586559b1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/ashishjain15491/tapcheck/blob/1b9ec12d9d0f3fa0873a49a0dadbbdb2586559b1/src/jev.ts) at the pinned commit. |

## When to use

- Add a UI and usability audit to CI for a web app in any stack.
- Mismatch: if you cannot send screenshots of the app to an external API.

## How it works

`src/jev.ts` uses the official `@typesafe-ai/sdk` with image inputs (`TypeSafe-Danger-Zone-Images` header) and reads `TYPESAFE_API_KEY` from the environment or `.env`. Integration evidence: [`src/jev.ts`](https://github.com/ashishjain15491/tapcheck/blob/1b9ec12d9d0f3fa0873a49a0dadbbdb2586559b1/src/jev.ts).

## Get started

Install as a dev dependency, install Chromium once, then run it.

```sh
npm install --save-dev tapcheck@npm:@ashishjain15491/tapcheck
npx playwright install chromium
npx tapcheck
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README data and safety notes: [github.com/ashishjain15491/tapcheck/blob/1b9ec12d9d0f3fa0873a49a0dadbbdb2586559b1/README.md](https://github.com/ashishjain15491/tapcheck/blob/1b9ec12d9d0f3fa0873a49a0dadbbdb2586559b1/README.md)

## Limits and data handling

Jev receives screenshots of the configured screens plus screen names, tasks and visible labels (no cookies or page source); run against test data. Signed-in sessions are saved under `.tapcheck`. The `interact` suite clicks controls (never delete, send, pay or submit).

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 1b9ec12d9d0f](https://github.com/ashishjain15491/tapcheck/tree/1b9ec12d9d0f3fa0873a49a0dadbbdb2586559b1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
