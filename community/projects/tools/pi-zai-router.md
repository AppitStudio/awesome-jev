# pi-zai-router by Dmitry Rybushkin (Pi coding agent extension: a virtual auto model where Jev classifies each new task for the z.ai subscription)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Start a Pi coding agent session on a virtual `zai/auto` model: Jev rates each new request as complex or standard and the extension picks the matching z.ai model (by default GLM-5.4 or GLM-5.3 Flash), then switches to the fast model and stays there after the first successful edit. Images go to the vision model. Russian README.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rybushkindmitry/pi-zai-router) |
| Maintainer | [rybushkindmitry](https://github.com/rybushkindmitry). Independently curated. |
| Format | Pi coding agent extension (TypeScript) |
| Requirements | The Pi coding agent with a z.ai coding subscription configured in `~/.pi/agent/models.json`; an OpenRouter key for Jev. |
| License | [MIT](https://github.com/rybushkindmitry/pi-zai-router/blob/d8a3dc17b10552b43929f4519b76dd1fbf403a31/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`extensions/zai-router.ts`](https://github.com/rybushkindmitry/pi-zai-router/blob/d8a3dc17b10552b43929f4519b76dd1fbf403a31/extensions/zai-router.ts) at the pinned commit. |

## When to use

- Let a cheap Jev classification pick between a strong and a fast model per task on a flat-rate coding subscription.
- Mismatch: other agents or providers; it targets Pi and z.ai.

## How it works

`extensions/zai-router.ts` asks `~typesafe/jev-latest` through OpenRouter via Pi's model registry (`classify`) with one Choice question about the prompt; if Jev is unavailable it uses the fast model. Integration evidence: [`extensions/zai-router.ts`](https://github.com/rybushkindmitry/pi-zai-router/blob/d8a3dc17b10552b43929f4519b76dd1fbf403a31/extensions/zai-router.ts).

## Get started

Install the pinned release with pi and add the z.ai provider to your local models file.

```sh
pi install git:github.com/rybushkindmitry/pi-zai-router@v1.0.1
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Russian): [github.com/rybushkindmitry/pi-zai-router/blob/d8a3dc17b10552b43929f4519b76dd1fbf403a31/README.md](https://github.com/rybushkindmitry/pi-zai-router/blob/d8a3dc17b10552b43929f4519b76dd1fbf403a31/README.md)

## Limits and data handling

The start of each new prompt (up to 16,000 characters) is sent to OpenRouter for the Jev call. The code notes that direct TypeSafe API access did not work for the author, so it uses OpenRouter.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit d8a3dc17b105](https://github.com/rybushkindmitry/pi-zai-router/tree/d8a3dc17b10552b43929f4519b76dd1fbf403a31). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
