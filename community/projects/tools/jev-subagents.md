# jev-subagents (Jev-assisted subagents for Pi)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension for running scout, worker and reviewer subagents as a native terminal task tree with explicit permissions, reviewed scope and bounded reference sharing, where Jev can optionally advise which candidate profile should take each task.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mud-the-developer/jev-subagents) |
| Maintainer | [mud-the-developer](https://github.com/mud-the-developer). Independently curated. |
| Format | Pi extension (TypeScript, Bun) |
| Requirements | Pi; Bun 1.4.3; Linux or native Windows (non-elevated); a TypeSafe key (or a Clef or OpenJEV server) for Jev advice; separate worker model access. |
| License | [MIT](https://github.com/mud-the-developer/jev-subagents/blob/d3e78f840cc1a392978dc7e28e85f8e63c14db65/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev-config.ts`](https://github.com/mud-the-developer/jev-subagents/blob/d3e78f840cc1a392978dc7e28e85f8e63c14db65/src/jev-config.ts) at the pinned commit. |

## When to use

- Split coding work across Pi subagents while reviewing exactly what each may touch.
- Let Jev suggest a profile for a task without giving it control.
- Mismatch: release candidate distributed as a source ZIP; not published to npm.

## How it works

`src/jev-config.ts` points Jev advice at `https://api.typesafe.ai/v1/systemone` with `TYPESAFE_API_KEY`, or at a Clef or OpenJEV server; the advice is separate from the worker models, which keep their own profiles. Integration evidence: [`src/jev-config.ts`](https://github.com/mud-the-developer/jev-subagents/blob/d3e78f840cc1a392978dc7e28e85f8e63c14db65/src/jev-config.ts).

## Get started

Download the `v1.0.0-rc.1` source ZIP and `SHA256SUMS` from the [release page](https://github.com/mud-the-developer/jev-subagents/releases/tag/v1.0.0-rc.1), prepare dependencies as in the [installation guide](https://github.com/mud-the-developer/jev-subagents/blob/main/docs/installation.md), then register it (not run on the review host):

```sh
pi install <absolute-extracted-folder>
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Usage: [github.com/mud-the-developer/jev-subagents/blob/main/docs/usage.md](https://github.com/mud-the-developer/jev-subagents/blob/main/docs/usage.md)
- Security notes: [github.com/mud-the-developer/jev-subagents/blob/main/docs/security.md](https://github.com/mud-the-developer/jev-subagents/blob/main/docs/security.md)

## Limits and data handling

Task descriptions are sent to the configured Jev backend when advice is on. The README's GIFs are synthetic previews, not recordings.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit d3e78f840cc1](https://github.com/mud-the-developer/jev-subagents/tree/d3e78f840cc1a392978dc7e28e85f8e63c14db65). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
