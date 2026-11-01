# LYRCENSOR (C terminal app that redacts slurs in Russian and English lyrics using Jev probabilities, editing letters locally)

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Native C17 terminal application for context-sensitive lyrics redaction: it asks one OpenRouter Decisions model (Jev by default) for noul probabilities and replaces selected letters locally in C, so the model never writes output text. Russian and English text, line endings and spacing are preserved.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/qememe/LYRCENSOR) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/qememe/LYRCENSOR#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (MIT); you supply an OpenRouter key. Checked 2026-11-01. |
| Jev evidence | [`src/openrouter.c`](https://github.com/qememe/LYRCENSOR/blob/c54b590402b812b20dfa26819e33610cfb252956/src/openrouter.c) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [qememe](https://github.com/qememe). Independently curated. |
| Format | Terminal app (C17, ncurses) |
| Platform and availability | Terminal on Linux/macOS (POSIX). |
| Jev's role | Scores words and phrases for redaction; code edits the letters. |
| Requirements | C17 compiler, make, pkg-config, ncursesw; an OpenRouter key. |
| License | [MIT](https://github.com/qememe/LYRCENSOR/blob/c54b590402b812b20dfa26819e33610cfb252956/LICENSE) |

## When to use

- Censor abusive slurs in lyrics without letting a model rewrite the text.
- Mismatch: needs a model that supports OpenRouter's Decisions API; no fallback.

## How it works

`src/openrouter.c` posts native `noul` questions to `https://openrouter.ai/api/alpha/decisions` with `typesafe/jev-1.13` (default in `src/config.c`); the C code applies the redaction policy to the returned probabilities. Integration evidence: [`src/openrouter.c`](https://github.com/qememe/LYRCENSOR/blob/c54b590402b812b20dfa26819e33610cfb252956/src/openrouter.c).

## Get started

From the upstream README (not run on the review host):

```sh
make && make test
export OPENROUTER_API_KEY=...
./lyrcensor lyrics.txt
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/qememe/LYRCENSOR#readme](https://github.com/qememe/LYRCENSOR#readme)

## Limits and data handling

Lyrics text is sent to OpenRouter. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit c54b590402b8](https://github.com/qememe/LYRCENSOR/tree/c54b590402b812b20dfa26819e33610cfb252956). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
