# System One Auto Tag (Obsidian)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Obsidian plugin that scores each note against your vault's existing tags with Jev Noul probabilities, sorts them into write, review and ignore bands, and only writes tags you accept from a heat-map matrix.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/holy-max/obsidian-systemone-auto-tag) |
| Maintainer | [holy-max](https://github.com/holy-max). Independently curated. |
| Format | Obsidian plugin (TypeScript); README in Chinese |
| Requirements | Obsidian; npm to build; a TypeSafe API key (or another System One endpoint). |
| License | [MIT](https://github.com/holy-max/obsidian-systemone-auto-tag/blob/62fdb4fb6ff012cb927c22d374262c7e13606c37/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/settings.ts`](https://github.com/holy-max/obsidian-systemone-auto-tag/blob/62fdb4fb6ff012cb927c22d374262c7e13606c37/src/settings.ts) at the pinned commit. |

## When to use

- Tag a backlog of notes with tags you already use, reviewing before anything is written.
- Tune the threshold and see notes re-bucket without new calls.
- Mismatch: it never invents new tags; a build step is needed unless a release exists.

## How it works

For each note it batches up to 10 Noul questions (one per candidate tag) to `{baseUrl}/v1/systemone` (default `https://api.typesafe.ai`, model `jev-1.14.0`, see `src/settings.ts`), caches the scores locally and shows a preflight count, ETA and rough cost. Integration evidence: [`src/settings.ts`](https://github.com/holy-max/obsidian-systemone-auto-tag/blob/62fdb4fb6ff012cb927c22d374262c7e13606c37/src/settings.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/holy-max/obsidian-systemone-auto-tag.git && cd obsidian-systemone-auto-tag
npm install && npm run build
# copy main.js, manifest.json, styles.css to .obsidian/plugins/systemone-auto-tag/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Feature summary and settings in the README: [github.com/holy-max/obsidian-systemone-auto-tag#readme](https://github.com/holy-max/obsidian-systemone-auto-tag#readme)

## Limits and data handling

Note text is sent to the configured System One endpoint. Workflow is modeled on Kaku Auto Tagging; independent implementation.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 62fdb4fb6ff0](https://github.com/holy-max/obsidian-systemone-auto-tag/tree/62fdb4fb6ff012cb927c22d374262c7e13606c37). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
