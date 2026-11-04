# pi-fabric (programmable tool and agent runtime for Pi with explicit Jev typed decisions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Runtime that gives the Pi coding agent one programmable `fabric_exec` tool for composing tools, MCP servers, agents and workflows in sandboxed TypeScript or Python. Its Jev integration lets programs call `jev.evaluate` for a fuzzy Choice, Noul or Score decision while ordinary code owns commands and checks, with `/login jev`, a guided `fabric-jev` skill, a per-program `maxEvaluations` budget and four upstream routes (TypeSafe, OpenRouter decisions, Vercel AI Gateway, SubQ).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fabric-runtime/pi-fabric) |
| Maintainer | [fabric-runtime](https://github.com/fabric-runtime). Independently curated. |
| Format | TypeScript package for Pi (npm `pi-fabric`) |
| Requirements | Node.js 24+ and Pi 1.0.0+; a TypeSafe or OpenRouter key only for Jev decisions. |
| License | [MIT](https://github.com/fabric-runtime/pi-fabric/blob/5e4eae52d364e4053848a6d2836fb7786cfb13ba/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/routes.ts`](https://github.com/fabric-runtime/pi-fabric/blob/5e4eae52d364e4053848a6d2836fb7786cfb13ba/src/jev/routes.ts) at the pinned commit. |

## When to use

- Add bounded, budgeted typed judgments to a shell-first agent workflow without letting a model write shell commands.
- Mismatch: Jev is one optional feature of a large runtime, and the README's other headline claims were not checked.

## How it works

`src/jev/routes.ts` resolves a model alias such as `jev-latest` or `jev-1.14.0` to `https://api.typesafe.ai/v1/systemone`, to OpenRouter's decisions endpoint, or to gateway routes; `src/jev/decisions.ts` keeps answers typed, and a program with `maxEvaluations: 0` is rejected before any inference. Integration evidence: [`src/jev/routes.ts`](https://github.com/fabric-runtime/pi-fabric/blob/5e4eae52d364e4053848a6d2836fb7786cfb13ba/src/jev/routes.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi install npm:pi-fabric
# in Pi: /login jev     (stores a TypeSafe key as a Pi credential)
# then: /skill:fabric-jev <task>
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with install and the Jev shell-orchestration doc: [github.com/fabric-runtime/pi-fabric#readme](https://github.com/fabric-runtime/pi-fabric#readme)
- Jev orchestration guide: [github.com/fabric-runtime/pi-fabric/blob/5e4eae52d364e4053848a6d2836fb7786cfb13ba/docs/jev.md](https://github.com/fabric-runtime/pi-fabric/blob/5e4eae52d364e4053848a6d2836fb7786cfb13ba/docs/jev.md)
- npm package: [www.npmjs.com/package/pi-fabric](https://www.npmjs.com/package/pi-fabric)

## Limits and data handling

Jev calls send the minimized state a program passes on your key (TypeSafe or OpenRouter); deterministic programs need no credentials. Fabric programs and ordinary tasks are session-owned, not restart-durable. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 5e4eae52d364](https://github.com/fabric-runtime/pi-fabric/tree/5e4eae52d364e4053848a6d2836fb7786cfb13ba). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
