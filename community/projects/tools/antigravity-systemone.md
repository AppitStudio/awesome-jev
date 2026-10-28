# Antigravity System One (agy-smart: Jev picks which skills the Google Antigravity CLI loads per prompt)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Wrapper for the Google Antigravity CLI (`agy`) that classifies each task with Jev and mounts only the relevant skills before handing off to the main reasoning model, instead of loading 50+ installed skills (3,000-8,000 tokens) into every turn. Includes a local dashboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sarayutbit58/antigravity-systemone) |
| Maintainer | [sarayutbit58](https://github.com/sarayutbit58). Independently curated. |
| Format | Node.js CLI (`agy-smart`) |
| Requirements | Node.js 20.6+, the Antigravity CLI and a TypeSafe API key. |
| License | [MIT](https://github.com/sarayutbit58/antigravity-systemone/blob/7679638b66005eabf0d03536a37aa2da35afa1f4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`index.mjs`](https://github.com/sarayutbit58/antigravity-systemone/blob/7679638b66005eabf0d03536a37aa2da35afa1f4/index.mjs) at the pinned commit. |

## When to use

- Cut prompt overhead in Antigravity sessions with many skills.
- Mismatch: only for the Antigravity CLI.

## How it works

`index.mjs` posts the prompt and skill descriptions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) and passes only the selected skills to `agy`. Integration evidence: [`index.mjs`](https://github.com/sarayutbit58/antigravity-systemone/blob/7679638b66005eabf0d03536a37aa2da35afa1f4/index.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/sarayutbit58/antigravity-systemone.git && cd antigravity-systemone
npm install && npm link
# set TYPESAFE_API_KEY in .env, then run agy-smart
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/sarayutbit58/antigravity-systemone#readme](https://github.com/sarayutbit58/antigravity-systemone#readme)

## Limits and data handling

Prompts and skill descriptions go to TypeSafe before the main model.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 7679638b6600](https://github.com/sarayutbit58/antigravity-systemone/tree/7679638b66005eabf0d03536a37aa2da35afa1f4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
