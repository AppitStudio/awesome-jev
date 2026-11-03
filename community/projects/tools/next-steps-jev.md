# next-steps-jev (Claude Code plugin that scores the model's suggested next prompts with Jev and recommends the most helpful)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Fork of Thariq Shihipar's next-steps plugin for Claude Code. After each answer the session's model suggests up to three next prompts, and Jev scores each by how much it would help your current goal; press 1, 2 or 3 to drop one into the prompt box as a draft, with the top pick marked recommended. The plugin never submits a prompt itself; its status text is in Traditional Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kevinyin9/next-steps-jev) |
| Maintainer | [kevinyin9](https://github.com/kevinyin9). Independently curated. |
| Format | Claude Code plugin (TypeScript hook) |
| Requirements | Claude Code in a terminal session; a TypeSafe API key; disable the original next-steps plugin. |
| License | [MIT](https://github.com/kevinyin9/next-steps-jev/blob/0246ac88441a7e9547830567821419119e1c99a9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/register.tsx`](https://github.com/kevinyin9/next-steps-jev/blob/0246ac88441a7e9547830567821419119e1c99a9/hooks/register.tsx) at the pinned commit. |

## When to use

- Choose the most useful follow-up prompt in a Claude Code session with a scored shortlist.
- Mismatch: terminal sessions only (not `claude -p`, the desktop app or VS Code), and the on-screen text is Traditional Chinese.

## How it works

`hooks/register.tsx` sends your latest message (up to 2,000 characters), the model's latest answer (up to 6,000) and the suggested prompts to `https://api.typesafe.ai/v1/systemone` (`jev-latest`), then ranks the suggestions by the returned scores; if Jev cannot answer the suggestions show unscored with the reason. Integration evidence: [`hooks/register.tsx`](https://github.com/kevinyin9/next-steps-jev/blob/0246ac88441a7e9547830567821419119e1c99a9/hooks/register.tsx).

## Get started

From the upstream README (not run on the review host):

```sh
# one-time: get a TypeSafe API key, then disable the original plugin
claude plugin disable next-steps@claude-community --scope user
/plugin install next-steps-jev --marketplace kevinyin9/next-steps-jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with what leaves your computer and the setup steps: [github.com/kevinyin9/next-steps-jev#readme](https://github.com/kevinyin9/next-steps-jev#readme)

## Limits and data handling

Conversation text, including any code or secrets in it, goes to TypeSafe after each answer, and there is no per-session off switch. The license carries the original author's copyright line. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 0246ac88441a](https://github.com/kevinyin9/next-steps-jev/tree/0246ac88441a7e9547830567821419119e1c99a9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
