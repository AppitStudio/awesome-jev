# gloss (streaming, annotated review tours for pull requests and local diffs, with Jev judging each file)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Turns a pull request or local diff into a guided review tour in the browser: ordered groups with summaries and notes pinned to the lines that matter, streamed stage by stage. An LLM defines groups and writes notes; Jev makes the per-file calls (which group, generated, tests-only, and whether a file touches auth, stored data, secrets or personal data). Requests are cached locally.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/brishin/gloss) |
| Maintainer | [brishin](https://github.com/brishin). Independently curated. |
| Format | Node.js CLI and web viewer (TypeScript, pnpm) |
| Requirements | Node.js with pnpm, a Claude or ChatGPT subscription or API key, and a TypeSafe or OpenRouter key for Jev. |
| License | [MIT](https://github.com/brishin/gloss/blob/978bb4ea21fb5e5558bfbd9863cf7d0709f9be9f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/models/src/jev-client.ts`](https://github.com/brishin/gloss/blob/978bb4ea21fb5e5558bfbd9863cf7d0709f9be9f/packages/models/src/jev-client.ts) at the pinned commit. |

## When to use

- Review a large PR in a sensible order with the risky files flagged.
- Mismatch: notes come from the LLM; Jev only classifies files.

## How it works

`packages/models/src/jev-client.ts` asks `typesafe/jev-latest` (TypeSafe or OpenRouter) per file; `packages/models/src/config.ts` lets you turn judging off. Integration evidence: [`packages/models/src/jev-client.ts`](https://github.com/brishin/gloss/blob/978bb4ea21fb5e5558bfbd9863cf7d0709f9be9f/packages/models/src/jev-client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/brishin/gloss && cd gloss
pnpm install && pnpm --filter @gloss/web build
node packages/cli/src/bin.ts https://github.com/owner/repo/pull/123
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/brishin/gloss#readme](https://github.com/brishin/gloss#readme)

## Limits and data handling

Diff content goes to your LLM provider and to TypeSafe or OpenRouter; results are cached in `~/.gloss`.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 978bb4ea21fb](https://github.com/brishin/gloss/tree/978bb4ea21fb5e5558bfbd9863cf7d0709f9be9f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
