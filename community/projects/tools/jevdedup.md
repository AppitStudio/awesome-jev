# jevdedup

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Bun CLI that finds duplicate files with size, quick-hash and SHA-256 checks, then asks Jev to confirm each group, flag mislabeled files, suggest which copy to keep and judge near-duplicate pairs; reports only, never deletes; self-described exercise project.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ruivalim/jevdedup) |
| Maintainer | [Ruivalim](https://github.com/Ruivalim). Independently curated. |
| Format | Bun CLI (`jevdedup`, via `bun link` or `make build` binary); source install |
| Requirements | Bun 1.1+; a TypeSafe API key in `~/.config/jevdedup/api-key` (or as documented upstream); `--no-jev` runs offline. |
| License | [MIT](https://github.com/Ruivalim/jevdedup/blob/fc753eab16c50742bb842b93980aa9f75e3bcf51/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Review a Downloads or photo folder for duplicates and get a suggested canonical copy per group.
- Use `--fail-on-duplicates` in CI to catch duplicated assets.
- Mismatch: upstream calls it an exercise project to test Jev, not a trustworthy cleanup tool.

## How it works

[`src/duplicates.ts`](https://github.com/Ruivalim/jevdedup/blob/fc753eab16c50742bb842b93980aa9f75e3bcf51/src/duplicates.ts) groups files by size and hashes; [`src/jev.ts`](https://github.com/Ruivalim/jevdedup/blob/fc753eab16c50742bb842b93980aa9f75e3bcf51/src/jev.ts) sends each group's metadata and a text excerpt (binary files: metadata only) with three questions — `verdict` (Choice), `safe_to_keep_one` (Noul) and `keep` (Choice) — and semantic pairs with `same_content` and `relation`. [`src/report.ts`](https://github.com/Ruivalim/jevdedup/blob/fc753eab16c50742bb842b93980aa9f75e3bcf51/src/report.ts) shows answers with probability, confidence and token usage.

## Get started

Install from source and run:

```sh
git clone https://github.com/Ruivalim/jevdedup.git && cd jevdedup
make setup      # bun install + .env from the example
make install    # bun link
jevdedup ~/Downloads
jevdedup . --no-jev   # offline, classic checks only
```

Each duplicate group or pair is a Jev request billed to your key; `--no-jev` is free.

## Examples and demos

- README *Usage* (min-size, ignore globs, `--json`, `--fail-on-duplicates`) and *Where Jev comes in*.
- Offline tests with a fake client: [`test/jev.test.ts`](https://github.com/Ruivalim/jevdedup/blob/fc753eab16c50742bb842b93980aa9f75e3bcf51/test/jev.test.ts).

## Limits and data handling

File paths, metadata and text excerpts go to TypeSafe; binaries are never sent (upstream). Nothing is deleted. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit fc753eab16c5](https://github.com/Ruivalim/jevdedup/tree/fc753eab16c50742bb842b93980aa9f75e3bcf51). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
