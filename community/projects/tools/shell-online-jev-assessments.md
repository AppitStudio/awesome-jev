# shell.online (remote terminal sessions with optional Jev assessments)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Run an agent or command on your computer and use it from any browser; an optional, consent-gated external-analysis panel asks Jev for advisory labels such as needs attention or possible loop.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TeoSlayer/shell.online) |
| Maintainer | [TeoSlayer](https://github.com/TeoSlayer). Independently curated. |
| Format | CLI and web app (TypeScript, MIT) |
| Requirements | The shell.online CLI, and a TypeSafe key configured on a self-hosted server for Jev assessments. |
| License | [MIT](https://github.com/TeoSlayer/shell.online/blob/62bc7003469297d8ff886d97db5a8fb29ac1288f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/server/lib/jev/provider.ts`](https://github.com/TeoSlayer/shell.online/blob/62bc7003469297d8ff886d97db5a8fb29ac1288f/app/server/lib/jev/provider.ts) at the pinned commit. |

## When to use

- Get advisory loop/attention labels on a remote agent session.
- Mismatch: Jev is optional and advisory; the default UI sends only counts, so many results come back unknown.

## How it works

`app/server/lib/jev/provider.ts` posts an allowlisted state to `https://api.typesafe.ai/v1/systemone`; `docs/JEV.md` says assessments need explicit owner consent, send only bounded request counts by default, and never control the agent. Integration evidence: [`app/server/lib/jev/provider.ts`](https://github.com/TeoSlayer/shell.online/blob/62bc7003469297d8ff886d97db5a8fb29ac1288f/app/server/lib/jev/provider.ts).

## Get started

Install the CLI, then follow `docs/JEV.md` to configure the provider on your deployment.

```sh
curl -fsSL https://shell.online/install | sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev doc: [github.com/TeoSlayer/shell.online/blob/62bc7003469297d8ff886d97db5a8fb29ac1288f/docs/JEV.md](https://github.com/TeoSlayer/shell.online/blob/62bc7003469297d8ff886d97db5a8fb29ac1288f/docs/JEV.md)
- Docs: [shell.online/docs/](https://shell.online/docs/)

## Limits and data handling

Only an allowlisted state (request counts by default) goes to TypeSafe after explicit consent.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 62bc70034692](https://github.com/TeoSlayer/shell.online/tree/62bc7003469297d8ff886d97db5a8fb29ac1288f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
