# dsh-sensitive-guard (DeepSeek Harness plugin that checks sensitive shell commands against built-in rules and a Jev verdict before they run; Chinese and English)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugin for DeepSeek Harness's full-permission mode, where approvals are set to `never` and `rm -rf` simply runs. Before a tool executes, it applies 43 built-in command rules (plus custom regexes) and can ask Jev for a verdict, reason and severity on the command, optionally using recent session context. A refusal is never diluted into advice, and with no key, a timeout or a bad answer it falls back to native behaviour, by default asking the human (which means a refusal in full-permission mode). It can tighten permissions but never force-allows.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yy1588133/dsh-sensitive-guard) |
| Maintainer | [yy1588133](https://github.com/yy1588133). Independently curated. |
| Format | DeepSeek Harness (DSH) plugin (plain JavaScript, no build step), Chinese and English UI |
| Requirements | DeepSeek Harness and a TypeSafe API key for the Jev assist (without a key the Jev part stays inert and the rules still apply). |
| License | [MIT](https://github.com/yy1588133/dsh-sensitive-guard/blob/5d55b949ba04ec65485bd72f17c799f054d847fe/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/store.js`](https://github.com/yy1588133/dsh-sensitive-guard/blob/5d55b949ba04ec65485bd72f17c799f054d847fe/lib/store.js) at the pinned commit. |

## When to use

- Add a last check on destructive shell commands to a DeepSeek Harness setup that has approvals turned off.
- Mismatch: it targets one harness, and its rule set and prompts are ported from another project's decision-assist feature.

## How it works

`lib/store.js` sets the default endpoint `https://api.typesafe.ai/v1/systemone` (default model `jev-latest`) and `client.js` asks `choice` and `score` questions for verdict, reason and severity; `lib/net.js` supports proxies for networks that cannot reach the API directly. Integration evidence: [`lib/store.js`](https://github.com/yy1588133/dsh-sensitive-guard/blob/5d55b949ba04ec65485bd72f17c799f054d847fe/lib/store.js).

## Get started

From the upstream README (not run on the review host):

```sh
dsh plugin --profile <your-profile> add yy1588133/dsh-sensitive-guard
# restart the DSH desktop app, then open Settings > sensitive command guard and add your TypeSafe key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese) with the rule table, fail-closed behaviour and setup steps: [github.com/yy1588133/dsh-sensitive-guard#readme](https://github.com/yy1588133/dsh-sensitive-guard#readme)

## Limits and data handling

With the Jev assist on, command text and a trimmed slice of recent session context go to TypeSafe on your key (the README caps text, arguments and output lengths). The README is Chinese-only. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 5d55b949ba04](https://github.com/yy1588133/dsh-sensitive-guard/tree/5d55b949ba04ec65485bd72f17c799f054d847fe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
