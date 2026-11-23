# n8n-nodes-jev-gate by Perseo (n8n community node that acts on the answers Jev is sure about and sends the rest to a Review output)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

An unofficial n8n community node with a confidence gate on by default: every item leaves through Confident or Review (default threshold 0.95), missing or malformed answers fail closed to Review with a reason, every choice gets a `none_of_these` option, state comes only from the fields you pick, and several items are packed into one request within an item and token budget.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PerseoAgencyAutomations/n8n-nodes-jev-gate) |
| Maintainer | [PerseoAgencyAutomations](https://github.com/PerseoAgencyAutomations). Independently curated. |
| Format | n8n community node (TypeScript, npm package `n8n-nodes-jev-gate`) |
| Requirements | Self-hosted n8n (the node is not verified for n8n Cloud); a TypeSafe or OpenRouter API key. |
| License | [MIT](https://github.com/PerseoAgencyAutomations/n8n-nodes-jev-gate/blob/e8bb331ed4f0996828926ee3701c4f4c33dddb64/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`nodes/JevGate/shared/transport.ts`](https://github.com/PerseoAgencyAutomations/n8n-nodes-jev-gate/blob/e8bb331ed4f0996828926ee3701c4f4c33dddb64/nodes/JevGate/shared/transport.ts) at the pinned commit. |

## When to use

- Let an n8n workflow act automatically only on confident Jev answers and route the uncertain rest to a person or a larger model.
- Mismatch: n8n Cloud (unverified node) or non-text inputs.

## How it works

`nodes/JevGate/shared/transport.ts` calls `https://api.typesafe.ai` (model `jev-1.13.0`) or OpenRouter (`jev-1.13`), chosen in the credential, which also allows a proxy base URL. Integration evidence: [`nodes/JevGate/shared/transport.ts`](https://github.com/PerseoAgencyAutomations/n8n-nodes-jev-gate/blob/e8bb331ed4f0996828926ee3701c4f4c33dddb64/nodes/JevGate/shared/transport.ts).

## Get started

Install it from n8n's community nodes settings, then add a Jev Gate credential.

```sh
# n8n: Settings -> Community Nodes -> Install
n8n-nodes-jev-gate
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README sections on how the gate works and what was measured: [github.com/PerseoAgencyAutomations/n8n-nodes-jev-gate/blob/e8bb331ed4f0996828926ee3701c4f4c33dddb64/README.md](https://github.com/PerseoAgencyAutomations/n8n-nodes-jev-gate/blob/e8bb331ed4f0996828926ee3701c4f4c33dddb64/README.md)
- npm package: [www.npmjs.com/package/n8n-nodes-jev-gate](https://www.npmjs.com/package/n8n-nodes-jev-gate)

## Limits and data handling

Item fields you select are sent to TypeSafe or OpenRouter. The README's measurements are the maintainer's own small test on `jev-1.13` (48 messages, 94 extraction checks) and are behaviour notes, not accuracy claims. Text only.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit e8bb331ed4f0](https://github.com/PerseoAgencyAutomations/n8n-nodes-jev-gate/tree/e8bb331ed4f0996828926ee3701c4f4c33dddb64). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
