# jev-skill-suggestion

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod that scores every installed skill against your prompt while you type, using Jev, and lets you choose whether Claude picks skills itself, loads none, or loads only Jev's pick.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ray-amjad/jev-skill-suggestion) |
| Maintainer | [ray-amjad](https://github.com/ray-amjad). Independently curated. |
| Format | Claude Code plugin (TypeScript hooks) |
| Requirements | Claude Code with plugin support; a TypeSafe API key (plugin `apiKey` option or `TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/ray-amjad/jev-skill-suggestion/blob/29e71afe2eddbcd260dee56bd49cd5cf6f735551/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Large skill libraries where Claude Code's truncated skill listing leads to wrong or unnecessary skill loads.
- Observe Jev's ranking before deciding to block or steer skill loading.
- Mismatch: Only affects model-initiated skill loads; slash commands you type always run.

## How it works

Following TypeSafe's skill-suggestion cookbook, 600 ms after you stop typing the draft goes to Jev: one Choice over all skill descriptions plus three Noul "needs a skill?" gates, then a second pass over the top three `SKILL.md` openings with a `fits` question each (0.30 thresholds). Modes `observe`, `block` and `steer` decide what Claude sees. Jev integration: [`hooks/register.tsx`](https://github.com/ray-amjad/jev-skill-suggestion/blob/29e71afe2eddbcd260dee56bd49cd5cf6f735551/hooks/register.tsx). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
/plugin install jev-skill-suggestion --marketplace ray-amjad/jev-skill-suggestion
```

## Limits and data handling

Each typed prompt, your skills' names/descriptions, and the first 700 characters of the top three `SKILL.md` files are sent to `api.typesafe.ai`; usage is billed by TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 29e71afe2edd](https://github.com/ray-amjad/jev-skill-suggestion/tree/29e71afe2eddbcd260dee56bd49cd5cf6f735551). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
