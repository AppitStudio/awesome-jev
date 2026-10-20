# jev-emoji

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Dependency-free npm package that picks or ranks an emoji for a piece of text with a Jev Choice call, from a curated list of about 250, the full Unicode set or your own list, with a confidence fallback.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DCPRevere/jev-emoji) |
| Maintainer | [DCPRevere](https://github.com/DCPRevere). Independently curated. |
| Format | npm package (JavaScript, Node 20.19+) |
| Requirements | Node 20.19+ or another server runtime with fetch; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/DCPRevere/jev-emoji/blob/45834369198ce71ff9ea17de19c838b701d23106/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/index.js`](https://github.com/DCPRevere/jev-emoji/blob/45834369198ce71ff9ea17de19c838b701d23106/src/index.js) at the pinned commit. |

## When to use

- Add an emoji to notifications, commit messages or chat replies from the text itself.
- Use your own small emoji list as labels for cheap classification.
- Mismatch: server-side only; the README warns never to put the key in browser code.

## How it works

`pickEmoji` and `rankEmojis` send the text and the candidate emojis (each with a short description) as a Jev Choice question and return the top pick or a ranked list with probabilities; `createEmojiPicker` adds a minimum confidence and a fallback. Integration evidence: [`src/index.js`](https://github.com/DCPRevere/jev-emoji/blob/45834369198ce71ff9ea17de19c838b701d23106/src/index.js).

## Get started

From the upstream README (not run on the review host):

```sh
npm install jev-emoji
export TYPESAFE_API_KEY=your-key
node -e 'import("jev-emoji").then(async m=>console.log(await m.pickEmoji("We won the cup final!")))'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Usage and cost table in the README: [github.com/DCPRevere/jev-emoji#readme](https://github.com/DCPRevere/jev-emoji#readme)

## Limits and data handling

Each call sends your text to TypeSafe and is billed per use (about $0.20 per 1,000 texts with the default list, per the README). Answers can vary slightly between calls.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 45834369198c](https://github.com/DCPRevere/jev-emoji/tree/45834369198ce71ff9ea17de19c838b701d23106). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
