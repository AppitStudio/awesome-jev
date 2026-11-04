# Patchwork Constellation (local web tool that maps which files and modules a set of pull requests or commits touches, with optional Jev regrouping of files into islands)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local-first web tool for seeing which parts of a repository a collection of pull requests or commits touches: files are connected circles, and labeled islands reveal modules, folders and components. It has an interactive sample that needs no credentials, public GitHub analysis and optional read-only GitHub App sign-in. An optional AI step lets Jev decide, for each file, which existing island fits best (with an `uncertain` option that keeps the original group) while a generative model proposes island names.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/oudaykhaled/patchwork-constellation) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/oudaykhaled/patchwork-constellation#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under Apache-2.0; you supply any TypeSafe, OpenAI and GitHub keys and hosting. Checked 2026-11-04. |
| Jev evidence | [`packages/ai/src/providers.ts`](https://github.com/oudaykhaled/patchwork-constellation/blob/97c2393e8116e146d236ea296240b4bee0e695a0/packages/ai/src/providers.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [oudaykhaled](https://github.com/oudaykhaled). Independently curated. |
| Format | Web app (Node 24 and pnpm monorepo; optional PostgreSQL) |
| Platform and availability | Self-hosted web app (loopback by default); hosted deployment needs your own configuration. |
| Jev's role | Optional grouping step that assigns each changed file to the island that best contains it, or leaves it where it was when evidence is weak. |
| Requirements | Node.js 24 and pnpm; for the AI step `AI_ENABLED`, `TYPESAFE_API_KEY`, `JEV_MODEL`, an OpenAI key and a reviewed evaluation manifest. |
| License | [Apache-2.0](https://github.com/oudaykhaled/patchwork-constellation/blob/97c2393e8116e146d236ea296240b4bee0e695a0/LICENSE) |

## When to use

- Understand how a batch of pull requests overlaps in a codebase and which modules they touch.
- Mismatch: the AI regrouping is off by default and needs a reviewed evaluation gate; without it the map still works.

## How it works

`packages/ai/src/providers.ts` sends per-file choice questions (which island contains this file, or uncertain) to `https://api.typesafe.ai/v1/systemone` with import and path evidence only, then validates that every answer maps to a known file and group before using it. Integration evidence: [`packages/ai/src/providers.ts`](https://github.com/oudaykhaled/patchwork-constellation/blob/97c2393e8116e146d236ea296240b4bee0e695a0/packages/ai/src/providers.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pnpm install --frozen-lockfile
pnpm dev   # opens http://127.0.0.1:4310 with the sample
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the sample walkthrough and configuration: [github.com/oudaykhaled/patchwork-constellation#readme](https://github.com/oudaykhaled/patchwork-constellation#readme)

## Limits and data handling

With AI enabled, file paths and import evidence (not file contents, per the README's exclusions setting) go to TypeSafe and OpenAI on your keys; credentials alone cannot enable the AI step without a version-matched evaluation manifest. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 97c2393e8116](https://github.com/oudaykhaled/patchwork-constellation/tree/97c2393e8116e146d236ea296240b4bee0e695a0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
