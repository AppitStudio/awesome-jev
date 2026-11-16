# noul-testlint (linter that asks Jev whether each test still establishes what its name claims, across TS, Python, Rust and Go)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A linter for tests, run as `ntlint`. A test's name is a claim about its behaviour; when the body stops establishing it (a `rejects` test that checks an ordinary value, a snapshot standing in for a property, a mock that supplies the very behaviour under test), no compiler or conventional linter notices. ntlint turns each test into Noul questions for one language-independent rule set (seventeen rules, with their cut-offs' provenance shown in the output), reports JSON Lines, pretty or GitHub annotations, and prices a run with `--dry-run` before any request. TypeScript, Python, Rust and Go for now.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/L4Ph/ntlint) |
| Maintainer | [L4Ph](https://github.com/L4Ph). Independently curated. |
| Format | npm CLI (`noul-testlint`, TypeScript, MIT) |
| Requirements | Node.js and `TYPESAFE_API_KEY` from the environment (`--dry-run` needs no key). |
| License | [MIT](https://github.com/L4Ph/ntlint/blob/b8b80dc4e14d6399a86842760b33befde8fcb0ae/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/R0u9h/status/2122267248618504350)). |
| Jev evidence | [`packages/core/src/client.ts`](https://github.com/L4Ph/ntlint/blob/b8b80dc4e14d6399a86842760b33befde8fcb0ae/packages/core/src/client.ts) at the pinned commit. |

## When to use

- Catch tests whose bodies no longer prove what their names say.
- Mismatch: anything a compiler, type checker or conventional linter already decides.

## How it works

`packages/core/src/client.ts` posts Noul questions to `https://api.typesafe.ai/v1/systemone` with the key from `TYPESAFE_API_KEY`; `packages/cli/src/main.ts` refuses to run without a key unless `--dry-run` is set. Integration evidence: [`packages/core/src/client.ts`](https://github.com/L4Ph/ntlint/blob/b8b80dc4e14d6399a86842760b33befde8fcb0ae/packages/core/src/client.ts).

## Get started

Install as a dev dependency, price a run, then check your tests.

```sh
npm install --save-dev noul-testlint
npx ntlint check src --dry-run   # cost estimate, no request
export TYPESAFE_API_KEY=...
npx ntlint check src
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/L4Ph/ntlint/blob/b8b80dc4e14d6399a86842760b33befde8fcb0ae/README.md](https://github.com/L4Ph/ntlint/blob/b8b80dc4e14d6399a86842760b33befde8fcb0ae/README.md)

## Limits and data handling

Test source goes to TypeSafe on your key. The rule cut-offs were not fitted on your corpus, as the output states; treat findings as review prompts.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit b8b80dc4e14d](https://github.com/L4Ph/ntlint/tree/b8b80dc4e14d6399a86842760b33befde8fcb0ae). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
