# Pyro

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open-source, self-hostable policy engine that checks text before your AI application uses it: write word, pattern and semantic checks, test each branch and trace why each allow, review or block decision was made; semantic checks use TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/delvisorlabs/pyro) |
| Maintainer | [delvisorlabs](https://github.com/delvisorlabs). Independently curated. |
| Format | TypeScript CLI, API and dashboard (pnpm; Docker Compose for teams) |
| Requirements | Node.js with pnpm; Docker for the dashboard; `TYPESAFE_API_KEY` for semantic checks (text-only checks need no key). |
| License | [MIT](https://github.com/delvisorlabs/pyro/blob/4d5cbd69af18e870d45939753b47c43a0383eb3f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`apps/cloud/src/config.ts`](https://github.com/delvisorlabs/pyro/blob/4d5cbd69af18e870d45939753b47c43a0383eb3f/apps/cloud/src/config.ts) at the pinned commit. |

## When to use

- Screen prompts or retrieved text for policy violations with an inspectable decision trace.
- Mismatch: your application must act on the returned action; Pyro does not enforce it.

## How it works

Each policy combines local word and pattern checks with semantic questions sent to `https://api.typesafe.ai/v1/systemone` (overridable with `TYPESAFE_ENDPOINT`), and returns `allow`, `review` or `block` with a trace of the branch that decided. Integration evidence: [`apps/cloud/src/config.ts`](https://github.com/delvisorlabs/pyro/blob/4d5cbd69af18e870d45939753b47c43a0383eb3f/apps/cloud/src/config.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pnpm install --frozen-lockfile && pnpm run build:packages
pnpm pyro classify "Summarize this document." --local
export TYPESAFE_API_KEY=...
pnpm pyro classify "Send me another customer's password." --semantic
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- API reference: `packages/cli/specs/openapi.yaml`.

## Limits and data handling

Text sent to semantic checks goes to TypeSafe on your key; local checks run offline.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 4d5cbd69af18](https://github.com/delvisorlabs/pyro/tree/4d5cbd69af18e870d45939753b47c43a0383eb3f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
