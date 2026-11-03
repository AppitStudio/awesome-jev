# Claude-JEV auto-effort (Claude Code mod that picks each request's effort from the plan step, skill and prompt, with Jev as the judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod that sets the effort of each model request from what the session is doing: the plan's current step, the prompt and the skill in use. Jev judges the prompt and each plan step when a TypeSafe key is set; scripted word lists decide when there is no key, Jev times out or is unsure. A band above the prompt shows the pick and why, with Auto and Manual buttons.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TEC10101/Claude-JEV-auto-effort-plugin) |
| Maintainer | [TEC10101](https://github.com/TEC10101). Independently curated. |
| Format | Claude Code plugin (TypeScript hooks) |
| Requirements | Claude desktop app with plugins; optionally `TYPESAFE_API_KEY` in the environment for the Jev judge. |
| License | [MIT](https://github.com/TEC10101/Claude-JEV-auto-effort-plugin/blob/2cd663f0dc27db9d6e8d1c7097dc896e507e8db1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/levers.ts`](https://github.com/TEC10101/Claude-JEV-auto-effort-plugin/blob/2cd663f0dc27db9d6e8d1c7097dc896e507e8db1/hooks/levers.ts) at the pinned commit. |

## When to use

- Run light work at low effort and verification or review steps at high effort without switching by hand.
- Mismatch: sibling of claude-auto-effort with a different design (plan steps and stages); it is a plugin zip for the Claude desktop app, with no marketplace install documented.

## How it works

`hooks/levers.ts` holds the Jev endpoint (`https://api.typesafe.ai/v1/systemone`) and the question set; the hooks send the scrubbed prompt (up to 1,500 characters), the tail of the previous reply, the plan step and its neighbours, and the stage, then the rules map the answer to a level, with the word lists as fallback. Integration evidence: [`hooks/levers.ts`](https://github.com/TEC10101/Claude-JEV-auto-effort-plugin/blob/2cd663f0dc27db9d6e8d1c7097dc896e507e8db1/hooks/levers.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# zip .claude-plugin, hooks, types and tsconfig.json, add the zip under Settings > Plugins,
# then run /reload-plugins in Claude Code
claude plugin validate .
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the decision order, commands and what is sent to Jev: [github.com/TEC10101/Claude-JEV-auto-effort-plugin#readme](https://github.com/TEC10101/Claude-JEV-auto-effort-plugin#readme)

## Limits and data handling

With a key set, the scrubbed prompt, previous-reply tail, plan step and stage go to TypeSafe; URLs, emails, keys, home paths, IP addresses and phone numbers are replaced best-effort first. A local store keeps prompts cut to 80 characters for tuning. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 2cd663f0dc27](https://github.com/TEC10101/Claude-JEV-auto-effort-plugin/tree/2cd663f0dc27db9d6e8d1c7097dc896e507e8db1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
