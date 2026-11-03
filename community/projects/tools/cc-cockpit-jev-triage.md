# Jev triage for cc-cockpit (plugin that gives mail, Jira and chat items a priority and kind, judged by Jev under your rules and corrections)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

cc-cockpit plugin that tells source plugins (mail, Jira, chat, Forgejo, calendar) how much each item needs you: a priority (urgent, action, fyi, noise) and a kind (request, incident, discussion, alert, notification, ack). Item hints and your project rules decide first; Jev judges what they leave open, and your corrections sit on top, with a panel of recent verdicts and an Improve loop.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BronOS/cc-cockpit-jev-triage) |
| Maintainer | [BronOS](https://github.com/BronOS). Independently curated. |
| Format | cc-cockpit plugin (plain JavaScript, no build step) |
| Requirements | cc-cockpit with the Jev plugin (bronos.jev) enabled in the same project. |
| License | [MIT](https://github.com/BronOS/cc-cockpit-jev-triage/blob/c3e30e52fb02f37329e9441334ba6713a4d92255/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`dist/lib/pipeline.js`](https://github.com/BronOS/cc-cockpit-jev-triage/blob/c3e30e52fb02f37329e9441334ba6713a4d92255/dist/lib/pipeline.js) at the pinned commit. |

## When to use

- Rank an inbox or issue feed by urgency with your own profile, rules and corrections.
- Mismatch: only works inside cc-cockpit and through its Jev service.

## How it works

`dist/lib/pipeline.js` applies the item's hint, then project rules, and only asks Jev for items with neither: one `jev.grid` call per 50 items with a five-way priority question and a kind question, cached per project by text, profile, question wording and model, then applies your overrides and the item's floor. Integration evidence: [`dist/lib/pipeline.js`](https://github.com/BronOS/cc-cockpit-jev-triage/blob/c3e30e52fb02f37329e9441334ba6713a4d92255/dist/lib/pipeline.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/BronOS/cc-cockpit-jev-triage.git
cd cc-cockpit-jev-triage
npm test
ccc triage questions
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the service API, settings and CLI: [github.com/BronOS/cc-cockpit-jev-triage#readme](https://github.com/BronOS/cc-cockpit-jev-triage#readme)

## Limits and data handling

Item text from your source plugins is sent to Jev through the jev plugin (TypeSafe or OpenRouter on your key); verdicts and a 4,000-entry cache stay in the project's plugin storage. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit c3e30e52fb02](https://github.com/BronOS/cc-cockpit-jev-triage/tree/c3e30e52fb02f37329e9441334ba6713a4d92255). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
