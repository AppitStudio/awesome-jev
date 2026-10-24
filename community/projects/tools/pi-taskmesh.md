# pi-taskmesh (task orchestration for Pi with optional Jev judgments)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Task-aware multi-model orchestration extension for the Pi coding agent: it decomposes work and coordinates subagents, and can use Jev to judge whether a request should be delegated and which model each task gets.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/0x1f/pi-taskmesh) |
| Maintainer | [0x1f](https://github.com/0x1f). Independently curated. |
| Format | Pi extension (TypeScript) |
| Requirements | Pi (or pi-bolt) with authenticated chat models and pi-subagents; optional TypeSafe or Vercel AI Gateway key. |
| License | [MIT](https://github.com/0x1f/pi-taskmesh/blob/3e0998bcf17272d9d0873fa2cb4ed16a79214a7e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/0x1f/pi-taskmesh/blob/3e0998bcf17272d9d0873fa2cb4ed16a79214a7e/src/jev.ts) at the pinned commit. |

## When to use

- Split a coding request into scout, worker and reviewer tasks in Pi.
- Let a cheap decision model handle routing judgments.
- Mismatch: needs a compatible pi-subagents extension; Jev is optional.

## How it works

`src/jev.ts` calls TypeSafe (`jev-latest`) or Vercel AI Gateway (`typesafe-ai/jev`); switch with `/taskmesh backend jev`. Pi chat models still write the plan. Integration evidence: [`src/jev.ts`](https://github.com/0x1f/pi-taskmesh/blob/3e0998bcf17272d9d0873fa2cb4ed16a79214a7e/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi-bolt install git:github.com/0x1f/pi-taskmesh
/jev setup typesafe
/taskmesh backend jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/0x1f/pi-taskmesh#readme](https://github.com/0x1f/pi-taskmesh#readme)

## Limits and data handling

Task text is sent to the Jev backend when selected. No Jev key is required for the default path.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 3e0998bcf172](https://github.com/0x1f/pi-taskmesh/tree/3e0998bcf17272d9d0873fa2cb4ed16a79214a7e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
