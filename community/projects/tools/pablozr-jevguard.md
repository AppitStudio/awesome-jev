# JevGuard (pablozr)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Semantic policy engine (distinct from Jhonnyr97/JevGuard) for coding agents: after each turn Jev makes one narrow judgment per repository rule on the attributed diff, and a local gate returns PASS, WARN or FAIL.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pablozr/JevGuard) |
| Maintainer | [pablozr](https://github.com/pablozr). Independently curated. |
| Format | Node.js packages and agent plugin (TypeScript) |
| Requirements | Node.js; TypeSafe API key. |
| License | [MIT](https://github.com/pablozr/JevGuard/blob/539a910216d9d264c67b75e76d56029a6333ad32/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/node-infra/src/jev/transport.ts`](https://github.com/pablozr/JevGuard/blob/539a910216d9d264c67b75e76d56029a6333ad32/packages/node-infra/src/jev/transport.ts) at the pinned commit. |

## When to use

- Check whether an agent's change violated a specific repository policy.
- Keep code generation with the agent while a decision model only judges.
- Mismatch: not a code generator or general linter.

## How it works

Task, attributed diff and local rules are sent to Jev per rule; a deterministic local gate maps probabilities to PASS / WARN / FAIL and marks incomplete evidence UNAVAILABLE. Integration evidence: [`packages/node-infra/src/jev/transport.ts`](https://github.com/pablozr/JevGuard/blob/539a910216d9d264c67b75e76d56029a6333ad32/packages/node-infra/src/jev/transport.ts).

## Get started

From a clone (see upstream README for agent setup; not run on the review host):

```sh
git clone https://github.com/pablozr/JevGuard.git
cd JevGuard
npm install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Calibration tooling: `tools/calibration/`.

## Limits and data handling

Diffs and rule text are sent to TypeSafe and billed to your key; sensitive files are blocked per the README.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 539a910216d9](https://github.com/pablozr/JevGuard/tree/539a910216d9d264c67b75e76d56029a6333ad32). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
