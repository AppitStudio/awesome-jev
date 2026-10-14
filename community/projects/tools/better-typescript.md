# Better TypeScript

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go-based TypeScript linter whose `semantic` mode asks TypeSafe Noul questions over bounded source spans for policy checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/andrueandersoncs/better-typescript) |
| Maintainer | [andrueandersoncs](https://github.com/andrueandersoncs). Independently curated. |
| Format | Linter CLI (Go; npm package) |
| Requirements | Node/npm; TypeSafe API key for `semantic` mode. |
| License | [MIT](https://github.com/andrueandersoncs/better-typescript/blob/433b7ee3826b4927c54992c96befef1904e799fc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/semanticlint/typesafe.go`](https://github.com/andrueandersoncs/better-typescript/blob/433b7ee3826b4927c54992c96befef1904e799fc/internal/semanticlint/typesafe.go) at the pinned commit. |

## When to use

- Add semantic lint policies that are hard to express as syntax rules.
- Mismatch: syntax/type rules run without Jev; only `semantic` uses it.

## How it works

Code selects changed files and candidate spans; Jev answers Noul questions per policy; the linter reports findings. Integration evidence: [`internal/semanticlint/typesafe.go`](https://github.com/andrueandersoncs/better-typescript/blob/433b7ee3826b4927c54992c96befef1904e799fc/internal/semanticlint/typesafe.go).

## Get started

From the upstream README (not run on the review host):

```sh
npm install --save-dev @better-typescript/better-typescript
npx better-typescript semantic
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs: [andrueandersoncs.github.io/better-typescript/](https://andrueandersoncs.github.io/better-typescript/)
- Tests: `internal/semanticlint/`.

## Limits and data handling

Source spans are sent to TypeSafe in semantic mode.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 433b7ee3826b](https://github.com/andrueandersoncs/better-typescript/tree/433b7ee3826b4927c54992c96befef1904e799fc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
