# dsh-jev-ultrafast (DeepSeek Harness plugin driving a real browser with TypeSafe Jev)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

DeepSeek Harness plugin port of jev-ultrafast: drive a real browser from natural language in dsh chats, using TypeSafe Jev for fast action decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xingzhen199186/dsh-jev-ultrafast) |
| Maintainer | [xingzhen199186](https://github.com/xingzhen199186). Independently curated. |
| Format | DeepSeek Harness plugin (TypeScript, MIT) |
| Requirements | DeepSeek Harness, a Chromium browser, and a TypeSafe API key. |
| License | [MIT](https://github.com/xingzhen199186/dsh-jev-ultrafast/blob/f49521eaf8756f6ae690049371ad4119e2c26a28/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision/typesafe.ts`](https://github.com/xingzhen199186/dsh-jev-ultrafast/blob/f49521eaf8756f6ae690049371ad4119e2c26a28/src/decision/typesafe.ts) at the pinned commit. |

## When to use

- Automate browser tasks inside DeepSeek Harness.
- Use Jev for low-latency click/type decisions.
- Mismatch: plugin for DeepSeek Harness only.

## How it works

`src/decision/typesafe.ts` targets the `https://api.typesafe.ai/v1/systemone` endpoint with `jev-latest` to choose browser actions. Integration evidence: [`src/decision/typesafe.ts`](https://github.com/xingzhen199186/dsh-jev-ultrafast/blob/f49521eaf8756f6ae690049371ad4119e2c26a28/src/decision/typesafe.ts).

## Get started

Install the plugin into DeepSeek Harness per README and set the key.

```sh
git clone https://github.com/xingzhen199186/dsh-jev-ultrafast.git && cd dsh-jev-ultrafast
export TYPESAFE_API_KEY=...
npm install && npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/xingzhen199186/dsh-jev-ultrafast/blob/f49521eaf8756f6ae690049371ad4119e2c26a28/README.md](https://github.com/xingzhen199186/dsh-jev-ultrafast/blob/f49521eaf8756f6ae690049371ad4119e2c26a28/README.md)

## Limits and data handling

Page content is sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit f49521eaf875](https://github.com/xingzhen199186/dsh-jev-ultrafast/tree/f49521eaf8756f6ae690049371ad4119e2c26a28). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
