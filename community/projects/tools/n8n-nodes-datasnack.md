# DataSnack node for n8n (workflow gate where Jev answers, a rules engine confirms every answer, and unconfirmed items go to your own AI or a person)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Community n8n node for DataSnack, a hosted service that puts Jev behind a Go rules engine: send a request to a gate and get a Confirmed output (Jev read it and a tested rule confirmed the answer, with reason and decision id) or a Not confirmed output to route to your own AI or a person. Record their answer back and the gate learns from it and drafts new rules; an Observe operation learns from your existing system. The node is MIT; the DataSnack service is a separate commercial product.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DataSnackAPI/n8n-nodes-datasnack) |
| Maintainer | [DataSnackAPI](https://github.com/DataSnackAPI). Independently curated. |
| Format | n8n community node (TypeScript, MIT) |
| Requirements | n8n with community nodes enabled and a DataSnack API key (`dsk_...`); Jev runs inside DataSnack, so no TypeSafe key is needed. |
| License | [MIT](https://github.com/DataSnackAPI/n8n-nodes-datasnack/blob/8903fdfe0b4a01c8040dd31818e95d490f24295e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`nodes/Datasnack/GenericFunctions.ts`](https://github.com/DataSnackAPI/n8n-nodes-datasnack/blob/8903fdfe0b4a01c8040dd31818e95d490f24295e/nodes/Datasnack/GenericFunctions.ts) at the pinned commit. |

## When to use

- Replace a per-item LLM call or manual review in n8n with an auditable Jev-plus-rules decision.
- Mismatch: a self-hosted gate; decisions run on DataSnack's hosted service.

## How it works

`nodes/Datasnack/GenericFunctions.ts` calls the DataSnack API (`https://datasnack.ai` by default) for decide, feedback and observe operations; Jev and the rules run on DataSnack's side, so the Jev call is not visible in this repository. Integration evidence: [`nodes/Datasnack/GenericFunctions.ts`](https://github.com/DataSnackAPI/n8n-nodes-datasnack/blob/8903fdfe0b4a01c8040dd31818e95d490f24295e/nodes/Datasnack/GenericFunctions.ts).

## Get started

Install the community node in n8n, add a DataSnack credential and place the node where your workflow needs a decision.

```sh
# n8n → Settings → Community nodes → Install: n8n-nodes-datasnack
# then create a DataSnack API credential (dsk_...) and add the DataSnack node
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/DataSnackAPI/n8n-nodes-datasnack/blob/8903fdfe0b4a01c8040dd31818e95d490f24295e/README.md](https://github.com/DataSnackAPI/n8n-nodes-datasnack/blob/8903fdfe0b4a01c8040dd31818e95d490f24295e/README.md)
- DataSnack pricing: [datasnack.ai/pricing](https://datasnack.ai/pricing)

## Limits and data handling

Request data goes to DataSnack, which runs Jev; its data handling was not reviewed. DataSnack pricing (checked 2026-11-19 at datasnack.ai/pricing): Free $0 with 2,000 decisions a month and 3 gates, Starter $19 a month, Pro $49 a month. Jev use is stated by DataSnack and not independently verified in the node source.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 8903fdfe0b4a](https://github.com/DataSnackAPI/n8n-nodes-datasnack/tree/8903fdfe0b4a01c8040dd31818e95d490f24295e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
