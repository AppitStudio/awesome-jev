# anti-slop by K-Mistele (Oxlint rules against low-evidence agent-written TypeScript, with 23 plain-English rules judged by Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Kyle Mistele's fork of Dillon Mulroy's anti-slop: Oxlint rules that reject the TypeScript coding agents tend to write (casts without a stated invariant, `unknown` leaking through contracts, module mocks) with diagnostics that tell the agent what to do instead. The fork adds a vendored `oxlint-plugin-jev` with 23 rules written as plain-English yes/no questions: 11 Effect review questions (such as `shallow-service`, `swallow-without-capture`, `read-then-write-race`) and 12 of Martin Fowler's code smells, plus Effect and Fowler AST rules and diff rules that judge a whole change set. Rules can run on changed code only; an install skill copies everything into your repository.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/K-Mistele/anti-slop) |
| Maintainer | [K-Mistele](https://github.com/K-Mistele). Independently curated. |
| Format | Oxlint rule set and vendored Oxlint JS plugin (TypeScript, MIT) |
| Requirements | Node.js 22.18+, Oxlint with `@oxlint/plugins` at the same version, and `TYPESAFE_API_KEY` (or a Factory or AI Gateway key) for the Jev rules. |
| License | [MIT](https://github.com/K-Mistele/anti-slop/blob/b7c1619b4d51b4815e89ba3700a975a6ec54b8c3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/0xblacklight/status/2122164674309521562)). |
| Jev evidence | [`docs/jev.md`](https://github.com/K-Mistele/anti-slop/blob/b7c1619b4d51b4815e89ba3700a975a6ec54b8c3/docs/jev.md) at the pinned commit. |

## When to use

- Catch semantic review problems in agent-written TypeScript and Effect code before pushing or in CI.
- Mismatch: editor-time linting; every Jev match is a paid, non-deterministic request, so the docs say not to run it in the editor.

## How it works

`docs/jev.md` documents the Jev rules: `src/jev/effect-rules.ts` holds the questions and `src/jev/plugin.ts` builds them into `anti-slop-effect-jev` on the vendored `oxlint-plugin-jev`, which asks TypeSafe Jev through the AI SDK (`@ai-sdk/typesafe-ai`) one request per file and reports when the yes-probability reaches a rule's cutoff. Jev is the default judge; any AI SDK chat model can be set instead. Integration evidence: [`docs/jev.md`](https://github.com/K-Mistele/anti-slop/blob/b7c1619b4d51b4815e89ba3700a975a6ec54b8c3/docs/jev.md).

## Get started

Clone with submodules, build the Jev plugin, then use the install skill or copy the rules into your project.

```sh
git clone --recurse-submodules https://github.com/K-Mistele/anti-slop && cd anti-slop
pnpm install && pnpm build:jev
export TYPESAFE_API_KEY=...
# in your repo: run the install-anti-slop skill (its --jev flag vendors oxlint-plugin-jev), then oxlint
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/K-Mistele/anti-slop/blob/b7c1619b4d51b4815e89ba3700a975a6ec54b8c3/README.md](https://github.com/K-Mistele/anti-slop/blob/b7c1619b4d51b4815e89ba3700a975a6ec54b8c3/README.md)
- Jev rules guide: [github.com/K-Mistele/anti-slop/blob/b7c1619b4d51b4815e89ba3700a975a6ec54b8c3/docs/jev.md](https://github.com/K-Mistele/anti-slop/blob/b7c1619b4d51b4815e89ba3700a975a6ec54b8c3/docs/jev.md)
- Martin Fowler rules: [github.com/K-Mistele/anti-slop/blob/b7c1619b4d51b4815e89ba3700a975a6ec54b8c3/docs/martinfowler.md](https://github.com/K-Mistele/anti-slop/blob/b7c1619b4d51b4815e89ba3700a975a6ec54b8c3/docs/martinfowler.md)

## Limits and data handling

Each linted file's source and the rule questions go to TypeSafe (or the configured judge) on your key. The AST rules run locally with no model calls. Fork of dmmulroy/anti-slop (MIT); the jev plugin fork is not on npm.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit b7c1619b4d51](https://github.com/K-Mistele/anti-slop/tree/b7c1619b4d51b4815e89ba3700a975a6ec54b8c3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
