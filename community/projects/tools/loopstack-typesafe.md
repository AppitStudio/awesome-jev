# Loopstack TypeSafe module (workflow framework registry package for TypeSafe Jev decisions)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Registry package in the Loopstack agent-workflow framework that answers named questions about a state with TypeSafe Jev via `systemOne()`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/loopstack-ai/loopstack) |
| Maintainer | [loopstack-ai](https://github.com/loopstack-ai). Independently curated. |
| Format | TypeScript module (MIT) |
| Requirements | Node, a Loopstack app, and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/loopstack-ai/loopstack/blob/52ae9af8e28c3f847d2aabd2fa38c33e201f5b47/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`registry/typesafe/src/services/typesafe-client.service.ts`](https://github.com/loopstack-ai/loopstack/blob/52ae9af8e28c3f847d2aabd2fa38c33e201f5b47/registry/typesafe/src/services/typesafe-client.service.ts) at the pinned commit. |

## When to use

- Add typed Jev decisions to Loopstack workflows.
- Branch workflows on calibrated answers.
- Mismatch: requires Loopstack.

## How it works

`typesafe-client.service.ts` calls System One; model defaults to `TYPESAFE_DEFAULT_MODEL` then `jev-latest`, and the module exposes typed answer helpers. Integration evidence: [`registry/typesafe/src/services/typesafe-client.service.ts`](https://github.com/loopstack-ai/loopstack/blob/52ae9af8e28c3f847d2aabd2fa38c33e201f5b47/registry/typesafe/src/services/typesafe-client.service.ts).

## Get started

Add the `registry/typesafe` module to a Loopstack workflow per its README and set the key.

```sh
git clone https://github.com/loopstack-ai/loopstack.git && cd loopstack
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Module README: [github.com/loopstack-ai/loopstack/blob/52ae9af8e28c3f847d2aabd2fa38c33e201f5b47/registry/typesafe/README.md](https://github.com/loopstack-ai/loopstack/blob/52ae9af8e28c3f847d2aabd2fa38c33e201f5b47/registry/typesafe/README.md)

## Limits and data handling

Workflow state you pass is sent to TypeSafe.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 52ae9af8e28c](https://github.com/loopstack-ai/loopstack/tree/52ae9af8e28c3f847d2aabd2fa38c33e201f5b47). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
