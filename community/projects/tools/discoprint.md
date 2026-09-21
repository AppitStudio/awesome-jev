# discoprint

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI that classifies an artist's discography for theme, mood, and lyrical complexity with TypeSafe Jev, then renders a colorful terminal dashboard (Ink TUI).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lirantal/discoprint) |
| Maintainer | [lirantal](https://github.com/lirantal). Independently curated; this page is not an upstream submission or endorsement. |
| Format | TypeScript npm CLI (`discoprint` 0.1.0) with Ink live TUI and `visualize` replay. |
| Requirements | Node.js **≥ 22**, `TYPESAFE_API_KEY` (or documented TypeSafe credential) for classification. MusicBrainz and lrclib are keyless. |
| License | [Apache-2.0](https://github.com/lirantal/discoprint/blob/09673335e98cf9119e2b659ae11e6508f8eb8524/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Offline `pnpm test` passed; live discography classification was **not** run. No live TypeSafe calls. |

## When to use

Use it to explore how Jev labels a public artist's albums for theme/mood/complexity in a terminal, or to demo batched System One song judgments. Prefer local lyrics tools without cloud inference when you must keep lyric text offline.

## How it works

MusicBrainz resolves the artist and discography; lrclib fetches plain lyrics; [src/jev.ts](https://github.com/lirantal/discoprint/blob/09673335e98cf9119e2b659ae11e6508f8eb8524/src/jev.ts) packs five atomic questions into one `systemOne` call per track. Results and fetches cache under `data/cache/` so reruns are incremental. `discoprint visualize` redraws from cache without new network calls.

## Get started

```sh
npx discoprint "Bon Jovi"
# or
npm install -g discoprint
discoprint "Bon Jovi" --limit 20
discoprint visualize "Bon Jovi"
```

Pinned source review:

```sh
git clone https://github.com/lirantal/discoprint.git
cd discoprint
git checkout 09673335e98cf9119e2b659ae11e6508f8eb8524
pnpm install
pnpm test
```

Live classify sends lyric text to TypeSafe and may incur charges. MusicBrainz is rate-limited (~1 req/s).

## Examples and demos

- README Ink TUI walkthrough and classifier question set.
- Offline tests: **149 passed** via `pnpm test` on the review host (Node 22 / pnpm 12).
- npm package [discoprint](https://www.npmjs.com/package/discoprint).

## Limits and data handling

Lyrics and artist metadata go to TypeSafe during classify. Cache files stay on disk under the working tree. Non-TTY/`--verbose` paths print plain progress instead of the live Ink frame. Themes/moods are model labels, not musicological ground truth.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 0967333](https://github.com/lirantal/discoprint/tree/09673335e98cf9119e2b659ae11e6508f8eb8524): package **0.1.0**, Apache-2.0. AI-assisted source review of README, LICENSE, `src/jev.ts`, and pipeline. **`pnpm test`: 149 passed**. No live TypeSafe, MusicBrainz, or lrclib calls in this review beyond what tests mock.

Related: [semantic-assert](semantic-assert.md) also packages TypeSafe Jev judgments for assertions; discoprint focuses on music metadata dashboards.
