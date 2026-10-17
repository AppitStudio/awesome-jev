# jev-docs

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code hook that asks Jev which pages in your project's docs folder matter for each prompt and adds a short reading list to the context; routine prompts get nothing. Includes a skill that writes docs in the format the hook reads best.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/asuma312/jev-docs) |
| Maintainer | [asuma312](https://github.com/asuma312). Independently curated. |
| Format | Claude Code hook and agent skill (Node.js) |
| Requirements | Node.js, Claude Code, a TypeSafe API key. |
| License | [MIT](https://github.com/asuma312/jev-docs/blob/1d41020926851fb1b35234be061e42d223d5193e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hook.mjs`](https://github.com/asuma312/jev-docs/blob/1d41020926851fb1b35234be061e42d223d5193e/hook.mjs) at the pinned commit. |

## When to use

- Point a coding agent at the two or three relevant docs pages instead of letting it search a large docs folder or skip it.
- Try it without Claude Code with the `--dry-run` mode to see what would be picked.
- Mismatch: early and experimental; it only helps if the project already has a `docs/` folder worth reading.

## How it works

On each prompt `hook.mjs` builds an index of the docs folder (path, title, description, headings) and asks Jev first whether docs are needed, then which pages, before the agent sees the prompt. The README's measurements on a 950-page project show one to three Jev requests and about 0.6 to 1.1 s per prompt. Integration evidence: [`hook.mjs`](https://github.com/asuma312/jev-docs/blob/1d41020926851fb1b35234be061e42d223d5193e/hook.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/asuma312/jev-docs.git
cd jev-docs
npm install
node install.mjs
node hook.mjs --dry-run --cwd /path/to/project "what you want to do"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- `create-jev-doc` skill in `skills/create-jev-doc/`.
- Measured results table in the README.

## Limits and data handling

The prompt, up to three earlier user messages (600 characters each) and the docs index go to TypeSafe on your key; code, tool output and full page contents are not sent.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 1d4102092685](https://github.com/asuma312/jev-docs/tree/1d41020926851fb1b35234be061e42d223d5193e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
