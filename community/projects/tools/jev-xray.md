# jev-xray

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Sends every file in a repo to TypeSafe Jev with eight typed lenses in one request per file (role, blast radius, complexity, security-sensitive, tech debt, deserves tests, start here, legacy) and renders a live treemap; ask a new question to relight all files, drill down to the line Jev ranks highest, and read 'doubt' (1 − mean confidence) as a reading list.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/viva-lee/jev-xray) |
| Maintainer | [viva-lee](https://github.com/viva-lee). Independently curated. |
| Format | Node CLI (`node bin/jev-xray.js <repo>`) serving a local web map |
| Requirements | Node.js and a `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/viva-lee/jev-xray/blob/9541a78066e645a6734c87457b252dbc8da0fd6c/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Orient in an unfamiliar repo: hotspots, security-sensitive files and where to start.
- Ask a custom yes/no or choice question of every file at once.
- Mismatch: every file's contents go to TypeSafe — not for code you can't share.

## How it works

[`src/jev.js`](https://github.com/viva-lee/jev-xray/blob/9541a78066e645a6734c87457b252dbc8da0fd6c/src/jev.js) calls `https://api.typesafe.ai/v1/systemone` and tracks cost (input-only pricing); [`bin/jev-xray.js`](https://github.com/viva-lee/jev-xray/blob/9541a78066e645a6734c87457b252dbc8da0fd6c/bin/jev-xray.js) walks the repo, streams decisions to the UI and computes hotspots (∛ blast × complexity × churn) and doubt in code.

## Get started

Clone and point it at a repo (README *Quickstart*):

```sh
git clone https://github.com/viva-lee/jev-xray.git && cd jev-xray
npm install
export TYPESAFE_API_KEY=...
node bin/jev-xray.js ~/code/your-repo
```

One Jev request per file (plus line drill-downs), billed by TypeSafe; upstream reports ~$0.05 for a 556-file scan.

## Examples and demos

- README run against honojs/hono (556 files, jev-1.13.0, upstream-reported 30 s / $0.050).
- README *Custom lens packs*.

## Limits and data handling

File contents go to TypeSafe. Cost/time figures are the author's. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 9541a78066e6](https://github.com/viva-lee/jev-xray/tree/9541a78066e645a6734c87457b252dbc8da0fd6c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
