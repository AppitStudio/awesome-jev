# Note Filer

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Obsidian desktop plugin that classifies the current note (or a selected tree) with TypeSafe Jev and moves Markdown files into Thema or IAB taxonomy folders after a human confirms candidates.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/someka-vrc/obsidian-note-filer) |
| Maintainer | [someka-vrc](https://github.com/someka-vrc). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Obsidian community-style plugin (TypeScript; esbuild bundle). Desktop only. |
| Requirements | Obsidian desktop; TypeSafe API URL (default `https://api.typesafe.ai/v1/systemone`) and API key stored via Obsidian SecretStorage. |
| License | [0BSD](https://github.com/someka-vrc/obsidian-note-filer/blob/6db39f376467105fe7f141125ef15c52768f944a/LICENSE). TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. `npm run build` succeeded offline; live Jev classification and Obsidian UI not run. Distinct from [Jev Second Brain](jev-second-brain.md) (vault CLI / link suggestions). |

## When to use

Use it when an Obsidian vault should be filed under a standard taxonomy folder tree with Jev-ranked labels and an explicit move review UI. Prefer [Jev Second Brain](jev-second-brain.md) for local FTS indexing and optional relationship judgments without moving files.

## How it works

Commands / status-bar / context-menu start classification. [`src/main.ts`](https://github.com/someka-vrc/obsidian-note-filer/blob/6db39f376467105fe7f141125ef15c52768f944a/src/main.ts) sends each note's title plus the first ~200 characters of body text (skipping image/blank lines) to the configured System One endpoint, ranks up to three taxonomy candidates with confidence, and shows a review list before `renameFile` moves. Taxonomy JSON (Thema / IAB) is bundled; depth and confidence threshold are settings.

## Get started

```sh
git clone https://github.com/someka-vrc/obsidian-note-filer.git
cd obsidian-note-filer
git checkout 6db39f376467105fe7f141125ef15c52768f944a
npm ci
npm run build
```

Copy the built plugin into an Obsidian vault `plugins/` folder per upstream Obsidian plugin practice, set the API key in settings, then run **Categorize current note and move**. Live classification sends title + excerpt to TypeSafe and can incur charges.

## Examples and demos

- Upstream README (Japanese) documents UI, undo limits, and data sent.
- This listing ran `npm run build` successfully. No live TypeSafe or Obsidian session.

## Limits and data handling

Desktop only; `.md` only. Title and leading body excerpt leave the machine for TypeSafe; remaining body/frontmatter are not sent. Same-name collisions disable move. Undo is not implemented. AI-assisted listing; not an Obsidian/TypeSafe endorsement.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 6db39f3](https://github.com/someka-vrc/obsidian-note-filer/tree/6db39f376467105fe7f141125ef15c52768f944a): 0BSD; AI-assisted source review of README, LICENSE, `src/main.ts` / settings, and production build. No live TypeSafe call.

Related: [Jev Second Brain](jev-second-brain.md).
