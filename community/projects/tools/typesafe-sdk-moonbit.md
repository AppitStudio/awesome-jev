# typesafe-sdk-moonbit (community MoonBit SDK for System One with verified confidence gates)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Community MoonBit SDK for TypeSafe's System One API with typed Noul, Choice and Score questions, confidence gates, token budgets and retry backoff whose contracts are proved with `moon prove` (Why3 and Z3), plus network-free testing; it states it is independent and not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/huanguan-Q/typesafe-sdk-moonbit) |
| Maintainer | [huanguan-Q](https://github.com/huanguan-Q). Independently curated. |
| Format | MoonBit library |
| Requirements | The MoonBit toolchain; a TypeSafe API key. |
| License | [MIT](https://github.com/huanguan-Q/typesafe-sdk-moonbit/blob/f07b8279f79b93c71a3741569b8d7dd1db041a05/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`client.mbt`](https://github.com/huanguan-Q/typesafe-sdk-moonbit/blob/f07b8279f79b93c71a3741569b8d7dd1db041a05/client.mbt) at the pinned commit. |

## When to use

- Call Jev from MoonBit with typed requests and answers.
- Rely on formally checked gate and retry logic rather than hand-written policy code.
- Mismatch: community SDK, early version.

## How it works

`client.mbt` defaults to `jev-latest` and `https://api.typesafe.ai`, sends requests to `/v1/systemone`, and decodes typed answers; the proofs cover the decision-core contracts. Integration evidence: [`client.mbt`](https://github.com/huanguan-Q/typesafe-sdk-moonbit/blob/f07b8279f79b93c71a3741569b8d7dd1db041a05/client.mbt).

## Get started

From the upstream README (not run on the review host):

```sh
moon add huanguan-Q/typesafe-sdk-moonbit
# build a SystemOneRequest with model "jev-latest" and your questions; set your TypeSafe key in the config
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/huanguan-Q/typesafe-sdk-moonbit#readme](https://github.com/huanguan-Q/typesafe-sdk-moonbit#readme)

## Limits and data handling

The state and questions you build go to TypeSafe. Unofficial; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit f07b8279f79b](https://github.com/huanguan-Q/typesafe-sdk-moonbit/tree/f07b8279f79b93c71a3741569b8d7dd1db041a05). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
