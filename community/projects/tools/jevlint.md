# JevLint

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Configurable semantic lint CLI: write coding conventions in plain English; TypeSafe Jev returns file-level Noul violation probabilities (default plugins: magic-strings, descriptive-names).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/huntedman/JevLint) |
| Maintainer | [Toomas Marjapuu / huntedman](https://github.com/huntedman). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package **@jevlint/cli 0.1.5** (`npx jevlint`) with JS/TS plugins. |
| Requirements | Node.js 24+; live lint needs `JEV_API_KEY` (loaded from `.env` or the environment). |
| License | [MIT](https://github.com/huntedman/JevLint/blob/8bf4b4e0c4c088b9cbcd9d735baa84c770a9c418/LICENSE). |

## When to use

Use it in an agent write→check→fix loop or CI when you want meaning-level convention checks that regex ESLint rules miss. Prefer [patdown](patdown.md) for fuzzy *markdown* rule trees; prefer [Moongate](moongate.md) for PR-diff semantic rules as CI annotations. JevLint reports file-level signals—it does not emit line diagnostics or auto-fixes.

## How it works

[`src/jev-client.ts`](https://github.com/huntedman/JevLint/blob/8bf4b4e0c4c088b9cbcd9d735baa84c770a9c418/src/jev-client.ts) posts `{ filePath, source }` plus one Noul question per enabled plugin to `https://api.typesafe.ai/v1/systemone`. Plugins under [`plugins/`](https://github.com/huntedman/JevLint/tree/8bf4b4e0c4c088b9cbcd9d735baa84c770a9c418/plugins) supply instructions. Default finding threshold is 0.8. `--dry-run` prints request JSON without calling Jev (plugins still execute locally).

## Get started

```sh
npm install --save-dev @jevlint/cli
npx jevlint init
# add JEV_API_KEY=… to .env
npx jevlint
npx jevlint src --dry-run
# or inspect:
git clone https://github.com/huntedman/JevLint.git
cd JevLint
git checkout 8bf4b4e0c4c088b9cbcd9d735baa84c770a9c418
```

Live runs send selected source files to TypeSafe. This listing did not call the API. Site: [jevlint.com](https://jevlint.com).

## Examples and demos

- [`examples/`](https://github.com/huntedman/JevLint/tree/8bf4b4e0c4c088b9cbcd9d735baa84c770a9c418/examples) for magic-strings and descriptive-names.
- Integration tests under `src/*.integration.test.ts`.
- `jevlint.config.example.json`.

## Limits and data handling

Selected source content leaves the machine for TypeSafe. Filename exclusions for `secrets/` / `credentials/` are not secret detection—other files can still leak sensitive values. Dry-run is not a sandbox for untrusted plugins. Findings are probabilistic file-level signals for agent/human review.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 8bf4b4e](https://github.com/huntedman/JevLint/tree/8bf4b4e0c4c088b9cbcd9d735baa84c770a9c418): **0.1.5**, MIT. AI-assisted source review of README, `jev-client.ts`, `package.json`, and license. Offline tests / live TypeSafe calls were not run on the review host.

Related: [patdown](patdown.md), [Moongate](moongate.md), [Supercov](supercov.md).
