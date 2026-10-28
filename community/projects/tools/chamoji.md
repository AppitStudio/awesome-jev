# chamoji (changelogs from gitmoji or Conventional Commits, with Jev sorting the commits rules can't place)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI and library that reads git history, parses gitmoji, Conventional Commits or plain messages, collapses dependency noise, groups commits into changelog sections, suggests the next semver version and renders Markdown, HTML or JSON. With `--ai`, commits no rule can place are sorted by Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HeavenlyEntity/chamoji-ai) |
| Maintainer | [HeavenlyEntity](https://github.com/HeavenlyEntity). Independently curated. |
| Format | Node.js CLI and library (npm `@chamoji/cli`, `@chamoji/core`) |
| Requirements | Node.js and git; a TypeSafe API key only for `--ai`. |
| License | [MIT](https://github.com/HeavenlyEntity/chamoji-ai/blob/b8674303aed7fec47e30ca8d1ae6deacf4544ac3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/cli/src/jev-classifier.ts`](https://github.com/HeavenlyEntity/chamoji-ai/blob/b8674303aed7fec47e30ca8d1ae6deacf4544ac3/packages/cli/src/jev-classifier.ts) at the pinned commit. |

## When to use

- Generate readable release notes from messy commit history.
- Mismatch: Jev is optional; without `--ai` it is fully rule-based.

## How it works

`packages/cli/src/jev-classifier.ts` asks one Choice question per unplaced commit through the official TypeSafe SDK and files the commit under the most likely section. Integration evidence: [`packages/cli/src/jev-classifier.ts`](https://github.com/HeavenlyEntity/chamoji-ai/blob/b8674303aed7fec47e30ca8d1ae6deacf4544ac3/packages/cli/src/jev-classifier.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npx @chamoji/cli --help
# or: git clone https://github.com/HeavenlyEntity/chamoji-ai
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- npm package: [www.npmjs.com/package/@chamoji/cli](https://www.npmjs.com/package/@chamoji/cli)
- Source: [github.com/HeavenlyEntity/chamoji-ai](https://github.com/HeavenlyEntity/chamoji-ai)

## Limits and data handling

Commit messages that rules can't place go to TypeSafe only with `--ai`.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit b8674303aed7](https://github.com/HeavenlyEntity/chamoji-ai/tree/b8674303aed7fec47e30ca8d1ae6deacf4544ac3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
