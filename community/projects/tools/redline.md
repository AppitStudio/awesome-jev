# Redline

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Visual PR review for Vite and Next.js apps: builds two commits, screenshots every page, and reports changed, new, broken, and removed pages; with a TypeSafe key, Jev picks the changed file most likely behind each visual change.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vvedantb/redline) |
| Maintainer | [vvedantb](https://github.com/vvedantb). Independently curated. |
| Format | npm CLI + Node API + static HTML report (`@vvedantb/redline`) |
| Requirements | Node, Playwright Chromium, a Vite or Next.js project; optional `TYPESAFE_API_KEY` for Jev linking. |
| License | No LICENSE file (source available) on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/vvedantb/status/2111905909370695817)). |
| Jev evidence | [`packages/redline/src/jev.ts`](https://github.com/vvedantb/redline/blob/2e313d31cef4123768c0dab702eaa2cf7b0acb49/packages/redline/src/jev.ts) at the pinned commit. |

## When to use

- Review what an agent or PR changed visually across every route before merging.
- Want a likely-culprit file per changed area, not just a pixel diff.
- Mismatch: no open-source license yet; Jev step is optional.

## How it works

Pixel diff marks changed pages first; then `packages/redline/src/jev.ts` asks Jev which changed file most likely caused each change and draws linked boxes on the after screenshot. Results are cached in `.redline/jev-cache`, and a Jev error only adds a notice. Integration evidence: [`packages/redline/src/jev.ts`](https://github.com/vvedantb/redline/blob/2e313d31cef4123768c0dab702eaa2cf7b0acb49/packages/redline/src/jev.ts).

## Get started

From the upstream README: install the package and Playwright, then compare HEAD~1 to HEAD and open the printed report.

```sh
npm install -D @vvedantb/redline playwright
npx playwright install chromium
export TYPESAFE_API_KEY=...   # optional, for Jev linking
npx redline compare
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [redline-vedantb.vercel.app](https://redline-vedantb.vercel.app)
- packages/redline/test/jev.test.ts

## Limits and data handling

With a key, screenshots and diff context for changed pages go to TypeSafe. No LICENSE at the pinned commit, so reuse rights are not granted. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 2e313d31cef4](https://github.com/vvedantb/redline/tree/2e313d31cef4123768c0dab702eaa2cf7b0acb49). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
