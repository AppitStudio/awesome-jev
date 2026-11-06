# pi-autothink (Pi extension that asks Jev how hard to think before each turn)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Pi extension that scores each user message with TypeSafe Jev (default) and sets that turn's thinking level from 0–5 so typos and deep redesigns no longer share the same reasoning budget—same model and prompt cache, only the thinking level moves.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/loofare/pi-autothink) |
| Maintainer | [loofare](https://github.com/loofare). Independently curated. |
| Format | Pi npm extension (MIT) |
| Requirements | Pi coding agent and a TypeSafe (or other configured) classifier key. |
| License | [MIT](https://github.com/loofare/pi-autothink/blob/6196be6f6901fadacfee02915c62f11bcc7bc49c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`extensions/auto-thinking.ts`](https://github.com/loofare/pi-autothink/blob/6196be6f6901fadacfee02915c62f11bcc7bc49c/extensions/auto-thinking.ts) at the pinned commit. |

## When to use

- Cut reasoning spend on trivial Pi turns.
- Keep one model while varying thinking depth.
- Mismatch: classifier quality depends on the chosen provider/model.

## How it works

`extensions/auto-thinking.ts` defaults to provider `typesafe` / model `jev-latest` to score request depth before the turn runs. Integration evidence: [`extensions/auto-thinking.ts`](https://github.com/loofare/pi-autothink/blob/6196be6f6901fadacfee02915c62f11bcc7bc49c/extensions/auto-thinking.ts).

## Get started

Install the npm package into Pi and set `TYPESAFE_API_KEY` (or override `PI_AUTO_THINKING_MODEL`).

```sh
npm install pi-autothink
export TYPESAFE_API_KEY=...
# enable per Pi extension docs in README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/loofare/pi-autothink/blob/6196be6f6901fadacfee02915c62f11bcc7bc49c/README.md](https://github.com/loofare/pi-autothink/blob/6196be6f6901fadacfee02915c62f11bcc7bc49c/README.md)

## Limits and data handling

User message text is sent to the classifier provider on your key.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 6196be6f6901](https://github.com/loofare/pi-autothink/tree/6196be6f6901fadacfee02915c62f11bcc7bc49c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
