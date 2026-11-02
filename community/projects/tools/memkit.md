# memkit (OpenClaw memory plugin for role-play companions where Jev makes every recall and write decision)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Memory plugin for OpenClaw companions that keeps a character from faking memory: what it knows comes only from recalled evidence, every pass/fail step (did the topic change, does this turn need memory, is a recalled file relevant, is it time-related) is a Jev judgment, and DeepSeek only writes. Ships an example character and a gold-set evaluation; README in English and Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/QiqianFu/memkit) |
| Maintainer | [QiqianFu](https://github.com/QiqianFu). Independently curated. |
| Format | OpenClaw plugin (TypeScript) |
| Requirements | OpenClaw, Node.js, a TypeSafe key (falls back to a DeepSeek-emulated judge), a DeepSeek key, BGE embeddings. |
| License | [MIT](https://github.com/QiqianFu/memkit/blob/64c49f4522bef1f2f1d2029a5992621a4b5e3720/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/judge.ts`](https://github.com/QiqianFu/memkit/blob/64c49f4522bef1f2f1d2029a5992621a4b5e3720/src/judge.ts) at the pinned commit. |

## When to use

- Add evidence-only long-term memory to a chat companion.
- Mismatch: built around OpenClaw and one example character.

## How it works

`src/judge.ts` posts noul and choice questions to TypeSafe `/v1/systemone` for the ingest and recall gates; thresholds, recall size and which files a write may touch are decided in code. Integration evidence: [`src/judge.ts`](https://github.com/QiqianFu/memkit/blob/64c49f4522bef1f2f1d2029a5992621a4b5e3720/src/judge.ts).

## Get started

From the upstream README (not run on the review host):

```sh
openclaw plugins install --link /path/to/memkit --force --accept-capabilities
npm test   # offline, scripted judge
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Gold-set evaluation: node scripts/eval_gold.ts (see the README)

## Limits and data handling

Conversation windows are sent to TypeSafe and DeepSeek. The example character is fan content. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 64c49f4522be](https://github.com/QiqianFu/memkit/tree/64c49f4522bef1f2f1d2029a5992621a4b5e3720). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
