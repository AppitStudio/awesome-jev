# pi-jevisual (pi extension that classifies images one by one with Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

pi coding-agent extension that adds an `independently_classify_visuals` tool: each local image is judged on its own against the same named Jev questions (choice, score, yes/no or bounding box), and other extensions can call the same function through its API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Piotr-Adamm/pi-jevisual) |
| Maintainer | [Piotr-Adamm](https://github.com/Piotr-Adamm). Independently curated. |
| Format | pi extension on npm (TypeScript, MIT) |
| Requirements | pi, `pi install npm:pi-jevisual`, and a TypeSafe key in `TYPESAFE_API_KEY` or stored in pi for the `typesafe` provider. |
| License | [MIT](https://github.com/Piotr-Adamm/pi-jevisual/blob/fa4f9ce6fee23cd9f079979d4bd13679760b2def/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/api.ts`](https://github.com/Piotr-Adamm/pi-jevisual/blob/fa4f9ce6fee23cd9f079979d4bd13679760b2def/src/api.ts) at the pinned commit. |

## When to use

- Let a coding agent sort, filter or locate things in screenshots and figures with typed answers.
- Reuse image classification from another pi extension via `pi-jevisual/api`.
- Mismatch: pi only; it never compares images with each other.

## How it works

`src/api.ts` uses `@typesafe-ai/sdk` to send images (in batches of up to 24 MB) with optional captions and shared state to Jev, returning one answer set per image in input order; images Jev cannot take, such as animated or multi-page files, come back as `unclassified` with a reason. Integration evidence: [`src/api.ts`](https://github.com/Piotr-Adamm/pi-jevisual/blob/fa4f9ce6fee23cd9f079979d4bd13679760b2def/src/api.ts).

## Get started

Install the package in pi and provide a TypeSafe key; without a key the tool stays registered but its calls fail.

```sh
pi install npm:pi-jevisual
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Piotr-Adamm/pi-jevisual/blob/fa4f9ce6fee23cd9f079979d4bd13679760b2def/README.md](https://github.com/Piotr-Adamm/pi-jevisual/blob/fa4f9ce6fee23cd9f079979d4bd13679760b2def/README.md)
- npm: [www.npmjs.com/package/pi-jevisual](https://www.npmjs.com/package/pi-jevisual)

## Limits and data handling

Images, captions and state are sent to TypeSafe's API on your key.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit fa4f9ce6fee2](https://github.com/Piotr-Adamm/pi-jevisual/tree/fa4f9ce6fee23cd9f079979d4bd13679760b2def). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
