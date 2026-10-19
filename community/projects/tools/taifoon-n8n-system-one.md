# System One for n8n (taifoon)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

n8n community node (`@taifoon/n8n-nodes-system-one`) that sends an item and your yes/no, pick-one and score questions to a System One host such as TypeSafe Jev or Venice and returns every answer with its probabilities, so n8n IF and Switch nodes can route on them.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/taifoon-io/n8n-nodes-system-one) |
| Maintainer | [taifoon-io](https://github.com/taifoon-io). Independently curated. |
| Format | n8n community node (TypeScript, npm package) |
| Requirements | An n8n instance with community nodes enabled; a key for TypeSafe, Venice or another `/v1/systemone` host. |
| License | [MIT](https://github.com/taifoon-io/n8n-nodes-system-one/blob/1f51d55e5792b56c37e6e200764c8038636d0a03/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`nodes/SystemOne/SystemOne.node.ts`](https://github.com/taifoon-io/n8n-nodes-system-one/blob/1f51d55e5792b56c37e6e200764c8038636d0a03/nodes/SystemOne/SystemOne.node.ts) at the pinned commit. |

## When to use

- Classify tickets or rows, pick a category or score a deliverable inside an n8n workflow.
- Switch between System One hosts by changing only the credential.
- Mismatch: judging only; not for writing, summarising or reasoning about code.

## How it works

The node in `nodes/SystemOne/SystemOne.node.ts` posts `{model, state, questions}` to `{base}/v1/systemone` with a Bearer key from the System One API credential. Host aliases map model names such as `jev-latest` or `jev-1.13.0` to each host's spelling. Results come back on one output with `p`, probabilities, confidence and a legend for each question. Integration evidence: [`nodes/SystemOne/SystemOne.node.ts`](https://github.com/taifoon-io/n8n-nodes-system-one/blob/1f51d55e5792b56c37e6e200764c8038636d0a03/nodes/SystemOne/SystemOne.node.ts).

## Get started

From the upstream README: install the package from n8n's Community Nodes settings, then create a System One API credential.

```sh
# In n8n: Settings → Community Nodes → Install
@taifoon/n8n-nodes-system-one
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [www.npmjs.com/package/@taifoon/n8n-nodes-system-one](https://www.npmjs.com/package/@taifoon/n8n-nodes-system-one)

## Limits and data handling

Item content goes to the host you configure. Keys are sent only over https, per the README.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 1f51d55e5792](https://github.com/taifoon-io/n8n-nodes-system-one/tree/1f51d55e5792b56c37e6e200764c8038636d0a03). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
