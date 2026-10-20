# pi-system-one-gate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Authorizer link for the Pi coding agent's permission system that asks a System One model (TypeSafe Jev or a Reflex server) whether a bash, MCP or tool call is safe and auto-approves only at P(safe) of 0.9 or more; everything else goes to your normal prompt.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kreeger/pi-system-one-gate) |
| Maintainer | [kreeger](https://github.com/kreeger). Independently curated. |
| Format | Pi extension (TypeScript, npm) |
| Requirements | Pi with `@gotgenes/pi-permission-system`; a TypeSafe login (`/login typesafe`) or a Reflex endpoint and key. |
| License | [MIT](https://github.com/kreeger/pi-system-one-gate/blob/817ebb84b2a417fa51331c75baf36766c3dff794/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/backend.ts`](https://github.com/kreeger/pi-system-one-gate/blob/817ebb84b2a417fa51331c75baf36766c3dff794/src/backend.ts) at the pinned commit. |

## When to use

- Cut permission prompts for clearly safe commands while keeping a human prompt for the rest.
- Log each decision with probabilities to the permission review log.
- Mismatch: it never denies; anything uncertain or erroring defers to you.

## How it works

When pi-permission-system would prompt, the `system-one` link sends the redacted command or tool call (capped at 8 KB) to the configured backend (`https://api.typesafe.ai` with `jev-latest` for TypeSafe, see `src/backend.ts`) and allows only a `safe` choice at 0.9 or above. Integration evidence: [`src/backend.ts`](https://github.com/kreeger/pi-system-one-gate/blob/817ebb84b2a417fa51331c75baf36766c3dff794/src/backend.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi install npm:@gotgenes/pi-permission-system
# then add "system-one" to authorizerChain in
# ~/.pi/agent/extensions/pi-permission-system/config.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Eval set of 99 commands and results in the README: [github.com/kreeger/pi-system-one-gate#eval](https://github.com/kreeger/pi-system-one-gate#eval)

## Limits and data handling

Commands are redacted for secrets before being sent to the backend. The author's eval used the Reflex `d3-mini` model on a small hand-labelled set, not Jev; treat the numbers as indicative.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 817ebb84b2a4](https://github.com/kreeger/pi-system-one-gate/tree/817ebb84b2a417fa51331c75baf36766c3dff794). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
