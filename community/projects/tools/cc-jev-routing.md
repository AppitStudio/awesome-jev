# jev-routing by harry18456 (Claude Code plugin where Jev picks haiku, sonnet, opus or fable for each turn and subagent)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that asks Jev, before the first model request of each turn, which tier the prompt needs and rewrites that turn's model, down-only by default and with a confidence gate. Subagents get their own pick from their brief. It fails open to the session's model on timeouts or errors, and shows each decision in the status line. English and Traditional Chinese docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/harry18456/cc-jev-routing) |
| Maintainer | [harry18456](https://github.com/harry18456). Independently curated. |
| Format | Claude Code plugin (TypeScript hooks) |
| Requirements | Claude Code and a TypeSafe API key (`TYPESAFE_API_KEY` or `/config`). |
| License | [MIT](https://github.com/harry18456/cc-jev-routing/blob/5f9b52a2469887bd27e196bf37254e355666865f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/question.ts`](https://github.com/harry18456/cc-jev-routing/blob/5f9b52a2469887bd27e196bf37254e355666865f/hooks/question.ts) at the pinned commit. |

## When to use

- Cut Claude Code spend by running mechanical turns and subagents on cheaper tiers automatically.
- Mismatch: if you always want one fixed model; the README's own tests show a long opus session costing slightly more with routing on.

## How it works

`hooks/question.ts` builds a Choice over the model tiers (`jev-1.13.0`) from the prompt and the previous exchange and posts it to `https://api.typesafe.ai/v1/systemone`; `hooks/routing.test.ts` covers the routing policy. Integration evidence: [`hooks/question.ts`](https://github.com/harry18456/cc-jev-routing/blob/5f9b52a2469887bd27e196bf37254e355666865f/hooks/question.ts).

## Get started

Install the plugin from its repository in Claude Code, set your TypeSafe key, and check `/jev status`.

```sh
git clone https://github.com/harry18456/cc-jev-routing.git
# install as a Claude Code plugin per the README, then set the TypeSafe API key in /config
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with measured savings: [github.com/harry18456/cc-jev-routing/blob/5f9b52a2469887bd27e196bf37254e355666865f/README.md](https://github.com/harry18456/cc-jev-routing/blob/5f9b52a2469887bd27e196bf37254e355666865f/README.md)
- Routing matrix: [github.com/harry18456/cc-jev-routing/blob/5f9b52a2469887bd27e196bf37254e355666865f/docs/matrix-2026-10.md](https://github.com/harry18456/cc-jev-routing/blob/5f9b52a2469887bd27e196bf37254e355666865f/docs/matrix-2026-10.md)

## Limits and data handling

Prompts (and the previous exchange) are sent to TypeSafe and billed to your key. Savings figures are the maintainer's own scripted sessions (October 2026); results depend on your mix of work.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 5f9b52a24698](https://github.com/harry18456/cc-jev-routing/tree/5f9b52a2469887bd27e196bf37254e355666865f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
