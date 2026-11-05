# Adhere (linter for rules a normal linter cannot check, powered by TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Linter for non-deterministic project rules: you write plain-language checks, and Adhere asks Jev whether the code under review follows them. Meant for style and policy rules that regex and AST linters miss.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/darkmatter/adhere) |
| Maintainer | [darkmatter](https://github.com/darkmatter). Independently curated. |
| Format | TypeScript CLI/library (MIT) |
| Requirements | Node.js and a TypeSafe API key configured for the Jev provider (`src/providers/jev.ts`). |
| License | [MIT](https://github.com/darkmatter/adhere/blob/796093bfdf3d014cfc9a7cbf6ee570a16dfaf387/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/providers/jev.ts`](https://github.com/darkmatter/adhere/blob/796093bfdf3d014cfc9a7cbf6ee570a16dfaf387/src/providers/jev.ts) at the pinned commit. |

## When to use

- Enforce plain-language engineering rules that ESLint cannot express.
- Keep deterministic checks in normal linters and reserve Jev for judgment calls.
- Mismatch: every finding is probabilistic; treat low-confidence hits as review prompts, not hard fails.

## How it works

`src/providers/jev.ts` and `src/services/Jev.ts` send rule text plus code context as typed System One questions and map probabilities into lint findings. Integration evidence: [`src/providers/jev.ts`](https://github.com/darkmatter/adhere/blob/796093bfdf3d014cfc9a7cbf6ee570a16dfaf387/src/providers/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# see upstream README for install and rule-file format
export TYPESAFE_API_KEY=...
# run Adhere against your tree with the project rule set
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/darkmatter/adhere/blob/796093bfdf3d014cfc9a7cbf6ee570a16dfaf387/README.md](https://github.com/darkmatter/adhere/blob/796093bfdf3d014cfc9a7cbf6ee570a16dfaf387/README.md)
- Jev provider: [github.com/darkmatter/adhere/blob/796093bfdf3d014cfc9a7cbf6ee570a16dfaf387/src/providers/jev.ts](https://github.com/darkmatter/adhere/blob/796093bfdf3d014cfc9a7cbf6ee570a16dfaf387/src/providers/jev.ts)

## Limits and data handling

Source snippets under review are sent to TypeSafe on your key. Findings are advisory probabilities, not proof of compliance.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 796093bfdf3d](https://github.com/darkmatter/adhere/tree/796093bfdf3d014cfc9a7cbf6ee570a16dfaf387). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
