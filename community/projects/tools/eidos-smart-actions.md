# Smart Actions for Eidos by Eidos (Jev classification, urgency and scoring actions that write back to your tables)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

An Eidos Lite plugin: pick input fields, define the judgment (which department, how urgent, how dissatisfied) and the output fields, then run the action on rows; Jev's answers are proposed and only written back to the `.eidos` table after you confirm. Actions can be drafted by an optional AI generator, and a sample file is included.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eidos-space/eidos-smart-actions-plugin) |
| Maintainer | [eidos-space](https://github.com/eidos-space). Independently curated. |
| Format | Eidos Lite plugin |
| Requirements | Eidos Lite (install from its plugin marketplace) and your own TypeSafe API key saved in the plugin settings; the optional Action Generator uses a separate connection. |
| License | [MIT](https://github.com/eidos-space/eidos-smart-actions-plugin/blob/e4bd0e5b0570e067917ac9cffce3fd4090285674/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugin.json`](https://github.com/eidos-space/eidos-smart-actions-plugin/blob/e4bd0e5b0570e067917ac9cffce3fd4090285674/plugin.json) at the pinned commit. |

## When to use

- Add typed Jev judgments (category, urgency, score) to rows in an Eidos workspace without writing code.
- Mismatch: you don't use Eidos; it is a plugin for that app only.

## How it works

`plugin.json` declares the TypeSafe connection at `https://api.typesafe.ai/v1/systemone`; each action builds a state from the selected fields and typed questions from the rules, and `scripts/live-smoke.mjs` shows the same request shape. Integration evidence: [`plugin.json`](https://github.com/eidos-space/eidos-smart-actions-plugin/blob/e4bd0e5b0570e067917ac9cffce3fd4090285674/plugin.json).

## Get started

Install Smart Actions from the Eidos Lite marketplace, save your TypeSafe key, then open the sample file and run the saved action on a row.

```sh
# In Eidos Lite: Plugins → Smart Actions → Settings → TypeSafe AI (save key)
# Sample: https://github.com/eidos-space/eidos-smart-actions-plugin/releases/download/v0.4.1/smart-actions-sample.eidos
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/eidos-space/eidos-smart-actions-plugin/blob/e4bd0e5b0570e067917ac9cffce3fd4090285674/README.md](https://github.com/eidos-space/eidos-smart-actions-plugin/blob/e4bd0e5b0570e067917ac9cffce3fd4090285674/README.md)
- Sample file (v0.4.1): [github.com/eidos-space/eidos-smart-actions-plugin/releases/download/v0.4.1/smart-actions-sample.eidos](https://github.com/eidos-space/eidos-smart-actions-plugin/releases/download/v0.4.1/smart-actions-sample.eidos)

## Limits and data handling

Field values of the rows you run are sent to TypeSafe. Results are proposals until confirmed.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit e4bd0e5b0570](https://github.com/eidos-space/eidos-smart-actions-plugin/tree/e4bd0e5b0570e067917ac9cffce3fd4090285674). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
